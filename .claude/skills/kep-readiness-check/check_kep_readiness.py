#!/usr/bin/env python3
"""
Check KEP readiness (formerly "PRR freeze") for a kubernetes/enhancements
tracking issue, and draft the reminder comment to post on it.

Usage:
    python3 check_kep_readiness.py <issue-number>

Requires: `gh` CLI, authenticated (gh auth status), and PyYAML.
Only reads from GitHub (kubernetes/enhancements + the KEP author's fork if
the KEP PR is still open). Never posts or modifies anything.
"""
import argparse
import base64
import json
import os
import re
import subprocess
import sys
from datetime import datetime, timezone

import yaml

REPO = "kubernetes/enhancements"
SIG_RELEASE_REPO = "kubernetes/sig-release"
TARGET_MILESTONE = "v1.38"

# Fallback deadline info, used only if the live fetch from kubernetes/sig-release
# (load_release_deadlines(), called once at the top of main()) fails or can't be
# parsed -- e.g. no network, or the release doc's format changed. Keeping these
# in sync with reality is a nice-to-have now, not a hard requirement, since the
# live fetch is what actually drives behavior; TARGET_MILESTONE above is the one
# thing that still needs a manual update each cycle (see "Updating for a new
# release cycle").
KEP_READINESS_DEADLINE_FALLBACK = (
    "Tuesday 22nd September 2026 (AoE) / Wednesday 23th September 2026 12:00 UTC"
)
KEP_READINESS_DEADLINE_UTC_FALLBACK = datetime(2026, 9, 23, 12, 0, tzinfo=timezone.utc)
ENHANCEMENTS_FREEZE_FALLBACK = (
    "Tuesday 29th September 2026 (AoE) / Wednesday 30th September 2026 12:00 UTC"
)

# Populated by load_release_deadlines() at the start of main() -- module-level
# so the existing f-string references throughout this file keep working.
KEP_READINESS_DEADLINE = KEP_READINESS_DEADLINE_FALLBACK
KEP_READINESS_DEADLINE_UTC = KEP_READINESS_DEADLINE_UTC_FALLBACK
ENHANCEMENTS_FREEZE = ENHANCEMENTS_FREEZE_FALLBACK

MONTH_NUMBERS = {
    "january": 1, "february": 2, "march": 3, "april": 4, "may": 5, "june": 6,
    "july": 7, "august": 8, "september": 9, "october": 10, "november": 11, "december": 12,
}

QUESTIONNAIRE_REQUIRED_SECTIONS = {
    "alpha": ["Feature Enablement and Rollback"],
    "beta": [
        "Feature Enablement and Rollback",
        "Rollout, Upgrade and Rollback Planning",
        "Monitoring Requirements",
        "Dependencies",
        "Scalability",
    ],
    "stable": [
        "Feature Enablement and Rollback",
        "Rollout, Upgrade and Rollback Planning",
        "Monitoring Requirements",
        "Dependencies",
        "Scalability",
        "Troubleshooting",
    ],
}

PLACEHOLDER_MARKERS = ["to be completed"]

PR_FIELDS = "number,state,mergedAt,author,headRefName,headRepository,files,url,createdAt"


# --------------------------------------------------------------------------
# GitHub access helpers (all read-only)
# --------------------------------------------------------------------------

def gh_json(*args):
    out = subprocess.run(["gh", *args], capture_output=True, text=True)
    if out.returncode != 0:
        raise RuntimeError(f"gh {' '.join(args)} failed: {out.stderr.strip()}")
    return json.loads(out.stdout)


def fetch_file(owner_repo, path, ref=None):
    """Return decoded text content of a file, or None if it doesn't exist."""
    url = f"repos/{owner_repo}/contents/{path}"
    if ref:
        url += f"?ref={ref}"
    out = subprocess.run(["gh", "api", url], capture_output=True, text=True)
    if out.returncode != 0:
        return None
    try:
        data = json.loads(out.stdout)
        return base64.b64decode(data["content"]).decode("utf-8")
    except (json.JSONDecodeError, KeyError):
        return None


def fetch_master_tree():
    out = subprocess.run(
        ["gh", "api", f"repos/{REPO}/git/trees/master?recursive=1"],
        capture_output=True,
        text=True,
    )
    if out.returncode != 0:
        return []
    data = json.loads(out.stdout)
    return [t["path"] for t in data.get("tree", [])]


def find_kep_dir_on_master(tree, issue_number):
    pattern = re.compile(rf"^keps/([^/]+)/{issue_number}-[^/]+/kep\.yaml$")
    for path in tree:
        m = pattern.match(path)
        if m:
            return path.rsplit("/", 1)[0], m.group(1)
    return None, None


def get_master_stage(kep_yaml_path):
    """Read `stage` from kep.yaml as currently merged, for the graduation check."""
    content = fetch_file(REPO, kep_yaml_path)
    if content is None:
        return None
    try:
        return (yaml.safe_load(content) or {}).get("stage")
    except (yaml.YAMLError, ValueError):
        # A malformed but timestamp-shaped value (e.g. a creation-date with an
        # invalid day/month) makes PyYAML's implicit date resolver raise a
        # raw ValueError rather than YAMLError -- catch that too so one KEP's
        # bad YAML doesn't take down a whole batch run.
        return None


def last_merged_pr_for_path(path):
    """When no open PR touches this KEP, attribute ownership to whoever
    authored the most recent merged change to kep.yaml, via the commit
    history on that path (squash-merge commit messages end in '(#NNNN)')."""
    out = subprocess.run(
        ["gh", "api", f"repos/{REPO}/commits?path={path}&per_page=1"],
        capture_output=True, text=True,
    )
    if out.returncode != 0:
        return None, None
    try:
        commits = json.loads(out.stdout)
    except json.JSONDecodeError:
        return None, None
    if not commits:
        return None, None
    commit = commits[0]
    author_login = (commit.get("author") or {}).get("login")
    message = (commit.get("commit") or {}).get("message", "")
    m = re.search(r"\(#(\d+)\)", message)
    pr_url = f"https://github.com/{REPO}/pull/{m.group(1)}" if m else None
    return author_login, pr_url


# --------------------------------------------------------------------------
# Fetching the KEP Readiness Deadline and Enhancements Freeze dates live from
# kubernetes/sig-release, instead of relying on hardcoded constants that need
# a manual update every release cycle. Falls back to the *_FALLBACK constants
# above if the page can't be fetched or its format has changed.
# --------------------------------------------------------------------------

def extract_timeline_row(text, keyword):
    """Find the Markdown table row in the release README's Timeline section
    whose first (bolded "What") column contains `keyword`, and return its
    cells. Row shape: | What | Who | When | Week | Release Signal |.

    Requires the "What" cell to start with "**Begin" -- the actual deadline
    row (e.g. "**Begin enforcing [KEP Readiness Deadline]**") -- because an
    earlier row in the same table ("Call for KEP Readiness Deadline and
    Enhancement Freeze Exceptions") also contains this keyword but is a
    different, unrelated date (when exceptions can be requested, not the
    deadline itself)."""
    for line in text.splitlines():
        line = line.strip()
        if not line.startswith("|") or "**Begin" not in line or keyword not in line:
            continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        if len(cells) >= 3:
            return cells
    return None


def parse_utc_datetime_from_when(when_text):
    """The 'When' column reads like
    '**Tuesday 22nd September 2026 (AoE) / Wednesday 23th September 2026 12:00 UTC**'
    -- two dates separated by '/', the AoE one and the actual UTC instant.
    Parse the second (UTC) one; returns None if the format doesn't match."""
    m = re.search(
        r"/\s*\w+\s+(\d{1,2})\w*\s+(\w+)\s+(\d{4})[, ]+(\d{1,2}):(\d{2})\s*UTC",
        when_text,
    )
    if not m:
        return None
    day, month_name, year, hour, minute = m.groups()
    month = MONTH_NUMBERS.get(month_name.lower())
    if not month:
        return None
    try:
        return datetime(int(year), month, int(day), int(hour), int(minute), tzinfo=timezone.utc)
    except ValueError:
        return None


def load_release_deadlines():
    """Return (kep_readiness_deadline_str, kep_readiness_deadline_utc,
    enhancements_freeze_str), fetched live from the current release's
    README on kubernetes/sig-release. Falls back to the hardcoded
    *_FALLBACK constants (with a note printed to stderr) if the fetch or
    parse fails for any reason -- this must never raise and block a run."""
    release_number = TARGET_MILESTONE.lstrip("vV")
    path = f"releases/release-{release_number}/README.md"
    try:
        text = fetch_file(SIG_RELEASE_REPO, path)
        if text is None:
            raise RuntimeError(f"{SIG_RELEASE_REPO}/{path} not found")
        kep_row = extract_timeline_row(text, "KEP Readiness Deadline")
        freeze_row = extract_timeline_row(text, "Enhancements Freeze")
        if not kep_row:
            raise RuntimeError("could not find the 'KEP Readiness Deadline' row in the Timeline table")
        kep_when = kep_row[2].strip("*")
        kep_utc = parse_utc_datetime_from_when(kep_when)
        if kep_utc is None:
            raise RuntimeError(f"could not parse a UTC datetime out of: {kep_when!r}")
        freeze_when = freeze_row[2].strip("*") if freeze_row else ENHANCEMENTS_FREEZE_FALLBACK
        return kep_when, kep_utc, freeze_when
    except RuntimeError as e:
        print(
            f"warning: could not load live release dates from {SIG_RELEASE_REPO}/{path} "
            f"({e}) -- falling back to hardcoded dates, which may be stale.",
            file=sys.stderr,
        )
        return (
            KEP_READINESS_DEADLINE_FALLBACK,
            KEP_READINESS_DEADLINE_UTC_FALLBACK,
            ENHANCEMENTS_FREEZE_FALLBACK,
        )


# --------------------------------------------------------------------------
# Finding the KEP's own PR via GitHub cross-references (NOT the issue body,
# which can go stale -- see the "PRs by stage and milestone" checklist that
# contributors often forget to update as a KEP moves through many PRs).
# --------------------------------------------------------------------------

def find_crossreferenced_open_prs(issue_number):
    """GitHub automatically records a 'cross-referenced' timeline event on
    an issue whenever some PR's body or *comments* mention '#N' or a link
    to it -- catches mentions that a plain text search of the PR body
    alone would miss (e.g. a mention left in a review comment)."""
    out = subprocess.run(
        ["gh", "api", f"repos/{REPO}/issues/{issue_number}/timeline", "--paginate"],
        capture_output=True, text=True,
    )
    if out.returncode != 0:
        return []
    try:
        events = json.loads(out.stdout)
    except json.JSONDecodeError:
        return []
    seen = set()
    numbers = []
    for e in events:
        if e.get("event") != "cross-referenced":
            continue
        src = (e.get("source") or {}).get("issue") or {}
        if not src.get("pull_request"):
            continue
        if src.get("state") != "open":
            continue
        repo_url = src.get("repository_url", "")
        if repo_url.rsplit("/repos/", 1)[-1] != REPO:
            continue
        number = src.get("number")
        if number and number not in seen:
            seen.add(number)
            numbers.append(number)
    return numbers


def find_prs_by_text_search(issue_number):
    """PRs whose *title* or *body* text mentions the issue number, via
    GitHub search. Catches PRs like kubernetes/enhancements#5672, titled
    "KEP-4958: ..." with the issue number right in the title, whose body
    never actually links the issue (an empty "Issue link:" template field)
    -- so no cross-reference timeline event was ever created for it."""
    out = subprocess.run(
        ["gh", "search", "prs", f"{issue_number} in:title,body",
         "--repo", REPO, "--state", "open", "--json", "number"],
        capture_output=True, text=True,
    )
    if out.returncode != 0:
        return []
    try:
        results = json.loads(out.stdout)
    except json.JSONDecodeError:
        return []
    return [r["number"] for r in results]


def find_prs_from_issue_body(issue_body, target_milestone):
    """Last resort: the issue's own "PRs by stage and milestone" checklist
    (or an older KEP's equivalent free-form list) can still name the right
    PR even when it's gone stale in other ways -- so any enhancements-repo
    PR link appearing on a line that also mentions the target milestone is
    still worth trying as a candidate, just not trusted on its own (every
    candidate from every source is confirmed by touches_kep_dir() below)."""
    if not issue_body:
        return []
    active = strip_html_comments(issue_body)
    ver_num = re.escape(target_milestone.lstrip("vV"))
    milestone_pat = re.compile(rf"(?<![\d.]){ver_num}(?![\d.])")
    pr_pat = re.compile(r"https://github\.com/kubernetes/enhancements/pull/(\d+)")
    numbers = []
    for line in active.splitlines():
        if milestone_pat.search(line):
            numbers.extend(int(n) for n in pr_pat.findall(line))
    return numbers


def touches_kep_dir(pr, issue_number):
    """A candidate PR only really is *this* KEP's PR if it actually touches
    this KEP's own directory. Merely mentioning '#<issue_number>' -- e.g. as
    a "related to" note from a completely different KEP's PR, or a stray
    match from a text search -- is NOT enough on its own."""
    pattern = re.compile(rf"^keps/[^/]+/{issue_number}-[^/]+/")
    return any(pattern.match(f["path"]) for f in pr["files"])


def find_kep_pr(issue_number, issue_body):
    """Return (confirmed_pr_or_None, other_confirmed_prs) -- the PR(s) that
    (a) are surfaced by at least one of three independent signals -- a
    GitHub cross-reference, a title/body text search, or the issue body's
    own PR checklist -- AND (b) actually touch this KEP's own directory.
    When more than one open PR does (e.g. a stray leftover from an earlier
    stage), the most recently created one is treated as authoritative and
    the rest are surfaced as an action item by the caller.
    """
    candidates = set(find_crossreferenced_open_prs(issue_number))
    candidates.update(find_prs_by_text_search(issue_number))
    candidates.update(find_prs_from_issue_body(issue_body, TARGET_MILESTONE))

    confirmed = []
    for number in candidates:
        pr = gh_json("pr", "view", str(number), "--repo", REPO, "--json", PR_FIELDS)
        if pr["state"] == "OPEN" and touches_kep_dir(pr, issue_number):
            confirmed.append(pr)
    confirmed.sort(key=lambda p: p.get("createdAt") or "", reverse=True)
    if not confirmed:
        return None, []
    return confirmed[0], confirmed[1:]


# --------------------------------------------------------------------------
# Resolving a batch of issue numbers from an Enhancement Contact or a SIG,
# instead of the caller having to already know the issue numbers. Both read
# the actual v1.38 Release Tracking board (org "kubernetes", project 269)
# via the Projects v2 GraphQL API -- this needs the `project` (or
# `read:project`) OAuth scope (`gh auth refresh -s read:project`), which is
# NOT covered by the `repo` scope used everywhere else in this script.
#
# "Enhancements Contact" is a genuinely different person from the issue's
# GitHub assignee: it's the Enhancements *team* member responsible for
# reminding the KEP's actual owner/assignee about deadlines, not the KEP
# owner themselves. It's a fixed-roster single-select field on the board
# (e.g. options like "@wendy-ha18"), not a people-picker, and not the same
# as the issue's "Assignees" field (which the board also tracks separately).
# --------------------------------------------------------------------------

PROJECT_ORG = "kubernetes"
PROJECT_NUMBER = 269

PROJECT_ITEMS_QUERY = """
query($cursor: String) {
  organization(login: "%s") {
    projectV2(number: %d) {
      items(first: 100, after: $cursor) {
        pageInfo { hasNextPage endCursor }
        nodes {
          content {
            __typename
            ... on Issue {
              number
              repository { nameWithOwner }
            }
          }
          fieldValues(first: 30) {
            nodes {
              ... on ProjectV2ItemFieldSingleSelectValue {
                name
                field { ... on ProjectV2SingleSelectField { name } }
              }
            }
          }
        }
      }
    }
  }
}
""" % (PROJECT_ORG, PROJECT_NUMBER)


def fetch_project_items():
    """Fetch every item on the v1.38 Release Tracking board, paginated."""
    items = []
    cursor = None
    while True:
        args = ["gh", "api", "graphql", "-f", f"query={PROJECT_ITEMS_QUERY}"]
        if cursor:
            args += ["-F", f"cursor={cursor}"]
        out = subprocess.run(args, capture_output=True, text=True)
        if out.returncode != 0:
            raise RuntimeError(
                f"querying the v1.38 tracking board (project {PROJECT_NUMBER}) failed "
                f"-- make sure `gh auth refresh -s read:project` has been run: {out.stderr.strip()}"
            )
        page = json.loads(out.stdout)["data"]["organization"]["projectV2"]["items"]
        items.extend(page["nodes"])
        if not page["pageInfo"]["hasNextPage"]:
            break
        cursor = page["pageInfo"]["endCursor"]
    return items


def project_field_value(item_node, field_name):
    for fv in (item_node.get("fieldValues") or {}).get("nodes", []):
        field = fv.get("field") or {}
        if field.get("name") == field_name:
            return fv.get("name")
    return None


def project_issue_numbers_matching(field_name, target_value):
    numbers = []
    for node in fetch_project_items():
        content = node.get("content") or {}
        if content.get("__typename") != "Issue":
            continue
        if (content.get("repository") or {}).get("nameWithOwner") != REPO:
            continue
        if project_field_value(node, field_name) == target_value:
            numbers.append(str(content["number"]))
    return numbers


def resolve_issues_by_enhancement_contact(handle):
    target = f"@{handle.strip().lstrip('@')}"
    return project_issue_numbers_matching("Enhancements Contact", target)


def normalize_sig_option(sig):
    """Accept 'sig-node', 'sig/node', or just 'node' (case-insensitive) and
    return the board's actual SIG field format: 'sig-node'."""
    s = sig.strip().lower().replace("_", "-")
    if s.startswith("sig/"):
        s = "sig-" + s[len("sig/"):]
    elif not s.startswith("sig-"):
        s = f"sig-{s}"
    return s


def resolve_issues_by_sig(sig):
    target = normalize_sig_option(sig)
    return project_issue_numbers_matching("SIG", target)


# --------------------------------------------------------------------------
# kep.yaml / PRR approval file / PRR questionnaire checks
# --------------------------------------------------------------------------

def norm_version(v):
    """Normalize a milestone version string for comparison (tolerate a missing 'v' prefix)."""
    return str(v or "").strip().lstrip("vV")


def check_kep_yaml(content, stage, target_milestone, is_graduating):
    """Validate kep.yaml against the KEP Readiness requirements in
    https://github.com/kubernetes/sig-release/blob/master/releases/release_phases.md#prr-freeze:

        - `stage` set to the current stage
        - `latest-milestone` set to the current release
        - `milestone` struct updated with the current stage and release
          (ONLY IF graduating to a new stage)

    `is_graduating` tells us whether `stage` actually changed relative to
    what's currently merged -- if the KEP is just continuing at the same
    stage as last release, `milestone.<stage>` is allowed to still show the
    older release when that stage was first reached, per the policy above.
    """
    try:
        data = yaml.safe_load(content) or {}
    except (yaml.YAMLError, ValueError) as e:
        return [f"kep.yaml failed to parse: {e}"]
    problems = []
    if data.get("stage") != stage:
        problems.append(f"`stage` is `{data.get('stage')}`, expected `{stage}`")
    if norm_version(data.get("latest-milestone")) != norm_version(target_milestone):
        problems.append(
            f"`latest-milestone` is `{data.get('latest-milestone')}`, expected `{target_milestone}`"
        )
    if is_graduating:
        milestone_struct = data.get("milestone") or {}
        stage_milestone = milestone_struct.get(stage)
        if norm_version(stage_milestone) != norm_version(target_milestone):
            problems.append(
                f"`milestone.{stage}` is `{stage_milestone}`, expected `{target_milestone}` "
                f"(this KEP appears to be graduating to {stage} this cycle)"
            )
    # else: per release_phases.md, `milestone.<stage>` only needs to be
    # updated when graduating to a new stage -- no check when staying put.
    return problems


def check_prr_approval(content, stage):
    try:
        data = yaml.safe_load(content) or {}
    except (yaml.YAMLError, ValueError) as e:
        return [f"PRR approval file failed to parse: {e}"]
    stage_block = data.get(stage)
    if not stage_block:
        return [f"no `{stage}:` entry in the PRR approval file"]
    approver = stage_block.get("approver") or stage_block.get("approvers")
    if not approver:
        return [f"`{stage}:` entry has no approver assigned"]
    return []


def extract_readme_prr_section(readme_text):
    m = re.search(r"^## Production Readiness Review Questionnaire\s*$", readme_text, re.M)
    if not m:
        return None
    start = m.end()
    rest = readme_text[start:]
    next_h2 = re.search(r"^## ", rest, re.M)
    end = start + next_h2.start() if next_h2 else len(readme_text)
    return readme_text[start:end]


def strip_html_comments(text):
    return re.sub(r"<!--.*?-->", "", text, flags=re.S)


def check_questionnaire(prr_section, stage):
    """Heuristic: flag a required subsection as unanswered if, once HTML
    comments and headings are stripped, there's *nothing* left, or it's
    still a literal "To be completed for X" placeholder. A short but real
    answer (e.g. "No.") must NOT be flagged -- that's a valid, complete
    answer, not a gap.

    This is a heuristic, not a source of truth -- always spot-check.
    """
    required = QUESTIONNAIRE_REQUIRED_SECTIONS.get(stage, QUESTIONNAIRE_REQUIRED_SECTIONS["alpha"])
    parts = re.split(r"^### (.+)$", prr_section, flags=re.M)
    sections = {}
    for i in range(1, len(parts), 2):
        heading = parts[i].strip()
        body = parts[i + 1] if i + 1 < len(parts) else ""
        sections[heading] = body

    unanswered = []
    for name in required:
        body = sections.get(name)
        if body is None:
            unanswered.append(f"{name} (section not found)")
            continue
        cleaned = strip_html_comments(body)
        cleaned_no_headings = "\n".join(
            line for line in cleaned.splitlines() if not line.strip().startswith("#")
        )
        stripped = cleaned_no_headings.strip()
        low = stripped.lower()
        if len(stripped) == 0 or any(marker in low for marker in PLACEHOLDER_MARKERS):
            unanswered.append(name)
    return unanswered


# --------------------------------------------------------------------------
# Report rendering -- builds Markdown, never prints the full report to the
# terminal. Everything goes to a report/kep-readiness-<timestamp>.md file;
# the terminal only gets a short pointer to it.
# --------------------------------------------------------------------------

def checkbox(ok):
    return "x" if ok else " "


def pr_label(kep_pr_url):
    """'PR #6267', or None if there's no PR at all."""
    if not kep_pr_url:
        return None
    m = re.search(r"/pull/(\d+)$", kep_pr_url)
    return f"PR #{m.group(1)}" if m else "PR"


def pr_link_md(kep_pr_url):
    """'[PR #6267](url)' for use in a table cell, or '--' when there's none."""
    label = pr_label(kep_pr_url)
    return f"[{label}]({kep_pr_url})" if label else "--"


def pr_mention_line(kep_pr_url):
    """One-sentence, unambiguous statement of which PR (if any) these checks
    were made against -- stated once, clearly, near the top of the draft
    comment, rather than repeated as a suffix on all three checklist lines."""
    label = pr_label(kep_pr_url)
    if label:
        return f"This is based on the KEP update [{label}]({kep_pr_url})."
    return "No open KEP update PR was found for this issue -- these checks reflect what's currently merged."


def md_escape_cell(s):
    """Make a string safe to embed in a Markdown table cell."""
    return (s or "").replace("|", "\\|").replace("\n", " ").strip()


def decide_status(all_ok, past_deadline):
    if all_ok:
        return "Tracked for KEP readiness"
    if past_deadline:
        return "Removed from Milestone"
    return "At risk for KEP readiness"


def render_issue_markdown(result):
    """Return (decision, markdown_block) for one successfully-checked issue."""
    issue = result["issue"]
    owner_login = result["owner_login"]
    target_stage = result["target_stage"]
    action_items = result["action_items"]
    questionnaire_ok = result["questionnaire_ok"]
    kep_yaml_ok = result["kep_yaml_ok"]
    prr_approval_ok = result["prr_approval_ok"]
    kep_pr_url = result["kep_pr_url"]
    milestone_ok = result["milestone_ok"]
    all_ok = result["all_ok"]

    past_deadline = datetime.now(timezone.utc) >= KEP_READINESS_DEADLINE_UTC
    decision = decide_status(all_ok, past_deadline)

    owner_mention = f"@{owner_login}" if owner_login else "{enhancement owner}"
    stage_display = target_stage or "{stage}"
    pr_line = pr_mention_line(kep_pr_url)

    if all_ok:
        comment = f"""\
Hello {owner_mention} :wave:, 1.38 Enhancements team here.

This is a reminder of the upcoming [KEP readiness (formerly named PRR freeze)](https://github.com/kubernetes/sig-release/blob/master/releases/release_phases.md#prr-freeze) on **{KEP_READINESS_DEADLINE}**.

This enhancement is targeting stage `{stage_display}` for 1.38 (correct me, if otherwise). {pr_line}

Here's where this enhancement currently stands:

- [x] PR open or merged with the KEP's [PRR questionnaire](https://github.com/kubernetes/enhancements/tree/master/keps/NNNN-kep-template#production-readiness-review-questionnaire) filled out.
- [x] PR open or merged with [kep.yaml](https://github.com/kubernetes/enhancements/blob/master/keps/NNNN-kep-template/kep.yaml) updated with the `stage`, `latest-milestone`, and `milestone` struct filled out.
- [x] PR open or merged with a [PRR approval file](https://github.com/kubernetes/enhancements/blob/master/keps/prod-readiness/template/nnnn.yaml) with the PRR approver listed for the stage the KEP is targeting.

Note that the PR is not required to be approved or merged by the KEP readiness (formerly named PRR freeze) deadline. Having the PRR questionnaire filled out by the deadline will help ensure that the PRR team has enough time to review your KEP before **enhancements freeze on {ENHANCEMENTS_FREEZE}**. For more information on the PRR process, see [here](https://github.com/kubernetes/community/blob/master/sig-architecture/production-readiness.md#submitting-a-kep-for-production-readiness-approval).

With all the KEP readiness (formerly named PRR freeze) requirements in place, this enhancement is now marked as `Tracked for KEP readiness`! Please keep the issue description up-to-date with appropriate stages as well.

/label tracked/yes"""
    elif past_deadline:
        bullet_items = "\n".join(f"- {item}" for item in action_items) if action_items else "- (see status above)"
        comment = f"""\
Hello {owner_mention} :wave:, 1.38 Enhancements team here.

This is a follow-up on the [KEP readiness (formerly named PRR freeze)](https://github.com/kubernetes/sig-release/blob/master/releases/release_phases.md#prr-freeze) deadline, which passed on **{KEP_READINESS_DEADLINE}**.

This enhancement was targeting stage `{stage_display}` for 1.38 (correct me, if otherwise). {pr_line}

Here's where this enhancement currently stands:

- [{checkbox(questionnaire_ok)}] PR open or merged with the KEP's [PRR questionnaire](https://github.com/kubernetes/enhancements/tree/master/keps/NNNN-kep-template#production-readiness-review-questionnaire) filled out.
- [{checkbox(kep_yaml_ok)}] PR open or merged with [kep.yaml](https://github.com/kubernetes/enhancements/blob/master/keps/NNNN-kep-template/kep.yaml) updated with the `stage`, `latest-milestone`, and `milestone` struct filled out.
- [{checkbox(prr_approval_ok)}] PR open or merged with a [PRR approval file](https://github.com/kubernetes/enhancements/blob/master/keps/prod-readiness/template/nnnn.yaml) with the PRR approver listed for the stage the KEP is targeting.

The following were still missing at the deadline:
{bullet_items}

Per the [KEP readiness policy](https://github.com/kubernetes/sig-release/blob/master/releases/release_phases.md#prr-freeze), an enhancement that doesn't meet these requirements by the deadline is removed from the milestone. This enhancement is now marked as `Removed from Milestone` for 1.38.

If you'd like this enhancement to remain in the v1.38 milestone, please file an [exception request](https://github.com/kubernetes/sig-release/blob/master/releases/EXCEPTIONS.md) as soon as possible. Thank you!"""
    else:
        bullet_items = "\n".join(f"- {item}" for item in action_items) if action_items else "- (see status above)"
        comment = f"""\
Hello {owner_mention} :wave:, 1.38 Enhancements team here.

This is a reminder of the upcoming [KEP readiness (formerly named PRR freeze)](https://github.com/kubernetes/sig-release/blob/master/releases/release_phases.md#prr-freeze) on **{KEP_READINESS_DEADLINE}**.

This enhancement is targeting stage `{stage_display}` for 1.38 (correct me, if otherwise). {pr_line}

Here's where this enhancement currently stands:

- [{checkbox(questionnaire_ok)}] PR open or merged with the KEP's [PRR questionnaire](https://github.com/kubernetes/enhancements/tree/master/keps/NNNN-kep-template#production-readiness-review-questionnaire) filled out.
- [{checkbox(kep_yaml_ok)}] PR open or merged with [kep.yaml](https://github.com/kubernetes/enhancements/blob/master/keps/NNNN-kep-template/kep.yaml) updated with the `stage`, `latest-milestone`, and `milestone` struct filled out.
- [{checkbox(prr_approval_ok)}] PR open or merged with a [PRR approval file](https://github.com/kubernetes/enhancements/blob/master/keps/prod-readiness/template/nnnn.yaml) with the PRR approver listed for the stage the KEP is targeting.

For this KEP, we would just need to update the following:
{bullet_items}

Note that the PR is not required to be approved or merged by the KEP readiness (formerly named PRR freeze) deadline. Having the PRR questionnaire filled out by the deadline will help ensure that the PRR team has enough time to review your KEP before **enhancements freeze on {ENHANCEMENTS_FREEZE}**. For more information on the PRR process, see [here](https://github.com/kubernetes/community/blob/master/sig-architecture/production-readiness.md#submitting-a-kep-for-production-readiness-approval).

The status of this enhancement is marked as `At risk for KEP readiness`. Please keep the issue description up-to-date with appropriate stages as well.

If you anticipate missing KEP readiness (formerly named PRR freeze), you can file an [exception request](https://github.com/kubernetes/sig-release/blob/master/releases/EXCEPTIONS.md) in advance. Thank you!"""

    row = summary_row(result, decision)
    lines = [
        f"### #{issue['number']} \u2014 {issue['title']}",
        "",
        "**Summary**",
        "",
        build_summary_table([row]),
        "",
        "**KEP Readiness**",
        "",
        f"- PRR questionnaire: {'\u2705' if questionnaire_ok else '\u274c'}",
        f"- `kep.yaml`: {'\u2705' if kep_yaml_ok else '\u274c'}",
        f"- PRR approval file: {'\u2705' if prr_approval_ok else '\u274c'}",
        "",
        "**Outstanding actions**",
        "",
    ]
    if action_items:
        lines += [f"- {item}" for item in action_items]
    else:
        lines.append("- None -- all criteria met.")
    lines += [
        "",
        "**Draft GitHub comment**",
        "",
        "*(review before posting -- do not auto-post)*",
        "",
        "```markdown",
        comment,
        "```",
    ]
    return decision, "\n".join(lines)


def summary_row(result, decision):
    issue = result["issue"]
    title = md_escape_cell(issue["title"])
    issue_cell = f"[#{issue['number']}]({issue['url']}) {title}"
    pr_cell = pr_link_md(result["kep_pr_url"])
    owner_cell = f"@{result['owner_login']}" if result["owner_login"] else "UNKNOWN"
    stage_cell = result["target_stage"] or "UNKNOWN"
    milestone_cell = "yes" if result["milestone_ok"] else "NO"
    return (issue_cell, pr_cell, owner_cell, stage_cell, milestone_cell, decision)


def summary_row_for_error(issue_number):
    return (f"#{issue_number}", "--", "--", "--", "--", "FAILED (see detail section)")


def error_markdown(issue_number, error):
    return f"### #{issue_number} \u2014 FAILED\n\nCould not check this issue: {error}\n"


def build_summary_table(rows):
    header = (
        f"| Issue | KEP PR | Enhancement owner (KEP PR author) | Target stage for {TARGET_MILESTONE} "
        f"| In {TARGET_MILESTONE} milestone | Recommended {TARGET_MILESTONE} tracking board status |"
    )
    sep = "|---|---|---|---|---|---|"
    body = "\n".join(f"| {a} | {b} | {c} | {d} | {e} | {f} |" for a, b, c, d, e, f in rows)
    return "\n".join([header, sep, body])


def build_report_document(issue_numbers, rows, sections, input_description):
    generated = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    header = "\n".join([
        f"# KEP Readiness Report -- {TARGET_MILESTONE}",
        "",
        f"Generated: {generated}",
        f"Issues checked: {len(issue_numbers)}",
        f"Generate draft reminder comment for {input_description}.",
        "",
        "## Summary",
        "",
        build_summary_table(rows),
    ])
    body = "\n\n---\n\n".join(sections)
    return header + "\n\n---\n\n" + body + "\n"


def write_report(doc):
    """Always write a new file, never overwrite a previous run's report.
    Written to the current working directory -- the repo root, alongside
    README.md, per this skill's usage instructions (run from the repo root).
    The timestamp alone (second granularity) could collide if two runs
    happen within the same second -- fall back to a numeric suffix rather
    than ever opening an existing path for writing."""
    timestamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    base = f"kep-readiness-{timestamp}"
    path = f"{base}.md"
    suffix = 1
    while os.path.exists(path):
        path = f"{base}-{suffix}.md"
        suffix += 1
    with open(path, "w") as f:
        f.write(doc)
    return path


# --------------------------------------------------------------------------
# Main
# --------------------------------------------------------------------------

def get_gh_scopes():
    """Parse 'Token scopes: ...' out of `gh auth status` (which writes to
    stderr, not stdout)."""
    out = subprocess.run(["gh", "auth", "status"], capture_output=True, text=True)
    combined = out.stdout + out.stderr
    m = re.search(r"Token scopes:\s*(.+)", combined)
    if not m:
        return set()
    return {s.strip().strip("'\"") for s in m.group(1).split(",")}


def run_preflight():
    """Check gh auth scope and v1.38 tracking board access, and print the
    resolved release dates -- run this before asking the user what to
    check, per this skill's design. Returns True if everything's usable."""
    ok = True

    scopes = get_gh_scopes()
    if "project" in scopes or "read:project" in scopes:
        print(f"OK   gh token has project scope (scopes: {', '.join(sorted(scopes)) or 'none'})")
    else:
        print(f"FAIL gh token is missing the `project` scope (scopes: {', '.join(sorted(scopes)) or 'none'})")
        print("     Fix: run `gh auth refresh -s read:project` (interactive; opens a browser flow).")
        ok = False

    if ok:
        try:
            items = fetch_project_items()
            print(f"OK   v1.38 tracking board (project {PROJECT_NUMBER}) is readable -- {len(items)} item(s) found.")
        except RuntimeError as e:
            print(f"FAIL could not read the v1.38 tracking board: {e}")
            ok = False

    kep_when, kep_utc, freeze_when = load_release_deadlines()
    print(f"KEP Readiness Deadline: {kep_when}")
    print(f"Enhancements Freeze:    {freeze_when}")
    print()
    print("All checks passed -- ready to take input." if ok else "Preflight FAILED -- fix the above before proceeding.")
    return ok


def parse_args():
    parser = argparse.ArgumentParser(
        description="Check KEP readiness for one or more kubernetes/enhancements issues.",
    )
    parser.add_argument(
        "--preflight", action="store_true",
        help="Check gh auth scope and v1.38 tracking board access, print the result, and exit "
             "(no issue is checked). Run this before asking the user what to review.",
    )
    group = parser.add_mutually_exclusive_group()
    group.add_argument(
        "--contact", metavar="GITHUB_HANDLE",
        help="Check every issue on the v1.38 tracking board whose Enhancements "
             "Contact field is this GitHub handle, instead of listing issue numbers.",
    )
    group.add_argument(
        "--sig", metavar="SIG_NAME",
        help="Check every issue on the v1.38 tracking board whose SIG field matches "
             "(e.g. sig-node, sig/node, or just node), instead of listing issue numbers.",
    )
    parser.add_argument(
        "issue_numbers", nargs="*",
        help="One or more kubernetes/enhancements issue numbers.",
    )
    args = parser.parse_args()
    if args.preflight:
        return args
    if not args.contact and not args.sig and not args.issue_numbers:
        parser.error("provide issue number(s), or --contact <github-handle>, or --sig <sig-name>")
    if (args.contact or args.sig) and args.issue_numbers:
        parser.error("--contact/--sig can't be combined with explicit issue numbers")
    return args


def main():
    global KEP_READINESS_DEADLINE, KEP_READINESS_DEADLINE_UTC, ENHANCEMENTS_FREEZE
    args = parse_args()

    if args.preflight:
        sys.exit(0 if run_preflight() else 1)

    KEP_READINESS_DEADLINE, KEP_READINESS_DEADLINE_UTC, ENHANCEMENTS_FREEZE = load_release_deadlines()

    if args.contact:
        handle = args.contact.lstrip("@")
        input_description = f"Enhancement Contact @{handle}"
        try:
            issue_numbers = resolve_issues_by_enhancement_contact(args.contact)
        except RuntimeError as e:
            print(f"error: {e}", file=sys.stderr)
            sys.exit(1)
        if not issue_numbers:
            print(
                f"No issues found on the v1.38 tracking board with Enhancements Contact "
                f"@{handle}.", file=sys.stderr,
            )
            sys.exit(1)
    elif args.sig:
        sig_value = normalize_sig_option(args.sig)
        input_description = f"SIG {sig_value}"
        try:
            issue_numbers = resolve_issues_by_sig(args.sig)
        except RuntimeError as e:
            print(f"error: {e}", file=sys.stderr)
            sys.exit(1)
        if not issue_numbers:
            print(f"No issues found on the v1.38 tracking board with SIG `{sig_value}`.", file=sys.stderr)
            sys.exit(1)
    else:
        issue_numbers = args.issue_numbers
        input_description = "KEP issue(s) " + ", ".join(f"#{n}" for n in issue_numbers)

    exit_code = 0
    rows = []
    sections = []
    for issue_number in issue_numbers:
        try:
            result = check_issue(issue_number)
        except Exception as e:
            # Broad on purpose: a batch run (--sig/--contact can cover dozens
            # of issues) should never crash entirely because one KEP has some
            # unanticipated malformed file -- isolate it to that issue's row.
            exit_code = 1
            rows.append(summary_row_for_error(issue_number))
            sections.append(error_markdown(issue_number, e))
            continue
        decision, detail_md = render_issue_markdown(result)
        rows.append(summary_row(result, decision))
        sections.append(detail_md)

    doc = build_report_document(issue_numbers, rows, sections, input_description)
    path = write_report(doc)

    print(f"Report written to: {path}")
    print(f"View the summary table and full draft comment(s) there ({len(issue_numbers)} issue(s) checked).")
    sys.exit(exit_code)


def check_issue(issue_number):
    issue = gh_json(
        "issue", "view", issue_number, "--repo", REPO,
        "--json", "number,title,labels,milestone,state,url,body",
    )
    labels = [l["name"] for l in issue["labels"]]
    milestone_title = (issue.get("milestone") or {}).get("title")
    milestone_ok = milestone_title == TARGET_MILESTONE
    lead_opted_in = "lead-opted-in" in labels
    stage_labels = [l for l in labels if l.startswith("stage/")]

    action_items = []
    if not milestone_ok:
        action_items.append(
            f"Issue is not in the **{TARGET_MILESTONE}** milestone (currently: `{milestone_title or 'none'}`)."
        )
    if not lead_opted_in:
        action_items.append("Missing the `lead-opted-in` label.")

    # Target stage comes from the issue's own `stage/*` label -- a
    # maintained, canonical field -- not from the free-form issue body,
    # which can go stale as a KEP moves through many PRs over many cycles.
    target_stage = None
    if len(stage_labels) == 1:
        target_stage = stage_labels[0].split("/", 1)[1]
    elif len(stage_labels) == 0:
        action_items.append("No `stage/{alpha,beta,stable}` label on the issue -- can't determine target stage.")
    else:
        action_items.append(f"Multiple stage labels found ({stage_labels}); expected exactly one.")

    owner_login = None
    kep_pr_url = None
    questionnaire_ok = False
    kep_yaml_ok = False
    prr_approval_ok = False

    # Find the KEP's own PR by looking at GitHub's cross-reference records
    # (which PR(s) actually mention/link this issue), not the issue body.
    confirmed_pr, other_confirmed = find_kep_pr(issue_number, issue.get("body") or "")
    if other_confirmed:
        others_str = ", ".join(f"#{p['number']}" for p in other_confirmed)
        action_items.append(
            f"Multiple open PRs touch this KEP's directory -- using #{confirmed_pr['number']} "
            f"(most recently created); also found {others_str}."
        )

    tree = fetch_master_tree()
    kep_dir, sig = find_kep_dir_on_master(tree, issue_number)
    if kep_dir is None and confirmed_pr:
        pr_kep_yaml_path = next(
            (f["path"] for f in confirmed_pr["files"]
             if re.match(rf"^keps/[^/]+/{issue_number}-[^/]+/kep\.yaml$", f["path"])),
            None,
        )
        if pr_kep_yaml_path:
            kep_dir = pr_kep_yaml_path.rsplit("/", 1)[0]
            sig = kep_dir.split("/")[1]

    if kep_dir is None:
        action_items.append(
            "Could not locate the KEP directory (`keps/<sig>/<number>-*/`) on master, and no open "
            "PR referencing this issue touches it either."
        )
    else:
        kep_yaml_path = f"{kep_dir}/kep.yaml"
        readme_path = f"{kep_dir}/README.md"
        prr_path = f"keps/prod-readiness/{sig}/{issue_number}.yaml"

        if confirmed_pr:
            owner_login = confirmed_pr["author"]["login"]
            kep_pr_url = confirmed_pr["url"]
            is_open = confirmed_pr["state"] == "OPEN"
            head_repo = confirmed_pr["headRepository"]["nameWithOwner"]
            head_ref = confirmed_pr["headRefName"]
            pr_file_paths = {f["path"] for f in confirmed_pr["files"]}

            def resolve_content(path):
                """Prefer the confirmed PR's own copy of a file it touches
                (master may still hold the stale pre-PR version); otherwise
                fall back to master, assuming the file is already correct
                from an earlier, separate, merged PR."""
                if path in pr_file_paths and is_open:
                    return fetch_file(head_repo, path, ref=head_ref), "open PR"
                return fetch_file(REPO, path), "existing on master"
        else:
            # No open PR references this KEP at all -- everything must
            # already be satisfied on master. Attribute ownership to
            # whoever authored the most recent merged change to kep.yaml.
            owner_login, kep_pr_url = last_merged_pr_for_path(kep_yaml_path)

            def resolve_content(path):
                return fetch_file(REPO, path), "existing on master"

        master_stage = get_master_stage(kep_yaml_path)
        is_graduating = target_stage is not None and master_stage != target_stage

        kep_yaml_content, source = resolve_content(kep_yaml_path)
        if kep_yaml_content is None:
            action_items.append(f"`kep.yaml` not found at `{kep_yaml_path}` on master or in the open PR.")
        elif target_stage is None:
            action_items.append("Can't validate `kep.yaml` without a known target stage.")
        else:
            problems = check_kep_yaml(kep_yaml_content, target_stage, TARGET_MILESTONE, is_graduating)
            if problems:
                action_items.append(
                    f"PR updating `kep.yaml` ({source} copy) -- " + "; ".join(problems) + "."
                )
            else:
                kep_yaml_ok = True

        readme_content, _readme_source = resolve_content(readme_path)
        if readme_content is None:
            action_items.append(f"`README.md` (PRR questionnaire) not found at `{readme_path}`.")
        elif target_stage is None:
            action_items.append("Can't validate the PRR questionnaire without a known target stage.")
        else:
            prr_section = extract_readme_prr_section(readme_content)
            if prr_section is None:
                action_items.append(
                    "Could not find the `## Production Readiness Review Questionnaire` section in the README."
                )
            else:
                unanswered = check_questionnaire(prr_section, target_stage)
                if unanswered:
                    action_items.append(
                        "PR with the PRR questionnaire filled out -- still unanswered "
                        "(heuristic, please verify manually): " + ", ".join(unanswered) + "."
                    )
                else:
                    questionnaire_ok = True

        prr_content, prr_source = resolve_content(prr_path)
        if prr_content is None:
            action_items.append(f"PR with the PRR approval file -- not found at `{prr_path}`.")
        elif target_stage is None:
            action_items.append("Can't validate the PRR approval file without a known target stage.")
        else:
            problems = check_prr_approval(prr_content, target_stage)
            if problems:
                action_items.append(f"PR with the PRR approval file ({prr_source} copy) -- " + "; ".join(problems) + ".")
            else:
                prr_approval_ok = True

    all_ok = (
        milestone_ok
        and lead_opted_in
        and target_stage is not None
        and not other_confirmed
        and kep_yaml_ok
        and questionnaire_ok
        and prr_approval_ok
    )

    return {
        "issue": issue,
        "owner_login": owner_login,
        "target_stage": target_stage,
        "action_items": action_items,
        "questionnaire_ok": questionnaire_ok,
        "kep_yaml_ok": kep_yaml_ok,
        "prr_approval_ok": prr_approval_ok,
        "kep_pr_url": kep_pr_url,
        "milestone_ok": milestone_ok,
        "all_ok": all_ok,
    }


if __name__ == "__main__":
    main()
