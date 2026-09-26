## 1. Does not meet the Enhancements Freeze criteria

If the enhancement does not meet the Enhancements Freeze criteria for inclusion in the current release, add an issue comment using this template:

```
Hello {enhancement owner} :wave:, v1.38 Enhancements team here.

Just checking in as we approach [enhancements freeze](https://github.com/kubernetes/sig-release/blob/master/releases/release_phases.md#enhancements-freeze) on **Tuesday 29th September 2026 (AoE) / Wednesday 30th September 2026 12:00 UTC**.

This enhancement is targeting stage `{stage}` for v1.38 (correct me, if otherwise)

Here's where this enhancement currently stands:

- [ ] KEP readme using the [latest template](https://github.com/kubernetes/enhancements/tree/master/keps/NNNN-kep-template) has been merged into the k/enhancements repo.
- [ ] KEP status is marked as `implementable` for `latest-milestone: v1.38`.
- [ ] KEP readme has up-to-date graduation criteria.
- [ ] KEP has a production readiness review that has been completed and merged into k/enhancements. (For more information on the PRR process, check [here](https://github.com/kubernetes/community/blob/master/sig-architecture/production-readiness.md#submitting-a-kep-for-production-readiness-approval)).
- [ ] There are no other outstanding (unmerged) PRs that modify the KEP readme or kep.yaml file.

For this KEP, we would just need to update the following:
- {insert list of action items}

The status of this enhancement is marked as `At risk for enhancements freeze`. Please keep the issue description up-to-date with appropriate stages as well.

If you anticipate missing enhancements freeze, you can file an [exception request](https://github.com/kubernetes/sig-release/blob/master/releases/EXCEPTIONS.md) in advance. Thank you!
```

Then make sure the status of the enhancement is set to `At risk for enhancements freeze`.

## 2. Meet the Enhancements Freeze criteria

If the enhancement does meet the Enhancements Freeze criteria for inclusion in the current release, add an issue comment using this template:

```
Hello {enhancement owner} :wave:, v1.38 Enhancements team here.

Just checking in as we approach [enhancements freeze](https://github.com/kubernetes/sig-release/blob/master/releases/release_phases.md#enhancements-freeze) on **Tuesday 29th September 2026 (AoE) / Wednesday 30th September 2026 12:00 UTC**.

This enhancement is targeting stage `{stage}` for v1.38 (correct me, if otherwise)

Here’s where this enhancement currently stands:

- [X] KEP readme using the [latest template](https://github.com/kubernetes/enhancements/tree/master/keps/NNNN-kep-template) has been merged into the k/enhancements repo.
- [X] KEP status is marked as `implementable` for `latest-milestone: v1.38`. KEPs targeting `stable` will need to be marked as `implemented` after code PRs are merged.
- [X] KEP readme has up-to-date graduation criteria.
- [X] KEP has [submitted a production readiness review](https://github.com/kubernetes/community/blob/master/sig-architecture/production-readiness.md#submitting-a-kep-for-production-readiness-approval) request for approval and has a reviewer assigned.
- [X] KEP has a production readiness review that has been completed and merged into k/enhancements. (For more information on the PRR process, check [here](https://github.com/kubernetes/community/blob/master/sig-architecture/production-readiness.md#submitting-a-kep-for-production-readiness-approval)).
- [X] There are no other outstanding (unmerged) PRs that modify the KEP readme or kep.yaml file.

With all the KEP requirements in place and merged into k/enhancements, this enhancement is all good for the upcoming enhancements freeze. :rocket:

The status of this enhancement is marked as `Tracked for enhancements freeze`. Please keep the issue description up-to-date with appropriate stages as well. Thank you!

/label tracked/yes
```

Then make sure the status of the enhancement is set to `Tracked for enhancements freeze`.
