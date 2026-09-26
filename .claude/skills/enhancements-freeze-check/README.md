# Enhancements Freeze Check

Check Kubernetes Enhancement Proposal (KEP) readiness for Enhancements Freeze
and generate draft reminder comments for human review. The skill never posts
comments or changes GitHub automatically.

## Prerequisites

- [Claude Code](https://docs.anthropic.com/en/docs/claude-code)
- Python 3 with PyYAML (`pip3 install pyyaml`)
- GitHub CLI (`gh`), authenticated with repository and project read access:

  ```bash
  gh auth login
  gh auth refresh -s read:project
  ```

## Use the skill

From the root of this repository, start Claude Code:

```bash
cd k8s-release-enhancement-skills
claude
```

Then run:

```text
/enhancements-freeze-check
```

The skill runs preflight checks and asks whether to review issue numbers, all
KEPs assigned to an Enhancements Contact, or all KEPs belonging to a SIG.

You can include the request directly:

```text
/enhancements-freeze-check check issues 6274 and 6371
/enhancements-freeze-check check everything assigned to @wendy-ha18
/enhancements-freeze-check check all KEPs for sig-node
```

Reports are written to `report/enhancements-freeze-<UTC-timestamp>.md`. Review
every draft before posting it to GitHub.
