# Enhancements Freeze Report -- v1.38

Generated: 2026-09-26 15:09 UTC
Issues checked: 45
Generate draft reminder comment for SIG sig-node.

## Summary

| Issue | KEP PR | Enhancement owner (KEP PR author) | Target stage for v1.38 | In v1.38 milestone | Recommended v1.38 tracking board status |
|---|---|---|---|---|---|
| [#5474](https://github.com/kubernetes/enhancements/issues/5474) Enable Writable cgroups for unprivileged containers | [PR #6424](https://github.com/kubernetes/enhancements/pull/6424) | @talkachou-ilya | alpha | yes | At risk for enhancements freeze |
| [#5683](https://github.com/kubernetes/enhancements/issues/5683) Specialized Lifecycle Management | [PR #6309](https://github.com/kubernetes/enhancements/pull/6309) | @rthallisey | alpha | yes | At risk for enhancements freeze |
| [#2172](https://github.com/kubernetes/enhancements/issues/2172) Warn about quietly-insecure container UIDs/GIDs | [PR #6343](https://github.com/kubernetes/enhancements/pull/6343) | @Priyankasaggu11929 | alpha | yes | At risk for enhancements freeze |
| [#2371](https://github.com/kubernetes/enhancements/issues/2371) cAdvisor-less, CRI-full Container and Pod Stats | [PR #6389](https://github.com/kubernetes/enhancements/pull/6389) | @dgrisonnet | beta | yes | At risk for enhancements freeze |
| [#2535](https://github.com/kubernetes/enhancements/issues/2535) Ensure secret pulled images | [PR #6267](https://github.com/kubernetes/enhancements/pull/6267) | @stlaz | beta | NO | At risk for enhancements freeze |
| [#2570](https://github.com/kubernetes/enhancements/issues/2570) Support memory qos with cgroups v2 | [PR #6362](https://github.com/kubernetes/enhancements/pull/6362) | @QiWang19 | beta | yes | At risk for enhancements freeze |
| [#2837](https://github.com/kubernetes/enhancements/issues/2837) Pod level resources | [PR #6393](https://github.com/kubernetes/enhancements/pull/6393) | @ndixita | stable | yes | At risk for enhancements freeze |
| [#3953](https://github.com/kubernetes/enhancements/issues/3953) In-place Node Resource Resize | [PR #3955](https://github.com/kubernetes/enhancements/pull/3955) | @Karthik-K-N | alpha | yes | At risk for enhancements freeze |
| [#4438](https://github.com/kubernetes/enhancements/issues/4438) Restarting sidecar containers during Pod termination | [PR #6218](https://github.com/kubernetes/enhancements/pull/6218) | @matthyx | alpha | yes | At risk for enhancements freeze |
| [#4563](https://github.com/kubernetes/enhancements/issues/4563) EvictionRequest API | [PR #6405](https://github.com/kubernetes/enhancements/pull/6405) | @atiratree | alpha | yes | Tracked for enhancements freeze |
| [#4939](https://github.com/kubernetes/enhancements/issues/4939) Support TLS Credentials in gRPC Probe | [PR #6336](https://github.com/kubernetes/enhancements/pull/6336) | @amritansh1502 | beta | yes | At risk for enhancements freeze |
| [#4960](https://github.com/kubernetes/enhancements/issues/4960) Container Stop Signals | [PR #6410](https://github.com/kubernetes/enhancements/pull/6410) | @sreeram-venkitesh | beta | yes | Tracked for enhancements freeze |
| [#5304](https://github.com/kubernetes/enhancements/issues/5304) DRA: Device Attributes in Downward API | [PR #6334](https://github.com/kubernetes/enhancements/pull/6334) | @SergeyKanzhelev | stable | NO | At risk for enhancements freeze |
| [#5365](https://github.com/kubernetes/enhancements/issues/5365) ImageVolume with an image digest | [PR #6368](https://github.com/kubernetes/enhancements/pull/6368) | @iholder101 | beta | yes | Tracked for enhancements freeze |
| [#5419](https://github.com/kubernetes/enhancements/issues/5419) Pod Level Resources Support With In Place Pod Vertical Scaling | [PR #6184](https://github.com/kubernetes/enhancements/pull/6184) | @ndixita | stable | yes | At risk for enhancements freeze |
| [#5517](https://github.com/kubernetes/enhancements/issues/5517) DRA: Node Allocatable Resource Requests | [PR #6324](https://github.com/kubernetes/enhancements/pull/6324) | @pravk03 | beta | yes | At risk for enhancements freeze |
| [#5554](https://github.com/kubernetes/enhancements/issues/5554) Support In place update pod resources alongside static cpu manager policy | [PR #6330](https://github.com/kubernetes/enhancements/pull/6330) | @esotsal | alpha | yes | Tracked for enhancements freeze |
| [#5677](https://github.com/kubernetes/enhancements/issues/5677) DRA: Resource Availability Visibility | [PR #6301](https://github.com/kubernetes/enhancements/pull/6301) | @nmn3m | alpha | yes | At risk for enhancements freeze |
| [#5714](https://github.com/kubernetes/enhancements/issues/5714) Allow specifying whether to unshare cgroup namespaces | [PR #5715](https://github.com/kubernetes/enhancements/pull/5715) | @AkihiroSuda | alpha | yes | At risk for enhancements freeze |
| [#5758](https://github.com/kubernetes/enhancements/issues/5758) Per-container ulimits configuration | [PR #6425](https://github.com/kubernetes/enhancements/pull/6425) | @HirazawaUi | alpha | yes | Tracked for enhancements freeze |
| [#5823](https://github.com/kubernetes/enhancements/issues/5823) Pod-Level Checkpoint/Restore | [PR #6428](https://github.com/kubernetes/enhancements/pull/6428) | @rst0git | alpha | yes | At risk for enhancements freeze |
| [#5825](https://github.com/kubernetes/enhancements/issues/5825) CRI List Streaming | [PR #6146](https://github.com/kubernetes/enhancements/pull/6146) | @bitoku | beta | yes | Tracked for enhancements freeze |
| [#5855](https://github.com/kubernetes/enhancements/issues/5855) Add bind mount options (noexec, nodev, nosuid) support on volumeMounts | [PR #6434](https://github.com/kubernetes/enhancements/pull/6434) | @nispriha | beta | NO | At risk for enhancements freeze |
| [#5894](https://github.com/kubernetes/enhancements/issues/5894) Node system partition | [PR #6409](https://github.com/kubernetes/enhancements/pull/6409) | @SergeyKanzhelev | alpha | yes | At risk for enhancements freeze |
| [#5945](https://github.com/kubernetes/enhancements/issues/5945) DRA: Optional Node Operations | [PR #6372](https://github.com/kubernetes/enhancements/pull/6372) | @troychiu | beta | yes | At risk for enhancements freeze |
| [#5972](https://github.com/kubernetes/enhancements/issues/5972) Dynamic Pod Mutation: Optimistic Execution & Hierarchical Resource Delegation | [PR #6435](https://github.com/kubernetes/enhancements/pull/6435) | @tallclair | alpha | yes | At risk for enhancements freeze |
| [#5996](https://github.com/kubernetes/enhancements/issues/5996) Support Default Pod Sysctls in Kubelet | [PR #6418](https://github.com/kubernetes/enhancements/pull/6418) | @VeraQin | beta | yes | At risk for enhancements freeze |
| [#5999](https://github.com/kubernetes/enhancements/issues/5999) HTTP/2 cleartext (h2c) for container probes | [PR #6338](https://github.com/kubernetes/enhancements/pull/6338) | @amritansh1502 | beta | yes | At risk for enhancements freeze |
| [#6007](https://github.com/kubernetes/enhancements/issues/6007) Add Topology Manager option to improve workload density for single-numa-node | [PR #6332](https://github.com/kubernetes/enhancements/pull/6332) | @swatisehgal | alpha | yes | At risk for enhancements freeze |
| [#6030](https://github.com/kubernetes/enhancements/issues/6030) Dynamic resize of memory-backed volumes | [PR #6320](https://github.com/kubernetes/enhancements/pull/6320) | @natasha41575 | beta | yes | Tracked for enhancements freeze |
| [#6061](https://github.com/kubernetes/enhancements/issues/6061) OCI Artifact-Based Security Profile Distribution | [PR #6062](https://github.com/kubernetes/enhancements/pull/6062) | @saschagrunert | alpha | yes | At risk for enhancements freeze |
| [#6063](https://github.com/kubernetes/enhancements/issues/6063) Configuration for Per-Pod PID Limit | [PR #6258](https://github.com/kubernetes/enhancements/pull/6258) | @BhargaviGudi | alpha | yes | Tracked for enhancements freeze |
| [#6122](https://github.com/kubernetes/enhancements/issues/6122) Support CPU Configurable Scaling Delay | [PR #6314](https://github.com/kubernetes/enhancements/pull/6314) | @Chunxia202410 | alpha | yes | At risk for enhancements freeze |
| [#6147](https://github.com/kubernetes/enhancements/issues/6147) Dynamic node declared features Discovery | [PR #6148](https://github.com/kubernetes/enhancements/pull/6148) | @HirazawaUi | alpha | yes | At risk for enhancements freeze |
| [#6232](https://github.com/kubernetes/enhancements/issues/6232) Tolerate benign per-NUMA memory drift in the Memory Manager | [PR #6233](https://github.com/kubernetes/enhancements/pull/6233) | @AI-Armless | alpha | yes | At risk for enhancements freeze |
| [#6247](https://github.com/kubernetes/enhancements/issues/6247) Kubelet systemd watchdog diagnostic guardrails | [PR #6248](https://github.com/kubernetes/enhancements/pull/6248) | @googs1025 | alpha | yes | At risk for enhancements freeze |
| [#6252](https://github.com/kubernetes/enhancements/issues/6252) KEP-6252: Support hugepages in kubelet's `--system-reserved` and `--kube-reserved flags` | [PR #6253](https://github.com/kubernetes/enhancements/pull/6253) | @Tal-or | alpha | yes | At risk for enhancements freeze |
| [#6274](https://github.com/kubernetes/enhancements/issues/6274) KEP-6274: GPU support for Pod-level Checkpoint/Restore | [PR #6275](https://github.com/kubernetes/enhancements/pull/6275) | @rst0git | alpha | yes | At risk for enhancements freeze |
| [#6318](https://github.com/kubernetes/enhancements/issues/6318) Allow in-place updates to container probes | [PR #6323](https://github.com/kubernetes/enhancements/pull/6323) | @HirazawaUi | alpha | yes | At risk for enhancements freeze |
| [#6035](https://github.com/kubernetes/enhancements/issues/6035) Exec session identity propagation | [PR #6205](https://github.com/kubernetes/enhancements/pull/6205) | @nispriha | alpha | yes | At risk for enhancements freeze |
| [#6249](https://github.com/kubernetes/enhancements/issues/6249) SLM: Publish Graceful Node Shutdown state for DaemonSet coordination | [PR #6351](https://github.com/kubernetes/enhancements/pull/6351) | @danbruno101 | alpha | yes | At risk for enhancements freeze |
| [#6369](https://github.com/kubernetes/enhancements/issues/6369) Pod Assigned Resource Exposure via Downward API | [PR #6370](https://github.com/kubernetes/enhancements/pull/6370) | @Chunxia202410 | alpha | yes | At risk for enhancements freeze |
| [#6371](https://github.com/kubernetes/enhancements/issues/6371) External Node Liveness Detection | [PR #6373](https://github.com/kubernetes/enhancements/pull/6373) | @jpbetz | alpha | yes | At risk for enhancements freeze |
| [#5359](https://github.com/kubernetes/enhancements/issues/5359) Workload Controlled Swap | [PR #5569](https://github.com/kubernetes/enhancements/pull/5569) | @ajaysundark | alpha | yes | At risk for enhancements freeze |
| [#6386](https://github.com/kubernetes/enhancements/issues/6386) Introduce the ability to configure ephemeral storage at the pod level | [PR #6394](https://github.com/kubernetes/enhancements/pull/6394) | @ndixita | alpha | yes | At risk for enhancements freeze |

---

### #5474 — Enable Writable cgroups for unprivileged containers

**Summary**

| Issue | KEP PR | Enhancement owner (KEP PR author) | Target stage for v1.38 | In v1.38 milestone | Recommended v1.38 tracking board status |
|---|---|---|---|---|---|
| [#5474](https://github.com/kubernetes/enhancements/issues/5474) Enable Writable cgroups for unprivileged containers | [PR #6424](https://github.com/kubernetes/enhancements/pull/6424) | @talkachou-ilya | alpha | yes | At risk for enhancements freeze |

**Enhancements Freeze**

- KEP README merged and latest template: ✅
- `kep.yaml` merged and current: ✅
- Graduation Criteria: ✅
- Test Plan: ✅
- Production Readiness Review: ✅
- No outstanding KEP metadata PRs: ❌

**Outstanding actions**

- Merge or close outstanding PR(s) that modify the KEP README or `kep.yaml`: [#6424](https://github.com/kubernetes/enhancements/pull/6424).

**Draft GitHub comment**

*(review before posting -- do not auto-post)*

```markdown
Hello @talkachou-ilya :wave:, v1.38 Enhancements team here.

Just checking in as we approach [enhancements freeze](https://github.com/kubernetes/sig-release/blob/master/releases/release_phases.md#enhancements-freeze) on **Tuesday 29th September 2026 (AoE) / Wednesday 30th September 2026 12:00 UTC**.

This enhancement is targeting stage `alpha` for v1.38 (correct me, if otherwise)

Here's where this enhancement currently stands:

- [x] KEP readme using the [latest template](https://github.com/kubernetes/enhancements/tree/master/keps/NNNN-kep-template) has been merged into the k/enhancements repo.
- [x] KEP status is marked as `implementable` for `latest-milestone: v1.38`.
- [x] KEP readme has up-to-date graduation criteria.
- [x] KEP readme has an updated detailed test plan.
- [x] KEP has a production readiness review that has been completed and merged into k/enhancements. (For more information on the PRR process, check [here](https://github.com/kubernetes/community/blob/master/sig-architecture/production-readiness.md#submitting-a-kep-for-production-readiness-approval)).
- [ ] There are no other outstanding (unmerged) PRs that modify the KEP readme or kep.yaml file.

For this KEP, we would just need to update the following:
- Merge or close outstanding PR(s) that modify the KEP README or `kep.yaml`: [#6424](https://github.com/kubernetes/enhancements/pull/6424).

The status of this enhancement is marked as `At risk for enhancements freeze`. Please keep the issue description up-to-date with appropriate stages as well.

If you anticipate missing enhancements freeze, you can file an [exception request](https://github.com/kubernetes/sig-release/blob/master/releases/EXCEPTIONS.md) in advance. Thank you!
```

---

### #5683 — Specialized Lifecycle Management

**Summary**

| Issue | KEP PR | Enhancement owner (KEP PR author) | Target stage for v1.38 | In v1.38 milestone | Recommended v1.38 tracking board status |
|---|---|---|---|---|---|
| [#5683](https://github.com/kubernetes/enhancements/issues/5683) Specialized Lifecycle Management | [PR #6309](https://github.com/kubernetes/enhancements/pull/6309) | @rthallisey | alpha | yes | At risk for enhancements freeze |

**Enhancements Freeze**

- KEP README merged and latest template: ✅
- `kep.yaml` merged and current: ❌
- Graduation Criteria: ✅
- Test Plan: ✅
- Production Readiness Review: ✅
- No outstanding KEP metadata PRs: ❌

**Outstanding actions**

- Merge or close outstanding PR(s) that modify the KEP README or `kep.yaml`: [#6309](https://github.com/kubernetes/enhancements/pull/6309), [#5769](https://github.com/kubernetes/enhancements/pull/5769).
- Merge the required `kep.yaml` updates -- `latest-milestone` is `v1.37`, expected `v1.38`.

**Draft GitHub comment**

*(review before posting -- do not auto-post)*

```markdown
Hello @rthallisey :wave:, v1.38 Enhancements team here.

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
- Merge or close outstanding PR(s) that modify the KEP README or `kep.yaml`: [#6309](https://github.com/kubernetes/enhancements/pull/6309), [#5769](https://github.com/kubernetes/enhancements/pull/5769).
- Merge the required `kep.yaml` updates -- `latest-milestone` is `v1.37`, expected `v1.38`.

The status of this enhancement is marked as `At risk for enhancements freeze`. Please keep the issue description up-to-date with appropriate stages as well.

If you anticipate missing enhancements freeze, you can file an [exception request](https://github.com/kubernetes/sig-release/blob/master/releases/EXCEPTIONS.md) in advance. Thank you!
```

---

### #2172 — Warn about quietly-insecure container UIDs/GIDs

**Summary**

| Issue | KEP PR | Enhancement owner (KEP PR author) | Target stage for v1.38 | In v1.38 milestone | Recommended v1.38 tracking board status |
|---|---|---|---|---|---|
| [#2172](https://github.com/kubernetes/enhancements/issues/2172) Warn about quietly-insecure container UIDs/GIDs | [PR #6343](https://github.com/kubernetes/enhancements/pull/6343) | @Priyankasaggu11929 | alpha | yes | At risk for enhancements freeze |

**Enhancements Freeze**

- KEP README merged and latest template: ❌
- `kep.yaml` merged and current: ❌
- Graduation Criteria: ❌
- Test Plan: ❌
- Production Readiness Review: ❌
- No outstanding KEP metadata PRs: ❌

**Outstanding actions**

- Merge or close outstanding PR(s) that modify the KEP README or `kep.yaml`: [#6343](https://github.com/kubernetes/enhancements/pull/6343).
- Could not locate a merged KEP directory (`keps/<sig>/<number>-*/`) on master.

**Draft GitHub comment**

*(review before posting -- do not auto-post)*

```markdown
Hello @Priyankasaggu11929 :wave:, v1.38 Enhancements team here.

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
- Merge or close outstanding PR(s) that modify the KEP README or `kep.yaml`: [#6343](https://github.com/kubernetes/enhancements/pull/6343).
- Could not locate a merged KEP directory (`keps/<sig>/<number>-*/`) on master.

The status of this enhancement is marked as `At risk for enhancements freeze`. Please keep the issue description up-to-date with appropriate stages as well.

If you anticipate missing enhancements freeze, you can file an [exception request](https://github.com/kubernetes/sig-release/blob/master/releases/EXCEPTIONS.md) in advance. Thank you!
```

---

### #2371 — cAdvisor-less, CRI-full Container and Pod Stats

**Summary**

| Issue | KEP PR | Enhancement owner (KEP PR author) | Target stage for v1.38 | In v1.38 milestone | Recommended v1.38 tracking board status |
|---|---|---|---|---|---|
| [#2371](https://github.com/kubernetes/enhancements/issues/2371) cAdvisor-less, CRI-full Container and Pod Stats | [PR #6389](https://github.com/kubernetes/enhancements/pull/6389) | @dgrisonnet | beta | yes | At risk for enhancements freeze |

**Enhancements Freeze**

- KEP README merged and latest template: ✅
- `kep.yaml` merged and current: ✅
- Graduation Criteria: ❌
- Test Plan: ✅
- Production Readiness Review: ✅
- No outstanding KEP metadata PRs: ✅

**Outstanding actions**

- Update Graduation Criteria (heuristic; verify manually) -- `Graduation Criteria` still contains template placeholder content.

**Draft GitHub comment**

*(review before posting -- do not auto-post)*

```markdown
Hello @dgrisonnet :wave:, v1.38 Enhancements team here.

Just checking in as we approach [enhancements freeze](https://github.com/kubernetes/sig-release/blob/master/releases/release_phases.md#enhancements-freeze) on **Tuesday 29th September 2026 (AoE) / Wednesday 30th September 2026 12:00 UTC**.

This enhancement is targeting stage `beta` for v1.38 (correct me, if otherwise)

Here's where this enhancement currently stands:

- [x] KEP readme using the [latest template](https://github.com/kubernetes/enhancements/tree/master/keps/NNNN-kep-template) has been merged into the k/enhancements repo.
- [x] KEP status is marked as `implementable` for `latest-milestone: v1.38`.
- [ ] KEP readme has up-to-date graduation criteria.
- [x] KEP readme has an updated detailed test plan.
- [x] KEP has a production readiness review that has been completed and merged into k/enhancements. (For more information on the PRR process, check [here](https://github.com/kubernetes/community/blob/master/sig-architecture/production-readiness.md#submitting-a-kep-for-production-readiness-approval)).
- [x] There are no other outstanding (unmerged) PRs that modify the KEP readme or kep.yaml file.

For this KEP, we would just need to update the following:
- Update Graduation Criteria (heuristic; verify manually) -- `Graduation Criteria` still contains template placeholder content.

The status of this enhancement is marked as `At risk for enhancements freeze`. Please keep the issue description up-to-date with appropriate stages as well.

If you anticipate missing enhancements freeze, you can file an [exception request](https://github.com/kubernetes/sig-release/blob/master/releases/EXCEPTIONS.md) in advance. Thank you!
```

---

### #2535 — Ensure secret pulled images

**Summary**

| Issue | KEP PR | Enhancement owner (KEP PR author) | Target stage for v1.38 | In v1.38 milestone | Recommended v1.38 tracking board status |
|---|---|---|---|---|---|
| [#2535](https://github.com/kubernetes/enhancements/issues/2535) Ensure secret pulled images | [PR #6267](https://github.com/kubernetes/enhancements/pull/6267) | @stlaz | beta | NO | At risk for enhancements freeze |

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
Hello @stlaz :wave:, v1.38 Enhancements team here.

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

### #2570 — Support memory qos with cgroups v2

**Summary**

| Issue | KEP PR | Enhancement owner (KEP PR author) | Target stage for v1.38 | In v1.38 milestone | Recommended v1.38 tracking board status |
|---|---|---|---|---|---|
| [#2570](https://github.com/kubernetes/enhancements/issues/2570) Support memory qos with cgroups v2 | [PR #6362](https://github.com/kubernetes/enhancements/pull/6362) | @QiWang19 | beta | yes | At risk for enhancements freeze |

**Enhancements Freeze**

- KEP README merged and latest template: ✅
- `kep.yaml` merged and current: ❌
- Graduation Criteria: ✅
- Test Plan: ✅
- Production Readiness Review: ✅
- No outstanding KEP metadata PRs: ❌

**Outstanding actions**

- Merge or close outstanding PR(s) that modify the KEP README or `kep.yaml`: [#6362](https://github.com/kubernetes/enhancements/pull/6362), [#6322](https://github.com/kubernetes/enhancements/pull/6322).
- Merge the required `kep.yaml` updates -- `latest-milestone` is `v1.37`, expected `v1.38`.

**Draft GitHub comment**

*(review before posting -- do not auto-post)*

```markdown
Hello @QiWang19 :wave:, v1.38 Enhancements team here.

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
- Merge or close outstanding PR(s) that modify the KEP README or `kep.yaml`: [#6362](https://github.com/kubernetes/enhancements/pull/6362), [#6322](https://github.com/kubernetes/enhancements/pull/6322).
- Merge the required `kep.yaml` updates -- `latest-milestone` is `v1.37`, expected `v1.38`.

The status of this enhancement is marked as `At risk for enhancements freeze`. Please keep the issue description up-to-date with appropriate stages as well.

If you anticipate missing enhancements freeze, you can file an [exception request](https://github.com/kubernetes/sig-release/blob/master/releases/EXCEPTIONS.md) in advance. Thank you!
```

---

### #2837 — Pod level resources

**Summary**

| Issue | KEP PR | Enhancement owner (KEP PR author) | Target stage for v1.38 | In v1.38 milestone | Recommended v1.38 tracking board status |
|---|---|---|---|---|---|
| [#2837](https://github.com/kubernetes/enhancements/issues/2837) Pod level resources | [PR #6393](https://github.com/kubernetes/enhancements/pull/6393) | @ndixita | stable | yes | At risk for enhancements freeze |

**Enhancements Freeze**

- KEP README merged and latest template: ✅
- `kep.yaml` merged and current: ❌
- Graduation Criteria: ✅
- Test Plan: ✅
- Production Readiness Review: ✅
- No outstanding KEP metadata PRs: ❌

**Outstanding actions**

- Merge or close outstanding PR(s) that modify the KEP README or `kep.yaml`: [#6393](https://github.com/kubernetes/enhancements/pull/6393).
- Merge the required `kep.yaml` updates -- `latest-milestone` is `v1.37`, expected `v1.38`.

**Draft GitHub comment**

*(review before posting -- do not auto-post)*

```markdown
Hello @ndixita :wave:, v1.38 Enhancements team here.

Just checking in as we approach [enhancements freeze](https://github.com/kubernetes/sig-release/blob/master/releases/release_phases.md#enhancements-freeze) on **Tuesday 29th September 2026 (AoE) / Wednesday 30th September 2026 12:00 UTC**.

This enhancement is targeting stage `stable` for v1.38 (correct me, if otherwise)

Here's where this enhancement currently stands:

- [x] KEP readme using the [latest template](https://github.com/kubernetes/enhancements/tree/master/keps/NNNN-kep-template) has been merged into the k/enhancements repo.
- [ ] KEP status is marked as `implementable` for `latest-milestone: v1.38`.
- [x] KEP readme has up-to-date graduation criteria.
- [x] KEP readme has an updated detailed test plan.
- [x] KEP has a production readiness review that has been completed and merged into k/enhancements. (For more information on the PRR process, check [here](https://github.com/kubernetes/community/blob/master/sig-architecture/production-readiness.md#submitting-a-kep-for-production-readiness-approval)).
- [ ] There are no other outstanding (unmerged) PRs that modify the KEP readme or kep.yaml file.

For this KEP, we would just need to update the following:
- Merge or close outstanding PR(s) that modify the KEP README or `kep.yaml`: [#6393](https://github.com/kubernetes/enhancements/pull/6393).
- Merge the required `kep.yaml` updates -- `latest-milestone` is `v1.37`, expected `v1.38`.

The status of this enhancement is marked as `At risk for enhancements freeze`. Please keep the issue description up-to-date with appropriate stages as well.

If you anticipate missing enhancements freeze, you can file an [exception request](https://github.com/kubernetes/sig-release/blob/master/releases/EXCEPTIONS.md) in advance. Thank you!
```

---

### #3953 — In-place Node Resource Resize

**Summary**

| Issue | KEP PR | Enhancement owner (KEP PR author) | Target stage for v1.38 | In v1.38 milestone | Recommended v1.38 tracking board status |
|---|---|---|---|---|---|
| [#3953](https://github.com/kubernetes/enhancements/issues/3953) In-place Node Resource Resize | [PR #3955](https://github.com/kubernetes/enhancements/pull/3955) | @Karthik-K-N | alpha | yes | At risk for enhancements freeze |

**Enhancements Freeze**

- KEP README merged and latest template: ❌
- `kep.yaml` merged and current: ❌
- Graduation Criteria: ❌
- Test Plan: ❌
- Production Readiness Review: ❌
- No outstanding KEP metadata PRs: ❌

**Outstanding actions**

- Merge or close outstanding PR(s) that modify the KEP README or `kep.yaml`: [#3955](https://github.com/kubernetes/enhancements/pull/3955).
- Could not locate a merged KEP directory (`keps/<sig>/<number>-*/`) on master.

**Draft GitHub comment**

*(review before posting -- do not auto-post)*

```markdown
Hello @Karthik-K-N :wave:, v1.38 Enhancements team here.

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
- Merge or close outstanding PR(s) that modify the KEP README or `kep.yaml`: [#3955](https://github.com/kubernetes/enhancements/pull/3955).
- Could not locate a merged KEP directory (`keps/<sig>/<number>-*/`) on master.

The status of this enhancement is marked as `At risk for enhancements freeze`. Please keep the issue description up-to-date with appropriate stages as well.

If you anticipate missing enhancements freeze, you can file an [exception request](https://github.com/kubernetes/sig-release/blob/master/releases/EXCEPTIONS.md) in advance. Thank you!
```

---

### #4438 — Restarting sidecar containers during Pod termination

**Summary**

| Issue | KEP PR | Enhancement owner (KEP PR author) | Target stage for v1.38 | In v1.38 milestone | Recommended v1.38 tracking board status |
|---|---|---|---|---|---|
| [#4438](https://github.com/kubernetes/enhancements/issues/4438) Restarting sidecar containers during Pod termination | [PR #6218](https://github.com/kubernetes/enhancements/pull/6218) | @matthyx | alpha | yes | At risk for enhancements freeze |

**Enhancements Freeze**

- KEP README merged and latest template: ✅
- `kep.yaml` merged and current: ❌
- Graduation Criteria: ❌
- Test Plan: ✅
- Production Readiness Review: ✅
- No outstanding KEP metadata PRs: ❌

**Outstanding actions**

- Merge or close outstanding PR(s) that modify the KEP README or `kep.yaml`: [#6218](https://github.com/kubernetes/enhancements/pull/6218).
- Merge the required `kep.yaml` updates -- `latest-milestone` is `v1.37`, expected `v1.38`.
- Update Graduation Criteria (heuristic; verify manually) -- `Graduation Criteria` still contains template placeholder content.

**Draft GitHub comment**

*(review before posting -- do not auto-post)*

```markdown
Hello @matthyx :wave:, v1.38 Enhancements team here.

Just checking in as we approach [enhancements freeze](https://github.com/kubernetes/sig-release/blob/master/releases/release_phases.md#enhancements-freeze) on **Tuesday 29th September 2026 (AoE) / Wednesday 30th September 2026 12:00 UTC**.

This enhancement is targeting stage `alpha` for v1.38 (correct me, if otherwise)

Here's where this enhancement currently stands:

- [x] KEP readme using the [latest template](https://github.com/kubernetes/enhancements/tree/master/keps/NNNN-kep-template) has been merged into the k/enhancements repo.
- [ ] KEP status is marked as `implementable` for `latest-milestone: v1.38`.
- [ ] KEP readme has up-to-date graduation criteria.
- [x] KEP readme has an updated detailed test plan.
- [x] KEP has a production readiness review that has been completed and merged into k/enhancements. (For more information on the PRR process, check [here](https://github.com/kubernetes/community/blob/master/sig-architecture/production-readiness.md#submitting-a-kep-for-production-readiness-approval)).
- [ ] There are no other outstanding (unmerged) PRs that modify the KEP readme or kep.yaml file.

For this KEP, we would just need to update the following:
- Merge or close outstanding PR(s) that modify the KEP README or `kep.yaml`: [#6218](https://github.com/kubernetes/enhancements/pull/6218).
- Merge the required `kep.yaml` updates -- `latest-milestone` is `v1.37`, expected `v1.38`.
- Update Graduation Criteria (heuristic; verify manually) -- `Graduation Criteria` still contains template placeholder content.

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

### #4939 — Support TLS Credentials in gRPC Probe

**Summary**

| Issue | KEP PR | Enhancement owner (KEP PR author) | Target stage for v1.38 | In v1.38 milestone | Recommended v1.38 tracking board status |
|---|---|---|---|---|---|
| [#4939](https://github.com/kubernetes/enhancements/issues/4939) Support TLS Credentials in gRPC Probe | [PR #6336](https://github.com/kubernetes/enhancements/pull/6336) | @amritansh1502 | beta | yes | At risk for enhancements freeze |

**Enhancements Freeze**

- KEP README merged and latest template: ✅
- `kep.yaml` merged and current: ❌
- Graduation Criteria: ✅
- Test Plan: ✅
- Production Readiness Review: ❌
- No outstanding KEP metadata PRs: ❌

**Outstanding actions**

- Merge or close outstanding PR(s) that modify the KEP README or `kep.yaml`: [#6336](https://github.com/kubernetes/enhancements/pull/6336).
- Merge the required `kep.yaml` updates -- `stage` is `alpha`, expected `beta`; `latest-milestone` is `v1.37`, expected `v1.38`.
- Complete and merge the PRR questionnaire -- still unanswered (heuristic; verify manually): Rollout, Upgrade and Rollback Planning, Dependencies.
- Complete and merge the PRR approval -- no `beta:` entry in the PRR approval file.

**Draft GitHub comment**

*(review before posting -- do not auto-post)*

```markdown
Hello @amritansh1502 :wave:, v1.38 Enhancements team here.

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
- Merge or close outstanding PR(s) that modify the KEP README or `kep.yaml`: [#6336](https://github.com/kubernetes/enhancements/pull/6336).
- Merge the required `kep.yaml` updates -- `stage` is `alpha`, expected `beta`; `latest-milestone` is `v1.37`, expected `v1.38`.
- Complete and merge the PRR questionnaire -- still unanswered (heuristic; verify manually): Rollout, Upgrade and Rollback Planning, Dependencies.
- Complete and merge the PRR approval -- no `beta:` entry in the PRR approval file.

The status of this enhancement is marked as `At risk for enhancements freeze`. Please keep the issue description up-to-date with appropriate stages as well.

If you anticipate missing enhancements freeze, you can file an [exception request](https://github.com/kubernetes/sig-release/blob/master/releases/EXCEPTIONS.md) in advance. Thank you!
```

---

### #4960 — Container Stop Signals

**Summary**

| Issue | KEP PR | Enhancement owner (KEP PR author) | Target stage for v1.38 | In v1.38 milestone | Recommended v1.38 tracking board status |
|---|---|---|---|---|---|
| [#4960](https://github.com/kubernetes/enhancements/issues/4960) Container Stop Signals | [PR #6410](https://github.com/kubernetes/enhancements/pull/6410) | @sreeram-venkitesh | beta | yes | Tracked for enhancements freeze |

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
Hello @sreeram-venkitesh :wave:, v1.38 Enhancements team here.

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

### #5304 — DRA: Device Attributes in Downward API

**Summary**

| Issue | KEP PR | Enhancement owner (KEP PR author) | Target stage for v1.38 | In v1.38 milestone | Recommended v1.38 tracking board status |
|---|---|---|---|---|---|
| [#5304](https://github.com/kubernetes/enhancements/issues/5304) DRA: Device Attributes in Downward API | [PR #6334](https://github.com/kubernetes/enhancements/pull/6334) | @SergeyKanzhelev | stable | NO | At risk for enhancements freeze |

**Enhancements Freeze**

- KEP README merged and latest template: ✅
- `kep.yaml` merged and current: ❌
- Graduation Criteria: ❌
- Test Plan: ✅
- Production Readiness Review: ❌
- No outstanding KEP metadata PRs: ✅

**Outstanding actions**

- Issue is not in the **v1.38** milestone (currently: `none`).
- Merge the required `kep.yaml` updates -- `stage` is `beta`, expected `stable`; `latest-milestone` is `v1.37`, expected `v1.38`.
- Update Graduation Criteria (heuristic; verify manually) -- `Graduation Criteria` still contains template placeholder content.
- Complete and merge the PRR approval -- no `stable:` entry in the PRR approval file.

**Draft GitHub comment**

*(review before posting -- do not auto-post)*

```markdown
Hello @SergeyKanzhelev :wave:, v1.38 Enhancements team here.

Just checking in as we approach [enhancements freeze](https://github.com/kubernetes/sig-release/blob/master/releases/release_phases.md#enhancements-freeze) on **Tuesday 29th September 2026 (AoE) / Wednesday 30th September 2026 12:00 UTC**.

This enhancement is targeting stage `stable` for v1.38 (correct me, if otherwise)

Here's where this enhancement currently stands:

- [x] KEP readme using the [latest template](https://github.com/kubernetes/enhancements/tree/master/keps/NNNN-kep-template) has been merged into the k/enhancements repo.
- [ ] KEP status is marked as `implementable` for `latest-milestone: v1.38`.
- [ ] KEP readme has up-to-date graduation criteria.
- [x] KEP readme has an updated detailed test plan.
- [ ] KEP has a production readiness review that has been completed and merged into k/enhancements. (For more information on the PRR process, check [here](https://github.com/kubernetes/community/blob/master/sig-architecture/production-readiness.md#submitting-a-kep-for-production-readiness-approval)).
- [x] There are no other outstanding (unmerged) PRs that modify the KEP readme or kep.yaml file.

For this KEP, we would just need to update the following:
- Issue is not in the **v1.38** milestone (currently: `none`).
- Merge the required `kep.yaml` updates -- `stage` is `beta`, expected `stable`; `latest-milestone` is `v1.37`, expected `v1.38`.
- Update Graduation Criteria (heuristic; verify manually) -- `Graduation Criteria` still contains template placeholder content.
- Complete and merge the PRR approval -- no `stable:` entry in the PRR approval file.

The status of this enhancement is marked as `At risk for enhancements freeze`. Please keep the issue description up-to-date with appropriate stages as well.

If you anticipate missing enhancements freeze, you can file an [exception request](https://github.com/kubernetes/sig-release/blob/master/releases/EXCEPTIONS.md) in advance. Thank you!
```

---

### #5365 — ImageVolume with an image digest

**Summary**

| Issue | KEP PR | Enhancement owner (KEP PR author) | Target stage for v1.38 | In v1.38 milestone | Recommended v1.38 tracking board status |
|---|---|---|---|---|---|
| [#5365](https://github.com/kubernetes/enhancements/issues/5365) ImageVolume with an image digest | [PR #6368](https://github.com/kubernetes/enhancements/pull/6368) | @iholder101 | beta | yes | Tracked for enhancements freeze |

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
Hello @iholder101 :wave:, v1.38 Enhancements team here.

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

### #5419 — Pod Level Resources Support With In Place Pod Vertical Scaling

**Summary**

| Issue | KEP PR | Enhancement owner (KEP PR author) | Target stage for v1.38 | In v1.38 milestone | Recommended v1.38 tracking board status |
|---|---|---|---|---|---|
| [#5419](https://github.com/kubernetes/enhancements/issues/5419) Pod Level Resources Support With In Place Pod Vertical Scaling | [PR #6184](https://github.com/kubernetes/enhancements/pull/6184) | @ndixita | stable | yes | At risk for enhancements freeze |

**Enhancements Freeze**

- KEP README merged and latest template: ✅
- `kep.yaml` merged and current: ❌
- Graduation Criteria: ✅
- Test Plan: ✅
- Production Readiness Review: ❌
- No outstanding KEP metadata PRs: ❌

**Outstanding actions**

- Merge or close outstanding PR(s) that modify the KEP README or `kep.yaml`: [#6184](https://github.com/kubernetes/enhancements/pull/6184).
- Merge the required `kep.yaml` updates -- `stage` is `beta`, expected `stable`; `latest-milestone` is `v1.36`, expected `v1.38`; `milestone.stable` is missing.
- Complete and merge the PRR approval -- no `stable:` entry in the PRR approval file.

**Draft GitHub comment**

*(review before posting -- do not auto-post)*

```markdown
Hello @ndixita :wave:, v1.38 Enhancements team here.

Just checking in as we approach [enhancements freeze](https://github.com/kubernetes/sig-release/blob/master/releases/release_phases.md#enhancements-freeze) on **Tuesday 29th September 2026 (AoE) / Wednesday 30th September 2026 12:00 UTC**.

This enhancement is targeting stage `stable` for v1.38 (correct me, if otherwise)

Here's where this enhancement currently stands:

- [x] KEP readme using the [latest template](https://github.com/kubernetes/enhancements/tree/master/keps/NNNN-kep-template) has been merged into the k/enhancements repo.
- [ ] KEP status is marked as `implementable` for `latest-milestone: v1.38`.
- [x] KEP readme has up-to-date graduation criteria.
- [x] KEP readme has an updated detailed test plan.
- [ ] KEP has a production readiness review that has been completed and merged into k/enhancements. (For more information on the PRR process, check [here](https://github.com/kubernetes/community/blob/master/sig-architecture/production-readiness.md#submitting-a-kep-for-production-readiness-approval)).
- [ ] There are no other outstanding (unmerged) PRs that modify the KEP readme or kep.yaml file.

For this KEP, we would just need to update the following:
- Merge or close outstanding PR(s) that modify the KEP README or `kep.yaml`: [#6184](https://github.com/kubernetes/enhancements/pull/6184).
- Merge the required `kep.yaml` updates -- `stage` is `beta`, expected `stable`; `latest-milestone` is `v1.36`, expected `v1.38`; `milestone.stable` is missing.
- Complete and merge the PRR approval -- no `stable:` entry in the PRR approval file.

The status of this enhancement is marked as `At risk for enhancements freeze`. Please keep the issue description up-to-date with appropriate stages as well.

If you anticipate missing enhancements freeze, you can file an [exception request](https://github.com/kubernetes/sig-release/blob/master/releases/EXCEPTIONS.md) in advance. Thank you!
```

---

### #5517 — DRA: Node Allocatable Resource Requests

**Summary**

| Issue | KEP PR | Enhancement owner (KEP PR author) | Target stage for v1.38 | In v1.38 milestone | Recommended v1.38 tracking board status |
|---|---|---|---|---|---|
| [#5517](https://github.com/kubernetes/enhancements/issues/5517) DRA: Node Allocatable Resource Requests | [PR #6324](https://github.com/kubernetes/enhancements/pull/6324) | @pravk03 | beta | yes | At risk for enhancements freeze |

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

### #5554 — Support In place update pod resources alongside static cpu manager policy

**Summary**

| Issue | KEP PR | Enhancement owner (KEP PR author) | Target stage for v1.38 | In v1.38 milestone | Recommended v1.38 tracking board status |
|---|---|---|---|---|---|
| [#5554](https://github.com/kubernetes/enhancements/issues/5554) Support In place update pod resources alongside static cpu manager policy | [PR #6330](https://github.com/kubernetes/enhancements/pull/6330) | @esotsal | alpha | yes | Tracked for enhancements freeze |

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
Hello @esotsal :wave:, v1.38 Enhancements team here.

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

### #5677 — DRA: Resource Availability Visibility

**Summary**

| Issue | KEP PR | Enhancement owner (KEP PR author) | Target stage for v1.38 | In v1.38 milestone | Recommended v1.38 tracking board status |
|---|---|---|---|---|---|
| [#5677](https://github.com/kubernetes/enhancements/issues/5677) DRA: Resource Availability Visibility | [PR #6301](https://github.com/kubernetes/enhancements/pull/6301) | @nmn3m | alpha | yes | At risk for enhancements freeze |

**Enhancements Freeze**

- KEP README merged and latest template: ✅
- `kep.yaml` merged and current: ❌
- Graduation Criteria: ✅
- Test Plan: ✅
- Production Readiness Review: ✅
- No outstanding KEP metadata PRs: ❌

**Outstanding actions**

- Merge or close outstanding PR(s) that modify the KEP README or `kep.yaml`: [#6301](https://github.com/kubernetes/enhancements/pull/6301).
- Merge the required `kep.yaml` updates -- `latest-milestone` is `v1.37`, expected `v1.38`.

**Draft GitHub comment**

*(review before posting -- do not auto-post)*

```markdown
Hello @nmn3m :wave:, v1.38 Enhancements team here.

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
- Merge or close outstanding PR(s) that modify the KEP README or `kep.yaml`: [#6301](https://github.com/kubernetes/enhancements/pull/6301).
- Merge the required `kep.yaml` updates -- `latest-milestone` is `v1.37`, expected `v1.38`.

The status of this enhancement is marked as `At risk for enhancements freeze`. Please keep the issue description up-to-date with appropriate stages as well.

If you anticipate missing enhancements freeze, you can file an [exception request](https://github.com/kubernetes/sig-release/blob/master/releases/EXCEPTIONS.md) in advance. Thank you!
```

---

### #5714 — Allow specifying whether to unshare cgroup namespaces

**Summary**

| Issue | KEP PR | Enhancement owner (KEP PR author) | Target stage for v1.38 | In v1.38 milestone | Recommended v1.38 tracking board status |
|---|---|---|---|---|---|
| [#5714](https://github.com/kubernetes/enhancements/issues/5714) Allow specifying whether to unshare cgroup namespaces | [PR #5715](https://github.com/kubernetes/enhancements/pull/5715) | @AkihiroSuda | alpha | yes | At risk for enhancements freeze |

**Enhancements Freeze**

- KEP README merged and latest template: ❌
- `kep.yaml` merged and current: ❌
- Graduation Criteria: ❌
- Test Plan: ❌
- Production Readiness Review: ❌
- No outstanding KEP metadata PRs: ❌

**Outstanding actions**

- Merge or close outstanding PR(s) that modify the KEP README or `kep.yaml`: [#5715](https://github.com/kubernetes/enhancements/pull/5715).
- Could not locate a merged KEP directory (`keps/<sig>/<number>-*/`) on master.

**Draft GitHub comment**

*(review before posting -- do not auto-post)*

```markdown
Hello @AkihiroSuda :wave:, v1.38 Enhancements team here.

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
- Merge or close outstanding PR(s) that modify the KEP README or `kep.yaml`: [#5715](https://github.com/kubernetes/enhancements/pull/5715).
- Could not locate a merged KEP directory (`keps/<sig>/<number>-*/`) on master.

The status of this enhancement is marked as `At risk for enhancements freeze`. Please keep the issue description up-to-date with appropriate stages as well.

If you anticipate missing enhancements freeze, you can file an [exception request](https://github.com/kubernetes/sig-release/blob/master/releases/EXCEPTIONS.md) in advance. Thank you!
```

---

### #5758 — Per-container ulimits configuration

**Summary**

| Issue | KEP PR | Enhancement owner (KEP PR author) | Target stage for v1.38 | In v1.38 milestone | Recommended v1.38 tracking board status |
|---|---|---|---|---|---|
| [#5758](https://github.com/kubernetes/enhancements/issues/5758) Per-container ulimits configuration | [PR #6425](https://github.com/kubernetes/enhancements/pull/6425) | @HirazawaUi | alpha | yes | Tracked for enhancements freeze |

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
Hello @HirazawaUi :wave:, v1.38 Enhancements team here.

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

### #5823 — Pod-Level Checkpoint/Restore

**Summary**

| Issue | KEP PR | Enhancement owner (KEP PR author) | Target stage for v1.38 | In v1.38 milestone | Recommended v1.38 tracking board status |
|---|---|---|---|---|---|
| [#5823](https://github.com/kubernetes/enhancements/issues/5823) Pod-Level Checkpoint/Restore | [PR #6428](https://github.com/kubernetes/enhancements/pull/6428) | @rst0git | alpha | yes | At risk for enhancements freeze |

**Enhancements Freeze**

- KEP README merged and latest template: ✅
- `kep.yaml` merged and current: ✅
- Graduation Criteria: ✅
- Test Plan: ✅
- Production Readiness Review: ✅
- No outstanding KEP metadata PRs: ❌

**Outstanding actions**

- Merge or close outstanding PR(s) that modify the KEP README or `kep.yaml`: [#6428](https://github.com/kubernetes/enhancements/pull/6428).

**Draft GitHub comment**

*(review before posting -- do not auto-post)*

```markdown
Hello @rst0git :wave:, v1.38 Enhancements team here.

Just checking in as we approach [enhancements freeze](https://github.com/kubernetes/sig-release/blob/master/releases/release_phases.md#enhancements-freeze) on **Tuesday 29th September 2026 (AoE) / Wednesday 30th September 2026 12:00 UTC**.

This enhancement is targeting stage `alpha` for v1.38 (correct me, if otherwise)

Here's where this enhancement currently stands:

- [x] KEP readme using the [latest template](https://github.com/kubernetes/enhancements/tree/master/keps/NNNN-kep-template) has been merged into the k/enhancements repo.
- [x] KEP status is marked as `implementable` for `latest-milestone: v1.38`.
- [x] KEP readme has up-to-date graduation criteria.
- [x] KEP readme has an updated detailed test plan.
- [x] KEP has a production readiness review that has been completed and merged into k/enhancements. (For more information on the PRR process, check [here](https://github.com/kubernetes/community/blob/master/sig-architecture/production-readiness.md#submitting-a-kep-for-production-readiness-approval)).
- [ ] There are no other outstanding (unmerged) PRs that modify the KEP readme or kep.yaml file.

For this KEP, we would just need to update the following:
- Merge or close outstanding PR(s) that modify the KEP README or `kep.yaml`: [#6428](https://github.com/kubernetes/enhancements/pull/6428).

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

### #5855 — Add bind mount options (noexec, nodev, nosuid) support on volumeMounts

**Summary**

| Issue | KEP PR | Enhancement owner (KEP PR author) | Target stage for v1.38 | In v1.38 milestone | Recommended v1.38 tracking board status |
|---|---|---|---|---|---|
| [#5855](https://github.com/kubernetes/enhancements/issues/5855) Add bind mount options (noexec, nodev, nosuid) support on volumeMounts | [PR #6434](https://github.com/kubernetes/enhancements/pull/6434) | @nispriha | beta | NO | At risk for enhancements freeze |

**Enhancements Freeze**

- KEP README merged and latest template: ✅
- `kep.yaml` merged and current: ❌
- Graduation Criteria: ✅
- Test Plan: ✅
- Production Readiness Review: ❌
- No outstanding KEP metadata PRs: ❌

**Outstanding actions**

- Issue is not in the **v1.38** milestone (currently: `none`).
- Merge or close outstanding PR(s) that modify the KEP README or `kep.yaml`: [#6434](https://github.com/kubernetes/enhancements/pull/6434).
- Merge the required `kep.yaml` updates -- `stage` is `alpha`, expected `beta`; `latest-milestone` is `v1.37`, expected `v1.38`.
- Complete and merge the PRR questionnaire -- still unanswered (heuristic; verify manually): Rollout, Upgrade and Rollback Planning.
- Complete and merge the PRR approval -- no `beta:` entry in the PRR approval file.

**Draft GitHub comment**

*(review before posting -- do not auto-post)*

```markdown
Hello @nispriha :wave:, v1.38 Enhancements team here.

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
- Issue is not in the **v1.38** milestone (currently: `none`).
- Merge or close outstanding PR(s) that modify the KEP README or `kep.yaml`: [#6434](https://github.com/kubernetes/enhancements/pull/6434).
- Merge the required `kep.yaml` updates -- `stage` is `alpha`, expected `beta`; `latest-milestone` is `v1.37`, expected `v1.38`.
- Complete and merge the PRR questionnaire -- still unanswered (heuristic; verify manually): Rollout, Upgrade and Rollback Planning.
- Complete and merge the PRR approval -- no `beta:` entry in the PRR approval file.

The status of this enhancement is marked as `At risk for enhancements freeze`. Please keep the issue description up-to-date with appropriate stages as well.

If you anticipate missing enhancements freeze, you can file an [exception request](https://github.com/kubernetes/sig-release/blob/master/releases/EXCEPTIONS.md) in advance. Thank you!
```

---

### #5894 — Node system partition

**Summary**

| Issue | KEP PR | Enhancement owner (KEP PR author) | Target stage for v1.38 | In v1.38 milestone | Recommended v1.38 tracking board status |
|---|---|---|---|---|---|
| [#5894](https://github.com/kubernetes/enhancements/issues/5894) Node system partition | [PR #6409](https://github.com/kubernetes/enhancements/pull/6409) | @SergeyKanzhelev | alpha | yes | At risk for enhancements freeze |

**Enhancements Freeze**

- KEP README merged and latest template: ✅
- `kep.yaml` merged and current: ❌
- Graduation Criteria: ✅
- Test Plan: ✅
- Production Readiness Review: ✅
- No outstanding KEP metadata PRs: ❌

**Outstanding actions**

- Merge or close outstanding PR(s) that modify the KEP README or `kep.yaml`: [#6409](https://github.com/kubernetes/enhancements/pull/6409).
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
- Merge or close outstanding PR(s) that modify the KEP README or `kep.yaml`: [#6409](https://github.com/kubernetes/enhancements/pull/6409).
- Merge the required `kep.yaml` updates -- `latest-milestone` is `v1.37`, expected `v1.38`.

The status of this enhancement is marked as `At risk for enhancements freeze`. Please keep the issue description up-to-date with appropriate stages as well.

If you anticipate missing enhancements freeze, you can file an [exception request](https://github.com/kubernetes/sig-release/blob/master/releases/EXCEPTIONS.md) in advance. Thank you!
```

---

### #5945 — DRA: Optional Node Operations

**Summary**

| Issue | KEP PR | Enhancement owner (KEP PR author) | Target stage for v1.38 | In v1.38 milestone | Recommended v1.38 tracking board status |
|---|---|---|---|---|---|
| [#5945](https://github.com/kubernetes/enhancements/issues/5945) DRA: Optional Node Operations | [PR #6372](https://github.com/kubernetes/enhancements/pull/6372) | @troychiu | beta | yes | At risk for enhancements freeze |

**Enhancements Freeze**

- KEP README merged and latest template: ✅
- `kep.yaml` merged and current: ❌
- Graduation Criteria: ✅
- Test Plan: ✅
- Production Readiness Review: ❌
- No outstanding KEP metadata PRs: ❌

**Outstanding actions**

- Merge or close outstanding PR(s) that modify the KEP README or `kep.yaml`: [#6372](https://github.com/kubernetes/enhancements/pull/6372).
- Merge the required `kep.yaml` updates -- `stage` is `alpha`, expected `beta`; `latest-milestone` is `v1.37`, expected `v1.38`.
- Complete and merge the PRR approval -- no `beta:` entry in the PRR approval file.

**Draft GitHub comment**

*(review before posting -- do not auto-post)*

```markdown
Hello @troychiu :wave:, v1.38 Enhancements team here.

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
- Merge or close outstanding PR(s) that modify the KEP README or `kep.yaml`: [#6372](https://github.com/kubernetes/enhancements/pull/6372).
- Merge the required `kep.yaml` updates -- `stage` is `alpha`, expected `beta`; `latest-milestone` is `v1.37`, expected `v1.38`.
- Complete and merge the PRR approval -- no `beta:` entry in the PRR approval file.

The status of this enhancement is marked as `At risk for enhancements freeze`. Please keep the issue description up-to-date with appropriate stages as well.

If you anticipate missing enhancements freeze, you can file an [exception request](https://github.com/kubernetes/sig-release/blob/master/releases/EXCEPTIONS.md) in advance. Thank you!
```

---

### #5972 — Dynamic Pod Mutation: Optimistic Execution & Hierarchical Resource Delegation

**Summary**

| Issue | KEP PR | Enhancement owner (KEP PR author) | Target stage for v1.38 | In v1.38 milestone | Recommended v1.38 tracking board status |
|---|---|---|---|---|---|
| [#5972](https://github.com/kubernetes/enhancements/issues/5972) Dynamic Pod Mutation: Optimistic Execution & Hierarchical Resource Delegation | [PR #6435](https://github.com/kubernetes/enhancements/pull/6435) | @tallclair | alpha | yes | At risk for enhancements freeze |

**Enhancements Freeze**

- KEP README merged and latest template: ✅
- `kep.yaml` merged and current: ✅
- Graduation Criteria: ✅
- Test Plan: ✅
- Production Readiness Review: ✅
- No outstanding KEP metadata PRs: ❌

**Outstanding actions**

- Merge or close outstanding PR(s) that modify the KEP README or `kep.yaml`: [#6435](https://github.com/kubernetes/enhancements/pull/6435).

**Draft GitHub comment**

*(review before posting -- do not auto-post)*

```markdown
Hello @tallclair :wave:, v1.38 Enhancements team here.

Just checking in as we approach [enhancements freeze](https://github.com/kubernetes/sig-release/blob/master/releases/release_phases.md#enhancements-freeze) on **Tuesday 29th September 2026 (AoE) / Wednesday 30th September 2026 12:00 UTC**.

This enhancement is targeting stage `alpha` for v1.38 (correct me, if otherwise)

Here's where this enhancement currently stands:

- [x] KEP readme using the [latest template](https://github.com/kubernetes/enhancements/tree/master/keps/NNNN-kep-template) has been merged into the k/enhancements repo.
- [x] KEP status is marked as `implementable` for `latest-milestone: v1.38`.
- [x] KEP readme has up-to-date graduation criteria.
- [x] KEP readme has an updated detailed test plan.
- [x] KEP has a production readiness review that has been completed and merged into k/enhancements. (For more information on the PRR process, check [here](https://github.com/kubernetes/community/blob/master/sig-architecture/production-readiness.md#submitting-a-kep-for-production-readiness-approval)).
- [ ] There are no other outstanding (unmerged) PRs that modify the KEP readme or kep.yaml file.

For this KEP, we would just need to update the following:
- Merge or close outstanding PR(s) that modify the KEP README or `kep.yaml`: [#6435](https://github.com/kubernetes/enhancements/pull/6435).

The status of this enhancement is marked as `At risk for enhancements freeze`. Please keep the issue description up-to-date with appropriate stages as well.

If you anticipate missing enhancements freeze, you can file an [exception request](https://github.com/kubernetes/sig-release/blob/master/releases/EXCEPTIONS.md) in advance. Thank you!
```

---

### #5996 — Support Default Pod Sysctls in Kubelet

**Summary**

| Issue | KEP PR | Enhancement owner (KEP PR author) | Target stage for v1.38 | In v1.38 milestone | Recommended v1.38 tracking board status |
|---|---|---|---|---|---|
| [#5996](https://github.com/kubernetes/enhancements/issues/5996) Support Default Pod Sysctls in Kubelet | [PR #6418](https://github.com/kubernetes/enhancements/pull/6418) | @VeraQin | beta | yes | At risk for enhancements freeze |

**Enhancements Freeze**

- KEP README merged and latest template: ✅
- `kep.yaml` merged and current: ❌
- Graduation Criteria: ✅
- Test Plan: ✅
- Production Readiness Review: ❌
- No outstanding KEP metadata PRs: ❌

**Outstanding actions**

- Merge or close outstanding PR(s) that modify the KEP README or `kep.yaml`: [#6418](https://github.com/kubernetes/enhancements/pull/6418).
- Merge the required `kep.yaml` updates -- `stage` is `alpha`, expected `beta`; `latest-milestone` is `v1.37`, expected `v1.38`.
- Complete and merge the PRR approval -- no `beta:` entry in the PRR approval file.

**Draft GitHub comment**

*(review before posting -- do not auto-post)*

```markdown
Hello @VeraQin :wave:, v1.38 Enhancements team here.

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
- Merge or close outstanding PR(s) that modify the KEP README or `kep.yaml`: [#6418](https://github.com/kubernetes/enhancements/pull/6418).
- Merge the required `kep.yaml` updates -- `stage` is `alpha`, expected `beta`; `latest-milestone` is `v1.37`, expected `v1.38`.
- Complete and merge the PRR approval -- no `beta:` entry in the PRR approval file.

The status of this enhancement is marked as `At risk for enhancements freeze`. Please keep the issue description up-to-date with appropriate stages as well.

If you anticipate missing enhancements freeze, you can file an [exception request](https://github.com/kubernetes/sig-release/blob/master/releases/EXCEPTIONS.md) in advance. Thank you!
```

---

### #5999 — HTTP/2 cleartext (h2c) for container probes

**Summary**

| Issue | KEP PR | Enhancement owner (KEP PR author) | Target stage for v1.38 | In v1.38 milestone | Recommended v1.38 tracking board status |
|---|---|---|---|---|---|
| [#5999](https://github.com/kubernetes/enhancements/issues/5999) HTTP/2 cleartext (h2c) for container probes | [PR #6338](https://github.com/kubernetes/enhancements/pull/6338) | @amritansh1502 | beta | yes | At risk for enhancements freeze |

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
Hello @amritansh1502 :wave:, v1.38 Enhancements team here.

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

### #6007 — Add Topology Manager option to improve workload density for single-numa-node

**Summary**

| Issue | KEP PR | Enhancement owner (KEP PR author) | Target stage for v1.38 | In v1.38 milestone | Recommended v1.38 tracking board status |
|---|---|---|---|---|---|
| [#6007](https://github.com/kubernetes/enhancements/issues/6007) Add Topology Manager option to improve workload density for single-numa-node | [PR #6332](https://github.com/kubernetes/enhancements/pull/6332) | @swatisehgal | alpha | yes | At risk for enhancements freeze |

**Enhancements Freeze**

- KEP README merged and latest template: ❌
- `kep.yaml` merged and current: ❌
- Graduation Criteria: ❌
- Test Plan: ❌
- Production Readiness Review: ❌
- No outstanding KEP metadata PRs: ❌

**Outstanding actions**

- Merge or close outstanding PR(s) that modify the KEP README or `kep.yaml`: [#6332](https://github.com/kubernetes/enhancements/pull/6332).
- Could not locate a merged KEP directory (`keps/<sig>/<number>-*/`) on master.

**Draft GitHub comment**

*(review before posting -- do not auto-post)*

```markdown
Hello @swatisehgal :wave:, v1.38 Enhancements team here.

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
- Merge or close outstanding PR(s) that modify the KEP README or `kep.yaml`: [#6332](https://github.com/kubernetes/enhancements/pull/6332).
- Could not locate a merged KEP directory (`keps/<sig>/<number>-*/`) on master.

The status of this enhancement is marked as `At risk for enhancements freeze`. Please keep the issue description up-to-date with appropriate stages as well.

If you anticipate missing enhancements freeze, you can file an [exception request](https://github.com/kubernetes/sig-release/blob/master/releases/EXCEPTIONS.md) in advance. Thank you!
```

---

### #6030 — Dynamic resize of memory-backed volumes

**Summary**

| Issue | KEP PR | Enhancement owner (KEP PR author) | Target stage for v1.38 | In v1.38 milestone | Recommended v1.38 tracking board status |
|---|---|---|---|---|---|
| [#6030](https://github.com/kubernetes/enhancements/issues/6030) Dynamic resize of memory-backed volumes | [PR #6320](https://github.com/kubernetes/enhancements/pull/6320) | @natasha41575 | beta | yes | Tracked for enhancements freeze |

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
Hello @natasha41575 :wave:, v1.38 Enhancements team here.

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

### #6061 — OCI Artifact-Based Security Profile Distribution

**Summary**

| Issue | KEP PR | Enhancement owner (KEP PR author) | Target stage for v1.38 | In v1.38 milestone | Recommended v1.38 tracking board status |
|---|---|---|---|---|---|
| [#6061](https://github.com/kubernetes/enhancements/issues/6061) OCI Artifact-Based Security Profile Distribution | [PR #6062](https://github.com/kubernetes/enhancements/pull/6062) | @saschagrunert | alpha | yes | At risk for enhancements freeze |

**Enhancements Freeze**

- KEP README merged and latest template: ❌
- `kep.yaml` merged and current: ❌
- Graduation Criteria: ❌
- Test Plan: ❌
- Production Readiness Review: ❌
- No outstanding KEP metadata PRs: ❌

**Outstanding actions**

- Merge or close outstanding PR(s) that modify the KEP README or `kep.yaml`: [#6062](https://github.com/kubernetes/enhancements/pull/6062).
- Could not locate a merged KEP directory (`keps/<sig>/<number>-*/`) on master.

**Draft GitHub comment**

*(review before posting -- do not auto-post)*

```markdown
Hello @saschagrunert :wave:, v1.38 Enhancements team here.

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
- Merge or close outstanding PR(s) that modify the KEP README or `kep.yaml`: [#6062](https://github.com/kubernetes/enhancements/pull/6062).
- Could not locate a merged KEP directory (`keps/<sig>/<number>-*/`) on master.

The status of this enhancement is marked as `At risk for enhancements freeze`. Please keep the issue description up-to-date with appropriate stages as well.

If you anticipate missing enhancements freeze, you can file an [exception request](https://github.com/kubernetes/sig-release/blob/master/releases/EXCEPTIONS.md) in advance. Thank you!
```

---

### #6063 — Configuration for Per-Pod PID Limit

**Summary**

| Issue | KEP PR | Enhancement owner (KEP PR author) | Target stage for v1.38 | In v1.38 milestone | Recommended v1.38 tracking board status |
|---|---|---|---|---|---|
| [#6063](https://github.com/kubernetes/enhancements/issues/6063) Configuration for Per-Pod PID Limit | [PR #6258](https://github.com/kubernetes/enhancements/pull/6258) | @BhargaviGudi | alpha | yes | Tracked for enhancements freeze |

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
Hello @BhargaviGudi :wave:, v1.38 Enhancements team here.

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

### #6122 — Support CPU Configurable Scaling Delay

**Summary**

| Issue | KEP PR | Enhancement owner (KEP PR author) | Target stage for v1.38 | In v1.38 milestone | Recommended v1.38 tracking board status |
|---|---|---|---|---|---|
| [#6122](https://github.com/kubernetes/enhancements/issues/6122) Support CPU Configurable Scaling Delay | [PR #6314](https://github.com/kubernetes/enhancements/pull/6314) | @Chunxia202410 | alpha | yes | At risk for enhancements freeze |

**Enhancements Freeze**

- KEP README merged and latest template: ✅
- `kep.yaml` merged and current: ❌
- Graduation Criteria: ✅
- Test Plan: ✅
- Production Readiness Review: ✅
- No outstanding KEP metadata PRs: ❌

**Outstanding actions**

- Merge or close outstanding PR(s) that modify the KEP README or `kep.yaml`: [#6314](https://github.com/kubernetes/enhancements/pull/6314), [#6230](https://github.com/kubernetes/enhancements/pull/6230).
- Merge the required `kep.yaml` updates -- `latest-milestone` is `v1.37`, expected `v1.38`.

**Draft GitHub comment**

*(review before posting -- do not auto-post)*

```markdown
Hello @Chunxia202410 :wave:, v1.38 Enhancements team here.

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
- Merge or close outstanding PR(s) that modify the KEP README or `kep.yaml`: [#6314](https://github.com/kubernetes/enhancements/pull/6314), [#6230](https://github.com/kubernetes/enhancements/pull/6230).
- Merge the required `kep.yaml` updates -- `latest-milestone` is `v1.37`, expected `v1.38`.

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

### #6232 — Tolerate benign per-NUMA memory drift in the Memory Manager

**Summary**

| Issue | KEP PR | Enhancement owner (KEP PR author) | Target stage for v1.38 | In v1.38 milestone | Recommended v1.38 tracking board status |
|---|---|---|---|---|---|
| [#6232](https://github.com/kubernetes/enhancements/issues/6232) Tolerate benign per-NUMA memory drift in the Memory Manager | [PR #6233](https://github.com/kubernetes/enhancements/pull/6233) | @AI-Armless | alpha | yes | At risk for enhancements freeze |

**Enhancements Freeze**

- KEP README merged and latest template: ❌
- `kep.yaml` merged and current: ❌
- Graduation Criteria: ❌
- Test Plan: ❌
- Production Readiness Review: ❌
- No outstanding KEP metadata PRs: ❌

**Outstanding actions**

- Merge or close outstanding PR(s) that modify the KEP README or `kep.yaml`: [#6233](https://github.com/kubernetes/enhancements/pull/6233).
- Could not locate a merged KEP directory (`keps/<sig>/<number>-*/`) on master.

**Draft GitHub comment**

*(review before posting -- do not auto-post)*

```markdown
Hello @AI-Armless :wave:, v1.38 Enhancements team here.

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
- Merge or close outstanding PR(s) that modify the KEP README or `kep.yaml`: [#6233](https://github.com/kubernetes/enhancements/pull/6233).
- Could not locate a merged KEP directory (`keps/<sig>/<number>-*/`) on master.

The status of this enhancement is marked as `At risk for enhancements freeze`. Please keep the issue description up-to-date with appropriate stages as well.

If you anticipate missing enhancements freeze, you can file an [exception request](https://github.com/kubernetes/sig-release/blob/master/releases/EXCEPTIONS.md) in advance. Thank you!
```

---

### #6247 — Kubelet systemd watchdog diagnostic guardrails

**Summary**

| Issue | KEP PR | Enhancement owner (KEP PR author) | Target stage for v1.38 | In v1.38 milestone | Recommended v1.38 tracking board status |
|---|---|---|---|---|---|
| [#6247](https://github.com/kubernetes/enhancements/issues/6247) Kubelet systemd watchdog diagnostic guardrails | [PR #6248](https://github.com/kubernetes/enhancements/pull/6248) | @googs1025 | alpha | yes | At risk for enhancements freeze |

**Enhancements Freeze**

- KEP README merged and latest template: ❌
- `kep.yaml` merged and current: ❌
- Graduation Criteria: ❌
- Test Plan: ❌
- Production Readiness Review: ❌
- No outstanding KEP metadata PRs: ❌

**Outstanding actions**

- Merge or close outstanding PR(s) that modify the KEP README or `kep.yaml`: [#6248](https://github.com/kubernetes/enhancements/pull/6248).
- Could not locate a merged KEP directory (`keps/<sig>/<number>-*/`) on master.

**Draft GitHub comment**

*(review before posting -- do not auto-post)*

```markdown
Hello @googs1025 :wave:, v1.38 Enhancements team here.

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
- Merge or close outstanding PR(s) that modify the KEP README or `kep.yaml`: [#6248](https://github.com/kubernetes/enhancements/pull/6248).
- Could not locate a merged KEP directory (`keps/<sig>/<number>-*/`) on master.

The status of this enhancement is marked as `At risk for enhancements freeze`. Please keep the issue description up-to-date with appropriate stages as well.

If you anticipate missing enhancements freeze, you can file an [exception request](https://github.com/kubernetes/sig-release/blob/master/releases/EXCEPTIONS.md) in advance. Thank you!
```

---

### #6252 — KEP-6252: Support hugepages in kubelet's `--system-reserved` and `--kube-reserved flags`

**Summary**

| Issue | KEP PR | Enhancement owner (KEP PR author) | Target stage for v1.38 | In v1.38 milestone | Recommended v1.38 tracking board status |
|---|---|---|---|---|---|
| [#6252](https://github.com/kubernetes/enhancements/issues/6252) KEP-6252: Support hugepages in kubelet's `--system-reserved` and `--kube-reserved flags` | [PR #6253](https://github.com/kubernetes/enhancements/pull/6253) | @Tal-or | alpha | yes | At risk for enhancements freeze |

**Enhancements Freeze**

- KEP README merged and latest template: ❌
- `kep.yaml` merged and current: ❌
- Graduation Criteria: ❌
- Test Plan: ❌
- Production Readiness Review: ❌
- No outstanding KEP metadata PRs: ❌

**Outstanding actions**

- Merge or close outstanding PR(s) that modify the KEP README or `kep.yaml`: [#6253](https://github.com/kubernetes/enhancements/pull/6253).
- Could not locate a merged KEP directory (`keps/<sig>/<number>-*/`) on master.

**Draft GitHub comment**

*(review before posting -- do not auto-post)*

```markdown
Hello @Tal-or :wave:, v1.38 Enhancements team here.

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
- Merge or close outstanding PR(s) that modify the KEP README or `kep.yaml`: [#6253](https://github.com/kubernetes/enhancements/pull/6253).
- Could not locate a merged KEP directory (`keps/<sig>/<number>-*/`) on master.

The status of this enhancement is marked as `At risk for enhancements freeze`. Please keep the issue description up-to-date with appropriate stages as well.

If you anticipate missing enhancements freeze, you can file an [exception request](https://github.com/kubernetes/sig-release/blob/master/releases/EXCEPTIONS.md) in advance. Thank you!
```

---

### #6274 — KEP-6274: GPU support for Pod-level Checkpoint/Restore

**Summary**

| Issue | KEP PR | Enhancement owner (KEP PR author) | Target stage for v1.38 | In v1.38 milestone | Recommended v1.38 tracking board status |
|---|---|---|---|---|---|
| [#6274](https://github.com/kubernetes/enhancements/issues/6274) KEP-6274: GPU support for Pod-level Checkpoint/Restore | [PR #6275](https://github.com/kubernetes/enhancements/pull/6275) | @rst0git | alpha | yes | At risk for enhancements freeze |

**Enhancements Freeze**

- KEP README merged and latest template: ❌
- `kep.yaml` merged and current: ❌
- Graduation Criteria: ❌
- Test Plan: ❌
- Production Readiness Review: ❌
- No outstanding KEP metadata PRs: ❌

**Outstanding actions**

- Merge or close outstanding PR(s) that modify the KEP README or `kep.yaml`: [#6275](https://github.com/kubernetes/enhancements/pull/6275).
- Could not locate a merged KEP directory (`keps/<sig>/<number>-*/`) on master.

**Draft GitHub comment**

*(review before posting -- do not auto-post)*

```markdown
Hello @rst0git :wave:, v1.38 Enhancements team here.

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
- Merge or close outstanding PR(s) that modify the KEP README or `kep.yaml`: [#6275](https://github.com/kubernetes/enhancements/pull/6275).
- Could not locate a merged KEP directory (`keps/<sig>/<number>-*/`) on master.

The status of this enhancement is marked as `At risk for enhancements freeze`. Please keep the issue description up-to-date with appropriate stages as well.

If you anticipate missing enhancements freeze, you can file an [exception request](https://github.com/kubernetes/sig-release/blob/master/releases/EXCEPTIONS.md) in advance. Thank you!
```

---

### #6318 — Allow in-place updates to container probes

**Summary**

| Issue | KEP PR | Enhancement owner (KEP PR author) | Target stage for v1.38 | In v1.38 milestone | Recommended v1.38 tracking board status |
|---|---|---|---|---|---|
| [#6318](https://github.com/kubernetes/enhancements/issues/6318) Allow in-place updates to container probes | [PR #6323](https://github.com/kubernetes/enhancements/pull/6323) | @HirazawaUi | alpha | yes | At risk for enhancements freeze |

**Enhancements Freeze**

- KEP README merged and latest template: ❌
- `kep.yaml` merged and current: ❌
- Graduation Criteria: ❌
- Test Plan: ❌
- Production Readiness Review: ❌
- No outstanding KEP metadata PRs: ❌

**Outstanding actions**

- Merge or close outstanding PR(s) that modify the KEP README or `kep.yaml`: [#6323](https://github.com/kubernetes/enhancements/pull/6323).
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
- Merge or close outstanding PR(s) that modify the KEP README or `kep.yaml`: [#6323](https://github.com/kubernetes/enhancements/pull/6323).
- Could not locate a merged KEP directory (`keps/<sig>/<number>-*/`) on master.

The status of this enhancement is marked as `At risk for enhancements freeze`. Please keep the issue description up-to-date with appropriate stages as well.

If you anticipate missing enhancements freeze, you can file an [exception request](https://github.com/kubernetes/sig-release/blob/master/releases/EXCEPTIONS.md) in advance. Thank you!
```

---

### #6035 — Exec session identity propagation

**Summary**

| Issue | KEP PR | Enhancement owner (KEP PR author) | Target stage for v1.38 | In v1.38 milestone | Recommended v1.38 tracking board status |
|---|---|---|---|---|---|
| [#6035](https://github.com/kubernetes/enhancements/issues/6035) Exec session identity propagation | [PR #6205](https://github.com/kubernetes/enhancements/pull/6205) | @nispriha | alpha | yes | At risk for enhancements freeze |

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
Hello @nispriha :wave:, v1.38 Enhancements team here.

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

### #6369 — Pod Assigned Resource Exposure via Downward API

**Summary**

| Issue | KEP PR | Enhancement owner (KEP PR author) | Target stage for v1.38 | In v1.38 milestone | Recommended v1.38 tracking board status |
|---|---|---|---|---|---|
| [#6369](https://github.com/kubernetes/enhancements/issues/6369) Pod Assigned Resource Exposure via Downward API | [PR #6370](https://github.com/kubernetes/enhancements/pull/6370) | @Chunxia202410 | alpha | yes | At risk for enhancements freeze |

**Enhancements Freeze**

- KEP README merged and latest template: ❌
- `kep.yaml` merged and current: ❌
- Graduation Criteria: ❌
- Test Plan: ❌
- Production Readiness Review: ❌
- No outstanding KEP metadata PRs: ❌

**Outstanding actions**

- Merge or close outstanding PR(s) that modify the KEP README or `kep.yaml`: [#6370](https://github.com/kubernetes/enhancements/pull/6370).
- Could not locate a merged KEP directory (`keps/<sig>/<number>-*/`) on master.

**Draft GitHub comment**

*(review before posting -- do not auto-post)*

```markdown
Hello @Chunxia202410 :wave:, v1.38 Enhancements team here.

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
- Merge or close outstanding PR(s) that modify the KEP README or `kep.yaml`: [#6370](https://github.com/kubernetes/enhancements/pull/6370).
- Could not locate a merged KEP directory (`keps/<sig>/<number>-*/`) on master.

The status of this enhancement is marked as `At risk for enhancements freeze`. Please keep the issue description up-to-date with appropriate stages as well.

If you anticipate missing enhancements freeze, you can file an [exception request](https://github.com/kubernetes/sig-release/blob/master/releases/EXCEPTIONS.md) in advance. Thank you!
```

---

### #6371 — External Node Liveness Detection

**Summary**

| Issue | KEP PR | Enhancement owner (KEP PR author) | Target stage for v1.38 | In v1.38 milestone | Recommended v1.38 tracking board status |
|---|---|---|---|---|---|
| [#6371](https://github.com/kubernetes/enhancements/issues/6371) External Node Liveness Detection | [PR #6373](https://github.com/kubernetes/enhancements/pull/6373) | @jpbetz | alpha | yes | At risk for enhancements freeze |

**Enhancements Freeze**

- KEP README merged and latest template: ❌
- `kep.yaml` merged and current: ❌
- Graduation Criteria: ❌
- Test Plan: ❌
- Production Readiness Review: ❌
- No outstanding KEP metadata PRs: ❌

**Outstanding actions**

- Merge or close outstanding PR(s) that modify the KEP README or `kep.yaml`: [#6373](https://github.com/kubernetes/enhancements/pull/6373).
- Could not locate a merged KEP directory (`keps/<sig>/<number>-*/`) on master.

**Draft GitHub comment**

*(review before posting -- do not auto-post)*

```markdown
Hello @jpbetz :wave:, v1.38 Enhancements team here.

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
- Merge or close outstanding PR(s) that modify the KEP README or `kep.yaml`: [#6373](https://github.com/kubernetes/enhancements/pull/6373).
- Could not locate a merged KEP directory (`keps/<sig>/<number>-*/`) on master.

The status of this enhancement is marked as `At risk for enhancements freeze`. Please keep the issue description up-to-date with appropriate stages as well.

If you anticipate missing enhancements freeze, you can file an [exception request](https://github.com/kubernetes/sig-release/blob/master/releases/EXCEPTIONS.md) in advance. Thank you!
```

---

### #5359 — Workload Controlled Swap

**Summary**

| Issue | KEP PR | Enhancement owner (KEP PR author) | Target stage for v1.38 | In v1.38 milestone | Recommended v1.38 tracking board status |
|---|---|---|---|---|---|
| [#5359](https://github.com/kubernetes/enhancements/issues/5359) Workload Controlled Swap | [PR #5569](https://github.com/kubernetes/enhancements/pull/5569) | @ajaysundark | alpha | yes | At risk for enhancements freeze |

**Enhancements Freeze**

- KEP README merged and latest template: ❌
- `kep.yaml` merged and current: ❌
- Graduation Criteria: ❌
- Test Plan: ❌
- Production Readiness Review: ❌
- No outstanding KEP metadata PRs: ❌

**Outstanding actions**

- Merge or close outstanding PR(s) that modify the KEP README or `kep.yaml`: [#5569](https://github.com/kubernetes/enhancements/pull/5569).
- Could not locate a merged KEP directory (`keps/<sig>/<number>-*/`) on master.

**Draft GitHub comment**

*(review before posting -- do not auto-post)*

```markdown
Hello @ajaysundark :wave:, v1.38 Enhancements team here.

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
- Merge or close outstanding PR(s) that modify the KEP README or `kep.yaml`: [#5569](https://github.com/kubernetes/enhancements/pull/5569).
- Could not locate a merged KEP directory (`keps/<sig>/<number>-*/`) on master.

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
