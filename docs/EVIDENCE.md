# Evidence files

The repository keeps the evidence needed to check the main claims in the survey.

## Paper-level notes

`notes/papers/` and `notes/original_sources/` contain the paper-specific notes used during the review. Final claim use should be checked against `data/final_synthesis_membership.csv`.

## Claim-level evidence

`data/c1_claim_evidence_matrix.csv` links the main manuscript claims to supporting studies, corroborating or boundary evidence, and the source locations that were checked.

## System-level gap claim

`data/g1_system_requirement_matrix.csv` checks representative systems against six requirements:

1. unfamiliar-site navigation,
2. explicit schema coverage,
3. field-level provenance,
4. unsupported-value control,
5. cross-site transfer,
6. complete dataset assembly.

`data/g1_near_miss_sweep.csv` records additional systems checked as possible counterexamples. The definitions used for YES, PARTIAL, NO, and NR are in `data/g2_operational_definitions.csv`.

The manuscript therefore makes a scoped claim: under these definitions, none of the representative reviewed systems demonstrates all six requirements together in one evaluated end-to-end pipeline.

## Search and publication evidence

The search files, publication-status checks, exclusion records, and final corpus membership are all under `data/`. The purpose of this repository is to make the final counts and major synthesis claims inspectable without requiring readers to reconstruct the internal revision workflow.
