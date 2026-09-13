# Final Response to Reviewer 2

We thank the reviewer for requesting stronger methodological transparency and tighter evidence traceability. We performed a corpus-level remediation rather than only revising the prose. The evidence repository now contains paper-specific notes, publication-status adjudication, claim-to-source traceability, operational definitions, system-level comparison matrices, final consistency checks, and a dedicated search/selection audit.

## B1–B10 — Search reproducibility, source reporting, selection, and deduplication

We re-audited the earliest preserved SLR manuscript, later manuscript versions, the current repository, and the author's original search workflow. The new authoritative audit is `docs/B1_B10_SEARCH_AND_SELECTION_AUDIT.md`, with machine-readable support in `data/search_queries_historical.csv`, `data/search_source_reporting.csv`, and `data/exclusion_ledger_availability.csv`.

### B1 — Search strings

The first 152-page SLR preserves five Boolean strings verbatim under “Representative Boolean queries included.” We now expose those historical strings directly rather than replacing them with later reconstructed/future-update templates:

1. `("LLM-based agent" OR "language agent" OR "AI agent") AND ("web automation" OR "browser automation" OR "web navigation")`
2. `("web scraping" OR "intelligent scraping" OR "web data extraction") AND (LLM OR agent OR "large language model")`
3. `("web agent" OR "browser agent") AND (benchmark OR evaluation OR dataset)`
4. `("GUI agent" OR "computer-use agent") AND (grounding OR screenshot OR DOM OR "accessibility tree")`
5. `("prompt injection" OR security OR robustness) AND ("web agent" OR "browser agent" OR "LLM agent")`

The author confirms that the recurring searches reused these expressions/keywords through each platform's default/general search interface. We do not invent database-specific field wrappers that were not used.

### B2 — Last search/update date

The searches were refreshed approximately monthly, with the final literature-search/update month in **April 2026**. The April 2026 pass also checked for newer archival/final versions of papers. Exact day-level timestamps were not retained and are not fabricated.

### B3 — Records retrieved per source

The combined two-phase process produced a **3,462-record consolidated identification ledger**. Gross hit/export counts by individual search source were not preserved and cannot be reconstructed reliably from the final corpus, because duplicate avoidance already occurred during ingestion. We therefore report these source-level counts as `NR` rather than infer them from publication venues or canonical links.

### B4 — Language restriction

The search/screening scope was **English only**.

### B5 — Search fields

The searches used the platforms' **default/general search fields**. They were not intentionally restricted to title-only, abstract-only, keywords-only, or a fixed title+abstract+keywords combination.

### B6 — Preprint/final-version handling

The mapping layer could contain preprints so that fast-moving work was not lost, but versions of the same work were canonicalized as one study. A published or formally accepted journal/conference version superseded preprint metadata when available. Preprint-only and non-archival records did not enter the strict publication-eligible layer unless archival publication/formal acceptance was verified. Preprints could still be consulted for supplementary implementation detail without being counted as a second study. The full status audit freezes the publication-eligible pool at **454 studies**.

### B7 — Identification/exclusion ledger

We expose all exclusion evidence that remains recoverable, including stage counts, the 805-study register, publication-status adjudication, strict-layer exclusion reasons, and final 385-study synthesis membership. However, the complete historical **2,643-row P4 record-level exclusion ledger** and row identities for every item removed in the earliest `3,462 → 3,455` cleanup have not been recovered in the current repository. We state this limitation explicitly and do not manufacture missing rows.

### B8 — Inclusion/exclusion rules

The repository now states the mapping-corpus topical, temporal, language, accessibility, duplication, and substantive-content rules explicitly. It also makes the later strict publication rule explicit: archival journal articles, full conference papers, and formally accepted equivalents are eligible for the claim-bearing publication layer; preprint-only/non-archival workshop records are not; **books and monographs are excluded from the strict journal/conference layer even when archival**, though they may remain in the wider mapping/background corpus.

### B9 — Direct database search versus repository-assisted discovery

The author-confirmed recurring direct-search interfaces are:

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

Repository-assisted discovery from curated GitHub literature lists is now reported separately as Phase 2. The May 2026 draft also grouped arXiv, ACL Anthology, PMLR, and official venue pages with Phase 1; because recurring direct-query logs for those additional interfaces were not separately recovered in the current audit, the final reporting conservatively identifies them as supplementary scholarly resolution/version-verification channels rather than silently treating them as confirmed recurring direct-search interfaces.

### B10 — Why only seven records were removed initially

The **3,462 records were already an ingestion-level consolidated ledger**, not a raw sum of overlapping database hits. Before adding a newly found paper, the local database of already downloaded/registered papers was checked and an existing paper was skipped; DOI/arXiv identifiers and bibliographic metadata were also used for consolidation. The later `3,462 → 3,455` operation therefore removed only seven residual duplicate/corrupted/non-usable rows. A separate post-inclusion reconciliation removed six duplicate study representations plus one non-study LaTeX-template artefact from the 812 provisional inclusions to obtain the 805-study mapping corpus. We now distinguish these two seven-record operations explicitly.

### Residual reproducibility limitations

We do not claim complete retrospective PRISMA-S reconstruction. Three requested historical details remain unavailable at full granularity: gross per-source retrieval counts, exact day-level timestamps for the April 2026 final searches, and the complete 2,643-row P4 record-level exclusion ledger. These limitations are now stated directly rather than obscured.

## A1/A2 — Full-text reading and analytical depth

The historical synthesis-candidate set contained 403 P0–P3 records. Final publication-status adjudication removed 17 candidates from synthesis eligibility, and one otherwise eligible P3 study (record 249) remained unavailable as a complete verifiable full text. The final qualitative synthesis therefore contains **385 studies**, all with documented full-text reading. **114 P0/P1 studies** received deep critical analysis and **271 P2/P3 studies** received complete structured reading. Priority determines analytical depth and evidentiary role; it is not a quality or risk-of-bias score.

## Publication-status verification and final counts

We reverified publication status across the complete **805-study mapping corpus**. The verifier flagged **297 records** for manual review because of possible upgrades, downgrades, venue mismatches, missing venues, or unresolved matches; all 297 were manually adjudicated against authoritative publisher/proceedings evidence. This produced a final publication-eligible pool of **454 archival published or accepted studies**. The manuscript now distinguishes **805 mapping records**, **454 publication-eligible records**, the **403-record historical synthesis-candidate set**, and the **385-study final qualitative synthesis**. Figure 1 and corpus statistics were rebuilt from these frozen sets.

## D1 — Reviewer process and agreement

We removed wording that could imply blinded independent coding. The primary reviewers worked collaboratively, cross-checked evidence, and reconciled disagreements through discussion. **Independent parallel reviewer-decision matrices were not generated**, so we do not report Cohen's kappa or another retrospective inter-rater reliability coefficient.

## E1 — Evidence weighting / risk of bias

We did not apply a numerical study-quality or risk-of-bias score. Evidence strength was judged qualitatively and holistically using the paper-level notes: empirical findings, limitations/boundary conditions, relevance to the review question, publication-status context, and traceability to supporting source locations. These considerations informed synthesis judgment but were not scored as a separate appraisal instrument.

## E2 — Independent audit

We do not present a post-hoc author check as an independent audit. Coauthors performed a final analytical audit of the reconciled corpus, taxonomy, gap synthesis, and evidential support. The limitations explicitly state that no reviewer outside the author team independently recoded a prespecified sample blind to the existing labels.

## C1 — Claim-to-study-to-source traceability

We created a machine-readable matrix for **11 load-bearing claims**, recording primary studies, corroboration, independent boundary/counter-direction evidence, quantitative evidence where applicable, checked source locations, and evidence strength. After the final corpus freeze, all C1 study IDs were revalidated against the 385-study synthesis. OmniParser (record 443) was removed from C1-02 corroboration because it is outside the final synthesis.

## G2/G1 — Operational definitions and the system-level gap claim

The six requirements are operationally defined: unfamiliar-site navigation, explicit schema coverage, field-level provenance, unsupported-value control, cross-site transfer, and complete dataset assembly. YES, PARTIAL, NO, and NR are kept distinct. We revalidated the 10 representative systems and performed a targeted sweep of 12 additional extraction/generalization/deployment near-misses. No candidate jointly satisfies all six requirements in one evaluated end-to-end pipeline. We therefore retain only the scoped wording:

> Under the operational definitions used in our system-level comparison, none of the representative reviewed systems jointly demonstrates unfamiliar-site navigation, explicit schema coverage, field-level provenance, unsupported-value control, cross-site transfer, and complete dataset assembly in one evaluated end-to-end pipeline.

This is a representative-system conclusion, not a universal claim over every possible system.

## A3 — Final consistency audit and figures

The final synthesis contains **377 published and 8 accepted studies**. Its priority distribution is **18 P0, 96 P1, 189 P2, and 82 P3**. **359/385 (93.2%)** were published from 2023 onward, including 66 studies coded for the partial 2026 publication year. Figure 2 was regenerated and its thematic bars sum exactly to **385**. Old final-count statements based on 403/402 studies and the historical 116/286 split were removed or explicitly relabeled as historical candidate-set information.

## Final evidence sets

- Mapping corpus: **805**.
- Publication-eligible pool: **454**.
- Historical synthesis-candidate / normalized-note set: **403**.
- Final qualitative synthesis: **385**.
- Deep critical analysis: **114** P0/P1 studies.
- Complete structured reading: **271** P2/P3 studies.

These revisions make the review procedure, evidence boundaries, corpus counts, main gap claims, and remaining historical preservation limits directly auditable from the manuscript and public evidence repository.
