# Methodology and Versioning

## Authoritative corpus construction pipeline

| Stage | Description | Count |
|---|---|---:|
| 1 | Consolidated identification ledger | 3,462 |
| 2 | After initial normalization and residual deduplication | 3,455 |
| 3 | Excluded during screening / eligibility | 2,643 |
| 4 | Provisional P0–P3 inclusions | 812 |
| 5 | Post-inclusion reconciliation: six duplicate study representations + one non-study template artefact | −7 |
| 6 | **Final systematic-mapping corpus** | **805** |
| 7 | **Publication-eligible pool after full status/version audit** | **454** |
| 8 | Historical normalized-note / synthesis-candidate set | 403 |
| 9 | **Final qualitative synthesis** | **385** |

The four retained evidence layers serve different purposes. The 403-record historical note set is not the current publication-eligible pool. The final frozen counts are defined in `data/publication_status_corpus_freeze_summary.json` and `data/final_synthesis_statistics.json`.

## Search and discovery protocol

The final search-provenance audit is `docs/B1_B10_SEARCH_AND_SELECTION_AUDIT.md`.

### Recurring direct scholarly-search interfaces

The author-confirmed recurring direct-search interfaces were:

- Google Scholar / Scholar Labs
- Scopus
- Web of Science
- ScienceDirect
- SpringerLink
- IEEE Xplore
- ACM Digital Library
- Semantic Scholar
- DBLP
- OpenReview

Scopus, Web of Science, ScienceDirect, and SpringerLink were accessed through `eressources.imist.ma`. The review window was January 2017 through April 2026. Searches were repeated approximately monthly through the final April 2026 update, were restricted to English, and used the platforms' default/general search facilities rather than explicit title/abstract/keyword field restrictions.

### Verbatim historical Boolean strings

The first 152-page SLR preserves five Boolean strings verbatim. They are stored in `data/search_queries_historical.csv` and are treated as the historical query evidence rather than later future-update templates.

### Repository-assisted discovery

Curated GitHub repositories and community-maintained literature lists formed a separate discovery phase. A custom script harvested candidate titles from README files, Markdown tables, and structured lists, normalized/deduplicated them, resolved candidates against scholarly records, and retrieved metadata/full text where available. Repository-assisted discovery is not reported as a bibliographic database.

The May 2026 working SLR also listed arXiv, ACL Anthology, PMLR, and official venue pages under Phase 1. In the final audit, those services are retained as supplementary scholarly-resolution/version-verification channels because recurring direct-query logs for them were not separately recovered. This is an explicit reconciliation of the historical draft rather than a silent rewrite.

### Source-level preservation limits

Historical gross hit/export counts per individual source and exact day-level search timestamps were not recovered. The last supported search/update time is April 2026 at month-level granularity. The source-by-source disclosure is machine-readable in `data/search_source_reporting.csv`.

## Why the initial deduplication removed only seven rows

The 3,462-record figure is an ingestion-level **consolidated ledger**, not a raw sum of overlapping source hits. Before a newly found paper was added, the local database of already downloaded/registered papers was checked; an existing paper was skipped. DOI/arXiv identifiers and normalized bibliographic metadata were also used for consolidation.

Consequently, the `3,462 → 3,455` cleanup removed only seven residual duplicate/corrupted/non-usable rows that survived collection-time consolidation.

A **different** seven-row operation occurred after screening: the 812 provisional inclusions contained six duplicate study representations plus one non-study LaTeX-template artefact. Removing those produced the 805-study mapping corpus. The two seven-record steps occur at different stages and must not be conflated.

## Inclusion and exclusion rules

### Mapping layer

A record could enter the mapping corpus when it:

1. investigated an LLM/foundation-model agent, or an extraction/data method directly relevant to the agent pipeline;
2. addressed Web/browser/GUI/computer-use, extraction, benchmark/evaluation, reliability/generalization, security, or deployment questions;
3. fell within January 2017–April 2026, except for a small number of explicitly historical pre-2017 baselines;
4. was in English; and
5. provided sufficient accessible substantive content for thematic coding.

Excluded records included topically/temporally out-of-scope work, duplicate study representations, non-study artefacts, inaccessible or insufficiently substantive records, pure NLP work with no transferable agent/tool/Web relevance, unrelated generic benchmarks, and irrelevant security work. Classical rule-based extraction was retained only as a historical or technical baseline when directly relevant.

### Strict publication-eligible layer

The final publication-eligible layer applies an additional archival rule:

- archival journal articles, full conference papers, and formally accepted equivalents are eligible;
- preprint-only and non-archival workshop records are not eligible unless archival publication/formal acceptance is verified;
- books and monographs are excluded from the strict journal/conference layer even when archival, although they may remain in the mapping/background corpus;
- duplicate/version representations are merged and counted once.

Record 93 is the explicit machine-readable book/monograph example.

## Exclusion-ledger preservation

The repository does not synthesize missing historical exclusions. `data/exclusion_ledger_availability.csv` documents availability by stage.

Preserved: stage counts; 805-study mapping records; current publication-status decisions; strict-layer exclusion reasons; 454 publication-eligible freeze; 403 historical note/candidate records; 385 final synthesis membership and exclusion reasons.

Not recovered: the complete 2,643 P4 rows with one record-specific reason each, and individual identities for every row removed in the earliest 3,462→3,455 cleanup.

## Publication-status and version policy

The full 805-study corpus was reverified for publication status. A verifier flagged 297 records for manual adjudication; all 297 were resolved before the final freeze.

- **Canonical published metadata supersedes preprint metadata.**
- Where a journal/conference version exists, canonical title, venue, year, and identifiers come from that version.
- Preprints may remain in the mapping corpus for coverage/context but do not support strict publication-eligible claims unless a final publication/formal acceptance is verified.
- A preprint may be consulted for supplementary implementation details or experiments absent from the final venue version without being counted as an additional study.
- Duplicate/version records are merged under one study identity.
- Record IDs are stable.
- Missing full text or unresolved status remains visible as a block, not silently converted into an eligible record.

The final publication-eligible pool is **454** (P0 18, P1 110, P2 233, P3 93).

## Full-text assessment and priority classification

Priority is an evidence-use/analysis-depth classification, not a quality or risk-of-bias score.

| Tier | Criterion | Synthesis treatment |
|---|---|---|
| P0 | Cornerstone work defining scope, core method, or indispensable foundation | Deep critical full-text analysis |
| P1 | Direct evidence for a central architecture, method, benchmark, empirical result, or risk claim | Deep critical full-text analysis |
| P2 | Supporting/extending evidence informing a comparison, component, or adjacent design choice | Complete structured full-text reading |
| P3 | Historical/contextual/peripheral-but-relevant evidence within the synthesis boundary | Complete structured full-text reading |
| P4 | Outside the intended synthesis boundary or insufficiently connected | Excluded |

The final synthesis contains **385 studies**: 114 P0/P1 deep analyses and 271 P2/P3 complete structured readings.

## A1 evidence-status correction and closure

Earlier repository states blurred intended protocol and documented reading evidence. Reviewer-A1 remediation therefore required explicit paper-grounded verification rather than treating file existence or historical source matching as proof of reading.

The final A1 audit reports:

| A1 closure measure | Final state |
|---|---:|
| Historical live/candidate notes audited | 403 |
| Accessible records without current-cycle full-text verification | 0 |
| Reading TODO/template blocks | 0 |
| Full-text access exceptions | 1 |
| Final qualitative synthesis studies | 385 |

Record 249 is the sole full-text access exception and is excluded from the final synthesis rather than reconstructed from metadata/code.

The relevant artifacts are `data/a1_live_note_audit.csv`, `data/a1_fulltext_rechecks.csv`, `data/paper_note_audit.csv`, and `data/final_synthesis_membership.csv`.

## Reading-depth standard

For final-synthesis studies:

- **P0/P1:** full-text reading plus deep critical analysis of methods, evaluation design, quantitative/qualitative findings, limitations/boundary conditions, evidentiary role, and checked source locations.
- **P2/P3:** complete full-text reading plus structured synthesis of relevance, method, principal findings/benchmark properties, contribution, limitations, and evidence locations.

A generic summary, future-reading checklist, or publication metadata alone does not qualify.

## Historical paper-note provenance

The historical review archive contained 1,522 Markdown files, including standalone notes, merged section notes, duplicate stubs, and verification reports. The historical source-note audit found 335 reliable mappings resolving to 229 unique Markdown files. Those snapshots remain under `notes/historical_source_snapshots/` and the frozen provenance manifest.

The live one-paper-per-file layers contain 403 historical candidate records:

- `notes/papers/`
- `notes/original_sources/`

These 403 files are retained for provenance and audit continuity. They are not the current 454 publication-eligible pool and do not define the final 385-study synthesis.

## Reviewer process

Search validation, deduplication, screening, eligibility assessment, priority coding, thematic mapping, evidence extraction, and synthesis were conducted and cross-checked collaboratively by the primary reviewers. Decisions were reconciled through discussion.

**Independent parallel reviewer-decision matrices were not generated.** Consequently, no retrospective Cohen's kappa or other inter-rater reliability coefficient is claimed. Coauthors performed the final analytical audit; this is not described as an external independent recoding audit.

## Validation status

| Check | Status |
|---|---|
| 805 mapping records | ✅ Frozen |
| 454 publication-eligible studies | ✅ Frozen after full status/version adjudication |
| 403 historical normalized-note/candidate records | ✅ Preserved |
| 385 final-synthesis studies | ✅ Frozen |
| Final synthesis P0/P1 deep | ✅ 114 |
| Final synthesis P2/P3 structured | ✅ 271 |
| Historical Boolean strings | ✅ Verbatim Q1–Q5 preserved |
| Direct search sources | ✅ 10 author-confirmed recurring interfaces |
| Final search month | ✅ April 2026 |
| Language restriction | ✅ English only |
| Search-field restriction | ✅ Default/general field; no explicit title/abstract/keyword restriction |
| Gross per-source hit counts | ⚠️ Not recovered; explicitly disclosed |
| Complete 2,643-row P4 ledger | ⚠️ Not recovered; explicitly disclosed |

The repository does not infer or fabricate unavailable historical search/exclusion records.
