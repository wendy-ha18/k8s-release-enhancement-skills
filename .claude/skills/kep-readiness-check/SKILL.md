---
name: kep-readiness-check
description: Use this whenever the user wants to check KEP readiness status and draft a reminder comment for a specific enhancements issue number.
date: 2026-09-20
---

# KEP Readiness Check

Checks one or more `kubernetes/enhancements` tracking issues against the
KEP Readiness (formerly "PRR freeze") criteria for the current release,
and drafts a dedicated reminder comment that Enhancements team can use to
posts on each issue. Issues can be given directly, or resolved from a
GitHub handle (Enhancement Contact) or a SIG name — see "Running it"
below. The skill never posts anything itself — it only produces a draft
for you to review and post by hand (e.g. via `gh issue comment`).

## What it checks

For the given issue number, against
[`release_phases.md#prr-freeze`](https://github.com/kubernetes/sig-release/blob/master/releases/release_phases.md#prr-freeze):

1. Issue is in the target milestone (currently **v1.38**).
2. `lead-opted-in` label is present.
3. `kep.yaml`'s own `stage` field matches the issue's `stage/{alpha,beta,stable}`
   label (this *is* the "stage label is accurate" check — kep.yaml is the
   authoritative source for what the KEP is actually targeting).
4. A PR (open or merged) has the KEP's PRR questionnaire filled out.
5. A PR (open or merged) has `kep.yaml` updated with `stage` and
   `latest-milestone` for the current milestone, and the `milestone` struct
   too **but only if the KEP is graduating to a new stage this cycle** — see
   "Graduation-aware kep.yaml check" below, straight from the policy text.
6. A PR (open or merged) has the PRR approval file
   (`keps/prod-readiness/<sig>/<kep-number>.yaml`) with an approver assigned
   for the target stage.

**Target stage** (used for checks 3, 5, 6, and which PRR questionnaire
sections are required) comes from the issue's own `stage/*` label, not from
free-form issue body text — labels are actively maintained metadata, not
prose that can silently drift.

**Finding the KEP's own PR** does *not* use the issue body's "PRs by stage
and milestone" checklist as its primary source — that checklist is the kind 
of free-form text contributors forget to update as a KEP moves
through many PRs over many release cycles (confirmed by testing against
real long-running KEPs). Instead the script pools candidates from three
independent signals, then requires every candidate to clear one shared
confirmation filter before it's trusted:

1. **GitHub's cross-reference records.** Whenever a PR's description or
   comments mention `#<issue-number>` or link to the issue, GitHub logs a
   `cross-referenced` timeline event on the issue — visible via `gh api
   repos/kubernetes/enhancements/issues/<N>/timeline`. Catches mentions
   left in review comments, not just the PR body.
2. **A title/body text search** (`gh search prs "<N> in:title,body"
   --repo kubernetes/enhancements --state open`). Catches PRs whose title
   names the KEP number (e.g. `KEP-4958: ...`) but whose body never
   actually links the issue — the template's "Issue link:" field left
   blank, so GitHub never creates a cross-reference event for it at all.
   (Real example: issue #4958's open PR, #5672, is only found this way.)
3. **The issue body's own PR checklist**, as a last resort — any
   enhancements-repo PR link on a line that also mentions the target
   milestone. Not trusted alone (see above), but still worth pooling in as
   a candidate.
4. **Confirmation, applied to every candidate from any of the above:**
   does the candidate PR's file list actually touch this KEP's own
   directory (`keps/<sig>/<N>-<slug>/...`)? A PR from a *different* KEP
   that merely name-drops "see also #N" passes signal 1 or 2 but fails
   this filter. (Verified on real data: issue #6318 has two
   cross-referencing open PRs; only the one whose files actually live
   under `keps/sig-node/6318-.../` survives.)

Then:

- If exactly one PR survives confirmation, it's the KEP's PR — its author
  becomes the "enhancement owner" in the draft comment, and its head
  branch (if still open) is read in preference to master for any file it
  touches, since master can still hold the pre-PR content.
- If **no** PR survives at all, everything must already be satisfied on
  master — the script attributes ownership to whoever authored the most
  recent commit to `kep.yaml` instead (via `gh api
  repos/.../commits?path=...`), and there's no PR link to show.
- If more than one PR survives (rare — e.g. a stray leftover PR from an
  earlier stage still open), the most recently created one is used and the
  rest are surfaced as an action item so you can sanity-check by hand;
  `all_ok` is never true while this is ambiguous.

### Graduation-aware kep.yaml check

Per policy, `milestone.<stage>` only needs updating **if the KEP is
graduating to a new stage this cycle**; `latest-milestone` always has to
equal the current release regardless. The script determines "graduating"
by comparing the target stage (from the label) to whatever `stage` is set
to on master right now, before any open PR's changes: if they differ (or
`kep.yaml` doesn't exist on master yet), it's a graduation and
`milestone.<stage>` must equal the current milestone; if they're the same,
the KEP is just continuing at its existing stage, so `milestone.<stage>`
is left alone and may still show whichever earlier release first reached
it.

(Real example: issue #2535 has been `stage: beta` since v1.35 and isn't
graduating now, so `milestone.beta` staying at `v1.35` is correct — only
its stale `latest-milestone: v1.37` is a real gap.)

Checks 1-3, 5, and 6 are exact (label/YAML field comparisons). Check 4 (the
PRR questionnaire) is a **heuristic** — it looks for the KEP template's own
`<!-- ... -->` placeholder comments and literal "To be completed for
{stage}" boilerplate still sitting under a required question, and only
flags a section when nothing but that placeholder is left (a short real
answer like "No." must not be flagged — it's complete, not empty). It
catches the common case well, but always sanity-check it against the
README before trusting it fully, especially if a KEP's questionnaire uses
non-standard phrasing.

### Recommended v1.38 tracking board status

The status summary also prints a recommendation for the issue's Status
field on the [v1.38 tracking board](https://github.com/orgs/kubernetes/projects/269/views/1),
derived straight from the [PRR Freeze policy text](https://github.com/kubernetes/sig-release/blob/master/releases/release_phases.md#prr-freeze):

- All criteria met → `Tracked for KEP readiness` (regardless of the
  deadline — a KEP that's fully ready stays tracked).
- Not all met, deadline hasn't passed yet → `At risk for KEP readiness`.
- Not all met, deadline has passed → `Removed from Milestone` — the
  policy is explicit that an enhancement failing to meet KEP Readiness by
  the deadline is removed from the milestone and needs an [Exception].
  The draft comment switches to a different template in this case (past
  tense, cites the policy, points at filing an exception) instead of the
  "still at risk" one.

These three strings were checked against the board's actual `Status`
field options (via the same GraphQL query `--contact`/`--sig` use) and
match exactly, along with several other statuses this script doesn't
compute (`At risk for enhancements freeze`, `Deferred`, `Exception
Pending`, etc.) — this recommendation only ever covers the KEP Readiness
phase, not the later ones.

This does **not** currently read the tracking board's own `Status` value
for a "move from `<current status>` to `<recommendation>`" comparison —
just the recommendation on its own. `fetch_project_items()` and
`project_field_value()` (added for `--contact`/`--sig`) already have
everything needed to add that comparison cheaply if it's wanted later:
call `project_field_value(item_node, "Status")` on the item matching the
issue.

The deadline check compares the current time against
`KEP_READINESS_DEADLINE_UTC`, a datetime constant kept in sync with the
human-readable `KEP_READINESS_DEADLINE` string — update both together each
release cycle (see "Updating for a new release cycle" below).

## Running it

Run the driver with **one of three kinds of input** (they're mutually
exclusive — pick one per run):

```bash
# 1. One or more issue numbers (space-separated)
python3 .claude/skills/kep-readiness-check/check_kep_readiness.py <issue-number> [<issue-number> ...]

# 2. Every issue on the v1.38 board whose Enhancements Contact is this handle
python3 .claude/skills/kep-readiness-check/check_kep_readiness.py --contact <github-handle>

# 3. Every issue on the v1.38 board whose SIG matches (accepts "sig-node", "sig/node", or just "node")
python3 .claude/skills/kep-readiness-check/check_kep_readiness.py --sig <sig-name>
```

(Path is relative to the repo root you're running Claude Code from — adjust
if your cwd differs.)

`--contact` and `--sig` query the actual [v1.38 Release Tracking
board](https://github.com/orgs/kubernetes/projects/269) (org `kubernetes`,
project 269) via the Projects v2 GraphQL API, reading its real
**"Enhancements Contact"** and **"SIG"** fields, then run the exact same
per-issue check as mode 1 on every matching issue — so `--sig` on a big
SIG can mean dozens of issues in one run, each needing several `gh` calls;
expect it to take a while and don't kill it early. This needs the
`project` (or `read:project`) OAuth scope, on top of the `repo` scope
everything else in this script uses — grant it once with `gh auth refresh
-s read:project` (interactive; opens a browser flow, so it can't be
scripted).

**"Enhancements Contact" is not the issue's assignee.** They're two
different stakeholders tracked as two different fields on the board: the
Enhancements Contact is the *Enhancements team member* responsible for
reminding a KEP's owner about deadlines (a fixed-roster single-select
field, e.g. `@wendy-ha18` — not a free people-picker), while the issue's
GitHub `assignees` is typically the KEP owner/author themselves. An earlier
version of this skill got this wrong (matched on assignees instead), which
is why this distinction is called out explicitly here. The **"SIG"** field
is similarly its own board field, not identical to the issue's `sig/*`
label — the two can diverge (verified on real data: `sig-network` returns
5 issues from the board's SIG field vs. 8 from the `sig/network` label),
so trust the board field, which is what both `--contact` and `--sig` read.

**The script does not print the report to the terminal.** It writes a
single Markdown file to `report/kep-readiness-<UTC-timestamp>.md`
(creating the `report/` directory if needed — one file per run, timestamped
so repeated runs don't clobber each other) and prints only a short pointer
to it, e.g.:

```
Report written to: report/kep-readiness-20260919T183007Z.md
View the summary table and full draft comment(s) there (3 issue(s) checked).
```

When this skill is invoked (e.g. via `/kep-readiness-check`) and the user
hasn't already given input, **ask which of the three they want** before
running anything — e.g. "Which kubernetes/enhancements issue number(s)
would you like to generate a KEP readiness deadline reminder for? (Or give
me your GitHub handle as the Enhancements Contact to check everything
assigned to you, or a SIG name to check everything for that SIG.)" To
sweep the whole [v1.38 tracking
board](https://github.com/orgs/kubernetes/projects/269/views/1) entirely,
pass every issue number from the board in one invocation instead — there's
no need to run it once per issue.

**Once the script finishes, just tell the user the report is ready and
give them the file path** — e.g. "Report ready at `report/kep-readiness-
<timestamp>.md`." Don't paste the report's contents into the chat and
don't re-summarize it into your own table; the file already has everything
(summary table + every issue's full status and draft comment) in the
format described below. If the user then asks about a specific issue from
that run, or wants to post one of the drafts, read the file to answer —
just don't proactively dump it.

The report file itself has, in order:

1. A title, generation timestamp, and issue count.
2. A **Summary** table — one row per issue: number/title (linked),
   enhancement owner, target stage, whether it's in the v1.38 milestone,
   and the recommended tracking-board status (see below). A failed lookup
   (e.g. a typo'd issue number) gets a `FAILED` row instead, and the run's
   exit code is non-zero if any issue failed — the rest of the batch still
   completes and gets its own section.
3. One `## Issue #N: <title>` section per issue checked, each with the same
   status detail as the summary row plus the full outstanding-items list
   and the draft comment in a fenced ```` ```markdown ```` block (so it's
   copy-pasteable as-is, checkboxes and links included, into `gh issue
   comment`). Each of the three checklist lines in the draft links the KEP
   PR that was actually checked (e.g. `([PR #6267](https://.../pull/6267))`)
   when one was found — omitted only when no open PR exists at all and
   everything is already satisfied on master.

**Do not post any comment automatically** — ask the user first (e.g. "want
me to post this with `gh issue comment <n> --repo kubernetes/enhancements
--body-file -`?"). Posting a comment on a public upstream issue is a
visible, hard-to-undo action, so it needs explicit sign-off every time, not
just a one-time approval.

## Prerequisites

- `gh` CLI, authenticated (`gh auth status`). Only read-only `gh` calls are
  made (`issue view`, `pr view`, `api .../timeline`, `api .../commits`, `api
  .../contents/...`, `api .../git/trees/master`, `api graphql`) — no writes.
- The `project` (or `read:project`) OAuth scope, needed only for
  `--contact`/`--sig` (they query the Projects v2 board). Grant with `gh
  auth refresh -s read:project` if `gh auth status` doesn't already list
  it — plain issue-number mode works without it.
- PyYAML (`python3 -c "import yaml"` to check; `pip3 install pyyaml` if
  missing).
- Write access to `report/` under the cwd (the script creates the directory
  if it doesn't exist). `report/` is gitignored — reports are working
  output, not something to commit.

## Updating for a new release cycle

The milestone and the two deadline dates are hardcoded as constants at the
top of `check_kep_readiness.py`:

```python
TARGET_MILESTONE = "v1.38"
KEP_READINESS_DEADLINE = "..."
KEP_READINESS_DEADLINE_UTC = datetime(2026, 9, 23, 12, 0, tzinfo=timezone.utc)
ENHANCEMENTS_FREEZE = "..."
```

Each release cycle, pull the new dates from
`https://github.com/kubernetes/sig-release/tree/master/releases/release-1.<N>`
(the "Timeline" table's **KEP Readiness Deadline** and **Enhancements
Freeze** rows) and update all four: the human-readable
`KEP_READINESS_DEADLINE` string AND `KEP_READINESS_DEADLINE_UTC` must
describe the *same instant* — the datetime constant is what actually drives
the `Tracked` / `At risk` / `Removed from Milestone` decision (see
"Recommended v1.38 tracking board status" above), so if only the string is
updated the decision logic will silently use the wrong cutoff. Also update
the milestone number implied by `kubernetes/enhancements/milestone/<N>` if
you want the script to sanity-check milestone numbers too (it currently
only compares milestone *titles*, e.g. `"v1.38"`, so no other change is
needed there).

## Gotchas found while building this

- **"Enhancements Contact" is a different person from the issue's
  assignee — don't infer one from the other.** An earlier version of
  `--contact` matched on the issue's GitHub `assignees` field on the
  (wrong) assumption that it correlated with the board's Enhancements
  Contact. It happened to line up on the handful of issues tested, which
  made the bug easy to miss — the actual field only exists on the Projects
  v2 board and has its own fixed-roster single-select values (e.g.
  `@wendy-ha18`), read via `fetch_project_items()` /
  `project_field_value()`. Same lesson for "SIG": it's the board's own
  field, not necessarily identical to the issue's `sig/*` label (verified:
  `sig-network` returns a different, smaller set of issues from the board
  field than from the label).
- **A single malformed `kep.yaml` can crash a whole batch run if you're not
  careful.** PyYAML's implicit timestamp resolver raises a raw `ValueError`
  (not `yaml.YAMLError`) for a date-shaped-but-invalid value like a
  `creation-date` with the day/month swapped -- found this for real while
  testing `--sig sig-network` across 8 issues at once. All three
  `yaml.safe_load` call sites catch `(yaml.YAMLError, ValueError)` now, and
  `main()`'s per-issue loop catches any `Exception`, not just `RuntimeError`
  -- a `--sig`/`--contact` run can cover dozens of issues, and one KEP's bad
  file should turn into a `FAILED` row, never take down the whole run.
- **The issue body's own "PRs by stage and milestone" checklist goes
  stale** — some real, currently-open KEPs (e.g. #6371) still say the
  literal `v1.xx` placeholder in that checklist even though the actual
  milestone is correctly set elsewhere, and older/long-running KEPs
  (e.g. #2535) don't even use that checklist format at all, nesting a
  version-labelled sub-bullet under a bare stage marker instead. This is
  exactly why PR discovery moved to GitHub's cross-reference timeline
  instead of parsing the body.
- **Merely mentioning `#<issue-number>` isn't enough to confirm a PR is
  *the* KEP's PR** — a PR for a completely different KEP can also
  cross-reference an issue (e.g. "related to #N"), which creates the same
  timeline event. Always additionally confirm the candidate PR's file list
  touches `keps/<sig>/<N>-<slug>/...` before trusting it.
- **Forks are not always named `enhancements`.** A contributor's fork can be
  renamed (e.g. `Tal-or/k8s-enhancements`). Always read the PR's
  `headRepository.nameWithOwner` field rather than assuming
  `<owner>/enhancements`.
- **Master can be stale relative to an open PR.** If the identified KEP PR
  is still open and touches `kep.yaml`/`README.md`/the PRR approval file,
  read *that PR's* copy of the file, not master's — master reflects the
  pre-PR state until it merges. Only fall back to master for a file the PR
  doesn't touch (meaning it's assumed already correct from an earlier,
  separate merge).
- **`latest-milestone` isn't always written with a `v` prefix** (e.g. `1.37`
  vs `v1.38`). Comparisons strip a leading `v` on both sides before
  comparing so this doesn't cause false mismatches.
- **The `milestone` struct is only required to change when the KEP is
  graduating to a new stage this cycle** — see "Graduation-aware kep.yaml
  check" above. Checking it unconditionally against the target milestone
  produces false positives for any KEP quietly continuing at the same
  stage across releases (this was a real bug caught by testing against
  issue #2535).
- Don't use a broad word like `"fill in"` as a placeholder marker for the
  PRR questionnaire heuristic — the KEP template's own boilerplate ("also
  fill in values in `kep.yaml`") contains that phrase even in a fully
  answered question, which caused a false positive during testing. Keep the
  marker list narrow (currently just `"to be completed"`).
- Don't flag a PRR questionnaire subsection as unanswered just because it's
  *short* — a real, complete answer like "No." is only a few characters.
  Flag emptiness (nothing left after stripping comments/headings) or the
  literal placeholder phrase, not length.
- **A PR's title can name the KEP number while its body never links the
  issue at all** — the KEP PR template has an "Issue link:" field that's
  easy to leave blank (real example: issue #4958's PR #5672, titled
  `KEP-4958: ...`, has an empty "Issue link:" field and never mentions
  `#4958` anywhere in its body, so GitHub creates no cross-reference event
  for it). This is why PR discovery pools three independent signals
  (cross-reference, title/body text search, issue body checklist) instead
  of trusting just one, with the file-touch check as the shared filter
  that keeps false positives out regardless of which signal found them.

## Verified against real issues

Tested against live `kubernetes/enhancements` issues in the v1.38 milestone
covering every branch: a fully-ready alpha KEP found via cross-reference
with no ambiguity (#6274, #6371, #6252, #6313), a beta KEP with a genuinely
unanswered questionnaire section (#6030 before its real answer was found;
confirmed complete after), an issue missing its stage label entirely
(#6361), a long-running KEP with no checklist-style body at all whose real
gap is a stale `latest-milestone` and not the `milestone` struct (#2535), a
KEP with an ambiguous second cross-referencing PR correctly excluded via
the file-touch filter (#6318), a KEP genuinely graduating stages this
cycle where the `milestone` struct addition is correctly required (#5419)
versus one already merged with no open PR, correctly falling back to
commit-history-based ownership attribution (#5589), and a KEP whose open
PR is only discoverable via the title/body text search since its body
never links the issue (#4958, PR #5672).
