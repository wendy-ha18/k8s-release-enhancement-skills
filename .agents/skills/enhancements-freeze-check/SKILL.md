---
name: enhancements-freeze-check
description: Use this whenever the user wants to check Kubernetes KEP Enhancements Freeze readiness or draft Enhancements Freeze reminder comments for one or more kubernetes/enhancements issues, an Enhancements Contact, or a SIG.
date: 2026-09-26
---

# Enhancements Freeze Check

## Purpose

Review KEPs against the current release's Enhancements Freeze requirements and
write a report containing status recommendations, actionable gaps, and draft
GitHub comments. Never post comments or modify issues, labels, milestones, or
the release tracking board unless the user separately and explicitly asks.

The driver is `check_enhancements_freeze.py` in this directory. It shares the
lookup behavior of `kep-readiness-check`, but validates the stricter
Enhancements Freeze requirement that all required KEP and PRR changes are
already merged.

## 1. Run preflight first

Before asking what to review, run from the repository root:

```bash
python3 .claude/skills/enhancements-freeze-check/check_enhancements_freeze.py --preflight
```

Preflight checks:

1. `gh` authentication includes `project` or `read:project`.
2. The v1.38 release tracking board is readable.
3. The Enhancements Freeze date can be fetched from the live v1.38 release
   timeline.

If the project scope is missing, stop and ask the user to run:

```bash
gh auth refresh -s read:project
```

That command is interactive; do not run it on the user's behalf.

## 2. Ask what to review

After preflight passes, accept exactly one input type:

1. One or more enhancement issue numbers:

   ```bash
   python3 .claude/skills/enhancements-freeze-check/check_enhancements_freeze.py 6274 6371
   ```

2. An Enhancements Contact from the tracking board:

   ```bash
   python3 .claude/skills/enhancements-freeze-check/check_enhancements_freeze.py --contact <github-handle>
   ```

3. A SIG from the tracking board:

   ```bash
   python3 .claude/skills/enhancements-freeze-check/check_enhancements_freeze.py --sig <sig-name>
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
  the live Enhancements Freeze deadline.
- [Enhancements Freeze policy](https://github.com/kubernetes/sig-release/blob/master/releases/release_phases.md#enhancements-freeze):
  requirements.
- `kubernetes/enhancements` master branch: merged KEP README, `kep.yaml`, and
  PRR approval state.
- `comm-template/enhancement-freeze.md`: reminder-comment wording.

`TARGET_MILESTONE = "v1.38"` in the script determines the release. Deadline
text and its UTC instant are fetched live from the matching release timeline.
If fetching fails, the script warns and uses a bundled fallback date.

## 4. Requirements checked

For every KEP, check that:

1. The issue is in the v1.38 milestone and has `lead-opted-in`.
2. Exactly one `stage/{alpha,beta,stable}` label identifies the target stage.
3. A KEP README is merged and contains the main sections from the latest KEP
   template.
4. Merged `kep.yaml` has:
   - `status: implementable`; `withdrawn` is accepted when the YAML stage is
     `deprecated`, `disabled`, or `removed`, and `implemented` is accepted for
     stable KEPs that completed implementation early;
   - `stage` matching the issue's stage label;
   - `latest-milestone: v1.38`;
   - a `milestone.<stage>` value.
5. The merged README has substantive Graduation Criteria.
6. The merged README has a substantive detailed Test Plan.
7. Production Readiness Review is complete and merged:
   - required questionnaire sections are answered for the target stage; and
   - the merged PRR approval file has an approver for that stage.
8. No discovered open PR modifies the KEP's README or `kep.yaml`.

README-template, Graduation Criteria, Test Plan, questionnaire completeness,
and open-PR discovery are heuristics. The report labels heuristic findings;
review them manually before acting. Exact checks include labels, milestone,
YAML values, file existence, and PRR approval entries.

Open PR discovery combines GitHub cross-reference events, title/body search,
and the issue's current-milestone PR links. A candidate is trusted only when
its changed files touch this KEP's own directory. This avoids confusing a PR
that merely mentions another KEP with that KEP's update PR.

## 5. Status recommendation

- Every requirement passes: `Tracked for enhancements freeze`.
- Requirements are missing before the deadline: `At risk for enhancements freeze`.
- Requirements are missing after the deadline: `Removed from Milestone`.

Never recommend a tracked status when any requirement is incomplete.

## 6. Draft comment

Base the draft on `comm-template/enhancement-freeze.md`:

- fill the owner, stage, deadline, checklist, and action items from gathered
  data;
- preserve the template's factual, concise tone;
- include the official detailed Test Plan requirement even though the current
  communication template omits it;
- use actual checkbox results rather than marking every item the same;
- use a past-deadline variant when the deadline has passed;
- never leave `{enhancement owner}`, `{stage}`, or action placeholders when
  the corresponding data is available.

Ownership falls back to the author of the most recent merged `kep.yaml` change.
If it cannot be resolved, leave the visible owner placeholder and surface the
uncertainty for human review.

## 7. Output

The script writes:

```text
report/enhancements-freeze-<UTC-timestamp>.md
```

It never overwrites a report. Each report contains:

1. A batch summary table.
2. One section per issue with:
   - a one-row summary;
   - Enhancements Freeze check results;
   - exact outstanding actions;
   - a draft GitHub comment in a fenced Markdown block.

After the run, tell the user only that the report is ready and provide its
path. Do not paste the full report into chat unless the user asks.

Never post a generated draft automatically. Posting to a public upstream issue
requires explicit confirmation for that action.

## Prerequisites

- `gh` CLI authenticated for read access.
- `project` or `read:project` OAuth scope.
- Python 3 and PyYAML.
- Write access to `report/` under the repository root.

## Updating for a new release

Update `TARGET_MILESTONE` in `check_enhancements_freeze.py`. The release
timeline path and live deadline derive from it. Also verify the tracking-board
project number and update the fallback deadline for resilience.
