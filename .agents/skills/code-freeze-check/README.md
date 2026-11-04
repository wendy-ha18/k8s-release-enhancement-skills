# Code Freeze Check

Check Kubernetes Enhancement Proposal (KEP) readiness for Code Freeze and
Test Freeze, and generate draft reminder comments for human review. The skill
never posts comments or changes GitHub automatically.

This is a project skill in `.agents/skills/`, so Cursor and other coding tools
that follow the [Agent Skills](https://cursor.com/docs/skills) layout can load
it. Code and test pull requests are read from `kubernetes/kubernetes` only.

## Prerequisites

- Python 3
- GitHub CLI (`gh`), authenticated with repository and project read access:

  ```bash
  gh auth login
  gh auth refresh -s read:project
  ```

## Use the skill

From the root of this repository, ask the coding agent to run the code-freeze
check. It should run preflight first, then review issue numbers, every KEP
assigned to an Enhancements Contact, or every KEP for a SIG.

You can also run the checker directly:

```bash
python3 .agents/skills/code-freeze-check/check_code_freeze.py --preflight
python3 .agents/skills/code-freeze-check/check_code_freeze.py 6274 6371
python3 .agents/skills/code-freeze-check/check_code_freeze.py --contact wendy-ha18
python3 .agents/skills/code-freeze-check/check_code_freeze.py --sig sig-node
```

Reports are written to `report/code-freeze-<UTC-timestamp>.md`. Review every
draft before posting it to GitHub.
