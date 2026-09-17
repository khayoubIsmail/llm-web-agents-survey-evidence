# LLM Web Agents Survey — Evidence and Experiment

This repository contains the evidence used for the survey **LLM-Based Agents for Generalized Web Automation and Schema-Guided Data Extraction** and the controlled wireless-headphones experiment added during revision.

The repository is kept intentionally small. It contains the final evidence files, paper notes, the formal provenance schema, and the experiment needed to check the main empirical claims. Internal revision queues, temporary scripts, caches, workflow files, smoke tests, and debugging artifacts are not part of this cleaned version.

## Final corpus

The review uses four different evidence layers:

| Layer | Count |
|---|---:|
| Mapping corpus | 805 |
| Publication-eligible pool | 454 |
| Historical P0–P3 candidate/note set | 403 |
| Final qualitative synthesis | 386 |

The 403-note set is historical. It yielded 385 retained synthesis studies after publication-status reconciliation and the documented full-text access exception. During revision, Record 760 (`A Survey on Trustworthy LLM Agents: Threats and Countermeasures`, KDD 2025) was re-adjudicated from the existing 454-study publication-eligible pool into the synthesis after complete full-text review, giving the final count of 386. This scope correction does not change the 805 mapping corpus, 454 publication-eligible pool, or historical 403-record set.

Among the 386 final synthesis studies:

- 114 P0/P1 studies received deep critical analysis.
- 272 P2/P3 studies received complete structured reading.

Priority controls analytical depth and evidentiary role. It is not a study-quality or risk-of-bias score.

## Repository layout

```text
data/               final corpus, search, publication, and claim-level evidence
notes/              historical notes plus the documented revision-stage scope addition
docs/               short description of the review method and evidence structure
schemas/            formal field-level evidence-object schema
IJDSA_experiment/   code, frozen inputs, 108 runs, and scored results
```

## Main evidence files

Start with these files:

- `data/studies_805_mapping_corpus.csv`
- `data/final_synthesis_membership.csv`
- `data/final_synthesis_revision_additions.csv`
- `data/reviewer_scope_readjudication.csv`
- `data/publication_status_verification.csv`
- `data/search_queries_historical.csv`
- `data/search_source_reporting.csv`
- `data/c1_claim_evidence_matrix.csv`
- `data/g1_system_requirement_matrix.csv`
- `data/g2_operational_definitions.csv`
- `data/doi_audit_386.csv`

`docs/METHOD.md` explains the review process in plain terms. `docs/EVIDENCE.md` explains how the main claims map to the released files.
The completed 386-record DOI audit is summarized in `docs/DOI_AUDIT_386_FINAL.md`.

## Paper notes

`notes/papers/` and `notes/original_sources/` preserve the 403 historical candidate-note records. Record 760 is additionally documented as `0760.md` in both directories because it was moved into the final synthesis during revision-stage scope re-adjudication. The note directories therefore contain 404 paper-specific files: 403 historical candidate records plus one transparent revision addition.

The pre-revision 385-study membership is preserved in `data/final_synthesis_membership.csv`. The effective final 386-study synthesis is the union of that file and `data/final_synthesis_revision_additions.csv`. This preserves the historical audit trail instead of silently rewriting the earlier freeze.

## Experiment

`IJDSA_experiment/` contains the complete controlled experiment used in the revised manuscript:

- 3 agent architectures,
- 3 model backends,
- 4 frozen commerce sites,
- 3 repetitions,
- 108 completed and scored runs.

The strongest observed configuration in this controlled study was A1 + Kimi with macro Field F1 0.9440. The experiment is a controlled illustration of the evaluation framework, not a general model or architecture ranking.

See `IJDSA_experiment/docs/PROTOCOL.md` and `IJDSA_experiment/docs/RESULTS.md` for the design and results.

## Known historical limits

Some early search records were not preserved at full detail. The repository therefore does not reconstruct them after the fact. In particular, gross retrieval counts for each search source, exact day-level dates for the final April 2026 searches, and the complete 2,643-row screening-exclusion ledger are unavailable. The available stage counts and final record-level evidence are kept in `data/`.

## Citation

Please cite the survey manuscript and this repository when using the released review data or experiment.

## License

Repository-authored review metadata, coding, documentation, and synthesis material are released under CC BY 4.0 as described in `LICENSE.md`. Third-party papers and publisher content are not redistributed.
