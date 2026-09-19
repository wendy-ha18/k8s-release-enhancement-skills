---
name: kep-readiness-check
description: Use this whenever the user wants to check KEP readiness status and draft a reminder comment for a specific enhancements issue number.
date: 2026-09-20
---

# KEP Readiness Check

Checks a single `kubernetes/enhancements` tracking issue against the KEP
Readiness (formerly "PRR freeze") criteria for the current release, and
drafts a dedicated reminder comment that Enhancements team can use to posts on the
issue. The skill never posts anything itself — it only produces a draft for you to
review and post by hand (e.g. via `gh issue comment`).

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

The policy text is specific:

> `milestone` struct updated with the current stage and release (**only if
> graduating to a new stage**)

So the script compares the target stage (from the label) against what
`stage` is set to **on master right now** (before any open PR's changes).
If they differ (or `kep.yaml` doesn't exist on master yet at all), the KEP
is graduating this cycle, and `milestone.<stage>` must equal the current
milestone. If they're the same — the KEP is just continuing at the stage it
was already at last release — `milestone.<stage>` is left alone; it's
allowed to still show whichever earlier release first reached that stage.
`latest-milestone`, by contrast, always has to equal the current milestone,
graduating or not.

(Real example: issue #2535 has `stage: beta`, `milestone: {alpha: v1.33,
beta: v1.35}` on master — it reached beta back in v1.35 and isn't
graduating now, so `milestone.beta` staying at `v1.35` is correct and not
flagged; only its stale `latest-milestone: v1.37` is a real gap. Contrast
with #5419, which is going from `beta` to `stable` this cycle: there,
`milestone.stable` genuinely needs to be added.)

Checks 1-3, 5, and 6 are exact (label/YAML field comparisons). Check 4 (the
PRR questionnaire) is a **heuristic** — it looks for the KEP template's own
`<!-- ... -->` placeholder comments and literal "To be completed for
{stage}" boilerplate still sitting under a required question, and only
flags a section when nothing but that placeholder is left (a short real
answer like "No." must not be flagged — it's complete, not empty). It
catches the common case well, but always sanity-check it against the
README before trusting it fully, especially if a KEP's questionnaire uses
non-standard phrasing.

## Running it

Run the driver with one or more issue numbers (space-separated):

```bash
python3 .claude/skills/kep-readiness-check/check_kep_readiness.py <issue-number> [<issue-number> ...]
```

(Path is relative to the repo root you're running Claude Code from — adjust
if your cwd differs.)

With a single issue number, it just prints that one report. With two or
more, it prints a `########## Issue N of M: #<number> ##########` header
before each one and keeps going even if one issue fails (e.g. a typo'd
issue number) — the error for that issue goes to stderr and the rest of
the batch still runs; the process exits non-zero if *any* issue failed.

When this skill is invoked (e.g. via `/kep-readiness-check`) and the user
hasn't already given at least one issue number, **ask for it** before
running anything — e.g. "Which kubernetes/enhancements issue number(s) do
you want a KEP readiness report for?" To sweep the whole [v1.38 tracking
board](https://github.com/orgs/kubernetes/projects/269/views/1), pass every
issue number from the board in one invocation and summarize the combined
results — there's no need to run it once per issue.

The script prints, for each issue, in order:

1. A short status summary (owner, target stage, milestone, the KEP's PR
   link if one is open, pass/fail per criterion).
2. The full draft comment, using the "still at risk" template (unchecked
   boxes + a bullet list of exactly what's missing) or the "fully tracked"
   template (all boxes checked, ends with `/label tracked/yes`) depending on
   whether every criterion passed. Each of the three checklist lines links
   the KEP PR that was actually checked (e.g. `([PR #6267](https://.../pull/6267))`)
   when one was found — omitted only when no open PR exists at all and
   everything is already satisfied on master.

Show the user both the status summary and the draft comment. **Do not post
the comment automatically** — ask the user first (e.g. "want me to post
this with `gh issue comment <n> --repo kubernetes/enhancements --body-file
-`?"). Posting a comment on a public upstream issue is a visible, hard-to-
undo action, so it needs explicit sign-off every time, not just a one-time
approval.

## Prerequisites

- `gh` CLI, authenticated (`gh auth status`). Only read-only `gh` calls are
  made (`issue view`, `pr view`, `api .../timeline`, `api .../commits`, `api
  .../contents/...`, `api .../git/trees/master`) — no writes.
- PyYAML (`python3 -c "import yaml"` to check; `pip3 install pyyaml` if
  missing).

## Updating for a new release cycle

The milestone and the two deadline dates are hardcoded as constants at the
top of `check_kep_readiness.py`:

```python
TARGET_MILESTONE = "v1.38"
KEP_READINESS_DEADLINE = "..."
ENHANCEMENTS_FREEZE = "..."
```

Each release cycle, pull the new dates from
`https://github.com/kubernetes/sig-release/tree/master/releases/release-1.<N>`
(the "Timeline" table's **KEP Readiness Deadline** and **Enhancements
Freeze** rows) and update these three constants, along with the milestone
number implied by `kubernetes/enhancements/milestone/<N>` if you want the
script to sanity-check milestone numbers too (it currently only compares
milestone *titles*, e.g. `"v1.38"`, so no other change is needed there).

## Gotchas found while building this

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
