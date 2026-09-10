<div align="center">

# Evidence Register for<br>LLM-Based Agents for Generalized Web Automation<br>and Schema-Guided Data Extraction: A Survey

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightblue.svg)](https://creativecommons.org/licenses/by/4.0/)
[![Studies: 805](https://img.shields.io/badge/Mapping%20Corpus-805%20studies-4c8cbf)](data/summary.json)
[![Evidence Pool: 403](https://img.shields.io/badge/Published%2FAccepted%20Pool-403%20studies-2e7d32)](data/summary.json)
[![Paper notes: 403](https://img.shields.io/badge/Normalized%20Notes-403-success)](notes/papers/)
[![A1 status](https://img.shields.io/badge/A1%20Full--Text%20Audit-In%20Progress-orange)](data/a1_live_note_audit_summary.json)

**Companion evidence repository for the survey manuscript under revision for the International Journal of Data Science and Analytics.**

</div>

---

## About

This repository is the machine-readable and auditable evidence register supporting the survey:

> **Khayoub, I., Chadi, M.-A., Mousannif, H., & Ait Mohamed, F. (2026).**  
> *LLM-Based Agents for Generalized Web Automation and Schema-Guided Data Extraction: A Survey.*

It exposes the systematic-mapping corpus, the strict published/accepted evidence pool, paper-level notes, paper-specific synthesis sources, remediation provenance, historical source-note snapshots, and explicit access exceptions.

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
│   ├── paper_note_audit.csv
│   ├── a1_fulltext_rechecks.csv              # papers explicitly re-read in A1 cycle
│   ├── a1_live_note_audit.csv                # current 403-note remediation state
│   ├── a1_live_note_audit_summary.json       # current aggregate A1 status
│   ├── note_remediation_log.csv
│   └── historical_original_note_source_manifest.csv
├── notes/
│   ├── papers/                               # 403 live normalized paper notes
│   ├── original_sources/                     # 403 generated paper-specific source records
│   └── historical_source_snapshots/          # 229 exact historical source files
├── docs/
│   ├── A1_MANUSCRIPT_AND_RESPONSE_TEXT.md
│   ├── DATA_DICTIONARY.md
│   ├── FULL_TEXT_ACCESS_EXCEPTIONS.md
│   ├── METHODOLOGY_AND_VERSIONING.md
│   └── PAPER_SYNTHESIS_SOURCES.md
├── scripts/
│   ├── audit_a1_live_notes.py
│   ├── apply_a1_fulltext_rechecks.py
│   └── materialize_paper_synthesis_sources.py
├── CITATION.cff
├── LICENSE.md
└── README.md
```

## A1 remediation status — important

The repository is currently undergoing a **paper-by-paper A1 full-text remediation**. Earlier versions overstated the evidence state by describing historical source-note matches as if they established completed full-text reading for all accessible papers. The reviewer-facing audit showed that some live notes still contained prospective language such as `When reading this paper, extract...`, and many records still carried the status `existing review archive audited; no current-cycle PDF verification`.

Those conditions are now treated as **unresolved**, not as completed reading evidence. This repository therefore **does not currently claim that all 403 included papers have been independently re-read in the current A1 remediation cycle**.

The current status is generated from the live notes and should be read directly from:

- [`data/a1_live_note_audit_summary.json`](data/a1_live_note_audit_summary.json) — aggregate live state;
- [`data/a1_live_note_audit.csv`](data/a1_live_note_audit.csv) — one audit row per included paper;
- [`data/a1_fulltext_rechecks.csv`](data/a1_fulltext_rechecks.csv) — explicit log of papers actually re-read/reverified during the A1 remediation.

**Closure rule:** A1 is not closed until the live audit contains zero prospective reading-TODO/template blocks and zero unresolved `no current-cycle ... verification` records, except any explicitly documented full-text access exception.

## What counts as a remediated paper

A file being present in `notes/papers/` or `notes/original_sources/` does **not** by itself prove that the paper was read. A record moves out of the A1 remediation queue only when its live note contains evidence actually checked against the paper at the tier-appropriate depth.

For **P0/P1**, that means deep full-text critical analysis with concrete methods/results, limitations, evidentiary role, survey relevance, and evidence locations. For **P2/P3**, it means complete full-text reading with a structured synthesis of relevance, methodology, concrete results or benchmark properties where applicable, contributions, limitations, and evidence locations. Generic summaries and future-reading checklists do not qualify.

## 403 normalized notes + 403 paper-specific synthesis files

The repository exposes two one-to-one file layers:

- **`notes/papers/` — 403 live normalized notes**, one per published/accepted register record.
- **`notes/original_sources/` — 403 generated paper-specific synthesis-source files**, keyed by the same stable record IDs.

The second layer improves traceability but is generated from the live note corpus; it does not independently establish reading completion. When a live note is remediated from full text, the materialization workflow updates the corresponding paper-specific source file.

## Historical provenance

The historical note audit found **335 reliable title/source mappings** resolving to **229 unique Markdown files** because 20 historical files were shared/merged syntheses. Exact historical snapshots are retained under `notes/historical_source_snapshots/` and in the immutable provenance commit `83aca98913e2202d912778917ff7c5b92ff67399`.

Historical source-note matching establishes where prior review material came from; it **does not prove a current-cycle full-text reread**. This distinction is why the historical archive is kept separate from the current A1 reread ledger.

The earlier structural audit also identified 68 records without a reliable historical source-note match and performed a remediation pass based on independently retrieved/title-checked papers where available. Those historical counts remain reproducible, but the current A1 audit applies a stricter standard to all 403 live notes.

## Full-text access exception

**Record 249**, *Meta-Agent-Workflow: Streamlining Tool Usage in LLMs through Workflow Construction, Retrieval, and Refinement*, remains the explicit unresolved access exception. Publisher/bibliographic metadata and the authors' public implementation are available, but a complete verifiable manuscript has not been obtained. The record is therefore blocked from claim-level synthesis rather than reconstructed from metadata or code. See [`docs/FULL_TEXT_ACCESS_EXCEPTIONS.md`](docs/FULL_TEXT_ACCESS_EXCEPTIONS.md).

## Methodological intent

The intended review protocol classifies papers P0–P4 after full-text eligibility assessment. P4 records are excluded. P0/P1 are intended for deep critical reading; P2/P3 for complete full-text reading with lighter structured synthesis. Priority is an evidence-use/analysis-depth classification, not a risk-of-bias score.

Because the A1 audit found live evidence inconsistent with claiming that this protocol had been fully documented for every record, the repository now distinguishes **intended protocol**, **historical source provenance**, and **currently verified rereading evidence**. See [`docs/METHODOLOGY_AND_VERSIONING.md`](docs/METHODOLOGY_AND_VERSIONING.md).

## Key audit artifacts

| Artifact | Purpose |
|---|---|
| `data/a1_live_note_audit_summary.json` | Current aggregate A1 remediation state |
| `data/a1_live_note_audit.csv` | One current A1 status row per live paper note |
| `data/a1_fulltext_rechecks.csv` | Explicit ledger of papers actually re-read in the A1 cycle |
| `data/paper_note_audit.csv` | Paper-level provenance/full-text/claim-use state |
| `notes/papers/` | 403 canonical live notes |
| `notes/original_sources/` | 403 generated one-paper-per-file synthesis records |
| `notes/historical_source_snapshots/` | Exact historical provenance snapshots |
| `docs/FULL_TEXT_ACCESS_EXCEPTIONS.md` | Access-exception evidence and synthesis restriction |

## Validation status

| Check | Status |
|---|---|
| 805-study corpus unique IDs | ✅ 805 |
| Published/accepted pool | ✅ 403 |
| Normalized paper-note files | ✅ 403 |
| Generated paper-specific source files | ✅ 403 |
| Historical source mappings | ✅ 335 mappings → 229 exact files |
| Live TODO/template-free evidence corpus | 🔄 **A1 remediation in progress** |
| Current-cycle full-text verification for every accessible paper | 🔄 **A1 remediation in progress** |
| Full-text access exception | ⚠️ Record 249 blocked from claim-level use |

Do not infer A1 completion from the 403/403 file counts. **The generated A1 audit is authoritative for completion status.**

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

*Evidence register v1.2.0 · A1 evidence remediation active · CC BY 4.0*

</div>
