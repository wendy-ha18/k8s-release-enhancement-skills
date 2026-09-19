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
import base64
import json
import os
import re
import subprocess
import sys
from datetime import datetime, timezone

import yaml

REPO = "kubernetes/enhancements"
TARGET_MILESTONE = "v1.38"
KEP_READINESS_DEADLINE = (
    "Tuesday 22nd September 2026 (AoE) / Wednesday 23th September 2026 12:00 UTC"
)
# The same deadline as an actual instant, used to decide whether it's already
# passed -- keep this in sync with KEP_READINESS_DEADLINE above every cycle.
KEP_READINESS_DEADLINE_UTC = datetime(2026, 9, 23, 12, 0, tzinfo=timezone.utc)
ENHANCEMENTS_FREEZE = (
    "Tuesday 29th September 2026 (AoE) / Wednesday 30th September 2026 12:00 UTC"
)

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
    except yaml.YAMLError:
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
    except yaml.YAMLError as e:
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
    except yaml.YAMLError as e:
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


def pr_ref(kep_pr_url):
    """Markdown link to append to a checklist line, e.g. ' ([PR #6267](https://...))'.
    Empty when no PR was found at all (everything already merged with no open PR)."""
    if not kep_pr_url:
        return ""
    m = re.search(r"/pull/(\d+)$", kep_pr_url)
    label = f"PR #{m.group(1)}" if m else "PR"
    return f" ([{label}]({kep_pr_url}))"


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
    pr_suffix = pr_ref(kep_pr_url)

    if all_ok:
        comment = f"""\
Hello {owner_mention} :wave:, 1.38 Enhancements team here.

This is a reminder of the upcoming [KEP readiness (formerly named PRR freeze)](https://github.com/kubernetes/sig-release/blob/master/releases/release_phases.md#prr-freeze) on **{KEP_READINESS_DEADLINE}**.

This enhancement is targeting stage `{stage_display}` for 1.38 (correct me, if otherwise)

Here's where this enhancement currently stands:

- [x] PR open or merged with the KEP's [PRR questionnaire](https://github.com/kubernetes/enhancements/tree/master/keps/NNNN-kep-template#production-readiness-review-questionnaire) filled out.{pr_suffix}
- [x] PR open or merged with [kep.yaml](https://github.com/kubernetes/enhancements/blob/master/keps/NNNN-kep-template/kep.yaml) updated with the `stage`, `latest-milestone`, and `milestone` struct filled out.{pr_suffix}
- [x] PR open or merged with a [PRR approval file](https://github.com/kubernetes/enhancements/blob/master/keps/prod-readiness/template/nnnn.yaml) with the PRR approver listed for the stage the KEP is targeting.{pr_suffix}

Note that the PR is not required to be approved or merged by the KEP readiness (formerly named PRR freeze) deadline. Having the PRR questionnaire filled out by the deadline will help ensure that the PRR team has enough time to review your KEP before **enhancements freeze on {ENHANCEMENTS_FREEZE}**. For more information on the PRR process, see [here](https://github.com/kubernetes/community/blob/master/sig-architecture/production-readiness.md#submitting-a-kep-for-production-readiness-approval).

With all the KEP readiness (formerly named PRR freeze) requirements in place, this enhancement is now marked as `Tracked for KEP readiness`! Please keep the issue description up-to-date with appropriate stages as well.

/label tracked/yes"""
    elif past_deadline:
        bullet_items = "\n".join(f"- {item}" for item in action_items) if action_items else "- (see status above)"
        comment = f"""\
Hello {owner_mention} :wave:, 1.38 Enhancements team here.

This is a follow-up on the [KEP readiness (formerly named PRR freeze)](https://github.com/kubernetes/sig-release/blob/master/releases/release_phases.md#prr-freeze) deadline, which passed on **{KEP_READINESS_DEADLINE}**.

This enhancement was targeting stage `{stage_display}` for 1.38 (correct me, if otherwise)

Here's where this enhancement currently stands:

- [{checkbox(questionnaire_ok)}] PR open or merged with the KEP's [PRR questionnaire](https://github.com/kubernetes/enhancements/tree/master/keps/NNNN-kep-template#production-readiness-review-questionnaire) filled out.{pr_suffix}
- [{checkbox(kep_yaml_ok)}] PR open or merged with [kep.yaml](https://github.com/kubernetes/enhancements/blob/master/keps/NNNN-kep-template/kep.yaml) updated with the `stage`, `latest-milestone`, and `milestone` struct filled out.{pr_suffix}
- [{checkbox(prr_approval_ok)}] PR open or merged with a [PRR approval file](https://github.com/kubernetes/enhancements/blob/master/keps/prod-readiness/template/nnnn.yaml) with the PRR approver listed for the stage the KEP is targeting.{pr_suffix}

The following were still missing at the deadline:
{bullet_items}

Per the [KEP readiness policy](https://github.com/kubernetes/sig-release/blob/master/releases/release_phases.md#prr-freeze), an enhancement that doesn't meet these requirements by the deadline is removed from the milestone. This enhancement is now marked as `Removed from Milestone` for 1.38.

If you'd like this enhancement to remain in the v1.38 milestone, please file an [exception request](https://github.com/kubernetes/sig-release/blob/master/releases/EXCEPTIONS.md) as soon as possible. Thank you!"""
    else:
        bullet_items = "\n".join(f"- {item}" for item in action_items) if action_items else "- (see status above)"
        comment = f"""\
Hello {owner_mention} :wave:, 1.38 Enhancements team here.

This is a reminder of the upcoming [KEP readiness (formerly named PRR freeze)](https://github.com/kubernetes/sig-release/blob/master/releases/release_phases.md#prr-freeze) on **{KEP_READINESS_DEADLINE}**.

This enhancement is targeting stage `{stage_display}` for 1.38 (correct me, if otherwise)

Here's where this enhancement currently stands:

- [{checkbox(questionnaire_ok)}] PR open or merged with the KEP's [PRR questionnaire](https://github.com/kubernetes/enhancements/tree/master/keps/NNNN-kep-template#production-readiness-review-questionnaire) filled out.{pr_suffix}
- [{checkbox(kep_yaml_ok)}] PR open or merged with [kep.yaml](https://github.com/kubernetes/enhancements/blob/master/keps/NNNN-kep-template/kep.yaml) updated with the `stage`, `latest-milestone`, and `milestone` struct filled out.{pr_suffix}
- [{checkbox(prr_approval_ok)}] PR open or merged with a [PRR approval file](https://github.com/kubernetes/enhancements/blob/master/keps/prod-readiness/template/nnnn.yaml) with the PRR approver listed for the stage the KEP is targeting.{pr_suffix}

For this KEP, we would just need to update the following:
{bullet_items}

Note that the PR is not required to be approved or merged by the KEP readiness (formerly named PRR freeze) deadline. Having the PRR questionnaire filled out by the deadline will help ensure that the PRR team has enough time to review your KEP before **enhancements freeze on {ENHANCEMENTS_FREEZE}**. For more information on the PRR process, see [here](https://github.com/kubernetes/community/blob/master/sig-architecture/production-readiness.md#submitting-a-kep-for-production-readiness-approval).

The status of this enhancement is marked as `At risk for KEP readiness`. Please keep the issue description up-to-date with appropriate stages as well.

If you anticipate missing KEP readiness (formerly named PRR freeze), you can file an [exception request](https://github.com/kubernetes/sig-release/blob/master/releases/EXCEPTIONS.md) in advance. Thank you!"""

    lines = [
        f"## Issue #{issue['number']}: {issue['title']}",
        "",
        f"- **URL:** {issue['url']}",
        f"- **Enhancement owner (KEP PR author):** {owner_mention if owner_login else 'UNKNOWN -- fill in manually'}",
        f"- **Target stage for {TARGET_MILESTONE}:** {target_stage or 'UNKNOWN'}",
        f"- **In {TARGET_MILESTONE} milestone:** {'yes' if milestone_ok else 'NO'}",
    ]
    if kep_pr_url:
        lines.append(f"- **KEP update PR:** {kep_pr_url}")
    lines.append(f"- **Recommended v1.38 tracking board status:** `{decision}`")
    lines.append("")
    if action_items:
        lines.append(f"**Status: NOT fully ready -- {len(action_items)} item(s) outstanding**")
        lines.append("")
        for item in action_items:
            lines.append(f"- {item}")
    else:
        lines.append("**Status: all KEP readiness criteria met.**")
    lines += [
        "",
        "### Draft comment",
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
    owner_cell = f"@{result['owner_login']}" if result["owner_login"] else "UNKNOWN"
    stage_cell = result["target_stage"] or "UNKNOWN"
    milestone_cell = "yes" if result["milestone_ok"] else "NO"
    return (issue_cell, owner_cell, stage_cell, milestone_cell, decision)


def summary_row_for_error(issue_number):
    return (f"#{issue_number}", "--", "--", "--", "FAILED (see detail section)")


def error_markdown(issue_number, error):
    return f"## Issue #{issue_number}: FAILED\n\nCould not check this issue: {error}\n"


def build_summary_table(rows):
    header = (
        f"| Issue | Enhancement owner (KEP PR author) | Target stage for {TARGET_MILESTONE} "
        f"| In {TARGET_MILESTONE} milestone | Recommended {TARGET_MILESTONE} tracking board status |"
    )
    sep = "|---|---|---|---|---|"
    body = "\n".join(f"| {a} | {b} | {c} | {d} | {e} |" for a, b, c, d, e in rows)
    return "\n".join([header, sep, body])


def build_report_document(issue_numbers, rows, sections):
    generated = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    header = "\n".join([
        f"# KEP Readiness Report -- {TARGET_MILESTONE}",
        "",
        f"Generated: {generated}",
        f"Issues checked: {len(issue_numbers)}",
        "",
        "## Summary",
        "",
        build_summary_table(rows),
    ])
    body = "\n\n---\n\n".join(sections)
    return header + "\n\n---\n\n" + body + "\n"


def write_report(doc):
    os.makedirs("report", exist_ok=True)
    timestamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    path = os.path.join("report", f"kep-readiness-{timestamp}.md")
    with open(path, "w") as f:
        f.write(doc)
    return path


# --------------------------------------------------------------------------
# Main
# --------------------------------------------------------------------------

def main():
    if len(sys.argv) < 2:
        print("usage: check_kep_readiness.py <issue-number> [<issue-number> ...]", file=sys.stderr)
        sys.exit(1)
    issue_numbers = sys.argv[1:]

    exit_code = 0
    rows = []
    sections = []
    for issue_number in issue_numbers:
        try:
            result = check_issue(issue_number)
        except RuntimeError as e:
            exit_code = 1
            rows.append(summary_row_for_error(issue_number))
            sections.append(error_markdown(issue_number, e))
            continue
        decision, detail_md = render_issue_markdown(result)
        rows.append(summary_row(result, decision))
        sections.append(detail_md)

    doc = build_report_document(issue_numbers, rows, sections)
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
