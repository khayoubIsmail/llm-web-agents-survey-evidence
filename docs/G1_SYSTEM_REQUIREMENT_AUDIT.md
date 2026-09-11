# G1 — System × Requirement Audit for the Complete Extraction Contract

## Status

**Current-cycle G1 matrix complete for the strongest representative counterexample candidates. Final closure is pending final `N_SYNTH` membership revalidation after publication-status adjudication.**

G1 tests the manuscript's central absence claim using the operational definitions frozen in `docs/G2_OPERATIONAL_DEFINITIONS.md`.

The claim under test is:

> Under the operational definitions used in our system-level comparison, none of the representative reviewed systems jointly demonstrates unfamiliar-site navigation, explicit schema coverage, field-level provenance, unsupported-value control, cross-site transfer, and complete dataset assembly in one evaluated end-to-end pipeline.

This is deliberately narrower than an absolute statement about all systems in existence.

## Coding rule

Each system is coded independently on:

1. unfamiliar-site navigation;
2. explicit schema coverage;
3. field-level provenance;
4. unsupported-value control;
5. cross-site transfer;
6. complete dataset assembly; and
7. joint evaluation.

Allowed values are `YES`, `PARTIAL`, `NO`, and `NR` exactly as defined in G2.

Critical rules:

- `NR` is not treated as `NO`.
- `PARTIAL` is not upgraded to `YES` because a capability appears plausible.
- a system closes the contract only if all six capability columns are `YES` **and** `joint_evaluation = YES`.
- benchmark-level or literature-level composition across different systems does not count as joint evaluation.

## Why these candidates were selected

The matrix intentionally tests the strongest plausible counterexamples from distinct parts of the reviewed literature rather than filling rows with obviously irrelevant papers.

### Navigation/generalist-agent side

- **SeeAct (282):** strong live-Web multimodal browser interaction and cross-site/domain evidence.
- **MindAct / Mind2Web (337):** explicit cross-website and cross-domain generalization protocol.
- **WebArena GPT-4 baseline (338):** realistic executable long-horizon Web interaction with functional validators.

### Structured/extraction side

- **AutoScraper (661):** reusable site-level scraper synthesis and multi-page executability.
- **SCRIBES (667):** RL-trained reusable extraction scripts with holdout grouping.
- **OneKE (675):** explicit schema-guided multi-agent extraction and reflection.

### Multi-source / continuous aggregation side

- **INFOGENT (663):** Navigator–Extractor–Aggregator with multi-source Web access.
- **WiNELL (692):** continuous Web search, citation-aware updates, and human review.

### Structured workflow / executable-evaluation side

- **Spider2-V (379):** executable data-science/engineering workflows across 20 enterprise applications.
- **DAAgent / InfiAgent-DABench (430):** execution-grounded structured outputs with machine-checkable evaluation.

Together these candidates challenge the absence claim from the strongest nearby capability families: live navigation, cross-site generalization, schema-guided extraction, reusable scripts, multi-source aggregation, continuous updating, structured workflows, and executable validation.

## Current result

The machine-readable audit is in:

- `data/g1_system_requirement_matrix.csv`

No current candidate is coded `YES` on all six capability requirements plus `YES` on joint evaluation.

The pattern is consistent but asymmetric:

- **Navigation-heavy systems** such as SeeAct and INFOGENT can explore the Web, but do not jointly provide explicit extraction schemas, field-level provenance, unsupported-value control, and complete dataset assembly.
- **Extraction-heavy systems** such as AutoScraper, SCRIBES, and OneKE provide structured extraction or reusable scripts, but do not jointly demonstrate unfamiliar-site navigation, field-level provenance, unsupported-value control, cross-site transfer, and complete dataset assembly.
- **Structured workflow/evaluation systems** such as Spider2-V and InfiAgent-DABench improve executable workflows and machine-checkable outputs, but are not end-to-end generalized Web extraction systems.
- **WiNELL** is a strong near-miss for source-aware continuous updating, but its unit of output is article/update-level rather than a schema-bound multi-record dataset with field-level provenance.

Therefore the current evidence supports the **scoped representative-system wording** above, but not an unrestricted universal statement such as “no system does this.”

## Important near-miss readings

### SeeAct

SeeAct provides a strong test of the navigation side. Its live-Web results and cross-website/domain evaluation justify `YES` for unfamiliar-site navigation and cross-site transfer, but its task is browser action generation/grounding rather than structured dataset extraction. It therefore does not close the schema/provenance/unsupported-value/dataset requirements.

Checked locations: Figure 1; Sections 2.1–2.3; Tables 2–4; online evaluation; error analysis; impact statement.

### AutoScraper

AutoScraper provides a strong test from the extraction side. Reusable XPath/action sequences operate across multiple pages of a site, so the matrix gives partial credit for schema/provenance-like structure and dataset behavior. However, the paper does not demonstrate arbitrary unfamiliar-site navigation, held-out cross-site transfer, audited field-level evidence binding, unsupported-value control, or complete collection assembly with coverage/deduplication.

Checked locations: Figures 1–2; SWDE/Extended-SWDE/DS1 experiments; executability metric; Table 6; error analysis; limitations.

### SCRIBES

SCRIBES is one of the strongest counterexamples because it learns reusable scripts and reports holdout grouping. G1 therefore records `PARTIAL`, not `NO`, for cross-site transfer. The remaining gap is that its transfer is tied to structurally similar groups, while field-level provenance, unsupported-value gating, unfamiliar-site navigation, and complete dataset assembly are not jointly demonstrated.

Checked locations: Figure 1; SemiBench/grouped-page evaluation; Table 1; Table 4; holdout grouping; CommonCrawl pipeline; limitations.

### OneKE

OneKE is explicitly schema-guided and includes a Reflection Agent. G1 therefore avoids coding the extraction side as absent. It still falls below the stricter G2 thresholds because the available evidence does not establish schema coverage/completeness tracking, field-level source binding, or field-specific unsupported-value control, and it does not evaluate generalized live-Web navigation or complete dataset assembly.

Checked locations: Schema/Extraction/Reflection agents; NER/RE evaluations; Web-news/PDF cases; deployment design; limitations.

### INFOGENT

INFOGENT directly challenges the navigation + multi-source part of the claim. It receives `YES` for unfamiliar-site navigation because its Navigator explores multiple sources under direct and interactive visual access. Its evaluated output, however, is answer-level aggregation rather than schema-bound rows with field-level provenance and collection-completeness guarantees.

Checked locations: Figure 1; FRAMES/AssistantBench experiments; component/action analysis; qualitative errors; limitations.

### WiNELL

WiNELL contributes continuous source discovery, citation-aware editing, section-specific criteria, and human review. G1 treats these as meaningful `PARTIAL` analogues of schema/provenance/unsupported-value control rather than dismissing them. It does not, however, assemble a multi-record dataset or establish field-level provenance and cross-site transfer under the G2 definitions.

Checked locations: section-criteria induction; agentic update aggregation; fine-grained editing; historical evaluation; findings; limitations.

## What G1 does not prove yet

A green G1 structural check does **not** mean the universal claim is permanently closed.

Final closure requires:

1. publication-status adjudication to finish;
2. final `N_SYNTH` membership to be frozen;
3. every G1 candidate record to be revalidated against final membership;
4. a final high-risk counterexample sweep of the synthesis set to ensure no plausible system family was omitted;
5. any newly included near-miss system to be coded using the same frozen G2 rules;
6. C1-11 wording to remain scoped to the representative reviewed systems.

If a system is found with `YES` on all six capability requirements and `YES` on joint evaluation, C1-11 must be revised or removed.

## Manuscript wording if final G1 remains unchanged

> Under the operational definitions used in our system-level comparison, none of the representative reviewed systems jointly demonstrates unfamiliar-site navigation, explicit schema coverage, field-level provenance, unsupported-value control, cross-site transfer, and complete dataset assembly in one evaluated end-to-end pipeline.

## Reviewer-response wording

> We agree that the previous absence claim required explicit system-level evidence rather than a narrative comparison. We therefore introduced operational definitions for the disputed requirements and coded the strongest representative counterexample systems in a system-by-requirement matrix using four states (YES, PARTIAL, NO, NR). Missing reporting was not treated as evidence of absence, and partial capabilities were not upgraded to full satisfaction. The resulting matrix shows that the reviewed systems cover many components individually, but none of the representative systems currently satisfies all six requirements together in one evaluated end-to-end pipeline. We consequently narrowed the manuscript wording to the representative reviewed systems under the published operational definitions rather than making an unrestricted universal claim. The matrix and checked source locations are provided in the evidence repository.

## Final completion criterion

G1 is finally closed only after final `N_SYNTH` is frozen and the candidate matrix has been revalidated against it. Until then, the current result is **methodologically complete but membership-pending**.
