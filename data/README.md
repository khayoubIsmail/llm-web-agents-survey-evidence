# Data files

This folder contains the files used to support the survey results.

## Corpus

- `studies_805_mapping_corpus.csv` — the full 805-study mapping corpus.
- `historical_403_candidates.csv` — the historical P0–P3 candidate set used to build the original note collection.
- `final_synthesis_membership.csv` — the preserved pre-revision 385-study synthesis membership derived from the historical candidate set.
- `final_synthesis_revision_additions.csv` — revision-stage scope additions to that preserved base membership; currently Record 760 only.
- `reviewer_scope_readjudication.csv` — rationale and provenance for the scope correction.
- `corpus_statistics_final.csv` and `final_synthesis_statistics.json` — final 386-study counts used in the revised manuscript.

The effective final synthesis is the union of `final_synthesis_membership.csv` and `final_synthesis_revision_additions.csv`. The split is intentional: it preserves the earlier 385-study freeze and makes the reviewer-driven scope re-adjudication auditable instead of silently rewriting history.

## Search and selection

- `search_queries_historical.csv` — the five preserved Boolean search strings.
- `search_source_reporting.csv` — search sources, search settings, and the last search month.
- `exclusion_ledger_availability.csv` — what historical exclusion data is and is not available, including the revision-stage addition.
- `records_excluded_from_strict_pool.csv` — records excluded when the strict publication rule was applied.

## Publication status

- `publication_status_verification.csv` — final publication-status verification across the mapping corpus.
- `publication_status_manual_adjudication.csv` — manual decisions for records that needed checking.
- `publication_status_corpus_freeze_summary.json` — the September 13 publication-status freeze plus an explicit post-freeze scope-re-adjudication addendum.

## DOI audit

- `doi_audit_386.csv` — completed row-level DOI audit for all 386 synthesis records.
- `doi_audit_386_summary.json` — audit totals and integrity checks.
- `doi_title_map_386.json` — compact title-to-DOI/status map.
- `doi_audit_386_manual_decisions.csv` — 26 official-source edge-case decisions.

The completed audit identifies 249 records with a verified archival DOI and 137
without one as of September 16, 2026. It has no unresolved rows or duplicate
final DOIs. See `docs/DOI_AUDIT_386_FINAL.md` for the method and corrections.

## Reading and evidence

- `paper_note_audit.csv` — historical audit rows for the original paper-note set.
- `a1_fulltext_rechecks.csv` — historical full-text recheck log.
- `a1_reading_tier_summary.json` — reading-depth summary with the revision addition recorded separately.
- `c1_claim_evidence_matrix.csv` — major manuscript claims and the studies/source locations that support them.
- `g1_system_requirement_matrix.csv` — representative systems checked against the six extraction requirements.
- `g1_near_miss_sweep.csv` — additional systems checked as possible counterexamples.
- `g2_operational_definitions.csv` — definitions used for YES/PARTIAL/NO/NR coding.
- `a3_final_consistency_checks.csv` — final consistency checks after the 386-study scope correction.

These are the final evidence files. Temporary queues, checkpoints, caches, and intermediate patch files are intentionally not kept in the cleaned repository.
