## 1. Does not meet the Code Freeze and Test Freeze criteria

If the enhancement does not meet the Code Freeze and Test Freeze criteria for inclusion in the current release, add an issue comment using this template:

```
Hey again {enhancement owner} :wave:, v1.38 Enhancements team here,

Just checking in as we approach [code freeze](https://github.com/kubernetes/sig-release/blob/master/releases/release_phases.md#code-freeze) and [test freeze](https://github.com/kubernetes/sig-release/blob/master/releases/release_phases.md#test-freeze) at **Monday 16th November 2026 (AoE) / Tuesday 17th November 2026, 12:00 UTC**.

Here's where this enhancement currently stands:

- [ ] All PRs to the Kubernetes repo that are related to your enhancement are linked in the above issue description (for tracking purposes).
- [ ] All PRs are ready to be merged (they have `approved` and `lgtm` labels applied) by the code freeze deadline. This **includes** tests.

Per the issue description, these are all of the implementation (code-related) PRs for v1.38, some of which are not merged yet:
- { list of PRs associated with this enhancement }

Please let me know (and keep the issue description updated) if there are any other PRs in [`k/k`](https://github.com/kubernetes/kubernetes) that we should track for this KEP, so that we can maintain accurate status.

If the implementation work for this enhancement is occurring **out-of-tree** (i.e., outside of `k/k`), please link the relevant PRs in the issue description for visibility. Alternatively, if you're unable to provide specific PR links, a confirmation that **all out-of-tree implementation work is complete and merged** will help us finalize tracking and maintain accuracy.

The status of this enhancement is marked as `At risk for code freeze`.

If you anticipate missing code freeze, you can file an [exception request](https://github.com/kubernetes/sig-release/blob/master/releases/EXCEPTIONS.md) in advance.
```

Then make sure the status of the enhancement is set to `At risk for code freeze`.

## 2. Meets the Code Freeze and Test Freeze criteria

If the enhancement does meet the Code Freeze and Test Freeze criteria for inclusion in the current release, add an issue comment using this template:

```
Hey again {enhancement owner} :wave:, v1.38 Enhancements team here,

Just checking in as we approach [code freeze](https://github.com/kubernetes/sig-release/blob/master/releases/release_phases.md#code-freeze) and [test freeze](https://github.com/kubernetes/sig-release/blob/master/releases/release_phases.md#test-freeze) at **Monday 16th November 2026 (AoE) / Tuesday 17th November 2026, 12:00 UTC**.

Here's where this enhancement currently stands:

- [x] All PRs to the Kubernetes repo that are related to your enhancement are linked in the above issue description (for tracking purposes).
- [x] All PRs are ready to be merged (they have `approved` and `lgtm` labels applied) by the code freeze deadline. This **includes** tests.

Per the issue description, these are all of the implementation (code-related) PRs for v1.38:
- { list of PRs associated with this enhancement }

Please let me know (and keep the issue description updated) if there are any other PRs in [`k/k`](https://github.com/kubernetes/kubernetes) that we should track for this KEP, so that we can maintain accurate status.

If the implementation work for this enhancement is occurring **out-of-tree** (i.e., outside of `k/k`), please link the relevant PRs in the issue description for visibility. Alternatively, if you're unable to provide specific PR links, a confirmation that **all out-of-tree implementation work is complete and merged** will help us finalize tracking and maintain accuracy.

This enhancement is now marked as `Tracked for code freeze`!

Please note that KEPs targeting `stable` need to have the `status` field marked as `implemented` in the kep.yaml file after code PRs are merged.

/label tracked/yes
```

Then make sure the status of the enhancement is set to `Tracked for code freeze`.
