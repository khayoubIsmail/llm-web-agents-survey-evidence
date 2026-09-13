# B1–B10 Search, Selection, and Deduplication Audit

**Review:** *LLM-Based Agents for Generalized Web Automation and Schema-Guided Data Extraction: A Survey*  
**Audit date:** 2026-09-13  
**Purpose:** Reviewer-2 search-reproducibility remediation.

This document records what can be supported by preserved historical material, the current evidence repository, and explicit author confirmation. It deliberately distinguishes **verbatim preserved evidence**, **author-confirmed historical procedure**, **current-cycle audit evidence**, and **information that is no longer recoverable**. Missing historical data are not back-filled with synthetic values.

## Evidence provenance used in this audit

1. **Verbatim historical manuscript evidence.** The first 152-page SLR version dated 2026-05-24 preserves the five Boolean strings under “Representative Boolean queries included,” the two-phase collection design, the 2017–April 2026 window, the 3,462-record combined identification count, and the original version-handling rule.
2. **Author-confirmed historical procedure (2026-09-13).** The recurring direct-search interfaces, monthly refresh through April 2026, English-only restriction, use of default/general search rather than title/abstract/keyword-specific fields, and ingestion-time local-database duplicate check were explicitly reconfirmed.
3. **Current repository audit.** Publication-status adjudication, canonical version handling, duplicate/version exclusions, the 805/454/403/385 evidence layers, and strict publication-type exclusions are machine-readable in the current repository.
4. **Unavailable historical detail.** Gross per-source hit/export counts, exact day-level search dates, and the complete record-level 2,643-row P4 exclusion ledger have not been recovered. They are reported as unavailable rather than reconstructed.

## B1 — Historical search strings

The following are the **verbatim historically preserved core Boolean strings** from the first SLR. They are not later reconstructed templates.

```text
Q1
("LLM-based agent" OR "language agent" OR "AI agent")
AND
("web automation" OR "browser automation" OR "web navigation")
```

```text
Q2
("web scraping" OR "intelligent scraping" OR "web data extraction")
AND
(LLM OR agent OR "large language model")
```

```text
Q3
("web agent" OR "browser agent")
AND
(benchmark OR evaluation OR dataset)
```

```text
Q4
("GUI agent" OR "computer-use agent")
AND
(grounding OR screenshot OR DOM OR "accessibility tree")
```

```text
Q5
("prompt injection" OR security OR robustness)
AND
("web agent" OR "browser agent" OR "LLM agent")
```

Machine-readable copy: [`../data/search_queries_historical.csv`](../data/search_queries_historical.csv).

The author confirms that these search expressions/keywords were reused across the recurring searches. The searches were entered through each platform's **default/general search interface**. No source-specific field wrapper such as Scopus `TITLE-ABS-KEY(...)` or Web of Science `TS=(...)` is claimed because no such field restriction was used.

## B2 — Search/update date by source

The search was refreshed approximately monthly over the review period, with the **last literature-search/update month in April 2026**. The April 2026 pass also checked whether newer archival versions of already identified papers had appeared.

The exact calendar day for each source was not retained. The auditable date is therefore `2026-04 (day not retained)` rather than an invented day-level timestamp.

See [`../data/search_source_reporting.csv`](../data/search_source_reporting.csv).

## B3 — Records retrieved by database/source

The combined two-phase collection produced an **identification ledger of 3,462 records**. Historical gross hit/export counts for each individual source were not preserved.

This matters because 3,462 is **not the raw arithmetic sum of all database result pages**. Candidate records were consolidated during collection: before adding a paper, the local database of already downloaded/registered studies was checked and existing papers were skipped; preserved later methodology also records DOI/arXiv-identifier merging at collection time. Therefore source-by-source gross retrieval counts cannot be reconstructed reliably from the final 805-study register or from publication venue metadata.

For that reason, `gross_records_retrieved` is explicitly `NR` (not recoverable) in `data/search_source_reporting.csv`. No per-source counts are inferred or fabricated.

## B4 — Language restriction

The recurring literature search and screening were restricted to **English-language material**. The historical inclusion criteria likewise required work to be written in English with sufficient metadata/content for assessment.

## B5 — Search-field restriction

The author confirms that searches were run mainly through each platform's **default/general search field**. The workflow did **not** deliberately restrict queries to title-only, abstract-only, keywords-only, or a fixed title+abstract+keywords field combination.

Consequently, the reproducibility record reports the actual interface-level practice rather than retroactively translating the strings into source-specific field syntax.

## B6 — Preprint, updated-version, and final-version handling

The collection/mapping layer could contain preprints and other non-archival versions so that fast-moving work was not lost. When multiple versions of one study existed:

- the record was treated as one underlying study rather than counted repeatedly;
- a peer-reviewed/published or formally accepted journal/conference version was preferred as the canonical version when available;
- canonical published metadata superseded preprint metadata;
- an arXiv/preprint version could still be consulted for supplementary implementation detail or experiments absent from the archival version, but it did not become an additional study;
- preprint-only and non-archival records did not enter the strict publication-eligible layer unless an archival publication or formal acceptance was verified.

The final publication-status audit manually adjudicated all flagged status/version cases and freezes the current publication-eligible pool at **454 studies**.

## B7 — Identification and exclusion ledger

The current repository exposes all exclusion evidence that remains recoverable, but it does **not** pretend that the complete historical 2,643-row P4 ledger can be regenerated.

What is preserved:

- stage-level counts for `3,462 → 3,455 → 812 → 805`;
- the reconciled 805-study mapping register;
- publication-status and version adjudication records for the 805-study corpus;
- final exclusion-reason fields where applicable;
- the publication-eligible pool freeze (`N_POOL = 454`);
- the historical 403-record note/candidate layer;
- final synthesis membership (`N_SYNTH = 385`) and its 18 exclusions;
- explicit strict-layer exclusions and special cases.

What has **not** been recovered:

- the complete 2,643 individual P4 rows with one record-specific exclusion reason each;
- record-level identities for every item removed in the earliest `3,462 → 3,455` cleanup.

The first SLR states that screening exclusions were assigned P4 and recorded with a brief reason, but those complete historical rows are not present in the current public repository. We therefore disclose this as a preservation limitation rather than create synthetic exclusion records.

Availability map: [`../data/exclusion_ledger_availability.csv`](../data/exclusion_ledger_availability.csv).

## B8 — Explicit inclusion and exclusion rules

### Mapping-corpus inclusion boundary

A record was eligible for mapping when it:

1. investigated an LLM/foundation-model agent, or an extraction/data method directly relevant to the agent pipeline;
2. addressed Web/browser/GUI/computer-use, extraction, benchmark/evaluation, reliability/generalization, security, or deployment questions;
3. fell within the January 2017–April 2026 analytical window, except for a small number of explicitly historical pre-2017 baselines;
4. was in English; and
5. provided sufficient accessible substantive content for thematic coding.

Classical rule-based extraction was retained only when it established a historical or technical baseline relevant to the generalized extraction problem.

### Mapping-corpus exclusion boundary

Records were excluded from the mapping/synthesis boundary when they were topically or temporally out of scope, duplicate representations of another study, non-study artefacts, inaccessible/insufficiently substantive for assessment, pure non-agent NLP with no transferable relevance, unrelated non-Web/non-GUI work, unrelated generic benchmarks, or security work without relevant LLM/agent/Web/tool-use connection.

### Strict publication-eligible layer

The later claim-bearing publication layer applies an additional archival-publication rule: **archival journal articles, full conference papers, and formally accepted equivalents are eligible; preprint-only/non-archival workshop records are not. Books and monographs are also excluded from this strict journal/conference layer even when archival**, although they may remain in the wider mapping/background corpus. Record 93 is the explicit machine-readable example of the book/monograph rule.

## B9 — Database search versus repository-assisted discovery

The final audit distinguishes three channels.

### A. Recurring direct scholarly-search interfaces — author confirmed

1. Google Scholar / Scholar Labs
2. Scopus
3. Web of Science
4. ScienceDirect
5. SpringerLink
6. IEEE Xplore
7. ACM Digital Library
8. Semantic Scholar
9. DBLP
10. OpenReview

Scopus, Web of Science, ScienceDirect, and SpringerLink were accessed through `eressources.imist.ma`; IEEE Xplore, ACM Digital Library, and Semantic Scholar were searched directly; Google Scholar was also used through its Scholar Labs interface.

### B. Repository-assisted discovery — separate Phase 2

Curated GitHub repositories/community-maintained literature lists were harvested for candidate paper titles. A custom script extracted titles from README files, Markdown tables, and structured lists, normalized/deduplicated them, and resolved candidates against scholarly records. This was a **discovery channel**, not a bibliographic database search.

### C. Supplementary scholarly resolution/version verification

The May 2026 SLR draft also grouped arXiv, ACL Anthology, PMLR, and official venue pages with Phase 1. In the final audit, recurring direct-query use of those interfaces has not been separately reconfirmed with logs, while their use for scholarly resolution, full-text/version discovery, and publication-status verification is well supported. They are therefore conservatively reported as supplementary discovery/verification channels rather than silently promoted to the author-confirmed recurring direct-search list.

This explicit reconciliation preserves the historical draft while preventing an unsupported claim about source-specific recurring query execution.

## B10 — Why only seven records were removed at the initial deduplication step

The `3,462` figure represents an **already consolidated identification ledger**, not the raw combined hit count from overlapping databases.

The workflow performed incremental duplicate avoidance during collection:

1. before a newly found paper was added, the local database of already downloaded/registered papers was checked;
2. if the paper was already present, it was skipped rather than appended again;
3. DOI and arXiv identifiers, plus title/author metadata, were used for record consolidation;
4. the later `3,462 → 3,455` step therefore removed only **seven residual duplicate, corrupted, or otherwise non-usable rows** that survived ingestion-level consolidation.

A separate later reconciliation occurs after the 812 provisional inclusions: **six duplicate study representations plus one non-study LaTeX-template artefact** were removed to obtain the final 805-study mapping corpus. These are different seven-record operations and should not be conflated.

## Current evidence layers

| Layer | Count | Meaning |
|---|---:|---|
| Identification ledger | 3,462 | Consolidated records entering reported selection flow |
| After initial normalization/deduplication | 3,455 | Screening input |
| Provisional inclusions | 812 | P0–P3 before post-inclusion reconciliation |
| Final systematic-mapping corpus | 805 | Unique mapped studies |
| Publication-eligible pool | 454 | Archival published/accepted studies after full status audit |
| Historical normalized-note / synthesis-candidate set | 403 | Historical P0–P3 note set retained for provenance |
| Final qualitative synthesis | 385 | Publication-eligible + verified full-text synthesis membership |

## Residual methodological limitations

Four historical items remain unavailable at the requested granularity:

- gross per-source retrieval/export counts;
- exact calendar day of the final April 2026 search for each source;
- complete record-level identities/reasons for all 2,643 historical P4 exclusions;
- recurring direct-query logs sufficient to classify arXiv, ACL Anthology, and PMLR identically to the ten author-confirmed recurring direct-search interfaces.

These gaps should remain visible in the reviewer response and limitations section. They are preferable to retrospective fabrication.
