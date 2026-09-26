# Enhancements Freeze Report -- v1.38

Generated: 2026-09-26 13:38 UTC
Issues checked: 16
Generate draft reminder comment for Enhancement Contact @wendy-ha18.

## Summary

| Issue | KEP PR | Enhancement owner (KEP PR author) | Target stage for v1.38 | In v1.38 milestone | Recommended v1.38 tracking board status |
|---|---|---|---|---|---|
| [#2535](https://github.com/kubernetes/enhancements/issues/2535) Ensure secret pulled images | [PR #6334](https://github.com/kubernetes/enhancements/pull/6334) | @SergeyKanzhelev | beta | NO | At risk for enhancements freeze |
| [#4563](https://github.com/kubernetes/enhancements/issues/4563) EvictionRequest API | [PR #6405](https://github.com/kubernetes/enhancements/pull/6405) | @atiratree | alpha | yes | Tracked for enhancements freeze |
| [#5517](https://github.com/kubernetes/enhancements/issues/5517) DRA: Node Allocatable Resource Requests | [PR #6082](https://github.com/kubernetes/enhancements/pull/6082) | @pravk03 | beta | yes | At risk for enhancements freeze |
| [#5825](https://github.com/kubernetes/enhancements/issues/5825) CRI List Streaming | [PR #6146](https://github.com/kubernetes/enhancements/pull/6146) | @bitoku | beta | yes | Tracked for enhancements freeze |
| [#5999](https://github.com/kubernetes/enhancements/issues/5999) HTTP/2 cleartext (h2c) for container probes | [PR #6334](https://github.com/kubernetes/enhancements/pull/6334) | @SergeyKanzhelev | beta | yes | At risk for enhancements freeze |
| [#6147](https://github.com/kubernetes/enhancements/issues/6147) Dynamic node declared features Discovery | [PR #6148](https://github.com/kubernetes/enhancements/pull/6148) | @HirazawaUi | alpha | yes | At risk for enhancements freeze |
| [#6032](https://github.com/kubernetes/enhancements/issues/6032) localhost NodePort userspace proxy for nftables | [PR #6378](https://github.com/kubernetes/enhancements/pull/6378) | @AustinAbro321 | beta | yes | Tracked for enhancements freeze |
| [#6035](https://github.com/kubernetes/enhancements/issues/6035) Exec session identity propagation | [PR #6201](https://github.com/kubernetes/enhancements/pull/6201) | @SergeyKanzhelev | alpha | yes | At risk for enhancements freeze |
| [#4958](https://github.com/kubernetes/enhancements/issues/4958) CSI Sidecars All in one | [PR #5153](https://github.com/kubernetes/enhancements/pull/5153) | @mowangdk | alpha | yes | At risk for enhancements freeze |
| [#6089](https://github.com/kubernetes/enhancements/issues/6089) WAS: Controller Integration APIs | [PR #6342](https://github.com/kubernetes/enhancements/pull/6342) | @mm4tt | beta | yes | Tracked for enhancements freeze |
| [#5598](https://github.com/kubernetes/enhancements/issues/5598) Opportunistic batching | [PR #6039](https://github.com/kubernetes/enhancements/pull/6039) | @romanbaron | beta | yes | At risk for enhancements freeze |
| [#3541](https://github.com/kubernetes/enhancements/issues/3541) Add Recreate Update Strategy to StatefulSet | [PR #6155](https://github.com/kubernetes/enhancements/pull/6155) | @galal-hussein | beta | yes | At risk for enhancements freeze |
| [#6249](https://github.com/kubernetes/enhancements/issues/6249) SLM: Publish Graceful Node Shutdown state for DaemonSet coordination | [PR #6351](https://github.com/kubernetes/enhancements/pull/6351) | @danbruno101 | alpha | yes | At risk for enhancements freeze |
| [#5381](https://github.com/kubernetes/enhancements/issues/5381) Mutable PersistentVolume Node Affinity | [PR #5382](https://github.com/kubernetes/enhancements/pull/5382) | @huww98 | alpha | yes | At risk for enhancements freeze |
| [#6361](https://github.com/kubernetes/enhancements/issues/6361) KEP: Controller Leader Election Recovery | [PR #6365](https://github.com/kubernetes/enhancements/pull/6365) | @jpbetz | UNKNOWN | yes | At risk for enhancements freeze |
| [#6386](https://github.com/kubernetes/enhancements/issues/6386) Introduce the ability to configure ephemeral storage at the pod level | [PR #6394](https://github.com/kubernetes/enhancements/pull/6394) | @ndixita | alpha | yes | At risk for enhancements freeze |

---

### #2535 — Ensure secret pulled images

**Summary**

| Issue | KEP PR | Enhancement owner (KEP PR author) | Target stage for v1.38 | In v1.38 milestone | Recommended v1.38 tracking board status |
|---|---|---|---|---|---|
| [#2535](https://github.com/kubernetes/enhancements/issues/2535) Ensure secret pulled images | [PR #6334](https://github.com/kubernetes/enhancements/pull/6334) | @SergeyKanzhelev | beta | NO | At risk for enhancements freeze |

**Enhancements Freeze**

- KEP README merged and latest template: ❌
- `kep.yaml` merged and current: ❌
- Graduation Criteria: ✅
- Test Plan: ❌
- Production Readiness Review: ✅
- No outstanding KEP metadata PRs: ❌

**Outstanding actions**

- Issue is not in the **v1.38** milestone (currently: `none`).
- Merge or close outstanding PR(s) that modify the KEP README or `kep.yaml`: [#6267](https://github.com/kubernetes/enhancements/pull/6267).
- Merge the required `kep.yaml` updates -- `latest-milestone` is `v1.37`, expected `v1.38`.
- Update the merged KEP README to the latest template (heading-based heuristic) -- missing current template section `## Alternatives`; missing current template section `## Drawbacks`.
- Complete the detailed Test Plan (heuristic; verify manually) -- `Test Plan` still contains template placeholder content.

**Draft GitHub comment**

*(review before posting -- do not auto-post)*

```markdown
Hello @SergeyKanzhelev :wave:, v1.38 Enhancements team here.

Just checking in as we approach [enhancements freeze](https://github.com/kubernetes/sig-release/blob/master/releases/release_phases.md#enhancements-freeze) on **Tuesday 29th September 2026 (AoE) / Wednesday 30th September 2026 12:00 UTC**.

This enhancement is targeting stage `beta` for v1.38 (correct me, if otherwise)

Here's where this enhancement currently stands:

- [ ] KEP readme using the [latest template](https://github.com/kubernetes/enhancements/tree/master/keps/NNNN-kep-template) has been merged into the k/enhancements repo.
- [ ] KEP status is marked as `implementable` for `latest-milestone: v1.38`.
- [x] KEP readme has up-to-date graduation criteria.
- [ ] KEP readme has an updated detailed test plan.
- [x] KEP has a production readiness review that has been completed and merged into k/enhancements. (For more information on the PRR process, check [here](https://github.com/kubernetes/community/blob/master/sig-architecture/production-readiness.md#submitting-a-kep-for-production-readiness-approval)).
- [ ] There are no other outstanding (unmerged) PRs that modify the KEP readme or kep.yaml file.

For this KEP, we would just need to update the following:
- Issue is not in the **v1.38** milestone (currently: `none`).
- Merge or close outstanding PR(s) that modify the KEP README or `kep.yaml`: [#6267](https://github.com/kubernetes/enhancements/pull/6267).
- Merge the required `kep.yaml` updates -- `latest-milestone` is `v1.37`, expected `v1.38`.
- Update the merged KEP README to the latest template (heading-based heuristic) -- missing current template section `## Alternatives`; missing current template section `## Drawbacks`.
- Complete the detailed Test Plan (heuristic; verify manually) -- `Test Plan` still contains template placeholder content.

The status of this enhancement is marked as `At risk for enhancements freeze`. Please keep the issue description up-to-date with appropriate stages as well.

If you anticipate missing enhancements freeze, you can file an [exception request](https://github.com/kubernetes/sig-release/blob/master/releases/EXCEPTIONS.md) in advance. Thank you!
```

---

### #4563 — EvictionRequest API

**Summary**

| Issue | KEP PR | Enhancement owner (KEP PR author) | Target stage for v1.38 | In v1.38 milestone | Recommended v1.38 tracking board status |
|---|---|---|---|---|---|
| [#4563](https://github.com/kubernetes/enhancements/issues/4563) EvictionRequest API | [PR #6405](https://github.com/kubernetes/enhancements/pull/6405) | @atiratree | alpha | yes | Tracked for enhancements freeze |

**Enhancements Freeze**

- KEP README merged and latest template: ✅
- `kep.yaml` merged and current: ✅
- Graduation Criteria: ✅
- Test Plan: ✅
- Production Readiness Review: ✅
- No outstanding KEP metadata PRs: ✅

**Outstanding actions**

- None -- all criteria met.

**Draft GitHub comment**

*(review before posting -- do not auto-post)*

```markdown
Hello @atiratree :wave:, v1.38 Enhancements team here.

Just checking in as we approach [enhancements freeze](https://github.com/kubernetes/sig-release/blob/master/releases/release_phases.md#enhancements-freeze) on **Tuesday 29th September 2026 (AoE) / Wednesday 30th September 2026 12:00 UTC**.

This enhancement is targeting stage `alpha` for v1.38 (correct me, if otherwise)

Here's where this enhancement currently stands:

- [x] KEP readme using the [latest template](https://github.com/kubernetes/enhancements/tree/master/keps/NNNN-kep-template) has been merged into the k/enhancements repo.
- [x] KEP status is marked as `implementable` for `latest-milestone: v1.38`.
- [x] KEP readme has up-to-date graduation criteria.
- [x] KEP readme has an updated detailed test plan.
- [x] KEP has a production readiness review that has been completed and merged into k/enhancements. (For more information on the PRR process, check [here](https://github.com/kubernetes/community/blob/master/sig-architecture/production-readiness.md#submitting-a-kep-for-production-readiness-approval)).
- [x] There are no other outstanding (unmerged) PRs that modify the KEP readme or kep.yaml file.

With all the KEP requirements in place and merged into k/enhancements, this enhancement is all good for the upcoming enhancements freeze. :rocket:

The status of this enhancement is marked as `Tracked for enhancements freeze`. Please keep the issue description up-to-date with appropriate stages as well. Thank you!

/label tracked/yes
```

---

### #5517 — DRA: Node Allocatable Resource Requests

**Summary**

| Issue | KEP PR | Enhancement owner (KEP PR author) | Target stage for v1.38 | In v1.38 milestone | Recommended v1.38 tracking board status |
|---|---|---|---|---|---|
| [#5517](https://github.com/kubernetes/enhancements/issues/5517) DRA: Node Allocatable Resource Requests | [PR #6082](https://github.com/kubernetes/enhancements/pull/6082) | @pravk03 | beta | yes | At risk for enhancements freeze |

**Enhancements Freeze**

- KEP README merged and latest template: ✅
- `kep.yaml` merged and current: ❌
- Graduation Criteria: ✅
- Test Plan: ✅
- Production Readiness Review: ❌
- No outstanding KEP metadata PRs: ❌

**Outstanding actions**

- Merge or close outstanding PR(s) that modify the KEP README or `kep.yaml`: [#6324](https://github.com/kubernetes/enhancements/pull/6324).
- Merge the required `kep.yaml` updates -- `stage` is `alpha`, expected `beta`; `latest-milestone` is `v1.37`, expected `v1.38`.
- Complete and merge the PRR questionnaire -- still unanswered (heuristic; verify manually): Rollout, Upgrade and Rollback Planning.
- Complete and merge the PRR approval -- no `beta:` entry in the PRR approval file.

**Draft GitHub comment**

*(review before posting -- do not auto-post)*

```markdown
Hello @pravk03 :wave:, v1.38 Enhancements team here.

Just checking in as we approach [enhancements freeze](https://github.com/kubernetes/sig-release/blob/master/releases/release_phases.md#enhancements-freeze) on **Tuesday 29th September 2026 (AoE) / Wednesday 30th September 2026 12:00 UTC**.

This enhancement is targeting stage `beta` for v1.38 (correct me, if otherwise)

Here's where this enhancement currently stands:

- [x] KEP readme using the [latest template](https://github.com/kubernetes/enhancements/tree/master/keps/NNNN-kep-template) has been merged into the k/enhancements repo.
- [ ] KEP status is marked as `implementable` for `latest-milestone: v1.38`.
- [x] KEP readme has up-to-date graduation criteria.
- [x] KEP readme has an updated detailed test plan.
- [ ] KEP has a production readiness review that has been completed and merged into k/enhancements. (For more information on the PRR process, check [here](https://github.com/kubernetes/community/blob/master/sig-architecture/production-readiness.md#submitting-a-kep-for-production-readiness-approval)).
- [ ] There are no other outstanding (unmerged) PRs that modify the KEP readme or kep.yaml file.

For this KEP, we would just need to update the following:
- Merge or close outstanding PR(s) that modify the KEP README or `kep.yaml`: [#6324](https://github.com/kubernetes/enhancements/pull/6324).
- Merge the required `kep.yaml` updates -- `stage` is `alpha`, expected `beta`; `latest-milestone` is `v1.37`, expected `v1.38`.
- Complete and merge the PRR questionnaire -- still unanswered (heuristic; verify manually): Rollout, Upgrade and Rollback Planning.
- Complete and merge the PRR approval -- no `beta:` entry in the PRR approval file.

The status of this enhancement is marked as `At risk for enhancements freeze`. Please keep the issue description up-to-date with appropriate stages as well.

If you anticipate missing enhancements freeze, you can file an [exception request](https://github.com/kubernetes/sig-release/blob/master/releases/EXCEPTIONS.md) in advance. Thank you!
```

---

### #5825 — CRI List Streaming

**Summary**

| Issue | KEP PR | Enhancement owner (KEP PR author) | Target stage for v1.38 | In v1.38 milestone | Recommended v1.38 tracking board status |
|---|---|---|---|---|---|
| [#5825](https://github.com/kubernetes/enhancements/issues/5825) CRI List Streaming | [PR #6146](https://github.com/kubernetes/enhancements/pull/6146) | @bitoku | beta | yes | Tracked for enhancements freeze |

**Enhancements Freeze**

- KEP README merged and latest template: ✅
- `kep.yaml` merged and current: ✅
- Graduation Criteria: ✅
- Test Plan: ✅
- Production Readiness Review: ✅
- No outstanding KEP metadata PRs: ✅

**Outstanding actions**

- None -- all criteria met.

**Draft GitHub comment**

*(review before posting -- do not auto-post)*

```markdown
Hello @bitoku :wave:, v1.38 Enhancements team here.

Just checking in as we approach [enhancements freeze](https://github.com/kubernetes/sig-release/blob/master/releases/release_phases.md#enhancements-freeze) on **Tuesday 29th September 2026 (AoE) / Wednesday 30th September 2026 12:00 UTC**.

This enhancement is targeting stage `beta` for v1.38 (correct me, if otherwise)

Here's where this enhancement currently stands:

- [x] KEP readme using the [latest template](https://github.com/kubernetes/enhancements/tree/master/keps/NNNN-kep-template) has been merged into the k/enhancements repo.
- [x] KEP status is marked as `implementable` for `latest-milestone: v1.38`.
- [x] KEP readme has up-to-date graduation criteria.
- [x] KEP readme has an updated detailed test plan.
- [x] KEP has a production readiness review that has been completed and merged into k/enhancements. (For more information on the PRR process, check [here](https://github.com/kubernetes/community/blob/master/sig-architecture/production-readiness.md#submitting-a-kep-for-production-readiness-approval)).
- [x] There are no other outstanding (unmerged) PRs that modify the KEP readme or kep.yaml file.

With all the KEP requirements in place and merged into k/enhancements, this enhancement is all good for the upcoming enhancements freeze. :rocket:

The status of this enhancement is marked as `Tracked for enhancements freeze`. Please keep the issue description up-to-date with appropriate stages as well. Thank you!

/label tracked/yes
```

---

### #5999 — HTTP/2 cleartext (h2c) for container probes

**Summary**

| Issue | KEP PR | Enhancement owner (KEP PR author) | Target stage for v1.38 | In v1.38 milestone | Recommended v1.38 tracking board status |
|---|---|---|---|---|---|
| [#5999](https://github.com/kubernetes/enhancements/issues/5999) HTTP/2 cleartext (h2c) for container probes | [PR #6334](https://github.com/kubernetes/enhancements/pull/6334) | @SergeyKanzhelev | beta | yes | At risk for enhancements freeze |

**Enhancements Freeze**

- KEP README merged and latest template: ✅
- `kep.yaml` merged and current: ❌
- Graduation Criteria: ✅
- Test Plan: ✅
- Production Readiness Review: ❌
- No outstanding KEP metadata PRs: ❌

**Outstanding actions**

- Merge or close outstanding PR(s) that modify the KEP README or `kep.yaml`: [#6338](https://github.com/kubernetes/enhancements/pull/6338).
- Merge the required `kep.yaml` updates -- `stage` is `alpha`, expected `beta`; `latest-milestone` is `v1.37`, expected `v1.38`.
- Complete and merge the PRR approval -- no `beta:` entry in the PRR approval file.

**Draft GitHub comment**

*(review before posting -- do not auto-post)*

```markdown
Hello @SergeyKanzhelev :wave:, v1.38 Enhancements team here.

Just checking in as we approach [enhancements freeze](https://github.com/kubernetes/sig-release/blob/master/releases/release_phases.md#enhancements-freeze) on **Tuesday 29th September 2026 (AoE) / Wednesday 30th September 2026 12:00 UTC**.

This enhancement is targeting stage `beta` for v1.38 (correct me, if otherwise)

Here's where this enhancement currently stands:

- [x] KEP readme using the [latest template](https://github.com/kubernetes/enhancements/tree/master/keps/NNNN-kep-template) has been merged into the k/enhancements repo.
- [ ] KEP status is marked as `implementable` for `latest-milestone: v1.38`.
- [x] KEP readme has up-to-date graduation criteria.
- [x] KEP readme has an updated detailed test plan.
- [ ] KEP has a production readiness review that has been completed and merged into k/enhancements. (For more information on the PRR process, check [here](https://github.com/kubernetes/community/blob/master/sig-architecture/production-readiness.md#submitting-a-kep-for-production-readiness-approval)).
- [ ] There are no other outstanding (unmerged) PRs that modify the KEP readme or kep.yaml file.

For this KEP, we would just need to update the following:
- Merge or close outstanding PR(s) that modify the KEP README or `kep.yaml`: [#6338](https://github.com/kubernetes/enhancements/pull/6338).
- Merge the required `kep.yaml` updates -- `stage` is `alpha`, expected `beta`; `latest-milestone` is `v1.37`, expected `v1.38`.
- Complete and merge the PRR approval -- no `beta:` entry in the PRR approval file.

The status of this enhancement is marked as `At risk for enhancements freeze`. Please keep the issue description up-to-date with appropriate stages as well.

If you anticipate missing enhancements freeze, you can file an [exception request](https://github.com/kubernetes/sig-release/blob/master/releases/EXCEPTIONS.md) in advance. Thank you!
```

---

### #6147 — Dynamic node declared features Discovery

**Summary**

| Issue | KEP PR | Enhancement owner (KEP PR author) | Target stage for v1.38 | In v1.38 milestone | Recommended v1.38 tracking board status |
|---|---|---|---|---|---|
| [#6147](https://github.com/kubernetes/enhancements/issues/6147) Dynamic node declared features Discovery | [PR #6148](https://github.com/kubernetes/enhancements/pull/6148) | @HirazawaUi | alpha | yes | At risk for enhancements freeze |

**Enhancements Freeze**

- KEP README merged and latest template: ❌
- `kep.yaml` merged and current: ❌
- Graduation Criteria: ❌
- Test Plan: ❌
- Production Readiness Review: ❌
- No outstanding KEP metadata PRs: ❌

**Outstanding actions**

- Merge or close outstanding PR(s) that modify the KEP README or `kep.yaml`: [#6148](https://github.com/kubernetes/enhancements/pull/6148).
- Could not locate a merged KEP directory (`keps/<sig>/<number>-*/`) on master.

**Draft GitHub comment**

*(review before posting -- do not auto-post)*

```markdown
Hello @HirazawaUi :wave:, v1.38 Enhancements team here.

Just checking in as we approach [enhancements freeze](https://github.com/kubernetes/sig-release/blob/master/releases/release_phases.md#enhancements-freeze) on **Tuesday 29th September 2026 (AoE) / Wednesday 30th September 2026 12:00 UTC**.

This enhancement is targeting stage `alpha` for v1.38 (correct me, if otherwise)

Here's where this enhancement currently stands:

- [ ] KEP readme using the [latest template](https://github.com/kubernetes/enhancements/tree/master/keps/NNNN-kep-template) has been merged into the k/enhancements repo.
- [ ] KEP status is marked as `implementable` for `latest-milestone: v1.38`.
- [ ] KEP readme has up-to-date graduation criteria.
- [ ] KEP readme has an updated detailed test plan.
- [ ] KEP has a production readiness review that has been completed and merged into k/enhancements. (For more information on the PRR process, check [here](https://github.com/kubernetes/community/blob/master/sig-architecture/production-readiness.md#submitting-a-kep-for-production-readiness-approval)).
- [ ] There are no other outstanding (unmerged) PRs that modify the KEP readme or kep.yaml file.

For this KEP, we would just need to update the following:
- Merge or close outstanding PR(s) that modify the KEP README or `kep.yaml`: [#6148](https://github.com/kubernetes/enhancements/pull/6148).
- Could not locate a merged KEP directory (`keps/<sig>/<number>-*/`) on master.

The status of this enhancement is marked as `At risk for enhancements freeze`. Please keep the issue description up-to-date with appropriate stages as well.

If you anticipate missing enhancements freeze, you can file an [exception request](https://github.com/kubernetes/sig-release/blob/master/releases/EXCEPTIONS.md) in advance. Thank you!
```

---

### #6032 — localhost NodePort userspace proxy for nftables

**Summary**

| Issue | KEP PR | Enhancement owner (KEP PR author) | Target stage for v1.38 | In v1.38 milestone | Recommended v1.38 tracking board status |
|---|---|---|---|---|---|
| [#6032](https://github.com/kubernetes/enhancements/issues/6032) localhost NodePort userspace proxy for nftables | [PR #6378](https://github.com/kubernetes/enhancements/pull/6378) | @AustinAbro321 | beta | yes | Tracked for enhancements freeze |

**Enhancements Freeze**

- KEP README merged and latest template: ✅
- `kep.yaml` merged and current: ✅
- Graduation Criteria: ✅
- Test Plan: ✅
- Production Readiness Review: ✅
- No outstanding KEP metadata PRs: ✅

**Outstanding actions**

- None -- all criteria met.

**Draft GitHub comment**

*(review before posting -- do not auto-post)*

```markdown
Hello @AustinAbro321 :wave:, v1.38 Enhancements team here.

Just checking in as we approach [enhancements freeze](https://github.com/kubernetes/sig-release/blob/master/releases/release_phases.md#enhancements-freeze) on **Tuesday 29th September 2026 (AoE) / Wednesday 30th September 2026 12:00 UTC**.

This enhancement is targeting stage `beta` for v1.38 (correct me, if otherwise)

Here's where this enhancement currently stands:

- [x] KEP readme using the [latest template](https://github.com/kubernetes/enhancements/tree/master/keps/NNNN-kep-template) has been merged into the k/enhancements repo.
- [x] KEP status is marked as `implementable` for `latest-milestone: v1.38`.
- [x] KEP readme has up-to-date graduation criteria.
- [x] KEP readme has an updated detailed test plan.
- [x] KEP has a production readiness review that has been completed and merged into k/enhancements. (For more information on the PRR process, check [here](https://github.com/kubernetes/community/blob/master/sig-architecture/production-readiness.md#submitting-a-kep-for-production-readiness-approval)).
- [x] There are no other outstanding (unmerged) PRs that modify the KEP readme or kep.yaml file.

With all the KEP requirements in place and merged into k/enhancements, this enhancement is all good for the upcoming enhancements freeze. :rocket:

The status of this enhancement is marked as `Tracked for enhancements freeze`. Please keep the issue description up-to-date with appropriate stages as well. Thank you!

/label tracked/yes
```

---

### #6035 — Exec session identity propagation

**Summary**

| Issue | KEP PR | Enhancement owner (KEP PR author) | Target stage for v1.38 | In v1.38 milestone | Recommended v1.38 tracking board status |
|---|---|---|---|---|---|
| [#6035](https://github.com/kubernetes/enhancements/issues/6035) Exec session identity propagation | [PR #6201](https://github.com/kubernetes/enhancements/pull/6201) | @SergeyKanzhelev | alpha | yes | At risk for enhancements freeze |

**Enhancements Freeze**

- KEP README merged and latest template: ✅
- `kep.yaml` merged and current: ❌
- Graduation Criteria: ✅
- Test Plan: ✅
- Production Readiness Review: ✅
- No outstanding KEP metadata PRs: ❌

**Outstanding actions**

- Merge or close outstanding PR(s) that modify the KEP README or `kep.yaml`: [#6205](https://github.com/kubernetes/enhancements/pull/6205).
- Merge the required `kep.yaml` updates -- `latest-milestone` is `v1.37`, expected `v1.38`.

**Draft GitHub comment**

*(review before posting -- do not auto-post)*

```markdown
Hello @SergeyKanzhelev :wave:, v1.38 Enhancements team here.

Just checking in as we approach [enhancements freeze](https://github.com/kubernetes/sig-release/blob/master/releases/release_phases.md#enhancements-freeze) on **Tuesday 29th September 2026 (AoE) / Wednesday 30th September 2026 12:00 UTC**.

This enhancement is targeting stage `alpha` for v1.38 (correct me, if otherwise)

Here's where this enhancement currently stands:

- [x] KEP readme using the [latest template](https://github.com/kubernetes/enhancements/tree/master/keps/NNNN-kep-template) has been merged into the k/enhancements repo.
- [ ] KEP status is marked as `implementable` for `latest-milestone: v1.38`.
- [x] KEP readme has up-to-date graduation criteria.
- [x] KEP readme has an updated detailed test plan.
- [x] KEP has a production readiness review that has been completed and merged into k/enhancements. (For more information on the PRR process, check [here](https://github.com/kubernetes/community/blob/master/sig-architecture/production-readiness.md#submitting-a-kep-for-production-readiness-approval)).
- [ ] There are no other outstanding (unmerged) PRs that modify the KEP readme or kep.yaml file.

For this KEP, we would just need to update the following:
- Merge or close outstanding PR(s) that modify the KEP README or `kep.yaml`: [#6205](https://github.com/kubernetes/enhancements/pull/6205).
- Merge the required `kep.yaml` updates -- `latest-milestone` is `v1.37`, expected `v1.38`.

The status of this enhancement is marked as `At risk for enhancements freeze`. Please keep the issue description up-to-date with appropriate stages as well.

If you anticipate missing enhancements freeze, you can file an [exception request](https://github.com/kubernetes/sig-release/blob/master/releases/EXCEPTIONS.md) in advance. Thank you!
```

---

### #4958 — CSI Sidecars All in one

**Summary**

| Issue | KEP PR | Enhancement owner (KEP PR author) | Target stage for v1.38 | In v1.38 milestone | Recommended v1.38 tracking board status |
|---|---|---|---|---|---|
| [#4958](https://github.com/kubernetes/enhancements/issues/4958) CSI Sidecars All in one | [PR #5153](https://github.com/kubernetes/enhancements/pull/5153) | @mowangdk | alpha | yes | At risk for enhancements freeze |

**Enhancements Freeze**

- KEP README merged and latest template: ❌
- `kep.yaml` merged and current: ❌
- Graduation Criteria: ✅
- Test Plan: ❌
- Production Readiness Review: ✅
- No outstanding KEP metadata PRs: ❌

**Outstanding actions**

- Merge or close outstanding PR(s) that modify the KEP README or `kep.yaml`: [#5672](https://github.com/kubernetes/enhancements/pull/5672).
- Merge the required `kep.yaml` updates -- `latest-milestone` is `v1.34`, expected `v1.38`.
- Update the merged KEP README to the latest template (heading-based heuristic) -- missing current template section `## Design Details`.
- Complete the detailed Test Plan (heuristic; verify manually) -- `Test Plan` section is empty.

**Draft GitHub comment**

*(review before posting -- do not auto-post)*

```markdown
Hello @mowangdk :wave:, v1.38 Enhancements team here.

Just checking in as we approach [enhancements freeze](https://github.com/kubernetes/sig-release/blob/master/releases/release_phases.md#enhancements-freeze) on **Tuesday 29th September 2026 (AoE) / Wednesday 30th September 2026 12:00 UTC**.

This enhancement is targeting stage `alpha` for v1.38 (correct me, if otherwise)

Here's where this enhancement currently stands:

- [ ] KEP readme using the [latest template](https://github.com/kubernetes/enhancements/tree/master/keps/NNNN-kep-template) has been merged into the k/enhancements repo.
- [ ] KEP status is marked as `implementable` for `latest-milestone: v1.38`.
- [x] KEP readme has up-to-date graduation criteria.
- [ ] KEP readme has an updated detailed test plan.
- [x] KEP has a production readiness review that has been completed and merged into k/enhancements. (For more information on the PRR process, check [here](https://github.com/kubernetes/community/blob/master/sig-architecture/production-readiness.md#submitting-a-kep-for-production-readiness-approval)).
- [ ] There are no other outstanding (unmerged) PRs that modify the KEP readme or kep.yaml file.

For this KEP, we would just need to update the following:
- Merge or close outstanding PR(s) that modify the KEP README or `kep.yaml`: [#5672](https://github.com/kubernetes/enhancements/pull/5672).
- Merge the required `kep.yaml` updates -- `latest-milestone` is `v1.34`, expected `v1.38`.
- Update the merged KEP README to the latest template (heading-based heuristic) -- missing current template section `## Design Details`.
- Complete the detailed Test Plan (heuristic; verify manually) -- `Test Plan` section is empty.

The status of this enhancement is marked as `At risk for enhancements freeze`. Please keep the issue description up-to-date with appropriate stages as well.

If you anticipate missing enhancements freeze, you can file an [exception request](https://github.com/kubernetes/sig-release/blob/master/releases/EXCEPTIONS.md) in advance. Thank you!
```

---

### #6089 — WAS: Controller Integration APIs

**Summary**

| Issue | KEP PR | Enhancement owner (KEP PR author) | Target stage for v1.38 | In v1.38 milestone | Recommended v1.38 tracking board status |
|---|---|---|---|---|---|
| [#6089](https://github.com/kubernetes/enhancements/issues/6089) WAS: Controller Integration APIs | [PR #6342](https://github.com/kubernetes/enhancements/pull/6342) | @mm4tt | beta | yes | Tracked for enhancements freeze |

**Enhancements Freeze**

- KEP README merged and latest template: ✅
- `kep.yaml` merged and current: ✅
- Graduation Criteria: ✅
- Test Plan: ✅
- Production Readiness Review: ✅
- No outstanding KEP metadata PRs: ✅

**Outstanding actions**

- None -- all criteria met.

**Draft GitHub comment**

*(review before posting -- do not auto-post)*

```markdown
Hello @mm4tt :wave:, v1.38 Enhancements team here.

Just checking in as we approach [enhancements freeze](https://github.com/kubernetes/sig-release/blob/master/releases/release_phases.md#enhancements-freeze) on **Tuesday 29th September 2026 (AoE) / Wednesday 30th September 2026 12:00 UTC**.

This enhancement is targeting stage `beta` for v1.38 (correct me, if otherwise)

Here's where this enhancement currently stands:

- [x] KEP readme using the [latest template](https://github.com/kubernetes/enhancements/tree/master/keps/NNNN-kep-template) has been merged into the k/enhancements repo.
- [x] KEP status is marked as `implementable` for `latest-milestone: v1.38`.
- [x] KEP readme has up-to-date graduation criteria.
- [x] KEP readme has an updated detailed test plan.
- [x] KEP has a production readiness review that has been completed and merged into k/enhancements. (For more information on the PRR process, check [here](https://github.com/kubernetes/community/blob/master/sig-architecture/production-readiness.md#submitting-a-kep-for-production-readiness-approval)).
- [x] There are no other outstanding (unmerged) PRs that modify the KEP readme or kep.yaml file.

With all the KEP requirements in place and merged into k/enhancements, this enhancement is all good for the upcoming enhancements freeze. :rocket:

The status of this enhancement is marked as `Tracked for enhancements freeze`. Please keep the issue description up-to-date with appropriate stages as well. Thank you!

/label tracked/yes
```

---

### #5598 — Opportunistic batching

**Summary**

| Issue | KEP PR | Enhancement owner (KEP PR author) | Target stage for v1.38 | In v1.38 milestone | Recommended v1.38 tracking board status |
|---|---|---|---|---|---|
| [#5598](https://github.com/kubernetes/enhancements/issues/5598) Opportunistic batching | [PR #6039](https://github.com/kubernetes/enhancements/pull/6039) | @romanbaron | beta | yes | At risk for enhancements freeze |

**Enhancements Freeze**

- KEP README merged and latest template: ✅
- `kep.yaml` merged and current: ❌
- Graduation Criteria: ✅
- Test Plan: ✅
- Production Readiness Review: ✅
- No outstanding KEP metadata PRs: ❌

**Outstanding actions**

- Merge or close outstanding PR(s) that modify the KEP README or `kep.yaml`: [#6411](https://github.com/kubernetes/enhancements/pull/6411).
- Merge the required `kep.yaml` updates -- `latest-milestone` is `v1.37`, expected `v1.38`.

**Draft GitHub comment**

*(review before posting -- do not auto-post)*

```markdown
Hello @romanbaron :wave:, v1.38 Enhancements team here.

Just checking in as we approach [enhancements freeze](https://github.com/kubernetes/sig-release/blob/master/releases/release_phases.md#enhancements-freeze) on **Tuesday 29th September 2026 (AoE) / Wednesday 30th September 2026 12:00 UTC**.

This enhancement is targeting stage `beta` for v1.38 (correct me, if otherwise)

Here's where this enhancement currently stands:

- [x] KEP readme using the [latest template](https://github.com/kubernetes/enhancements/tree/master/keps/NNNN-kep-template) has been merged into the k/enhancements repo.
- [ ] KEP status is marked as `implementable` for `latest-milestone: v1.38`.
- [x] KEP readme has up-to-date graduation criteria.
- [x] KEP readme has an updated detailed test plan.
- [x] KEP has a production readiness review that has been completed and merged into k/enhancements. (For more information on the PRR process, check [here](https://github.com/kubernetes/community/blob/master/sig-architecture/production-readiness.md#submitting-a-kep-for-production-readiness-approval)).
- [ ] There are no other outstanding (unmerged) PRs that modify the KEP readme or kep.yaml file.

For this KEP, we would just need to update the following:
- Merge or close outstanding PR(s) that modify the KEP README or `kep.yaml`: [#6411](https://github.com/kubernetes/enhancements/pull/6411).
- Merge the required `kep.yaml` updates -- `latest-milestone` is `v1.37`, expected `v1.38`.

The status of this enhancement is marked as `At risk for enhancements freeze`. Please keep the issue description up-to-date with appropriate stages as well.

If you anticipate missing enhancements freeze, you can file an [exception request](https://github.com/kubernetes/sig-release/blob/master/releases/EXCEPTIONS.md) in advance. Thank you!
```

---

### #3541 — Add Recreate Update Strategy to StatefulSet

**Summary**

| Issue | KEP PR | Enhancement owner (KEP PR author) | Target stage for v1.38 | In v1.38 milestone | Recommended v1.38 tracking board status |
|---|---|---|---|---|---|
| [#3541](https://github.com/kubernetes/enhancements/issues/3541) Add Recreate Update Strategy to StatefulSet | [PR #6155](https://github.com/kubernetes/enhancements/pull/6155) | @galal-hussein | beta | yes | At risk for enhancements freeze |

**Enhancements Freeze**

- KEP README merged and latest template: ✅
- `kep.yaml` merged and current: ❌
- Graduation Criteria: ✅
- Test Plan: ✅
- Production Readiness Review: ❌
- No outstanding KEP metadata PRs: ❌

**Outstanding actions**

- Merge or close outstanding PR(s) that modify the KEP README or `kep.yaml`: [#6360](https://github.com/kubernetes/enhancements/pull/6360).
- Merge the required `kep.yaml` updates -- `stage` is `alpha`, expected `beta`; `latest-milestone` is `v1.37`, expected `v1.38`; `milestone.beta` is missing.
- Complete and merge the PRR approval -- no `beta:` entry in the PRR approval file.

**Draft GitHub comment**

*(review before posting -- do not auto-post)*

```markdown
Hello @galal-hussein :wave:, v1.38 Enhancements team here.

Just checking in as we approach [enhancements freeze](https://github.com/kubernetes/sig-release/blob/master/releases/release_phases.md#enhancements-freeze) on **Tuesday 29th September 2026 (AoE) / Wednesday 30th September 2026 12:00 UTC**.

This enhancement is targeting stage `beta` for v1.38 (correct me, if otherwise)

Here's where this enhancement currently stands:

- [x] KEP readme using the [latest template](https://github.com/kubernetes/enhancements/tree/master/keps/NNNN-kep-template) has been merged into the k/enhancements repo.
- [ ] KEP status is marked as `implementable` for `latest-milestone: v1.38`.
- [x] KEP readme has up-to-date graduation criteria.
- [x] KEP readme has an updated detailed test plan.
- [ ] KEP has a production readiness review that has been completed and merged into k/enhancements. (For more information on the PRR process, check [here](https://github.com/kubernetes/community/blob/master/sig-architecture/production-readiness.md#submitting-a-kep-for-production-readiness-approval)).
- [ ] There are no other outstanding (unmerged) PRs that modify the KEP readme or kep.yaml file.

For this KEP, we would just need to update the following:
- Merge or close outstanding PR(s) that modify the KEP README or `kep.yaml`: [#6360](https://github.com/kubernetes/enhancements/pull/6360).
- Merge the required `kep.yaml` updates -- `stage` is `alpha`, expected `beta`; `latest-milestone` is `v1.37`, expected `v1.38`; `milestone.beta` is missing.
- Complete and merge the PRR approval -- no `beta:` entry in the PRR approval file.

The status of this enhancement is marked as `At risk for enhancements freeze`. Please keep the issue description up-to-date with appropriate stages as well.

If you anticipate missing enhancements freeze, you can file an [exception request](https://github.com/kubernetes/sig-release/blob/master/releases/EXCEPTIONS.md) in advance. Thank you!
```

---

### #6249 — SLM: Publish Graceful Node Shutdown state for DaemonSet coordination

**Summary**

| Issue | KEP PR | Enhancement owner (KEP PR author) | Target stage for v1.38 | In v1.38 milestone | Recommended v1.38 tracking board status |
|---|---|---|---|---|---|
| [#6249](https://github.com/kubernetes/enhancements/issues/6249) SLM: Publish Graceful Node Shutdown state for DaemonSet coordination | [PR #6351](https://github.com/kubernetes/enhancements/pull/6351) | @danbruno101 | alpha | yes | At risk for enhancements freeze |

**Enhancements Freeze**

- KEP README merged and latest template: ❌
- `kep.yaml` merged and current: ❌
- Graduation Criteria: ❌
- Test Plan: ❌
- Production Readiness Review: ❌
- No outstanding KEP metadata PRs: ❌

**Outstanding actions**

- Merge or close outstanding PR(s) that modify the KEP README or `kep.yaml`: [#6351](https://github.com/kubernetes/enhancements/pull/6351).
- Could not locate a merged KEP directory (`keps/<sig>/<number>-*/`) on master.

**Draft GitHub comment**

*(review before posting -- do not auto-post)*

```markdown
Hello @danbruno101 :wave:, v1.38 Enhancements team here.

Just checking in as we approach [enhancements freeze](https://github.com/kubernetes/sig-release/blob/master/releases/release_phases.md#enhancements-freeze) on **Tuesday 29th September 2026 (AoE) / Wednesday 30th September 2026 12:00 UTC**.

This enhancement is targeting stage `alpha` for v1.38 (correct me, if otherwise)

Here's where this enhancement currently stands:

- [ ] KEP readme using the [latest template](https://github.com/kubernetes/enhancements/tree/master/keps/NNNN-kep-template) has been merged into the k/enhancements repo.
- [ ] KEP status is marked as `implementable` for `latest-milestone: v1.38`.
- [ ] KEP readme has up-to-date graduation criteria.
- [ ] KEP readme has an updated detailed test plan.
- [ ] KEP has a production readiness review that has been completed and merged into k/enhancements. (For more information on the PRR process, check [here](https://github.com/kubernetes/community/blob/master/sig-architecture/production-readiness.md#submitting-a-kep-for-production-readiness-approval)).
- [ ] There are no other outstanding (unmerged) PRs that modify the KEP readme or kep.yaml file.

For this KEP, we would just need to update the following:
- Merge or close outstanding PR(s) that modify the KEP README or `kep.yaml`: [#6351](https://github.com/kubernetes/enhancements/pull/6351).
- Could not locate a merged KEP directory (`keps/<sig>/<number>-*/`) on master.

The status of this enhancement is marked as `At risk for enhancements freeze`. Please keep the issue description up-to-date with appropriate stages as well.

If you anticipate missing enhancements freeze, you can file an [exception request](https://github.com/kubernetes/sig-release/blob/master/releases/EXCEPTIONS.md) in advance. Thank you!
```

---

### #5381 — Mutable PersistentVolume Node Affinity

**Summary**

| Issue | KEP PR | Enhancement owner (KEP PR author) | Target stage for v1.38 | In v1.38 milestone | Recommended v1.38 tracking board status |
|---|---|---|---|---|---|
| [#5381](https://github.com/kubernetes/enhancements/issues/5381) Mutable PersistentVolume Node Affinity | [PR #5382](https://github.com/kubernetes/enhancements/pull/5382) | @huww98 | alpha | yes | At risk for enhancements freeze |

**Enhancements Freeze**

- KEP README merged and latest template: ✅
- `kep.yaml` merged and current: ❌
- Graduation Criteria: ✅
- Test Plan: ❌
- Production Readiness Review: ✅
- No outstanding KEP metadata PRs: ❌

**Outstanding actions**

- Merge or close outstanding PR(s) that modify the KEP README or `kep.yaml`: [#6231](https://github.com/kubernetes/enhancements/pull/6231).
- Merge the required `kep.yaml` updates -- `latest-milestone` is `v1.35`, expected `v1.38`.
- Complete the detailed Test Plan (heuristic; verify manually) -- `Test Plan` still contains template placeholder content.

**Draft GitHub comment**

*(review before posting -- do not auto-post)*

```markdown
Hello @huww98 :wave:, v1.38 Enhancements team here.

Just checking in as we approach [enhancements freeze](https://github.com/kubernetes/sig-release/blob/master/releases/release_phases.md#enhancements-freeze) on **Tuesday 29th September 2026 (AoE) / Wednesday 30th September 2026 12:00 UTC**.

This enhancement is targeting stage `alpha` for v1.38 (correct me, if otherwise)

Here's where this enhancement currently stands:

- [x] KEP readme using the [latest template](https://github.com/kubernetes/enhancements/tree/master/keps/NNNN-kep-template) has been merged into the k/enhancements repo.
- [ ] KEP status is marked as `implementable` for `latest-milestone: v1.38`.
- [x] KEP readme has up-to-date graduation criteria.
- [ ] KEP readme has an updated detailed test plan.
- [x] KEP has a production readiness review that has been completed and merged into k/enhancements. (For more information on the PRR process, check [here](https://github.com/kubernetes/community/blob/master/sig-architecture/production-readiness.md#submitting-a-kep-for-production-readiness-approval)).
- [ ] There are no other outstanding (unmerged) PRs that modify the KEP readme or kep.yaml file.

For this KEP, we would just need to update the following:
- Merge or close outstanding PR(s) that modify the KEP README or `kep.yaml`: [#6231](https://github.com/kubernetes/enhancements/pull/6231).
- Merge the required `kep.yaml` updates -- `latest-milestone` is `v1.35`, expected `v1.38`.
- Complete the detailed Test Plan (heuristic; verify manually) -- `Test Plan` still contains template placeholder content.

The status of this enhancement is marked as `At risk for enhancements freeze`. Please keep the issue description up-to-date with appropriate stages as well.

If you anticipate missing enhancements freeze, you can file an [exception request](https://github.com/kubernetes/sig-release/blob/master/releases/EXCEPTIONS.md) in advance. Thank you!
```

---

### #6361 — KEP: Controller Leader Election Recovery

**Summary**

| Issue | KEP PR | Enhancement owner (KEP PR author) | Target stage for v1.38 | In v1.38 milestone | Recommended v1.38 tracking board status |
|---|---|---|---|---|---|
| [#6361](https://github.com/kubernetes/enhancements/issues/6361) KEP: Controller Leader Election Recovery | [PR #6365](https://github.com/kubernetes/enhancements/pull/6365) | @jpbetz | UNKNOWN | yes | At risk for enhancements freeze |

**Enhancements Freeze**

- KEP README merged and latest template: ✅
- `kep.yaml` merged and current: ❌
- Graduation Criteria: ❌
- Test Plan: ❌
- Production Readiness Review: ❌
- No outstanding KEP metadata PRs: ✅

**Outstanding actions**

- No `stage/{alpha,beta,stable}` label on the issue -- can't determine target stage.
- Can't validate `kep.yaml` without a known target stage.
- Update Graduation Criteria (heuristic; verify manually) -- `Graduation Criteria` still contains template placeholder content.
- Complete the detailed Test Plan (heuristic; verify manually) -- `Test Plan` still contains template placeholder content.
- Can't validate the PRR questionnaire without a known target stage.
- Can't validate the PRR approval file without a known target stage.

**Draft GitHub comment**

*(review before posting -- do not auto-post)*

```markdown
Hello @jpbetz :wave:, v1.38 Enhancements team here.

Just checking in as we approach [enhancements freeze](https://github.com/kubernetes/sig-release/blob/master/releases/release_phases.md#enhancements-freeze) on **Tuesday 29th September 2026 (AoE) / Wednesday 30th September 2026 12:00 UTC**.

This enhancement is targeting stage `{stage}` for v1.38 (correct me, if otherwise)

Here's where this enhancement currently stands:

- [x] KEP readme using the [latest template](https://github.com/kubernetes/enhancements/tree/master/keps/NNNN-kep-template) has been merged into the k/enhancements repo.
- [ ] KEP status is marked as `implementable` for `latest-milestone: v1.38`.
- [ ] KEP readme has up-to-date graduation criteria.
- [ ] KEP readme has an updated detailed test plan.
- [ ] KEP has a production readiness review that has been completed and merged into k/enhancements. (For more information on the PRR process, check [here](https://github.com/kubernetes/community/blob/master/sig-architecture/production-readiness.md#submitting-a-kep-for-production-readiness-approval)).
- [x] There are no other outstanding (unmerged) PRs that modify the KEP readme or kep.yaml file.

For this KEP, we would just need to update the following:
- No `stage/{alpha,beta,stable}` label on the issue -- can't determine target stage.
- Can't validate `kep.yaml` without a known target stage.
- Update Graduation Criteria (heuristic; verify manually) -- `Graduation Criteria` still contains template placeholder content.
- Complete the detailed Test Plan (heuristic; verify manually) -- `Test Plan` still contains template placeholder content.
- Can't validate the PRR questionnaire without a known target stage.
- Can't validate the PRR approval file without a known target stage.

The status of this enhancement is marked as `At risk for enhancements freeze`. Please keep the issue description up-to-date with appropriate stages as well.

If you anticipate missing enhancements freeze, you can file an [exception request](https://github.com/kubernetes/sig-release/blob/master/releases/EXCEPTIONS.md) in advance. Thank you!
```

---

### #6386 — Introduce the ability to configure ephemeral storage at the pod level

**Summary**

| Issue | KEP PR | Enhancement owner (KEP PR author) | Target stage for v1.38 | In v1.38 milestone | Recommended v1.38 tracking board status |
|---|---|---|---|---|---|
| [#6386](https://github.com/kubernetes/enhancements/issues/6386) Introduce the ability to configure ephemeral storage at the pod level | [PR #6394](https://github.com/kubernetes/enhancements/pull/6394) | @ndixita | alpha | yes | At risk for enhancements freeze |

**Enhancements Freeze**

- KEP README merged and latest template: ❌
- `kep.yaml` merged and current: ❌
- Graduation Criteria: ❌
- Test Plan: ❌
- Production Readiness Review: ❌
- No outstanding KEP metadata PRs: ❌

**Outstanding actions**

- Merge or close outstanding PR(s) that modify the KEP README or `kep.yaml`: [#6394](https://github.com/kubernetes/enhancements/pull/6394).
- Could not locate a merged KEP directory (`keps/<sig>/<number>-*/`) on master.

**Draft GitHub comment**

*(review before posting -- do not auto-post)*

```markdown
Hello @ndixita :wave:, v1.38 Enhancements team here.

Just checking in as we approach [enhancements freeze](https://github.com/kubernetes/sig-release/blob/master/releases/release_phases.md#enhancements-freeze) on **Tuesday 29th September 2026 (AoE) / Wednesday 30th September 2026 12:00 UTC**.

This enhancement is targeting stage `alpha` for v1.38 (correct me, if otherwise)

Here's where this enhancement currently stands:

- [ ] KEP readme using the [latest template](https://github.com/kubernetes/enhancements/tree/master/keps/NNNN-kep-template) has been merged into the k/enhancements repo.
- [ ] KEP status is marked as `implementable` for `latest-milestone: v1.38`.
- [ ] KEP readme has up-to-date graduation criteria.
- [ ] KEP readme has an updated detailed test plan.
- [ ] KEP has a production readiness review that has been completed and merged into k/enhancements. (For more information on the PRR process, check [here](https://github.com/kubernetes/community/blob/master/sig-architecture/production-readiness.md#submitting-a-kep-for-production-readiness-approval)).
- [ ] There are no other outstanding (unmerged) PRs that modify the KEP readme or kep.yaml file.

For this KEP, we would just need to update the following:
- Merge or close outstanding PR(s) that modify the KEP README or `kep.yaml`: [#6394](https://github.com/kubernetes/enhancements/pull/6394).
- Could not locate a merged KEP directory (`keps/<sig>/<number>-*/`) on master.

The status of this enhancement is marked as `At risk for enhancements freeze`. Please keep the issue description up-to-date with appropriate stages as well.

If you anticipate missing enhancements freeze, you can file an [exception request](https://github.com/kubernetes/sig-release/blob/master/releases/EXCEPTIONS.md) in advance. Thank you!
```
