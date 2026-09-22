---
name: kep-readiness-check
description: Use this whenever the user wants to check KEP readiness status and draft a reminder comment for one or more kubernetes/enhancements issues, an Enhancements Contact's handle, or a SIG.
date: 2026-09-20
---

# KEP Readiness Check

## Purpose

This skill is for the **Kubernetes Enhancements team** to review KEPs
against the current release's requirements, identify upcoming milestone
risks, and generate summaries and draft reminder comments for KEP
authors. It never posts anything itself — it only produces drafts and
recommendations for a human to review and act on.

It treats the **[v1.38 Release Tracking board](https://github.com/orgs/kubernetes/projects/269/views/1)**
as the source of truth for release tracking (Enhancement Contact, SIG),
and the **official SIG Release documentation** as the source of truth
for milestone dates and requirements (fetched live, not hardcoded — see
Section 3).

The driver script is `check_kep_readiness.py` in this skill's directory;
everything below describes what it does and how to use it.

## 1. Preflight Checks

Before asking the user what to review, run:

```bash
python3 .claude/skills/kep-readiness-check/check_kep_readiness.py --preflight
```

This checks, in order:

1. **`gh` auth scope** — the `project` (or `read:project`) OAuth scope is
   required to query the tracking board, on top of the `repo` scope
   everything else uses. Checked by parsing `gh auth status`.
2. **Board access** — a real query against the [v1.38 tracking
   board](https://github.com/orgs/kubernetes/projects/269) (org
   `kubernetes`, project 269), reporting how many items it can see.
3. **Live release dates** — fetches and prints the current KEP Readiness
   Deadline and Enhancements Freeze dates (see Section 3).

`gh auth refresh -s read:project` is **interactive** (it opens a browser
device-code flow) — it cannot be run non-interactively on the user's
behalf. If the preflight fails on the scope check, stop and tell the user
exactly that command to run themselves; do not attempt to run it for
them, and do not continue to ask about issues/contact/SIG or perform any
analysis until a rerun of `--preflight` passes.

## 2. Ask the User What to Review

Once preflight passes, ask the user to pick **one** of three inputs — do
not ask for issue numbers if they've already picked Enhancement Contact
or SIG:

1. **KEP issue numbers** (e.g. "1234, 5678") — check only those issues:
   ```bash
   python3 .claude/skills/kep-readiness-check/check_kep_readiness.py <issue-number> [<issue-number> ...]
   ```
2. **Enhancement Contact** — a GitHub handle from the board's
   **Enhancements Contact** column. The script resolves every issue on
   the board with that value and checks all of them:
   ```bash
   python3 .claude/skills/kep-readiness-check/check_kep_readiness.py --contact <github-handle>
   ```
3. **SIG** — a SIG name from the board's **SIG** column (always
   `sig-<name>`, e.g. `sig-node`, `sig-storage`; `sig/node` or just `node`
   are also accepted and normalized). Resolves and checks every matching
   issue:
   ```bash
   python3 .claude/skills/kep-readiness-check/check_kep_readiness.py --sig <sig-name>
   ```

Example prompt: "Which kubernetes/enhancements issue number(s) would you
like to generate a KEP readiness deadline reminder for? (Or give me your
GitHub handle as the Enhancements Contact to check everything assigned to
you, or a SIG name to check everything for that SIG.)"

A `--sig` on a big SIG, or a `--contact` with many issues, can mean
dozens of issues in one run, each needing several `gh` calls — expect it
to take a while and don't kill it early.

**"Enhancements Contact" is not the issue's assignee.** They're two
different stakeholders tracked as two different fields on the board: the
Enhancements Contact is the *Enhancements team member* responsible for
reminding a KEP's owner about deadlines (a fixed-roster single-select
field, e.g. `@wendy-ha18` — not a free people-picker), while the issue's
GitHub `assignees` is typically the KEP owner/author themselves. An
earlier version of this skill got this wrong (matched on assignees
instead — see Gotchas), which is why this distinction is called out
explicitly. The **SIG** field is likewise the board's own field, not
necessarily identical to the issue's `sig/*` label — the two can diverge
(verified: `sig-network` returns a different, smaller set of issues from
the board field than from the label) — so trust the board field, which is
what both `--contact` and `--sig` read via the Projects v2 GraphQL API
(`fetch_project_items()` / `project_field_value()`).

## 3. Official Sources

| Source | Used for | How it's read |
|---|---|---|
| [v1.38 tracking board](https://github.com/orgs/kubernetes/projects/269/views/1) (project 269) | Enhancement Contact, SIG | Projects v2 GraphQL (`fetch_project_items()`) |
| [`release-1.38` timeline](https://github.com/kubernetes/sig-release/tree/master/releases/release-1.38) | KEP Readiness Deadline & Enhancements Freeze dates | Fetched live every run (`load_release_deadlines()`) — see below |
| [`release_phases.md`](https://github.com/kubernetes/sig-release/blob/master/releases/release_phases.md#prr-freeze) | The KEP Readiness requirements themselves | Read once while building this skill; encoded as the checks in Section 6 |
| [`kubernetes/enhancements` issues](https://github.com/kubernetes/enhancements/issues) | The KEP tracking issue itself | `gh issue view` |
| [`kubernetes/enhancements` PRs](https://github.com/kubernetes/enhancements/pulls) | The KEP's implementation PR | See Section 4 |

**The deadline dates are fetched live, not hardcoded.** `TARGET_MILESTONE
= "v1.38"` in `check_kep_readiness.py` is the one thing that still needs a
manual bump each release cycle (see "Updating for a new release cycle"
below) — everything downstream of it, including the two deadline dates,
is derived automatically: `load_release_deadlines()` fetches
`releases/release-<N>/README.md` from `kubernetes/sig-release`, finds the
Timeline table row for `**Begin enforcing [KEP Readiness
Deadline]**`/`**Begin [Enhancements Freeze]**` (a naive keyword search
would also match an unrelated, earlier "Call for exceptions" row that
happens to contain the same words — the `**Begin` prefix disambiguates),
and parses the UTC half of its dual AoE/UTC date string into an actual
`datetime`. If the fetch or parse fails for any reason, it falls back to
the hardcoded `*_FALLBACK` constants and prints a warning — this must
never raise and block a run.

## 4. Identify KEP PRs Related to Each Issue

For each issue, the script pools PR candidates from **three independent
signals**, then requires every candidate to clear one shared confirmation
filter before it's trusted (`find_kep_pr()`):

1. **GitHub's cross-reference records** (`find_crossreferenced_open_prs()`).
   Whenever a PR's description or *comments* mention `#<issue-number>` or
   link to the issue, GitHub logs a `cross-referenced` timeline event —
   visible via `gh api repos/kubernetes/enhancements/issues/<N>/timeline`.
   Catches mentions left in review comments, not just the PR body.
2. **A title/body text search** (`find_prs_by_text_search()`, via `gh
   search prs "<N> in:title,body" --repo kubernetes/enhancements --state
   open`). Catches PRs whose title names the KEP number (e.g. `KEP-4958:
   ...`) but whose body never actually links the issue — the template's
   "Issue link:" field left blank, so GitHub never creates a
   cross-reference event for it at all. (Real example: issue #4958's open
   PR, #5672, is only found this way.)
3. **The issue body's own PR checklist** (`find_prs_from_issue_body()`),
   as a last resort — any enhancements-repo PR link on a line that also
   mentions the target milestone. Not trusted alone (see below), but
   still worth pooling as a candidate.
4. **Confirmation** (`touches_kep_dir()`), applied to every candidate from
   any of the above: does the candidate PR's file list actually touch
   this KEP's own directory (`keps/<sig>/<N>-<slug>/...`)? A PR from a
   *different* KEP that merely name-drops "see also #N" passes signal 1
   or 2 but fails this filter. (Verified: issue #6318 has two
   cross-referencing open PRs; only the one whose files actually live
   under `keps/sig-node/6318-.../` survives.)

The issue body's own "PRs by stage and milestone" checklist is
deliberately **not** the primary source — it's exactly the kind of
free-form text contributors forget to update as a KEP moves through many
PRs over many release cycles (some real, currently-open KEPs still say
the literal `v1.xx` placeholder; older/long-running KEPs don't even use
that checklist format at all).

Then:

- If exactly one PR survives confirmation, it's the KEP's PR — its author
  becomes the "enhancement owner," and its head branch (if still open) is
  read in preference to master for any file it touches, since master can
  still hold the pre-PR content.
- If **no** PR survives at all, everything must already be satisfied on
  master — ownership is attributed to whoever authored the most recent
  commit to `kep.yaml` instead (`last_merged_pr_for_path()`), and there's
  no PR link to show.
- If more than one PR survives (rare — e.g. a stray leftover PR from an
  earlier stage still open), the most recently created one is used and
  the rest are surfaced as an outstanding action so you can sanity-check
  by hand; the KEP is never marked fully ready while this is ambiguous.

## 5. Determine the Current Release Context

For each KEP, determine:

- **Target release**: is the issue's GitHub milestone `v1.38`?
- **Target stage**: the issue's own `stage/{alpha,beta,stable}` label — a
  maintained, canonical field, not free-form issue-body text that can go
  stale. (This session deliberately kept stage sourced from the label
  rather than the board's own "Stage" field, even though the board can
  diverge from labels for other fields like SIG — see Gotchas for the
  reasoning.)
- **Which milestone it's working toward**: derived from the target
  stage/release above, and whether `kep.yaml`'s `stage` on master already
  matches it (used for the graduation check in Section 6).
- **Whether it's expected to meet KEP Readiness**: the pass/fail result of
  Section 6's checks.
- **What's still outstanding**: the specific, actionable list of gaps.

## 6. Validate KEP Readiness

For each KEP targeting v1.38, against
[`release_phases.md#prr-freeze`](https://github.com/kubernetes/sig-release/blob/master/releases/release_phases.md#prr-freeze):

1. Issue is in the target milestone.
2. `lead-opted-in` label is present.
3. `kep.yaml`'s own `stage` matches the issue's `stage/*` label (this *is*
   the "stage label is accurate" check — kep.yaml is authoritative for
   what the KEP is actually targeting).
4. A PR (open or merged — from Section 4) has the KEP's **PRR
   questionnaire** filled out.
5. A PR (open or merged) has **`kep.yaml`** updated with `stage` and
   `latest-milestone` for the current milestone, and the `milestone`
   struct too **only if graduating to a new stage this cycle** — see
   below.
6. A PR (open or merged) has the **PRR approval file**
   (`keps/prod-readiness/<sig>/<kep-number>.yaml`) with an approver
   assigned for the target stage.

Checks 1-3, 5, and 6 are exact (label/YAML field comparisons), inspecting
the actual KEP PR and files directly rather than relying on the issue
description. Check 4 (the questionnaire) is a **heuristic** — it looks for
the KEP template's own `<!-- ... -->` placeholder comments and literal "To
be completed for {stage}" boilerplate still sitting under a required
question, flagging a section only when nothing but that placeholder is
left (a short real answer like "No." must not be flagged — it's complete,
not empty). It catches the common case well, but always sanity-check it
against the README before trusting it fully, especially for non-standard
phrasing.

Each requirement resolves to **complete** (✅) or **incomplete** (❌) in the
report's "KEP Readiness" section; when incomplete, the specific action
needed is named in "Outstanding actions" (never just "not ready").

### Graduation-aware kep.yaml check

Per policy, `milestone.<stage>` only needs updating **if the KEP is
graduating to a new stage this cycle**; `latest-milestone` always has to
equal the current release regardless. The script determines "graduating"
by comparing the target stage (from the label) to whatever `stage` is set
to on master right now, before any open PR's changes: if they differ (or
`kep.yaml` doesn't exist on master yet), it's a graduation and
`milestone.<stage>` must equal the current milestone; if they're the
same, the KEP is just continuing at its existing stage, so
`milestone.<stage>` is left alone and may still show whichever earlier
release first reached it.

(Real example: issue #2535 has been `stage: beta` since v1.35 and isn't
graduating now, so `milestone.beta` staying at `v1.35` is correct — only
its stale `latest-milestone: v1.37` is a real gap.)

### Recommended v1.38 tracking board status

Derived straight from the policy text:

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
phase, not the later ones. It does **not** currently read the board's own
`Status` value for a "move from `<current>` to `<recommendation>`"
comparison — just the recommendation on its own; `fetch_project_items()` /
`project_field_value()` already have everything needed to add that
cheaply later (`project_field_value(item_node, "Status")`).

## 7. Generate the KEP Summary

For every KEP checked, a summary table row with these exact columns (also
reused as-is for each per-issue **Summary** subsection in Section 9):

| Column | Content |
|---|---|
| Issue | Linked issue number + title |
| KEP PR | Linked KEP update PR (Section 4), or `--` if none was found |
| Enhancement owner (KEP PR author) | The KEP PR's author (Section 4) |
| Target stage for v1.38 | From the issue's `stage/*` label |
| In v1.38 milestone | `yes`/`NO` |
| Recommended v1.38 tracking board status | Section 6's recommendation |

A failed lookup (e.g. a typo'd issue number) gets a `FAILED` row instead,
and the run's exit code is non-zero if any issue failed — the rest of the
batch still completes and gets its own section.

## 8. Generate the Reminder Comment

One draft per KEP, chosen by the recommended status from Section 6.
Placeholders (`{enhancement owner}`, `{stage}`, the PR link, action
items) are filled from the actual data gathered in Sections 4-6, never
left as literal template text in the output.

### 8.1 KEP does not meet KEP Readiness requirements (`At risk for KEP readiness`)

```text
Hello {enhancement owner} :wave:, 1.38 Enhancements team here.

This is a reminder of the upcoming [KEP readiness (formerly named PRR freeze)](https://github.com/kubernetes/sig-release/blob/master/releases/release_phases.md#prr-freeze) on **{deadline}**.

This enhancement is targeting stage `{stage}` for 1.38 (correct me, if otherwise). {one-line mention of the KEP PR checked, or that none was found}

Here's where this enhancement currently stands:

- [ ] PR open or merged with the KEP's [PRR questionnaire](https://github.com/kubernetes/enhancements/tree/master/keps/NNNN-kep-template#production-readiness-review-questionnaire) filled out.
- [ ] PR open or merged with [kep.yaml](https://github.com/kubernetes/enhancements/blob/master/keps/NNNN-kep-template/kep.yaml) updated with the `stage`, `latest-milestone`, and `milestone` struct filled out.
- [ ] PR open or merged with a [PRR approval file](https://github.com/kubernetes/enhancements/blob/master/keps/prod-readiness/template/nnnn.yaml) with the PRR approver listed for the stage the KEP is targeting.

For this KEP, we would just need to update the following:
- {specific outstanding action item(s)}

Note that the PR is not required to be approved or merged by the KEP readiness (formerly named PRR freeze) deadline. Having the PRR questionnaire filled out by the deadline will help ensure that the PRR team has enough time to review your KEP before **enhancements freeze on {freeze date}**. For more information on the PRR process, see [here](https://github.com/kubernetes/community/blob/master/sig-architecture/production-readiness.md#submitting-a-kep-for-production-readiness-approval).

The status of this enhancement is marked as `At risk for KEP readiness`. Please keep the issue description up-to-date with the appropriate stages as well.

If you anticipate missing KEP readiness (formerly named PRR freeze), you can file an [exception request](https://github.com/kubernetes/sig-release/blob/master/releases/EXCEPTIONS.md) in advance. Thank you!
```

Each checkbox reflects that specific requirement's actual pass/fail — not
all three unchecked by default.

### 8.2 KEP is past deadline and still doesn't meet requirements (`Removed from Milestone`)

Same shape, but past tense, cites removal, and closes with a call to file
an exception rather than "in advance" phrasing (see the live template in
`render_issue_markdown()` in the script — its wording differs enough from
8.1 that duplicating it here would drift out of sync).

### 8.3 KEP meets KEP Readiness requirements (`Tracked for KEP readiness`)

```text
Hello {enhancement owner} :wave:, 1.38 Enhancements team here.

This is a reminder of the upcoming [KEP readiness (formerly named PRR freeze)](https://github.com/kubernetes/sig-release/blob/master/releases/release_phases.md#prr-freeze) on **{deadline}**.

This enhancement is targeting stage `{stage}` for 1.38 (correct me, if otherwise). {one-line mention of the KEP PR checked}

Here's where this enhancement currently stands:

- [x] PR open or merged with the KEP's [PRR questionnaire](https://github.com/kubernetes/enhancements/tree/master/keps/NNNN-kep-template#production-readiness-review-questionnaire) filled out.
- [x] PR open or merged with [kep.yaml](https://github.com/kubernetes/enhancements/blob/master/keps/NNNN-kep-template/kep.yaml) updated with the `stage`, `latest-milestone`, and `milestone` struct filled out.
- [x] PR open or merged with a [PRR approval file](https://github.com/kubernetes/enhancements/blob/master/keps/prod-readiness/template/nnnn.yaml) with the PRR approver listed for the stage the KEP is targeting.

Note that the PR is not required to be approved or merged by the KEP readiness (formerly named PRR freeze) deadline. Having the PRR questionnaire filled out by the deadline will help ensure that the PRR team has enough time to review your KEP before **enhancements freeze on {freeze date}**. For more information on the PRR process, see [here](https://github.com/kubernetes/community/blob/master/sig-architecture/production-readiness.md#submitting-a-kep-for-production-readiness-approval).

With all the KEP readiness (formerly named PRR freeze) requirements in place, this enhancement is now marked as `Tracked for KEP readiness`! Please keep the issue description up-to-date with the appropriate stages as well.

/label tracked/yes
```

## 9. Output Format

**The script writes a Markdown file — it does not print the report to the
terminal.** Each run writes `kep-readiness-<UTC-timestamp>.md` to the
current working directory (the repo root, alongside `README.md` — the
skill's usage instructions have the user `cd` there before starting
Claude Code) and never overwrites a previous run's file —
`write_report()` never opens an existing path for writing; if the
timestamp alone (second granularity) would collide with an existing file
(e.g. two runs within the same second), it appends `-1`, `-2`, etc. until
it finds an unused name. The terminal only gets a short pointer, e.g.:

```
Report written to: kep-readiness-20260919T183007Z.md
View the summary table and full draft comment(s) there (3 issue(s) checked).
```

**Once the script finishes, just tell the user the report is ready and
give them the file path.** Don't paste the report's contents into the
chat and don't re-summarize it into your own table; the file already has
everything. If the user then asks about a specific issue from that run,
or wants to post one of the drafts, read the file to answer — just don't
proactively dump it.

The file itself, in order:

1. Title, generation timestamp, issue count, and **which input was used**
   to generate the run — the specific issue numbers, or `Enhancement
   Contact @<handle>`, or `SIG <sig-name>` — as its own line, e.g.
   `Generate draft reminder comment for SIG sig-network.` This makes a
   report self-describing without needing to check how it was invoked.
2. The **Summary** table from Section 7, one row per issue checked (or a
   `FAILED` row).
3. One section per issue, in this exact structure:

   ```markdown
   ### #{issue number} — {issue title}

   **Summary**

   {the same single-row table as this issue's Section 7 row}

   **KEP Readiness**

   - PRR questionnaire: ✅ / ❌
   - `kep.yaml`: ✅ / ❌
   - PRR approval file: ✅ / ❌

   **Outstanding actions**

   - {action item, if any -- or "None -- all criteria met."}

   **Draft GitHub comment**

   *(review before posting -- do not auto-post)*

   ```markdown
   {generated comment from Section 8}
   ```
   ```

**Do not post any comment automatically** — ask the user first (e.g.
"want me to post this with `gh issue comment <n> --repo
kubernetes/enhancements --body-file -`?"). Posting a comment on a public
upstream issue is a visible, hard-to-undo action, so it needs explicit
sign-off every time, not just a one-time approval.

## 10. Important Behaviour

- Always run `--preflight` before asking the user what to review — never
  skip straight to asking for issue numbers.
- Treat the **v1.38 tracking board** as the source of truth for
  Enhancement Contact and SIG lookups; treat **live-fetched SIG Release
  docs** as the source of truth for milestone dates and requirements —
  never rely on a hardcoded date when the release timeline has a current
  one (Section 3).
- Never assume a KEP is ready based only on the tracking board's own
  status field — validate the actual KEP PR and files directly (Sections
  4-6).
- Never mark a KEP `Tracked for KEP readiness` unless *all* required
  criteria are satisfied.
- When requirements are missing, name the exact outstanding action —
  never just "not ready."
- Use the actual KEP PR's author as the Enhancement owner.
- A user may give multiple issue numbers, an Enhancement Contact, or a
  SIG — process every matching KEP consistently, the same way.
- Keep the generated reminder factual and action-oriented.
- Never modify GitHub issues, labels, or tracking-board fields
  automatically unless the user explicitly asks — by default, only
  generate drafts and recommendations for review.

## Prerequisites

- `gh` CLI, authenticated (`gh auth status`). Only read-only `gh` calls
  are made (`issue view`, `pr view`, `api .../timeline`, `api
  .../commits`, `api .../contents/...`, `api .../git/trees/master`, `api
  graphql`) — no writes.
- The `project` (or `read:project`) OAuth scope, needed for
  `--contact`/`--sig` and for `--preflight`. Grant with `gh auth refresh
  -s read:project` if `gh auth status` doesn't already list it (checked
  automatically by `--preflight`) — plain issue-number mode works without
  it, but the preflight step still expects it per Section 1.
- PyYAML (`python3 -c "import yaml"` to check; `pip3 install pyyaml` if
  missing).
- Write access to the current working directory (expected to be the repo
  root, alongside `README.md`) — the script writes the report file there.

## Updating for a new release cycle

Only one constant needs a manual bump each cycle, at the top of
`check_kep_readiness.py`:

```python
TARGET_MILESTONE = "v1.38"
```

Everything else derives from it automatically: `load_release_deadlines()`
fetches `releases/release-<N>/README.md` from `kubernetes/sig-release`
live every run and parses the current KEP Readiness Deadline and
Enhancements Freeze dates out of its Timeline table (see Section 3) — no
hardcoded date needs updating anymore. The `KEP_READINESS_DEADLINE_
FALLBACK` / `KEP_READINESS_DEADLINE_UTC_FALLBACK` / `ENHANCEMENTS_FREEZE_
FALLBACK` constants only matter if that live fetch ever fails; they're not
load-bearing in normal operation, so there's no need to keep them
perfectly current, just plausible. Also update the milestone number
implied by `kubernetes/enhancements/milestone/<N>` if you want the script
to sanity-check milestone numbers too (it currently only compares
milestone *titles*, e.g. `"v1.38"`, so no other change is needed there).

## Gotchas found while building this

- **"Enhancements Contact" is a different person from the issue's
  assignee — don't infer one from the other.** An earlier version of
  `--contact` matched on the issue's GitHub `assignees` field on the
  (wrong) assumption that it correlated with the board's Enhancements
  Contact. It happened to line up on the handful of issues tested, which
  made the bug easy to miss — the actual field only exists on the
  Projects v2 board and has its own fixed-roster single-select values
  (e.g. `@wendy-ha18`), read via `fetch_project_items()` /
  `project_field_value()`.
- **The board's own fields can genuinely diverge from the issue's
  labels** — verified for SIG (`sig-network` returns a different, smaller
  set of issues from the board field than from the `sig/network` label).
  This session deliberately did *not* extend the same switch to "Target
  stage," keeping it sourced from the issue's `stage/*` label rather than
  the board's "Stage" field, since that check is already well-tested and
  the board/label divergence wasn't verified for Stage specifically — if
  you ever see them disagree in practice, that's the place to revisit.
- **The Timeline table has two rows mentioning "KEP Readiness Deadline"**
  — a "Call for ... Exceptions" row with an unrelated date, and the actual
  "**Begin enforcing [KEP Readiness Deadline]**" row. A naive keyword
  search grabs the wrong (earlier) one; `extract_timeline_row()` requires
  the `**Begin` prefix to disambiguate.
- **A single malformed `kep.yaml` can crash a whole batch run if you're
  not careful.** PyYAML's implicit timestamp resolver raises a raw
  `ValueError` (not `yaml.YAMLError`) for a date-shaped-but-invalid value
  like a `creation-date` with the day/month swapped -- found this for
  real while testing `--sig sig-network` across 8 issues at once. All
  `yaml.safe_load` call sites catch `(yaml.YAMLError, ValueError)` now,
  and `main()`'s per-issue loop catches any `Exception`, not just
  `RuntimeError` -- a `--sig`/`--contact` run can cover dozens of issues,
  and one KEP's bad file should turn into a `FAILED` row, never take down
  the whole run.
- **The issue body's own "PRs by stage and milestone" checklist goes
  stale** — some real, currently-open KEPs (e.g. #6371) still say the
  literal `v1.xx` placeholder even though the actual milestone is
  correctly set elsewhere, and older/long-running KEPs (e.g. #2535) don't
  even use that checklist format at all. Exactly why PR discovery (Section
  4) moved to GitHub's cross-reference timeline instead of parsing the
  body.
- **Merely mentioning `#<issue-number>` isn't enough to confirm a PR is
  *the* KEP's PR** — a PR for a completely different KEP can also
  cross-reference an issue (e.g. "related to #N"), which creates the same
  timeline event. Always additionally confirm the candidate PR's file
  list touches `keps/<sig>/<N>-<slug>/...` before trusting it.
- **Forks are not always named `enhancements`.** A contributor's fork can
  be renamed (e.g. `Tal-or/k8s-enhancements`). Always read the PR's
  `headRepository.nameWithOwner` field rather than assuming
  `<owner>/enhancements`.
- **Master can be stale relative to an open PR.** If the identified KEP
  PR is still open and touches `kep.yaml`/`README.md`/the PRR approval
  file, read *that PR's* copy of the file, not master's — master reflects
  the pre-PR state until it merges. Only fall back to master for a file
  the PR doesn't touch (meaning it's assumed already correct from an
  earlier, separate merge).
- **`latest-milestone` isn't always written with a `v` prefix** (e.g.
  `1.37` vs `v1.38`). Comparisons strip a leading `v` on both sides
  before comparing so this doesn't cause false mismatches.
- **The `milestone` struct is only required to change when the KEP is
  graduating to a new stage this cycle** — see "Graduation-aware kep.yaml
  check" in Section 6. Checking it unconditionally against the target
  milestone produces false positives for any KEP quietly continuing at
  the same stage across releases (a real bug caught by testing against
  issue #2535).
- Don't use a broad word like `"fill in"` as a placeholder marker for the
  PRR questionnaire heuristic — the KEP template's own boilerplate ("also
  fill in values in `kep.yaml`") contains that phrase even in a fully
  answered question, which caused a false positive during testing. Keep
  the marker list narrow (currently just `"to be completed"`).
- Don't flag a PRR questionnaire subsection as unanswered just because
  it's *short* — a real, complete answer like "No." is only a few
  characters. Flag emptiness (nothing left after stripping
  comments/headings) or the literal placeholder phrase, not length.
- **A PR's title can name the KEP number while its body never links the
  issue at all** — the KEP PR template has an "Issue link:" field that's
  easy to leave blank (real example: issue #4958's PR #5672, titled
  `KEP-4958: ...`, has an empty "Issue link:" field and never mentions
  `#4958` anywhere in its body, so GitHub creates no cross-reference
  event for it). Exactly why PR discovery (Section 4) pools three
  independent signals instead of trusting just one.

## Verified against real issues

Tested against live `kubernetes/enhancements` issues in the v1.38
milestone covering every branch: a fully-ready alpha KEP found via
cross-reference with no ambiguity (#6274, #6371, #6252, #6313), a beta
KEP with a genuinely unanswered questionnaire section (#6030 before its
real answer was found; confirmed complete after), an issue missing its
stage label entirely (#6361), a long-running KEP with no checklist-style
body at all whose real gap is a stale `latest-milestone` and not the
`milestone` struct (#2535), a KEP with an ambiguous second
cross-referencing PR correctly excluded via the file-touch filter
(#6318), a KEP genuinely graduating stages this cycle where the
`milestone` struct addition is correctly required (#5419) versus one
already merged with no open PR, correctly falling back to
commit-history-based ownership attribution (#5589), a KEP whose open PR
is only discoverable via the title/body text search since its body never
links the issue (#4958, PR #5672), `--contact wendy-ha18` and `--sig
sig-network` resolving correctly against the real board (including
proving the board's SIG field diverges from the `sig/*` label), the live
release-date fetch correctly parsing the real `release-1.38` Timeline
table (and initially grabbing the wrong row before the `**Begin` fix),
and a simulated post-deadline clock exercising the `Removed from
Milestone` template end-to-end.
