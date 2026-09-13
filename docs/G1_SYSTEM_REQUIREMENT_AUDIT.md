# G1 — System × Requirement Audit for the Complete Extraction Contract

## Final status

**G1 is complete and closed against the final 385-study qualitative synthesis.**

G1 tests the manuscript's central system-level gap claim using the operational definitions frozen in `docs/G2_OPERATIONAL_DEFINITIONS.md`.

The final claim is:

> Under the operational definitions used in our system-level comparison, none of the representative reviewed systems jointly demonstrates unfamiliar-site navigation, explicit schema coverage, field-level provenance, unsupported-value control, cross-site transfer, and complete dataset assembly in one evaluated end-to-end pipeline.

This wording is deliberately scoped to the reviewed representative systems. It is not an unrestricted universal claim over every possible system.

## Operational requirements

Each candidate system is coded independently on:

1. unfamiliar-site navigation;
2. explicit schema coverage;
3. field-level provenance;
4. unsupported-value control;
5. cross-site transfer;
6. complete dataset assembly; and
7. joint evaluation.

Allowed values are `YES`, `PARTIAL`, `NO`, and `NR`, exactly as defined in G2.

Critical rules:

- `NR` is not treated as `NO`;
- `PARTIAL` is not upgraded to `YES` because a capability appears plausible;
- a system closes the contract only if all six requirement columns are `YES` and `joint_evaluation = YES`;
- capabilities assembled across different systems do not count as joint end-to-end evaluation.

## Representative system matrix

The machine-readable matrix is:

- `data/g1_system_requirement_matrix.csv`

The 10 representative systems are:

- SeeAct (282);
- MindAct / Mind2Web (337);
- WebArena GPT-4 baseline (338);
- Spider2-V (379);
- DAAgent / InfiAgent-DABench (430);
- AutoScraper (661);
- INFOGENT (663);
- SCRIBES (667);
- OneKE (675);
- WiNELL (692).

All 10 records remain members of the final 385-study synthesis. None is coded `YES` on all six capability requirements plus `YES` on joint evaluation.

## Final targeted counterexample sweep

After the final corpus freeze, G1 performed a targeted second-pass sweep over **12 additional extraction/generalization/deployment near-misses** beyond the original 10-row matrix.

The additional cases cover:

- broad Web-scraping survey/context work;
- practical Web-data collection;
- conversational product search;
- historical webpage interaction systems;
- natural-language data analysis;
- data-cleaning workflow generation;
- business-intelligence/data-agent platforms;
- question-aware data preparation;
- agent-generalizability survey evidence;
- human-agent collaborative Web navigation;
- live-Web A/B-testing agents; and
- value-sensitive GUI-agent evaluation.

These studies provide important adjacent capabilities but do not form a counterexample to the six-requirement end-to-end extraction contract. They are either surveys/background, post-extraction data preparation/analysis systems, search/aggregation systems, human-in-the-loop navigation systems, or deployment/HCI evaluations rather than one pipeline jointly demonstrating all six G2 requirements.

The final gate is recorded in:

- `data/final_c1_g1_revalidation_summary.json`
- `data/final_g1_targeted_counterexample_sweep.csv`
- `data/final_g1_high_risk_candidate_sweep.csv`

Final result:

- representative G1 matrix systems checked: **10**;
- targeted additional near-misses checked: **12**;
- total explicit final system/edge cases checked: **22**;
- full-contract counterexamples found: **0**;
- scoped absence claim supported: **YES**.

## Interpretation of the near-miss pattern

The result is not that the literature lacks progress. Instead, capabilities remain distributed across different system families:

- **Navigation-heavy systems** can explore unfamiliar or varied Web environments but generally do not jointly provide extraction schemas, field-level provenance, unsupported-value controls, and complete dataset assembly.
- **Extraction-heavy systems** provide schemas, scripts, selectors, or structured output but generally do not jointly demonstrate unfamiliar-site navigation, field-level source binding, arbitrary cross-site transfer, and complete collection coverage.
- **Structured data-workflow systems** provide machine-checkable outputs and executable evaluation but are not generalized live-Web extraction systems.
- **Multi-source aggregation/update systems** improve source discovery and citation-aware synthesis but operate at answer/report/article level rather than a field-provenance-preserving multi-record dataset contract.
- **Deployment/HCI systems** address collaboration, behavior, safety, efficiency, or user values, not the complete extraction contract.

This is why the manuscript uses a scoped representative-system conclusion rather than an absolute absence statement.

## Final C1-11 wording

The manuscript and C1 matrix use the following wording:

> Under the operational definitions used in our system-level comparison, none of the representative reviewed systems jointly demonstrates unfamiliar-site navigation, explicit schema coverage, field-level provenance, unsupported-value control, cross-site transfer, and complete dataset assembly in one evaluated end-to-end pipeline.

## Reviewer-response wording

> We agree that the previous absence claim required explicit system-level evidence rather than a narrative comparison. We therefore operationalized the six disputed requirements and coded the strongest representative counterexample systems in a system-by-requirement matrix using four states (YES, PARTIAL, NO, NR). Missing reporting was not treated as evidence of absence, and partial capabilities were not upgraded to full satisfaction. After freezing the final 385-study synthesis, we revalidated all 10 matrix systems and conducted a targeted sweep of 12 additional extraction/generalization/deployment near-misses. No candidate satisfied all six requirements together in one jointly evaluated end-to-end pipeline. We therefore retain only the scoped representative-system wording rather than an unrestricted universal claim.

## Completion checklist

- [x] six operational requirements fixed in G2;
- [x] YES/PARTIAL/NO/NR rules fixed;
- [x] 10 strongest representative systems coded;
- [x] final `N_SYNTH = 385` membership frozen;
- [x] all 10 G1 matrix records revalidated against final membership;
- [x] targeted final counterexample sweep completed;
- [x] 12 additional near-misses explicitly checked;
- [x] no full-contract counterexample found;
- [x] C1-11 wording retained only in scoped representative-system form;
- [x] final manuscript wording updated consistently.

**G1 final status: CLOSED.**