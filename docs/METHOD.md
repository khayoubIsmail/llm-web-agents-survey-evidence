# Review method

This file gives the short version of the review process used in the final manuscript.

## Search

The literature search ran from January 2017 through April 2026. The recurring direct-search interfaces were Google Scholar / Scholar Labs, Scopus, Web of Science, ScienceDirect, SpringerLink, IEEE Xplore, ACM Digital Library, Semantic Scholar, DBLP, and OpenReview.

Five Boolean search strings are preserved in `data/search_queries_historical.csv`. Searches were run through the platforms' default/general search interfaces and were limited to English-language material.

Repository-assisted discovery and later version checks were kept separate from the recurring direct searches. Details are in `data/search_source_reporting.csv`.

Three historical items were not preserved at full granularity: gross hit counts for each source, exact day-level dates for the final April 2026 searches, and the complete 2,643-row record-level exclusion ledger. These gaps are reported directly rather than reconstructed.

## Evidence layers

The final review uses four different sets:

- 805 studies in the mapping corpus.
- 454 studies in the publication-eligible pool.
- 403 records in the historical P0–P3 candidate/note set.
- 386 studies in the final qualitative synthesis.

The historical 403-record set yielded 385 retained synthesis studies after publication-status reconciliation and one documented full-text access exception. During revision, Record 760 was re-adjudicated for scope from the already-existing 454-study publication-eligible pool and added after complete full-text review. This changed the final synthesis from 385 to 386 without changing the search, mapping corpus, publication-eligible pool, or historical 403-record set.

## Publication status

Publication status was checked across the 805-study mapping corpus. Records that needed manual checking were adjudicated against publisher, proceedings, OpenReview, Crossref, or other authoritative bibliographic evidence. The final status files are in `data/publication_status_verification.csv` and `data/publication_status_manual_adjudication.csv`.

A published or formally accepted journal/conference version replaces earlier preprint metadata for the strict evidence layer. Preprint-only and non-archival works may still appear as background but do not enter the strict publication-eligible pool. Books and monographs are outside the strict journal/conference layer.

Record 760 was already verified as an archival KDD 2025 publication and already belonged to the publication-eligible pool. Its revision-stage change is therefore a scope-coding correction, not a publication-status upgrade or a new search result. The decision is documented in `data/reviewer_scope_readjudication.csv`.

## Reading and notes

All 386 studies in the final qualitative synthesis have documented full-text reading.

- 114 P0/P1 studies received deep critical analysis.
- 272 P2/P3 studies received complete structured reading.

Priority controls analytical depth and evidentiary role. It is not a study-quality score or a risk-of-bias score.

Record 249 is kept for traceability but excluded from the final qualitative synthesis because a complete verifiable full text could not be obtained. Record 760 has a new normalized note and synthesis-source file (`notes/papers/0760.md` and `notes/original_sources/0760.md`).

## Reviewer process

Screening and coding were collaborative. Separate blinded decision matrices were not produced, so no retrospective inter-rater coefficient is reported.

Evidence strength was judged qualitatively from the paper-level notes and source checks. No numerical study-quality or risk-of-bias score was created after the fact.
