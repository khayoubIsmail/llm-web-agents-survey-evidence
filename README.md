<div align="center">

# Evidence Register for  
## LLM-Based Agents for Generalized Web Automation and Schema-Guided Data Extraction: A Survey

[![Mapping corpus: 805](https://img.shields.io/badge/Mapping%20Corpus-805-4c8cbf)](data/summary.json)
[![Publication eligible: 454](https://img.shields.io/badge/Publication--Eligible-454-2e7d32)](data/publication_status_corpus_freeze_summary.json)
[![Historical notes: 403](https://img.shields.io/badge/Historical%20Candidate%20Notes-403-success)](notes/papers/)
[![Final synthesis: 385](https://img.shields.io/badge/Final%20Synthesis-385-success)](data/final_synthesis_statistics.json)

**Companion evidence repository for the survey manuscript under revision for the International Journal of Data Science and Analytics.**

</div>

---

## Authoritative evidence layers

The repository intentionally distinguishes four different sets. They must not be conflated.

| Layer | Count | Meaning |
|---|---:|---|
| Identification ledger | 3,462 | Consolidated records entering the reported selection flow |
| After initial normalization/deduplication | 3,455 | Records entering screening |
| Provisional inclusions | 812 | P0–P3 before post-inclusion reconciliation |
| **Final systematic-mapping corpus** | **805** | Unique mapped studies |
| **Publication-eligible pool** | **454** | Archival published/accepted studies after final status/version audit |
| **Historical normalized-note / synthesis-candidate set** | **403** | Historical P0–P3 candidate set for which normalized notes were materialized |
| **Final qualitative synthesis** | **385** | Final claim-bearing synthesis after publication eligibility and full-text availability |

The frozen counts are defined in [`data/publication_status_corpus_freeze_summary.json`](data/publication_status_corpus_freeze_summary.json), [`data/final_synthesis_statistics.json`](data/final_synthesis_statistics.json), and [`data/summary.json`](data/summary.json).

### Priority counts

| Tier | Meaning | Mapping 805 | Publication-eligible 454 | Final synthesis 385 |
|---|---|---:|---:|---:|
| P0 | Cornerstone | 20 | 18 | 18 |
| P1 | Primary evidence | 179 | 110 | 96 |
| P2 | Supporting/extending evidence | 444 | 233 | 189 |
| P3 | Contextual/historical evidence | 162 | 93 | 82 |

Priority is an evidence-use and reading-depth classification, **not** a study-quality or risk-of-bias score.

## Search and selection reproducibility — B1–B10

Reviewer-2's search-reproducibility block is documented in:

- [`docs/B1_B10_SEARCH_AND_SELECTION_AUDIT.md`](docs/B1_B10_SEARCH_AND_SELECTION_AUDIT.md) — full evidence/provenance audit;
- [`data/search_queries_historical.csv`](data/search_queries_historical.csv) — five verbatim historically preserved Boolean strings;
- [`data/search_source_reporting.csv`](data/search_source_reporting.csv) — source-by-source search settings, last-search month, language/field restrictions, and unavailable-count disclosure;
- [`data/exclusion_ledger_availability.csv`](data/exclusion_ledger_availability.csv) — what exclusion evidence is and is not preserved;
- [`docs/B1_B10_MANUSCRIPT_PATCH.md`](docs/B1_B10_MANUSCRIPT_PATCH.md) — synchronized manuscript replacement text.

### Confirmed recurring direct-search interfaces

Google Scholar / Scholar Labs, Scopus, Web of Science, ScienceDirect, SpringerLink, IEEE Xplore, ACM Digital Library, Semantic Scholar, DBLP, and OpenReview.

Searches were refreshed approximately monthly through **April 2026**, restricted to **English**, and run through the platforms' **default/general search facilities** rather than title/abstract/keyword-specific fields.

Repository-assisted discovery from curated GitHub literature lists is reported separately from direct scholarly searching.

### Historical preservation limits

The repository does **not** fabricate information that was not preserved. In particular:

- gross per-source retrieval/export counts were not recovered;
- exact day-level timestamps for the final April 2026 source searches were not retained;
- the complete 2,643-row P4 record-level exclusion ledger has not been recovered.

The combined two-phase identification ledger is 3,462 records. It was already incrementally consolidated during collection, which explains why only seven residual duplicate/corrupt/non-usable rows were removed in the subsequent `3,462 → 3,455` cleanup.

## Publication-status and version audit

The full 805-study corpus was reverified for publication status. **297 records** were flagged for manual adjudication and all 297 were resolved. The frozen publication-eligible pool contains **454 studies**:

- P0: 18
- P1: 110
- P2: 233
- P3: 93

Version policy:

- a journal/conference published or formally accepted version supersedes preprint metadata;
- duplicate versions are merged under one study identity;
- preprints may remain in the mapping corpus but do not enter the strict publication-eligible layer unless an archival/final acceptance is verified;
- books/monographs are excluded from the strict journal/conference layer even when archival;
- missing or unresolved evidence remains visible rather than being silently upgraded.

See [`docs/METHODOLOGY_AND_VERSIONING.md`](docs/METHODOLOGY_AND_VERSIONING.md) and the `data/publication_status_*` artifacts.

## Full-text reading and synthesis depth

The final qualitative synthesis contains **385 studies**, all with documented full-text reading:

- **114 P0/P1** studies received deep critical analysis;
- **271 P2/P3** studies received complete structured reading.

The historical 403-note layer is retained for provenance. Eighteen historical candidates do not enter the final synthesis: 17 are not publication-eligible after final adjudication and one (record 249) is the full-text access exception.

The authoritative membership file is [`data/final_synthesis_membership.csv`](data/final_synthesis_membership.csv).

## Paper-specific evidence

The repository retains:

- `notes/papers/` — 403 normalized notes keyed to the historical candidate set;
- `notes/original_sources/` — 403 paper-specific synthesis-source files keyed by the same stable IDs;
- `notes/historical_source_snapshots/` — exact historical provenance snapshots;
- `data/a1_live_note_audit.csv` and `data/a1_fulltext_rechecks.csv` — current-cycle full-text verification evidence.

File existence alone is not treated as proof of reading; the explicit audit/verification ledgers determine evidence status.

## Claim-level and system-level audit artifacts

Important reviewer-remediation artifacts include:

| Artifact | Purpose |
|---|---|
| `data/c1_claim_evidence_matrix.csv` | Major claim → primary/corroborating/boundary studies and checked source locations |
| `data/g1_system_requirement_matrix.csv` | Representative systems × operational requirements |
| `data/g1_final_targeted_near_miss_sweep.csv` | Targeted counterexample/near-miss sweep |
| `data/g2_operational_definitions.csv` | Operational definitions and YES/PARTIAL/NO/NR rules |
| `data/d1_reviewer_process_claim_audit.csv` | Reviewer-process wording audit |
| `data/e1_evidence_weighting_claim_audit.csv` | Evidence-weighting claim audit |
| `data/e2_independent_audit_decision.csv` | Independent-audit disclosure |
| `data/a3_final_consistency_checks.csv` | Final corpus/manuscript consistency checks |

## Repository structure

```text
llm-web-agents-survey-evidence/
├── data/
│   ├── studies_805_mapping_corpus.{csv,json}
│   ├── publication_status_corpus_freeze_summary.json
│   ├── final_synthesis_membership.csv
│   ├── final_synthesis_statistics.json
│   ├── search_queries_historical.csv
│   ├── search_source_reporting.csv
│   ├── exclusion_ledger_availability.csv
│   ├── c1_claim_evidence_matrix.csv
│   ├── g1_system_requirement_matrix.csv
│   └── ...
├── docs/
│   ├── B1_B10_SEARCH_AND_SELECTION_AUDIT.md
│   ├── B1_B10_MANUSCRIPT_PATCH.md
│   ├── REVIEWER_2_FINAL_RESPONSE.md
│   ├── METHODOLOGY_AND_VERSIONING.md
│   ├── DATA_DICTIONARY.md
│   └── ...
├── notes/
│   ├── papers/
│   ├── original_sources/
│   └── historical_source_snapshots/
├── scripts/
├── CITATION.cff
└── LICENSE.md
```

## Full-text access exception

Record **249**, *Meta-Agent-Workflow: Streamlining Tool Usage in LLMs through Workflow Construction, Retrieval, and Refinement*, is retained for traceability but excluded from final qualitative synthesis because a complete verifiable full text could not be obtained. See [`docs/FULL_TEXT_ACCESS_EXCEPTIONS.md`](docs/FULL_TEXT_ACCESS_EXCEPTIONS.md).

## Citation

```bibtex
@dataset{khayoub2026evidenceregister,
  author    = {Khayoub, Ismail and Chadi, Mohamed-Amine and
               Mousannif, Hajar and {Ait Mohamed}, Firdaous},
  title     = {{Evidence Register for LLM-Based Agents for Generalized
                Web Automation and Schema-Guided Data Extraction: A Survey}},
  year      = {2026},
  publisher = {GitHub},
  url       = {https://github.com/khayoubIsmail/llm-web-agents-survey-evidence},
  license   = {CC BY 4.0}
}
```

## License

Repository-authored bibliographic metadata, review coding, documentation, and synthesis material are licensed under **CC BY 4.0**. This does not grant rights to third-party papers or publisher content. Third-party full-text PDFs are not redistributed.
