# B1–B10 Manuscript Patch

This file provides the reviewer-facing manuscript text that should replace/add to the current `sn-article.tex`. It is synchronized with `docs/B1_B10_SEARCH_AND_SELECTION_AUDIT.md` and the frozen 805/454/403/385 corpus counts.

## 1. Replace §2.2 — Information sources and discovery

```latex
\subsection{Information sources and discovery}

The collection combined two discovery phases. The recurring direct scholarly-search interfaces were Google Scholar (including the Scholar Labs interface), Scopus, Web of Science, ScienceDirect, SpringerLink, IEEE Xplore, ACM Digital Library, Semantic Scholar, DBLP, and OpenReview. Scopus, Web of Science, ScienceDirect, and SpringerLink were accessed through the IMIST e-resources portal. Searches covered January 2017 through April 2026, were restricted to English-language material, and were rerun approximately monthly through the final April 2026 update. Searches used each platform's default/general search facility rather than an explicit title-only, abstract-only, keyword-only, or fixed title--abstract--keyword field restriction.

The first SLR manuscript preserves five core Boolean strings verbatim:
\begin{enumerate}
\item \texttt{("LLM-based agent" OR "language agent" OR "AI agent") AND ("web automation" OR "browser automation" OR "web navigation")}
\item \texttt{("web scraping" OR "intelligent scraping" OR "web data extraction") AND (LLM OR agent OR "large language model")}
\item \texttt{("web agent" OR "browser agent") AND (benchmark OR evaluation OR dataset)}
\item \texttt{("GUI agent" OR "computer-use agent") AND (grounding OR screenshot OR DOM OR "accessibility tree")}
\item \texttt{("prompt injection" OR security OR robustness) AND ("web agent" OR "browser agent" OR "LLM agent")}
\end{enumerate}
The same core expressions/keywords were reused across the recurring searches without retrospectively adding database-specific field wrappers. Source-by-source reporting, including the last-search month and the fact that historical gross per-source result counts were not retained, is provided in the companion evidence repository.

The second phase was repository-assisted discovery. Candidate titles were harvested from curated GitHub repositories and community-maintained research lists focused on LLM agents, Web/GUI agents, computer-use agents, benchmarks, extraction, and security. Titles were normalized and deduplicated before being resolved against scholarly records. This discovery channel is reported separately from direct scholarly-database searching. ArXiv, ACL Anthology, PMLR, and official venue/publisher pages were also used for scholarly resolution, full-text/version discovery, and publication-status verification; an earlier working manuscript grouped them with Phase~1, but recurring direct-query logs for these interfaces were not retained, so the final audit reports them conservatively as supplementary discovery/verification channels.
```

## 2. Replace the first paragraph of §2.3 — Record management and selection

```latex
The final author-approved identification ledger contained 3,462 records. This number was already consolidated during collection rather than being the raw sum of hits from overlapping sources: before a newly found paper was added, the local database of already downloaded/registered papers was checked and an existing paper was skipped, and DOI/arXiv identifiers plus title/author metadata were used for consolidation. Initial normalization therefore removed only seven residual duplicate, corrupted, or otherwise non-usable rows, yielding 3,455 records for screening. Screening and eligibility assessment excluded 2,643 records and yielded 812 provisional inclusions. Post-inclusion reconciliation then identified a separate set of six duplicate study representations and one non-study LaTeX-template artifact; removing those seven rows produced the final analytical corpus of 805 unique studies (Fig.~\ref{fig:review-flow}). These two seven-record operations occur at different stages and should not be conflated.
```

## 3. Replace the eligibility paragraph in §2.3

```latex
Studies were eligible for the mapping corpus when they (i) investigated an LLM-based or foundation-model-based agent, or an extraction/data method directly relevant to the agent pipeline; (ii) addressed Web, browser, GUI, computer-use, extraction, benchmark/evaluation, reliability/generalization, security, or deployment questions; (iii) fell within the analytical time window, apart from a small number of explicitly historical baselines; (iv) were in English; and (v) provided sufficient accessible substantive content for thematic coding. We excluded records outside the topical or temporal scope, duplicate representations, non-study artefacts, and records without sufficient accessible content. Classical rule-based extraction was retained only where it established a historical or technical baseline.

The publication-eligible layer used for claim-bearing synthesis applied an additional archival rule. Archival journal articles, full conference papers, and formally accepted equivalents were eligible. Preprint-only and non-archival workshop records were excluded unless a final archival publication or formal acceptance was verified. Books and monographs were also excluded from this strict journal/conference layer even when archival, although they could remain in the broader mapping/background corpus. When multiple versions of one study existed, the published or formally accepted version superseded preprint metadata and duplicate versions were merged under one study identity; a preprint could still be consulted for supplementary implementation detail without being counted as a second study.
```

## 4. Add one reproducibility paragraph at the end of §2.3

```latex
The evidence repository exposes the verbatim historical Boolean strings, source-by-source search settings, version-handling rules, current publication-status adjudication, exclusion-availability map, and final synthesis membership. Historical gross retrieval/export counts for individual search sources and the complete record-level 2,643-row P4 exclusion ledger were not recovered. We therefore report the combined consolidated identification count (3,462) and the preserved stage counts, but do not reconstruct source-specific counts or missing exclusion rows retrospectively.
```

## 5. Replace Limitations item 4

Current text incorrectly says that reviewer-decision matrices “were not preserved,” which can imply that independent matrices once existed.

Use:

```latex
\item Review and coding decisions were reconciled collaboratively rather than generated as blinded independent rating sets. No reviewer outside the author team independently recoded a prespecified sample blind to the existing labels, and independent parallel reviewer-decision matrices were not generated; consequently, no retrospective inter-rater reliability coefficient is claimed.
```

## 6. Replace Limitations item 5

The historical Boolean strings have now been recovered, so the current statement that query-level detail is missing is too broad.

Use:

```latex
\item Historical gross retrieval/export counts by individual search source, exact day-level search timestamps, and the complete record-level ledger for the 2,643 P4 screening exclusions were not recovered. Searches were refreshed through April 2026 and the verbatim core Boolean strings are preserved, but these missing source-level records prevent a complete retrospective PRISMA-S reconstruction; the review is therefore described as PRISMA-informed.
```

## 7. Reviewer-facing status after this patch

- Exact historical core Boolean strings: **reported verbatim**.
- Direct search interfaces: **10 author-confirmed sources, explicitly listed**.
- Last search: **April 2026 for all recurring direct sources; exact day not retained**.
- Language: **English only**.
- Fields: **default/general search; no explicit title/abstract/keyword restriction**.
- Version handling: **explicit canonicalization and preprint/final rule**.
- Database vs repository-assisted discovery: **separated**.
- Low initial deduplication count: **explained by ingestion-time consolidation**.
- Per-source gross retrieval counts: **not recoverable; disclosed**.
- Complete 2,643-row P4 ledger: **not recoverable; disclosed**.
