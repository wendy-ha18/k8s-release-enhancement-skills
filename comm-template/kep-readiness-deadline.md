## 1. Does not meet the KEP Readiness Deadline criteria

If the enhancement *does not* meet the KEP readiness (formerly named PRR freeze) criteria for inclusion in the current release, add an issue comment using this template:

```
Hello {enhancement owner} :wave:, 1.38 Enhancements team here.

This is a reminder of the upcoming [KEP readiness (formerly named PRR freeze)](https://github.com/kubernetes/sig-release/blob/master/releases/release_phases.md#prr-freeze) on **Tuesday 22nd September 2026 (AoE) / Wednesday 23th September 2026 12:00 UTC**.

This enhancement is targeting stage `{stage}` for 1.38 (correct me, if otherwise)

Here's where this enhancement currently stands:

- [ ] PR open or merged with the KEP's [PRR questionnaire](https://github.com/kubernetes/enhancements/tree/master/keps/NNNN-kep-template#production-readiness-review-questionnaire) filled out.
- [ ] PR open or merged with [kep.yaml](https://github.com/kubernetes/enhancements/blob/master/keps/NNNN-kep-template/kep.yaml) updated with the `stage`, `latest-milestone`, and `milestone` struct filled out.
- [ ] PR open or merged with a [PRR approval file](https://github.com/kubernetes/enhancements/blob/master/keps/prod-readiness/template/nnnn.yaml) with the PRR approver listed for the stage the KEP is targeting.

For this KEP, we would just need to update the following:
- {insert list of action items}

Note that the PR is not required to be approved or merged by the KEP readiness (formerly named PRR freeze) deadline. Having the PRR questionnaire filled out by the deadline will help ensure that the PRR team has enough time to review your KEP before **enhancements freeze on Tuesday 29th September 2026 (AoE) / Wednesday 30th September 2026 12:00 UTC**. For more information on the PRR process, see [here](https://github.com/kubernetes/community/blob/master/sig-architecture/production-readiness.md#submitting-a-kep-for-production-readiness-approval).

The status of this enhancement is marked as `At risk for KEP readiness`. Please keep the issue description up-to-date with appropriate stages as well.

If you anticipate missing KEP readiness (formerly named PRR freeze), you can file an [exception request](https://github.com/kubernetes/sig-release/blob/master/releases/EXCEPTIONS.md) in advance. Thank you!
```

Then make sure the status of the enhancement is set to `At risk for KEP readiness`.

## 2. Meet the KEP Readiness Deadline criteria

If the enhancement *does* meet the KEP readiness (formerly named PRR freeze) criteria for inclusion in the current release, add an issue comment using this template:

```
Hello {enhancement owner} :wave:, 1.38 Enhancements team here.

This is a reminder of the upcoming [KEP readiness (formerly named PRR freeze)](https://github.com/kubernetes/sig-release/blob/master/releases/release_phases.md#prr-freeze) on **Tuesday 22nd September 2026 (AoE) / Wednesday 23th September 2026 12:00 UTC**.

This enhancement is targeting stage `{stage}` for 1.38 (correct me, if otherwise)

Here's where this enhancement currently stands:

- [x] PR open or merged with the KEP's [PRR questionnaire](https://github.com/kubernetes/enhancements/tree/master/keps/NNNN-kep-template#production-readiness-review-questionnaire) filled out.
- [x] PR open or merged with [kep.yaml](https://github.com/kubernetes/enhancements/blob/master/keps/NNNN-kep-template/kep.yaml) updated with the `stage`, `latest-milestone`, and `milestone` struct filled out.
- [x] PR open or merged with a [PRR approval file](https://github.com/kubernetes/enhancements/blob/master/keps/prod-readiness/template/nnnn.yaml) with the PRR approver listed for the stage the KEP is targeting.

Note that the PR is not required to be approved or merged by the KEP readiness (formerly named PRR freeze) deadline. Having the PRR questionnaire filled out by the deadline will help ensure that the PRR team has enough time to review your KEP before **enhancements freeze on Tuesday 29th September 2026 (AoE) / Wednesday 30th September 2026 12:00 UTC**. For more information on the PRR process, see [here](https://github.com/kubernetes/community/blob/master/sig-architecture/production-readiness.md#submitting-a-kep-for-production-readiness-approval).

With all the KEP readiness (formerly named PRR freeze) requirements in place, this enhancement is now marked as `Tracked for KEP readiness`! Please keep the issue description up-to-date with appropriate stages as well.

/label tracked/yes
```

Then make sure the status of the enhancement is set to `Tracked for KEP readiness`.
