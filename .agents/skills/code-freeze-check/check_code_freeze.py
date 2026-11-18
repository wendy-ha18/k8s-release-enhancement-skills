#!/usr/bin/env python3
"""
Check Code Freeze and Test Freeze readiness for a kubernetes/enhancements
tracking issue, and draft the reminder comment to post on it.

Code and test pull requests are looked up in kubernetes/kubernetes only.
kubernetes/enhancements pull requests are KEP metadata, not this freeze.

Usage:
    python3 check_code_freeze.py <issue-number> [<issue-number> ...]
    python3 check_code_freeze.py --contact <github-handle>
    python3 check_code_freeze.py --sig <sig-name>
    python3 check_code_freeze.py --preflight

Requires: `gh` CLI, authenticated (gh auth status).
Only reads from GitHub. Never posts or modifies anything.
"""
import argparse
import base64
import json
import os
import re
import subprocess
import sys
from datetime import datetime, timezone


REPO = "kubernetes/enhancements"
K8S_REPO = "kubernetes/kubernetes"
SIG_RELEASE_REPO = "kubernetes/sig-release"
TARGET_MILESTONE = "v1.38"

# Used only when the live release timeline cannot be fetched or parsed.
# The live v1.38 row is "Begin [Code Freeze] and [Test Freeze]".
CODE_FREEZE_FALLBACK = (
    "Monday 16th November 2026 (AoE) / Tuesday 17th November 2026, 12:00 UTC"
)
CODE_FREEZE_UTC_FALLBACK = datetime(2026, 11, 17, 12, 0, tzinfo=timezone.utc)

CODE_FREEZE = CODE_FREEZE_FALLBACK
CODE_FREEZE_UTC = CODE_FREEZE_UTC_FALLBACK

MONTH_NUMBERS = {
    "january": 1, "february": 2, "march": 3, "april": 4, "may": 5, "june": 6,
    "july": 7, "august": 8, "september": 9, "october": 10, "november": 11, "december": 12,
}

PROJECT_ORG = "kubernetes"
PROJECT_NUMBER = 269

PR_FIELDS = "number,state,isDraft,mergedAt,title,url,body,labels,milestone"

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


def gh_api_list(path):
    """GET a JSON list, following GitHub pagination.

    `gh api --paginate` usually returns one JSON array. Some versions emit
    one array per page, so accept that shape too.
    """
    out = subprocess.run(
        ["gh", "api", "--paginate", path],
        capture_output=True, text=True,
    )
    if out.returncode != 0:
        raise RuntimeError(out.stderr.strip() or f"gh api {path} failed")
    text = out.stdout.strip()
    if not text:
        return []
    try:
        data = json.loads(text)
    except json.JSONDecodeError:
        decoder = json.JSONDecoder()
        items = []
        idx = 0
        while idx < len(text):
            while idx < len(text) and text[idx].isspace():
                idx += 1
            if idx >= len(text):
                break
            obj, end = decoder.raw_decode(text, idx)
            if isinstance(obj, list):
                items.extend(obj)
            else:
                items.append(obj)
            idx = end
        return items
    if isinstance(data, list):
        return data
    return [data]


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
        match = pattern.match(path)
        if match:
            return path.rsplit("/", 1)[0], match.group(1)
    return None, None


def last_merged_pr_author(path):
    """Author of the most recent merged change to kep.yaml.

    Used as the enhancement owner in the reminder comment. Returns None when
    the path has no merged pull request we can attribute.
    """
    out = subprocess.run(
        ["gh", "api", f"repos/{REPO}/commits?path={path}&per_page=1"],
        capture_output=True, text=True,
    )
    if out.returncode != 0:
        return None
    try:
        commits = json.loads(out.stdout)
    except json.JSONDecodeError:
        return None
    if not commits:
        return None
    commit = commits[0]
    author_login = (commit.get("author") or {}).get("login")
    sha = commit.get("sha")
    if not sha:
        return author_login
    pulls_out = subprocess.run(
        ["gh", "api", f"repos/{REPO}/commits/{sha}/pulls"],
        capture_output=True, text=True,
    )
    if pulls_out.returncode != 0:
        return author_login
    try:
        pulls = json.loads(pulls_out.stdout)
    except json.JSONDecodeError:
        return author_login
    merged_pulls = [pr for pr in pulls if pr.get("merged_at")]
    if not merged_pulls:
        return author_login
    merged_pulls.sort(key=lambda pr: pr.get("merged_at") or "", reverse=True)
    author_login = (merged_pulls[0].get("user") or {}).get("login") or author_login
    return author_login


# --------------------------------------------------------------------------
# Fetch the Code Freeze date live from kubernetes/sig-release.
# Code Freeze and Test Freeze share one timeline row.
# --------------------------------------------------------------------------

def extract_timeline_row(text, keyword):
    """Find the Timeline row whose "What" cell begins with "**Begin" and
    contains `keyword`. An earlier "call for exceptions" row also contains
    the keyword, but it is not the deadline."""
    for line in text.splitlines():
        line = line.strip()
        if not line.startswith("|") or "**Begin" not in line or keyword not in line:
            continue
        cells = [cell.strip() for cell in line.strip("|").split("|")]
        if len(cells) >= 3:
            return cells
    return None


def parse_utc_datetime_from_when(when_text):
    """Parse the UTC instant from a When cell such as
    'Monday 16th November 2026 (AoE) / Tuesday 17th November 2026 12:00 UTC'.
    """
    match = re.search(
        r"/\s*\w+\s+(\d{1,2})\w*\s+(\w+)\s+(\d{4})[, ]+(\d{1,2}):(\d{2})\s*UTC",
        when_text,
    )
    if not match:
        return None
    day, month_name, year, hour, minute = match.groups()
    month = MONTH_NUMBERS.get(month_name.lower())
    if not month:
        return None
    try:
        return datetime(int(year), month, int(day), int(hour), int(minute), tzinfo=timezone.utc)
    except ValueError:
        return None


def load_code_freeze():
    """Return (display string, UTC datetime) for Code Freeze / Test Freeze.

    Fall back to the bundled value if the live document is unavailable. A
    reporting run should not fail solely because its deadline source is
    temporarily unavailable.
    """
    release_number = TARGET_MILESTONE.lstrip("vV")
    path = f"releases/release-{release_number}/README.md"
    try:
        text = fetch_file(SIG_RELEASE_REPO, path)
        if text is None:
            raise RuntimeError(f"{SIG_RELEASE_REPO}/{path} not found")
        freeze_row = extract_timeline_row(text, "Code Freeze")
        if not freeze_row:
            raise RuntimeError("could not find the 'Code Freeze' row in the Timeline table")
        freeze_when = freeze_row[2].strip("*").strip()
        freeze_utc = parse_utc_datetime_from_when(freeze_when)
        if freeze_utc is None:
            raise RuntimeError(f"could not parse a UTC datetime out of: {freeze_when!r}")
        return freeze_when, freeze_utc
    except RuntimeError as exc:
        print(
            f"warning: could not load live release dates from {SIG_RELEASE_REPO}/{path} "
            f"({exc}) -- falling back to hardcoded dates, which may be stale.",
            file=sys.stderr,
        )
        return CODE_FREEZE_FALLBACK, CODE_FREEZE_UTC_FALLBACK


# --------------------------------------------------------------------------
# Tracking board lookup. Enhancements Contact is a board field, not the
# issue assignee. SIG is the board's SIG field.
# --------------------------------------------------------------------------

def fetch_project_items():
    """Fetch every item on the release tracking board, paginated."""
    items = []
    cursor = None
    while True:
        args = ["gh", "api", "graphql", "-f", f"query={PROJECT_ITEMS_QUERY}"]
        if cursor:
            args += ["-F", f"cursor={cursor}"]
        out = subprocess.run(args, capture_output=True, text=True)
        if out.returncode != 0:
            raise RuntimeError(
                f"querying the {TARGET_MILESTONE} tracking board (project {PROJECT_NUMBER}) failed "
                f"-- make sure `gh auth refresh -s read:project` has been run: {out.stderr.strip()}"
            )
        page = json.loads(out.stdout)["data"]["organization"]["projectV2"]["items"]
        items.extend(page["nodes"])
        if not page["pageInfo"]["hasNextPage"]:
            break
        cursor = page["pageInfo"]["endCursor"]
    return items


def project_field_value(item_node, field_name):
    for field_value in (item_node.get("fieldValues") or {}).get("nodes", []):
        field = field_value.get("field") or {}
        if field.get("name") == field_name:
            return field_value.get("name")
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
    """Accept 'sig-node', 'sig/node', or just 'node' and return 'sig-node'."""
    value = sig.strip().lower().replace("_", "-")
    if value.startswith("sig/"):
        value = "sig-" + value[len("sig/"):]
    elif not value.startswith("sig-"):
        value = f"sig-{value}"
    return value


def resolve_issues_by_sig(sig):
    return project_issue_numbers_matching("SIG", normalize_sig_option(sig))


# --------------------------------------------------------------------------
# kubernetes/kubernetes pull request discovery
# --------------------------------------------------------------------------

def strip_html_comments(text):
    return re.sub(r"<!--.*?-->", "", text or "", flags=re.S)


def pr_numbers_in_body(issue_body):
    """Pull request numbers linked in the issue description.

    Accepts full pull URLs and kubernetes/kubernetes#N. HTML comments are
    ignored so a stale checklist example does not count as a current link.
    """
    active = strip_html_comments(issue_body)
    patterns = (
        r"https://github\.com/kubernetes/kubernetes/pull/(\d+)",
        r"(?<![\w/])kubernetes/kubernetes#(\d+)",
    )
    numbers = set()
    for pattern in patterns:
        numbers.update(int(number) for number in re.findall(pattern, active))
    return numbers


def mentions_kep(text, issue_number):
    """True when text cites this KEP, not a longer number that merely shares a prefix."""
    number = re.escape(str(issue_number))
    patterns = (
        rf"KEP[-\s]?{number}(?!\d)",
        rf"kubernetes/enhancements#{number}(?!\d)",
        rf"kubernetes/enhancements/issues/{number}(?!\d)",
    )
    return any(re.search(pattern, text or "", flags=re.I) for pattern in patterns)


def cross_referenced_k8s_prs(issue_number):
    """kubernetes/kubernetes pull requests GitHub recorded against this issue."""
    try:
        events = gh_api_list(f"repos/{REPO}/issues/{issue_number}/timeline")
    except RuntimeError:
        return None
    numbers = set()
    for event in events:
        if event.get("event") != "cross-referenced":
            continue
        source = (event.get("source") or {}).get("issue") or {}
        if not source.get("pull_request"):
            continue
        repo_url = source.get("repository_url", "")
        if repo_url.rsplit("/repos/", 1)[-1] != K8S_REPO:
            continue
        number = source.get("number")
        if number:
            numbers.add(int(number))
    return numbers


def search_k8s_prs(issue_number):
    """Title/body search for this KEP inside kubernetes/kubernetes.

    Returns a set of pull request numbers, or None when search fails. Open
    and merged pulls are both queried. Closed-unmerged pulls are included
    only when the issue description links them.
    """
    query = f"kubernetes/enhancements#{issue_number} OR KEP-{issue_number}"
    numbers = set()
    # `gh search prs` accepts state open|closed. Merged pulls are closed pulls
    # with --merged. Closed-unmerged pulls are included only from the issue body.
    searches = (
        ["--state", "open"],
        ["--state", "closed", "--merged"],
    )
    for extra in searches:
        out = subprocess.run(
            ["gh", "search", "prs", query, "--repo", K8S_REPO, *extra,
             "--limit", "100", "--json", "number"],
            capture_output=True, text=True,
        )
        if out.returncode != 0:
            return None
        try:
            results = json.loads(out.stdout)
        except json.JSONDecodeError:
            return None
        numbers.update(int(item["number"]) for item in results)
    return numbers


def view_k8s_pr(number):
    return gh_json("pr", "view", str(number), "--repo", K8S_REPO, "--json", PR_FIELDS)


def label_names(pr):
    names = set()
    for label in pr.get("labels") or []:
        if isinstance(label, dict):
            name = label.get("name")
        else:
            name = label
        if name:
            names.add(name)
    return names


def milestone_title(pr):
    milestone = pr.get("milestone") or {}
    if isinstance(milestone, dict):
        return milestone.get("title")
    return None


def in_scope(pr, linked):
    """Whether this kubernetes/kubernetes pull request counts for the current release.

    A set milestone for another release keeps historical implementation work
    out of this freeze. An open pull request with no milestone still counts:
    that is the usual shape of work that has not been marked merge-ready yet.
    """
    milestone = milestone_title(pr)
    state = pr.get("state")
    if milestone and milestone != TARGET_MILESTONE:
        return False
    if state == "OPEN":
        return True
    if milestone == TARGET_MILESTONE:
        return True
    return bool(linked and state in ("MERGED", "CLOSED"))


def is_ready(pr):
    """Merged, or open with both approval labels. Drafts are not merge-ready."""
    if pr.get("state") == "MERGED":
        return True
    if pr.get("state") != "OPEN" or pr.get("isDraft"):
        return False
    names = label_names(pr)
    return "approved" in names and "lgtm" in names


def pr_comment_bullet(pr):
    """One list item for the reminder comment."""
    url = pr.get("url") or f"https://github.com/{K8S_REPO}/pull/{pr.get('number')}"
    state = pr.get("state")
    names = label_names(pr)
    if state == "MERGED":
        detail = "merged"
    elif state == "CLOSED":
        detail = "closed without merge"
    else:
        missing = [name for name in ("approved", "lgtm") if name not in names]
        prefix = "draft" if pr.get("isDraft") else "open"
        if missing:
            joined = " and ".join(f"`{name}`" for name in missing)
            detail = f"{prefix}, missing {joined}"
        else:
            detail = f"{prefix}, has `approved` and `lgtm`"
    return f"- {url} ({detail})"


def discover_prs(issue_number, issue_body):
    """Return (in-scope PRs, unresolved linked numbers, discovery_ok, warnings).

    discovery_ok is false when a lookup failed. The enhancement then stays
    at risk, because a missing search result could hide an unlinked pull request.
    """
    warnings = []
    body_numbers = pr_numbers_in_body(issue_body)
    sources = {number: {"issue description"} for number in body_numbers}

    cross_refs = cross_referenced_k8s_prs(issue_number)
    if cross_refs is None:
        warnings.append(
            "Could not read cross-references on the enhancement issue, so some "
            f"{K8S_REPO} pull requests may be missing."
        )
        cross_refs = set()
    for number in cross_refs:
        sources.setdefault(number, set()).add("cross-reference")

    searched = search_k8s_prs(issue_number)
    if searched is None:
        warnings.append(
            f"GitHub search in {K8S_REPO} failed, so some code or test pull requests may be missing."
        )
        searched = set()
    for number in searched:
        sources.setdefault(number, set()).add("search")

    in_scope_prs = []
    unresolved = []
    for number in sorted(sources):
        try:
            pr = view_k8s_pr(number)
        except RuntimeError:
            unresolved.append(number)
            continue
        found_via = sources[number]
        if found_via == {"search"} and not mentions_kep(
            f"{pr.get('title') or ''}\n{pr.get('body') or ''}", issue_number
        ):
            continue
        if not in_scope(pr, number in body_numbers):
            continue
        pr["found_via"] = sorted(found_via)
        pr["linked"] = number in body_numbers
        in_scope_prs.append(pr)

    discovery_ok = not any(
        warning.startswith("Could not read cross-references") or warning.startswith("GitHub search")
        for warning in warnings
    )
    return in_scope_prs, unresolved, discovery_ok, warnings


# --------------------------------------------------------------------------
# Report rendering. The comment wording comes from comm-template/code-freeze.md.
# --------------------------------------------------------------------------

def checkbox(ok):
    return "x" if ok else " "


def md_escape_cell(value):
    return (value or "").replace("|", "\\|").replace("\n", " ").strip()


def decide_status(all_ok):
    if all_ok:
        return "Tracked for code freeze"
    return "At risk for code freeze"


def render_comment(owner_login, prs, linked_ok, ready_ok):
    """Fill comm-template/code-freeze.md from the check results."""
    owner_mention = f"@{owner_login}" if owner_login else "{enhancement owner}"
    if prs:
        pr_list = "\n".join(pr_comment_bullet(pr) for pr in prs)
    else:
        pr_list = f"- None found in `{K8S_REPO}` for {TARGET_MILESTONE}."
    tracked = linked_ok and ready_ok
    any_unmerged = any(pr.get("state") != "MERGED" for pr in prs)
    if not tracked and any_unmerged:
        list_intro = (
            "Per the issue description, these are all of the implementation "
            f"(code-related) PRs for {TARGET_MILESTONE}, some of which are not merged yet:"
        )
    else:
        list_intro = (
            "Per the issue description, these are all of the implementation "
            f"(code-related) PRs for {TARGET_MILESTONE}:"
        )
    checklist = f"""\
- [{checkbox(linked_ok)}] All PRs to the Kubernetes repo that are related to your enhancement are linked in the above issue description (for tracking purposes).
- [{checkbox(ready_ok)}] All PRs are ready to be merged (they have `approved` and `lgtm` labels applied) by the code freeze deadline. This **includes** tests."""
    shared = f"""\
Hey again {owner_mention} :wave:, {TARGET_MILESTONE} Enhancements team here,

Just checking in as we approach [code freeze](https://github.com/kubernetes/sig-release/blob/master/releases/release_phases.md#code-freeze) and [test freeze](https://github.com/kubernetes/sig-release/blob/master/releases/release_phases.md#test-freeze) at **{CODE_FREEZE}**.

Here's where this enhancement currently stands:

{checklist}

{list_intro}
{pr_list}

Please let me know (and keep the issue description updated) if there are any other PRs in [`k/k`](https://github.com/kubernetes/kubernetes) that we should track for this KEP, so that we can maintain accurate status.

If the implementation work for this enhancement is occurring **out-of-tree** (i.e., outside of `k/k`), please link the relevant PRs in the issue description for visibility. Alternatively, if you're unable to provide specific PR links, a confirmation that **all out-of-tree implementation work is complete and merged** will help us finalize tracking and maintain accuracy."""
    if linked_ok and ready_ok:
        return shared + f"""

This enhancement is now marked as `Tracked for code freeze`!

Please note that KEPs targeting `stable` need to have the `status` field marked as `implemented` in the kep.yaml file after code PRs are merged.

/label tracked/yes"""
    return shared + """

The status of this enhancement is marked as `At risk for code freeze`.

If you anticipate missing code freeze, you can file an [exception request](https://github.com/kubernetes/sig-release/blob/master/releases/EXCEPTIONS.md) in advance."""


def ready_phrase(pr):
    if is_ready(pr):
        return "yes"
    return "no"


def pr_table(prs):
    header = "| PR | State | Milestone | Linked in issue | Merge-ready | Found via |"
    sep = "|---|---|---|---|---|---|"
    if not prs:
        return "\n".join([header, sep, "| -- | -- | -- | -- | -- | -- |"])
    rows = []
    for pr in prs:
        number = pr.get("number")
        url = pr.get("url") or f"https://github.com/{K8S_REPO}/pull/{number}"
        state = "draft" if pr.get("isDraft") and pr.get("state") == "OPEN" else (pr.get("state") or "").lower()
        rows.append(
            f"| [#{number}]({url}) | {state} | {md_escape_cell(milestone_title(pr)) or '--'} "
            f"| {'yes' if pr.get('linked') else 'NO'} | {ready_phrase(pr)} "
            f"| {md_escape_cell(', '.join(pr.get('found_via') or []))} |"
        )
    return "\n".join([header, sep, *rows])


def summary_row(result, decision):
    issue = result["issue"]
    title = md_escape_cell(issue["title"])
    issue_cell = f"[#{issue['number']}]({issue['url']}) {title}"
    owner_cell = f"@{result['owner_login']}" if result["owner_login"] else "UNKNOWN"
    stage_cell = result["target_stage"] or "UNKNOWN"
    milestone_cell = "yes" if result["milestone_ok"] else "NO"
    ready_count = sum(1 for pr in result["prs"] if is_ready(pr))
    pr_cell = f"{ready_count}/{len(result['prs'])} ready"
    return (issue_cell, owner_cell, stage_cell, milestone_cell, pr_cell, decision)


def summary_row_for_error(issue_number):
    return (f"#{issue_number}", "--", "--", "--", "--", "FAILED (see detail section)")


def error_markdown(issue_number, error):
    return f"### #{issue_number} — FAILED\n\nCould not check this issue: {error}\n"


def build_summary_table(rows):
    header = (
        f"| Issue | Enhancement owner | Target stage for {TARGET_MILESTONE} "
        f"| In {TARGET_MILESTONE} milestone | k/k PRs | Recommended {TARGET_MILESTONE} tracking board status |"
    )
    sep = "|---|---|---|---|---|---|"
    body = "\n".join(
        f"| {issue} | {owner} | {stage} | {milestone} | {prs} | {decision} |"
        for issue, owner, stage, milestone, prs, decision in rows
    )
    return "\n".join([header, sep, body])


def render_issue_markdown(result):
    issue = result["issue"]
    decision = decide_status(result["all_ok"])
    comment = render_comment(
        result["owner_login"], result["prs"], result["linked_ok"], result["ready_ok"],
    )
    lines = [
        f"### #{issue['number']} — {issue['title']}",
        "",
        "**Summary**",
        "",
        build_summary_table([summary_row(result, decision)]),
        "",
        "**Code Freeze**",
        "",
        f"- All related `{K8S_REPO}` pull requests are linked in the issue description: "
        f"{'✅' if result['linked_ok'] else '❌'}",
        "- All of those pull requests are merge-ready (`approved` and `lgtm`, including tests): "
        f"{'✅' if result['ready_ok'] else '❌'}",
        f"- Code freeze deadline: {CODE_FREEZE}",
        "",
        f"**{K8S_REPO} pull requests**",
        "",
        pr_table(result["prs"]),
        "",
        "**Outstanding actions**",
        "",
    ]
    lines += [f"- {item}" for item in result["action_items"]] or ["- None — all criteria met."]
    if result["notes"]:
        lines += ["", "**Notes**", ""]
        lines += [f"- {note}" for note in result["notes"]]
    lines += [
        "",
        "**Draft GitHub comment**",
        "",
        "*(review before posting — do not auto-post)*",
        "",
        "```markdown",
        comment,
        "```",
    ]
    return decision, "\n".join(lines)


def build_report_document(issue_numbers, rows, sections, input_description):
    generated = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    passed = datetime.now(timezone.utc) >= CODE_FREEZE_UTC
    deadline_state = "passed" if passed else "upcoming"
    header = "\n".join([
        f"# Code Freeze Report -- {TARGET_MILESTONE}",
        "",
        f"Generated: {generated}",
        f"Issues checked: {len(issue_numbers)}",
        f"Code Freeze and Test Freeze: {CODE_FREEZE} ({deadline_state})",
        f"Generate draft reminder comment for {input_description}.",
        "",
        "Code and test pull requests are checked in `kubernetes/kubernetes` only.",
        "",
        "## Summary",
        "",
        build_summary_table(rows),
    ])
    body = "\n\n---\n\n".join(sections)
    return header + "\n\n---\n\n" + body + "\n"


REPORT_DIR = "report"


def write_report(doc):
    """Write a new report file. Never overwrite a previous run."""
    os.makedirs(REPORT_DIR, exist_ok=True)
    timestamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    base = f"code-freeze-{timestamp}"
    path = os.path.join(REPORT_DIR, f"{base}.md")
    suffix = 1
    while os.path.exists(path):
        path = os.path.join(REPORT_DIR, f"{base}-{suffix}.md")
        suffix += 1
    with open(path, "w") as handle:
        handle.write(doc)
    return path


# --------------------------------------------------------------------------
# Per-issue check
# --------------------------------------------------------------------------

def check_issue(issue_number, tree):
    issue = gh_json(
        "issue", "view", str(issue_number), "--repo", REPO,
        "--json", "number,title,labels,milestone,state,url,body",
    )
    labels = [label["name"] for label in issue["labels"]]
    milestone = (issue.get("milestone") or {}).get("title")
    milestone_ok = milestone == TARGET_MILESTONE
    stage_labels = [label for label in labels if label.startswith("stage/")]
    target_stage = stage_labels[0].split("/", 1)[1] if len(stage_labels) == 1 else None

    notes = []
    if not milestone_ok:
        notes.append(
            f"Issue milestone is `{milestone or 'none'}`. "
            f"This check still evaluates {TARGET_MILESTONE} code and test pull requests."
        )
    if len(stage_labels) == 0:
        notes.append("No `stage/{alpha,beta,stable}` label on the issue.")
    elif len(stage_labels) > 1:
        notes.append(f"Multiple stage labels found ({', '.join(stage_labels)}).")
    elif target_stage == "stable":
        notes.append(
            "Target stage is `stable`. After the code pull requests merge, `kep.yaml` "
            "`status` needs to be `implemented`. The tracked comment already says this."
        )

    owner_login = None
    kep_dir, _sig = find_kep_dir_on_master(tree, str(issue["number"]))
    if kep_dir is None:
        notes.append(
            "Could not resolve the enhancement owner because no merged "
            f"`keps/<sig>/{issue['number']}-*/kep.yaml` was found."
        )
    else:
        owner_login = last_merged_pr_author(f"{kep_dir}/kep.yaml")
        if not owner_login:
            notes.append(
                "Could not resolve the enhancement owner from the latest merged `kep.yaml` change."
            )

    prs, unresolved, discovery_ok, warnings = discover_prs(issue["number"], issue.get("body") or "")
    action_items = []
    for warning in warnings:
        action_items.append(warning)

    unlinked = [pr for pr in prs if not pr.get("linked")]
    not_ready = [pr for pr in prs if not is_ready(pr)]
    for pr in unlinked:
        action_items.append(
            f"Link {K8S_REPO}#{pr['number']} in the issue description "
            f"(found via {', '.join(pr.get('found_via') or ['unknown'])})."
        )
    for pr in not_ready:
        names = label_names(pr)
        missing = [name for name in ("approved", "lgtm") if name not in names]
        if pr.get("state") == "CLOSED":
            action_items.append(f"{K8S_REPO}#{pr['number']} is closed and was not merged.")
        elif pr.get("isDraft"):
            if missing:
                action_items.append(
                    f"{K8S_REPO}#{pr['number']} is still a draft and is missing "
                    + " and ".join(f"`{name}`" for name in missing) + "."
                )
            else:
                action_items.append(f"{K8S_REPO}#{pr['number']} is still a draft.")
        elif missing:
            action_items.append(
                f"{K8S_REPO}#{pr['number']} is missing "
                + " and ".join(f"`{name}`" for name in missing) + "."
            )
        else:
            action_items.append(f"{K8S_REPO}#{pr['number']} is not merge-ready.")

    if not prs:
        action_items.append(
            f"No {K8S_REPO} code or test pull requests for {TARGET_MILESTONE} were found. "
            "Link them in the issue description, or confirm that the implementation is "
            "out-of-tree and already merged."
        )
    for number in unresolved:
        action_items.append(f"Resolve the unreadable {K8S_REPO}#{number} link.")

    for pr in prs:
        holds = sorted(name for name in label_names(pr) if name.startswith("do-not-merge/"))
        if holds and is_ready(pr):
            notes.append(
                f"{K8S_REPO}#{pr['number']} has `approved` and `lgtm`, and also "
                + ", ".join(f"`{name}`" for name in holds)
                + ". This check treats `approved` and `lgtm` as merge-ready."
            )

    linked_ok = bool(prs) and not unlinked and not unresolved and discovery_ok
    ready_ok = bool(prs) and not not_ready and not unresolved and discovery_ok
    all_ok = linked_ok and ready_ok
    return {
        "issue": issue,
        "owner_login": owner_login,
        "target_stage": target_stage,
        "milestone_ok": milestone_ok,
        "prs": prs,
        "linked_ok": linked_ok,
        "ready_ok": ready_ok,
        "all_ok": all_ok,
        "action_items": action_items,
        "notes": notes,
    }


# --------------------------------------------------------------------------
# Main
# --------------------------------------------------------------------------

def get_gh_scopes():
    """Parse 'Token scopes: ...' out of `gh auth status` (written to stderr)."""
    out = subprocess.run(["gh", "auth", "status"], capture_output=True, text=True)
    combined = out.stdout + out.stderr
    match = re.search(r"Token scopes:\s*(.+)", combined)
    if not match:
        return set()
    return {item.strip().strip("'\"") for item in match.group(1).split(",")}


def run_preflight():
    """Check auth, board access, and the live Code Freeze date."""
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
            print(
                f"OK   {TARGET_MILESTONE} tracking board (project {PROJECT_NUMBER}) "
                f"is readable -- {len(items)} item(s) found."
            )
        except RuntimeError as exc:
            print(f"FAIL could not read the {TARGET_MILESTONE} tracking board: {exc}")
            ok = False

    freeze_when, _freeze_utc = load_code_freeze()
    print(f"Code Freeze and Test Freeze: {freeze_when}")
    print()
    print("All checks passed -- ready to take input." if ok else "Preflight FAILED -- fix the above before proceeding.")
    return ok


def parse_args():
    parser = argparse.ArgumentParser(
        description="Check Code Freeze readiness for kubernetes/enhancements issues.",
    )
    parser.add_argument(
        "--preflight", action="store_true",
        help="Check gh auth scope, tracking board access, and the Code Freeze date, then exit.",
    )
    group = parser.add_mutually_exclusive_group()
    group.add_argument(
        "--contact", metavar="GITHUB_HANDLE",
        help="Check every tracking-board issue whose Enhancements Contact is this GitHub handle.",
    )
    group.add_argument(
        "--sig", metavar="SIG_NAME",
        help="Check every tracking-board issue whose SIG field matches (sig-node, sig/node, or node).",
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
    global CODE_FREEZE, CODE_FREEZE_UTC
    args = parse_args()

    if args.preflight:
        sys.exit(0 if run_preflight() else 1)

    CODE_FREEZE, CODE_FREEZE_UTC = load_code_freeze()

    if args.contact:
        handle = args.contact.lstrip("@")
        input_description = f"Enhancement Contact @{handle}"
        try:
            issue_numbers = resolve_issues_by_enhancement_contact(args.contact)
        except RuntimeError as exc:
            print(f"error: {exc}", file=sys.stderr)
            sys.exit(1)
        if not issue_numbers:
            print(
                f"No issues found on the {TARGET_MILESTONE} tracking board with Enhancements Contact "
                f"@{handle}.",
                file=sys.stderr,
            )
            sys.exit(1)
    elif args.sig:
        sig_value = normalize_sig_option(args.sig)
        input_description = f"SIG {sig_value}"
        try:
            issue_numbers = resolve_issues_by_sig(args.sig)
        except RuntimeError as exc:
            print(f"error: {exc}", file=sys.stderr)
            sys.exit(1)
        if not issue_numbers:
            print(
                f"No issues found on the {TARGET_MILESTONE} tracking board with SIG `{sig_value}`.",
                file=sys.stderr,
            )
            sys.exit(1)
    else:
        issue_numbers = args.issue_numbers
        input_description = "KEP issue(s) " + ", ".join(f"#{number}" for number in issue_numbers)

    try:
        tree = fetch_master_tree()
    except (json.JSONDecodeError, RuntimeError) as exc:
        print(f"error: could not list keps on master: {exc}", file=sys.stderr)
        sys.exit(1)

    exit_code = 0
    rows = []
    sections = []
    for issue_number in issue_numbers:
        try:
            result = check_issue(issue_number, tree)
        except Exception as exc:
            # A batch run should keep going when one KEP cannot be read.
            exit_code = 1
            rows.append(summary_row_for_error(issue_number))
            sections.append(error_markdown(issue_number, exc))
            continue
        decision, detail = render_issue_markdown(result)
        rows.append(summary_row(result, decision))
        sections.append(detail)

    document = build_report_document(issue_numbers, rows, sections, input_description)
    path = write_report(document)
    print(f"Report written to: {path}")
    print(f"View the summary table and full draft comment(s) there ({len(issue_numbers)} issue(s) checked).")
    sys.exit(exit_code)


if __name__ == "__main__":
    main()
