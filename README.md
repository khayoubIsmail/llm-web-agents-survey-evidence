<div align="center">

# Evidence Register for<br>LLM-Based Agents for Generalized Web Automation<br>and Schema-Guided Data Extraction: A Survey

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightblue.svg)](https://creativecommons.org/licenses/by/4.0/)
[![Studies: 805](https://img.shields.io/badge/Mapping%20Corpus-805%20studies-4c8cbf)](data/summary.json)
[![Evidence Pool: 403](https://img.shields.io/badge/Published%2FAccepted%20Pool-403%20studies-2e7d32)](data/summary.json)
[![Paper notes: 403](https://img.shields.io/badge/Normalized%20Notes-403-success)](notes/papers/)
[![Synthesis sources: 403](https://img.shields.io/badge/Paper--Specific%20Sources-403-success)](notes/original_sources/)

**Companion evidence repository for the survey manuscript under revision for the International Journal of Data Science and Analytics.**

</div>

---

## About

This repository is the machine-readable and auditable evidence register supporting the survey:

> **Khayoub, I., Chadi, M.-A., Mousannif, H., & Ait Mohamed, F. (2026).**  
> *LLM-Based Agents for Generalized Web Automation and Schema-Guided Data Extraction: A Survey.*

It exposes the systematic-mapping corpus, the strict published/accepted evidence pool, paper-level reading notes, paper-specific synthesis sources, note-remediation provenance, historical note snapshots, and explicit access exceptions.

## Corpus at a glance

| Layer | Count |
|---|---:|
| Identification ledger | 3,462 |
| After normalization and deduplication | 3,455 |
| Provisional inclusions | 812 |
| **Final systematic-mapping corpus** | **805** |
| **Published/accepted citation-eligibility pool** | **403** |
| Strict pool exclusions after final validation | 3 |

### Priority tiers

| Tier | Meaning | Mapping (805) | Eligible (403) |
|---|---|---:|---:|
| P0 | Cornerstone | 20 | 18 |
| P1 | Primary evidence | 179 | 98 |
| P2 | Supporting/extending evidence | 444 | 204 |
| P3 | Contextual/historical evidence | 162 | 83 |

## Repository structure

```text
llm-web-agents-survey-evidence/
├── data/
│   ├── summary.json
│   ├── studies_805_mapping_corpus.{csv,json}
│   ├── studies_403_published_accepted_pool.{csv,json}
│   ├── records_excluded_from_strict_pool.csv
│   ├── bibliographic_patch_log.csv
│   ├── note_source_overrides.csv
│   ├── note_remediation_log.csv
│   ├── paper_note_audit.csv
│   └── historical_original_note_source_manifest.csv
├── notes/
│   ├── papers/                          # 403 normalized paper notes
│   ├── original_sources/                # 403 one-paper-per-file synthesis sources
│   └── historical_source_snapshots/     # 229 exact historical source files
├── docs/
│   ├── A1_MANUSCRIPT_AND_RESPONSE_TEXT.md
│   ├── DATA_DICTIONARY.md
│   ├── FULL_TEXT_ACCESS_EXCEPTIONS.md
│   ├── METHODOLOGY_AND_VERSIONING.md
│   └── PAPER_SYNTHESIS_SOURCES.md
├── scripts/
├── CITATION.cff
├── LICENSE.md
└── README.md
```

## 403 normalized notes + 403 paper-specific synthesis sources

The current release deliberately exposes two one-to-one paper-level layers:

- **`notes/papers/` — 403 normalized notes.** Exactly one canonical note for every record in the published/accepted pool.
- **`notes/original_sources/` — 403 paper-specific synthesis source records.** Exactly one source record for every one of the same 403 register IDs. The filenames match `notes/papers/` by stable record ID.

The synthesis-source files contain the detailed paper-specific analysis and provenance used by the audit. They are review artifacts, not copies of copyrighted publisher PDFs.

### Where the source material came from

The historical note audit found **335 reliable source-note mappings**. Those mappings originally resolved to only **229 unique Markdown files** because 20 historical files were merged syntheses covering 126 records. Release v1.2.0 separates the paper-specific synthesis layer from that historical storage layout so a reviewer can inspect one source record per paper without following merged multi-paper files.

**68 records had no reliable historical paper-specific source match.** They were selected for remediation rather than being assigned invented historical provenance. Where full text was obtainable, the paper was independently retrieved, extracted, title-checked, and synthesized; current-cycle page counts, SHA-256 hashes, and title-similarity evidence are recorded in `data/paper_note_audit.csv`. Across the audit, **134 papers** received current-cycle PDF verification.

The repository documents full-text analysis for **402 of the 403 records**. **Record 249** (*Meta-Agent-Workflow: Streamlining Tool Usage in LLMs through Workflow Construction, Retrieval, and Refinement*) remains the sole access exception. It is publication-eligible for traceability but blocked from claim-level synthesis until a complete paper copy is obtained. The 403rd source file records that exception rather than fabricating a full-text reading. See `docs/FULL_TEXT_ACCESS_EXCEPTIONS.md`.

## Historical provenance

The byte-for-byte historical Markdown sources from the previous provenance release are retained under `notes/historical_source_snapshots/`. The frozen historical mapping is `data/historical_original_note_source_manifest.csv`:

- 335 register records with reliable historical source mappings;
- 229 unique historical source files;
- 20 shared/merged historical files;
- 126 records represented within those shared files.

The exact v1.1.1 provenance state is permanently recoverable at commit `83aca98913e2202d912778917ff7c5b92ff67399`.

## Reading protocol

Candidate studies underwent an initial full-text assessment for eligibility and P0–P4 priority classification. P4 records were excluded as peripheral/out of scope. All accessible P0–P3 papers in the 403-study pool were then read in full at tier-appropriate depth:

- **P0/P1:** deep critical analysis and detailed methods/results/limitations/evidence notes.
- **P2/P3:** complete full-text reading with lighter structured analysis focused on relevance, method, results, contributions, and limitations.

Priority governs analytical depth and evidence use; it is not a risk-of-bias or publication-quality score. See `docs/METHODOLOGY_AND_VERSIONING.md`.

## Key audit artifacts

| Artifact | Purpose |
|---|---|
| `data/paper_note_audit.csv` | One provenance/full-text/claim-use row per included paper |
| `data/note_remediation_log.csv` | 71 notes created or replaced during remediation |
| `notes/papers/` | 403 canonical normalized notes |
| `notes/original_sources/` | 403 one-paper-per-file synthesis-source records |
| `notes/historical_source_snapshots/` | Exact historical provenance snapshots |
| `docs/PAPER_SYNTHESIS_SOURCES.md` | Semantics of the new 403-file source layer |
| `docs/FULL_TEXT_ACCESS_EXCEPTIONS.md` | Record 249 retrieval history and synthesis restriction |

## Validation summary — v1.2.0

| Check | Result |
|---|---|
| 805-study corpus unique IDs | ✅ 805 |
| Published/accepted pool | ✅ 403 |
| Normalized paper notes | ✅ 403 |
| Paper-specific synthesis-source records | ✅ 403 |
| Historical source mappings | ✅ 335 mappings → 229 exact files |
| Current-cycle PDF checks | ✅ 134 |
| Documented full-text analyses | ✅ 402 |
| Full-text access exceptions | ⚠️ 1 — record 249, blocked from claim-level use |

## Citation

```bibtex
@dataset{khayoub2026evidenceregister,
  author    = {Khayoub, Ismail and Chadi, Mohamed-Amine and
               Mousannif, Hajar and {Ait Mohamed}, Firdaous},
  title     = {{Evidence Register for LLM-Based Agents for Generalized
                Web Automation and Schema-Guided Data Extraction: A Survey}},
  year      = {2026},
  version   = {1.2.0},
  publisher = {GitHub},
  url       = {https://github.com/khayoubIsmail/llm-web-agents-survey-evidence},
  license   = {CC BY 4.0}
}
```

## License

Repository-authored bibliographic metadata, review coding, documentation, and synthesis material are licensed under **CC BY 4.0**. This license does not apply to third-party papers or other material for which the repository authors do not hold copyright. No publisher full-text PDFs are redistributed.

---

<div align="center">

*Evidence register v1.2.0 · Released 2026-09-10 · CC BY 4.0*

</div>
