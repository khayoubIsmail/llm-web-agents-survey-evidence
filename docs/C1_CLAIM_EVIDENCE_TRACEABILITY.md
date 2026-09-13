# C1 — Load-Bearing Claim → Study → Source-Location Traceability

## Final status

**C1 is complete and revalidated against the final 385-study qualitative synthesis.**

The machine-readable claim matrix is:

- `data/c1_claim_evidence_matrix.csv`

It contains **11 load-bearing claims**. Each row records the claim, manuscript location, primary studies, corroborating studies, within-study boundary evidence, independent boundary/counter-direction studies, quantitative evidence where relevant, checked source locations, evidence strength, and verification status.

## Final membership gate

After publication-status adjudication and synthesis-membership reconciliation, every study ID used by the C1 matrix was rechecked against `data/final_synthesis_membership.csv`.

Final result:

- final synthesis size: **385**;
- C1 claims: **11**;
- all referenced C1 study IDs belong to the final synthesis: **YES**;
- stale evidence removed: **record 443 (OmniParser)** from C1-02;
- record 249 is not used as C1 evidence because of the documented full-text exception.

The final gate is recorded in:

- `data/final_c1_g1_revalidation_summary.json`
- `data/final_c1_membership_revalidation.csv`

## Evidence-role definitions

C1 distinguishes three roles:

- **Primary support:** the study or studies that most directly establish the claim.
- **Corroboration:** additional studies that independently support the same direction, mechanism, or empirical pattern.
- **Boundary / contradictory evidence:** evidence that limits the scope of a claim, exposes a failure mode, or shows a setting in which the claim does not generalize.

A paper's generic limitations section is not automatically treated as claim-level boundary evidence; the limitation must be relevant to the specific claim.

## Final load-bearing claims

The final matrix covers these 11 claims:

1. **Benchmark coverage is fragmented.** Representative benchmarks cover different pipeline components but do not jointly evaluate the complete source-to-dataset extraction contract.
2. **Grounding is distinct from high-level reasoning.** A plausible action plan can still fail at executable element localization.
3. **Dominant Web-agent training objectives are not extraction contracts.** Task/trajectory/action success does not by itself establish schema, field support, provenance, or record completeness.
4. **Clean benchmark success can overstate deployment robustness.** Fault-aware and recovery-aware evaluation is required.
5. **Structured extraction benefits from schemas and executable programs but remains incomplete.** Current systems do not by themselves establish generalized provenance-aware live-Web extraction.
6. **Open-ended aggregation is not equivalent to schema-bound dataset extraction.** Answer/report synthesis does not ensure row coverage, field provenance, or complete dataset assembly.
7. **Automatic agent evaluators are themselves fallible.** LLM judges should supplement deterministic checks where state/value/source evidence can be checked programmatically.
8. **Externally controlled Web/environment content is an active security boundary.** Page content can function as both task data and adversarial instruction/grounding input.
9. **Safety must control the execution loop, not only the final answer.** Unsafe tool/action choices can occur before output moderation.
10. **A successful trajectory does not establish data integrity.** Extraction requires field/source/schema checks in addition to behavioral monitoring.
11. **Scoped system-level gap claim.** No representative reviewed system jointly demonstrates all six G2 requirements in one evaluated end-to-end pipeline.

The exact study IDs, quantitative evidence, boundary evidence, and checked source locations remain in `data/c1_claim_evidence_matrix.csv`.

## C1-02 repair after final publication adjudication

The pre-freeze version of C1-02 listed OmniParser (record 443) as corroborating grounding evidence. Final publication-status reconciliation removed record 443 from the qualitative synthesis. C1-02 was therefore repaired rather than carrying an ineligible study forward.

Final C1-02 uses:

- primary: **SeeAct (282)**;
- corroboration: **SeeClick (441)**;
- independent progress/boundary evidence: **GUI-Actor (450)**.

The final matrix explicitly records that OmniParser was removed after final membership adjudication.

## C1-11 and G1 dependency

C1-11 is intentionally scoped. Its final accepted wording is:

> Under the operational definitions used in our system-level comparison, none of the representative reviewed systems jointly demonstrates unfamiliar-site navigation, explicit schema coverage, field-level provenance, unsupported-value control, cross-site transfer, and complete dataset assembly in one evaluated end-to-end pipeline.

This wording is supported by the final G1 system×requirement audit and targeted counterexample sweep. It is **not** a universal claim that no system anywhere can satisfy the contract.

## Reviewer-response wording

> We created a machine-readable claim-to-study-to-source matrix for 11 load-bearing claims. Each claim records its primary evidence, corroborating evidence, independent boundary or counter-direction studies, quantitative evidence where applicable, and the exact source locations checked. After publication-status adjudication and synthesis reconciliation, we revalidated every C1 study ID against the final 385-study synthesis. One stale corroborating record (OmniParser, record 443) was removed from C1-02 because it no longer belonged to the final synthesis. All remaining C1 evidence IDs now pass final-membership validation. The system-level absence claim was additionally gated through G1 and retained only in scoped representative-system form.

## Completion checklist

- [x] 11 load-bearing claims enumerated;
- [x] claim → primary study → source location traceability recorded;
- [x] corroborating and boundary/counter-direction evidence recorded;
- [x] record 249 excluded from claim-level evidence;
- [x] final 385-study membership frozen;
- [x] every C1 evidence ID revalidated against final membership;
- [x] stale record 443 removed from C1-02;
- [x] C1-11 revalidated through final G1;
- [x] final manuscript wording kept within evidence scope.

**C1 final status: CLOSED.**