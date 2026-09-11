# C1 boundary audit and G1 handoff

## Why this addendum exists

A post-C1 audit found that the first version of the matrix reused at least one primary supporting study as `boundary_study_ids` in every one of the 11 claim rows. That pattern blurred two different things:

1. a primary study's **own scope/limitations**, which can legitimately bound what its positive result establishes; and
2. **independent boundary, counter-direction, or contradictory evidence**, which must come from a different study/system if it is to provide an independent challenge to the claim.

The matrix has therefore been revised so these roles cannot be conflated.

## Revised evidence roles

The machine-readable C1 matrix now uses:

- `primary_study_ids` — direct support for the normalized claim;
- `corroborating_study_ids` — additional evidence in the same direction;
- `within_study_boundary_ids` — primary studies whose own design, scope, or limitations directly constrain the inference drawn from their positive results;
- `independent_boundary_study_ids` — distinct studies/systems that provide a counter-direction, near-miss, mitigation, or contrasting capability;
- `boundary_overlap_justification` — mandatory explanation whenever a primary study is reused as a within-study boundary;
- `boundary_rationale` — claim-specific explanation of what the independent boundary evidence changes or limits.

A paper's generic limitations section still does not count automatically. The limitation must bear on the specific C1 claim.

## Structural rule now enforced by CI

`independent_boundary_study_ids` may **never** overlap `primary_study_ids`.

A primary study may appear in `within_study_boundary_ids` only when:

- the ID is already a primary ID; and
- an explicit claim-specific overlap justification is recorded.

Every C1 row must also contain at least one independent boundary/counter-direction study. The CI validator checks those conditions in addition to register membership, normalized-note existence, record-249 exclusion, and checked source-location entries for primary and independent-boundary evidence.

## Independent-boundary pass across the 11 claims

| Claim | Independent boundary/counter-direction evidence | Why it matters |
|---|---|---|
| C1-01 | 379 Spider2-V; 430 InfiAgent-DABench | Structured/executable workflow benchmarks narrow the fragmentation claim but still do not close the Web source-to-dataset contract. |
| C1-02 | 450 GUI-Actor | Demonstrates material progress in grounding, so 'bottleneck' is not an assertion that grounding cannot improve. |
| C1-03 | 667 SCRIBES | Provides a genuine extraction-aware RL counter-direction; the claim is about dominant objectives, not total absence. |
| C1-04 | 503 BacktrackAgent | Shows recovery is trainable/architectable, limiting a purely diagnostic reading of robustness failures. |
| C1-05 | 663 INFOGENT | Extends open-ended source access/aggregation beyond scraper systems while still lacking schema-bound field provenance. |
| C1-06 | 675 OneKE; 667 SCRIBES | Provides the contrasting schema/script extraction family against which answer-level aggregation is distinguished. |
| C1-07 | 338 WebArena; 430 InfiAgent-DABench | Shows deterministic functional/closed-form evaluation can be strong when state/output is observable. |
| C1-08 | 738 GuardAgent | Demonstrates mitigation through external policy enforcement; compromise is not treated as inevitable. |
| C1-09 | 738 GuardAgent | Provides an independent execution-stage control case that bounds ToolSword's vulnerability evidence. |
| C1-10 | 430 InfiAgent-DABench | Shows structured outputs can be made machine-checkable in bounded settings even though Web provenance remains unsolved. |
| C1-11 | 379 Spider2-V; 430 InfiAgent-DABench | Adds independent near-miss systems to the counterexample search, but does **not** close the universal absence claim. |

## C1-11 is not G1

C1-11 is the most consequential row because it supports the manuscript statement that no representative reviewed system jointly demonstrates:

1. unfamiliar-site navigation;
2. explicit schema coverage;
3. field-level provenance;
4. unsupported-value control;
5. cross-site transfer; and
6. complete dataset assembly.

C1 establishes **claim → study → source-location traceability** for that statement. It does **not** establish the universal absence claim by itself.

The universal claim remains provisional until **G1** exists: a system-by-requirement matrix that codes each plausible counterexample against operational definitions and shows whether any single evaluated system satisfies all required dimensions jointly.

Accordingly, C1-11 is now labeled:

- evidence strength: `provisional_absence_claim_requires_G1`;
- verification status: `C1_traceability_complete_G1_system_requirement_matrix_pending_final_membership_pending`.

A green C1 CI run therefore means the traceability structure is internally valid. It must never be interpreted as G1 passing.

## Dependency on G2

G1 cannot be coded defensibly until terms such as **field-level provenance**, **complete dataset assembly**, **cross-site transfer**, and **joint evaluation** have operational definitions. Those definitions are provided separately in G2 and are the coding rules G1 must use.
