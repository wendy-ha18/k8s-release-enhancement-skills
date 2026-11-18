# KEP Readiness Check

Check Kubernetes Enhancement Proposal (KEP) readiness and generate draft
reminder comments for review. The skill never posts comments automatically.

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

Then run this command inside Claude Code:

```text
/kep-readiness-check
```

The skill runs its preflight checks and then asks whether to review:

- one or more `kubernetes/enhancements` issue numbers;
- all KEPs assigned to an Enhancements Contact; or
- all KEPs belonging to a SIG.

You can also include the request directly:

```text
/kep-readiness-check check issues 6089 and 5598
/kep-readiness-check check everything assigned to @wendy-ha18
/kep-readiness-check check all KEPs for sig-network
```

The generated Markdown report is written to `report/`. Review every draft
before posting it to GitHub.
