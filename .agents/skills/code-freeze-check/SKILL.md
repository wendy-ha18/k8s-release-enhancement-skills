---
name: code-freeze-check
description: Use this whenever the user wants to check Kubernetes KEP Code Freeze and Test Freeze readiness or draft Code Freeze reminder comments for one or more kubernetes/enhancements issues, an Enhancements Contact, or a SIG.
date: 2026-11-04
---

# Code Freeze Check

## Purpose

Review KEPs against the current release's Code Freeze and Test Freeze
requirements and write a report containing status recommendations, pull
request gaps, and draft GitHub comments. Never post comments or modify
issues, labels, milestones, or the release tracking board unless the user
separately and explicitly asks.

The driver is `check_code_freeze.py` in this directory. It reuses the
tracking-board lookup of `enhancements-freeze-check`, but the requirement
is different: every v1.38 code and test pull request in
`kubernetes/kubernetes` must be linked from the enhancement issue and be
merge-ready.

## 1. Run preflight first

Before asking what to review, run from the repository root:

```bash
python3 .agents/skills/code-freeze-check/check_code_freeze.py --preflight
```

Preflight checks:

1. `gh` authentication includes `project` or `read:project`.
2. The v1.38 release tracking board is readable.
3. The Code Freeze date can be fetched from the live v1.38 release
   timeline. Code Freeze and Test Freeze are the same deadline.

If the project scope is missing, stop and ask the user to run:

```bash
gh auth refresh -s read:project
```

That command is interactive; do not run it on the user's behalf.

## 2. Ask what to review

After preflight passes, accept exactly one input type:

1. One or more enhancement issue numbers:

   ```bash
   python3 .agents/skills/code-freeze-check/check_code_freeze.py 6274 6371
   ```

2. An Enhancements Contact from the tracking board:

   ```bash
   python3 .agents/skills/code-freeze-check/check_code_freeze.py --contact <github-handle>
   ```

3. A SIG from the tracking board:

   ```bash
   python3 .agents/skills/code-freeze-check/check_code_freeze.py --sig <sig-name>
   ```

Accept `sig-node`, `sig/node`, or `node`; the script normalizes the value.
Contact and SIG runs can take several minutes because every matching issue
requires multiple read-only GitHub calls.

The tracking board's **Enhancements Contact** is not the issue assignee. Use
the board field, not GitHub assignees. Likewise, resolve SIG input from the
board's SIG field rather than assuming the issue's `sig/*` label is identical.

## 3. Sources of truth

- [v1.38 release tracking board](https://github.com/orgs/kubernetes/projects/269/views/1):
  Enhancements Contact and SIG.
- [v1.38 release timeline](https://github.com/kubernetes/sig-release/tree/master/releases/release-1.38):
  the live Code Freeze and Test Freeze deadline.
- [Code Freeze policy](https://github.com/kubernetes/sig-release/blob/master/releases/release_phases.md#code-freeze)
  and [Test Freeze policy](https://github.com/kubernetes/sig-release/blob/master/releases/release_phases.md#test-freeze).
- `kubernetes/kubernetes` pull requests for code and tests. Do not look for
  implementation pull requests in `kubernetes/enhancements`.
- `comm-template/code-freeze.md`: reminder-comment wording.

`TARGET_MILESTONE = "v1.38"` in the script determines the release. Deadline
text and its UTC instant are fetched live from the matching release timeline.
If fetching fails, the script warns and uses a bundled fallback date.

## 4. Requirements checked

For every KEP, check that:

1. Every in-scope `kubernetes/kubernetes` pull request is linked in the
   enhancement issue description. Ignore HTML comments.
2. Every in-scope pull request is merge-ready. This includes tests.
   - An open pull request needs both the `approved` and `lgtm` labels.
   - A merged pull request counts as ready.
   - A draft, or a pull request closed without merging, does not.

A pull request is in scope when it belongs to this KEP and this release:

- Its milestone is `v1.38`, or
- It is still open and has no milestone, or
- It is merged or closed, has no milestone, and is linked in the issue.

Merged pull requests whose milestone is an earlier release are historical and
are left out. Pull requests in `kubernetes/enhancements` and documentation
pull requests in `kubernetes/website` are ignored.

Discovery uses the issue description, GitHub cross-references on the
enhancement issue, and a `kubernetes/kubernetes` search for
`kubernetes/enhancements#<issue>` or `KEP-<issue>`. Search-only hits must
contain that exact KEP reference. These lookups are heuristics. The report
shows where each pull request was found; review them before acting.

No linked `kubernetes/kubernetes` pull request is enough to call the
enhancement tracked. Out-of-tree work needs a human to confirm that it is
already merged.

An issue's milestone and stage label are reported for context. They do not
by themselves pass or fail this check.

## 5. Status recommendation

- Both requirements pass, and at least one in-scope pull request was found:
  `Tracked for code freeze`.
- Anything else, before or after the deadline: `At risk for code freeze`.

Never recommend a tracked status when pull request discovery failed, when no
code or test pull request was found, or when any in-scope pull request is
unlinked or not merge-ready.

The tracked comment tells stable KEPs to set `kep.yaml` `status: implemented`
after the code pull requests merge. That note is not a separate code-freeze
failure while those pull requests are still open.

## 6. Draft comment

Base the draft on `comm-template/code-freeze.md`:

- fill the owner and the pull request list from gathered data;
- preserve the template's wording;
- check the two boxes from the actual results;
- use the tracked comment, including `/label tracked/yes`, only when both
  requirements pass;
- use the at-risk comment otherwise, and include "some of which are not
  merged yet" only when at least one listed pull request is not merged;
- never leave `{enhancement owner}` when the owner login is known.

The deadline in the comment is the live timeline text when that fetch
succeeds. Ownership is the author of the most recent merged `kep.yaml`
change. If it cannot be resolved, leave the visible owner placeholder and
surface the uncertainty for human review.

## 7. Output

The script writes:

```text
report/code-freeze-<UTC-timestamp>.md
```

It never overwrites a report. Each report contains:

1. A batch summary table.
2. One section per issue with:
   - a one-row summary;
   - Code Freeze check results;
   - the in-scope `kubernetes/kubernetes` pull requests;
   - exact outstanding actions;
   - a draft GitHub comment in a fenced Markdown block.

After the run, tell the user only that the report is ready and provide its
path. Do not paste the full report into chat unless the user asks.

Never post a generated draft automatically. Posting to a public upstream issue
requires explicit confirmation for that action.

## Prerequisites

- `gh` CLI authenticated for read access.
- `project` or `read:project` OAuth scope.
- Python 3.
- Write access to `report/` under the repository root.

## Updating for a new release

Update `TARGET_MILESTONE` in `check_code_freeze.py`. The release timeline
path and live deadline derive from it. Also verify the tracking-board project
number and update the fallback deadline for resilience.
