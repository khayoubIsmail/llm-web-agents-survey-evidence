<div align="center">

# Evidence Register for<br>LLM-Based Agents for Generalized Web Automation<br>and Schema-Guided Data Extraction: A Survey

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightblue.svg)](https://creativecommons.org/licenses/by/4.0/)
[![Studies: 805](https://img.shields.io/badge/Mapping%20Corpus-805%20studies-4c8cbf)](data/summary.json)
[![Evidence Pool: 403](https://img.shields.io/badge/Published%2FAccepted%20Pool-403%20studies-2e7d32)](data/summary.json)
[![Paper notes: 403](https://img.shields.io/badge/Normalized%20Notes-403-success)](notes/papers/)
[![A1 status](https://img.shields.io/badge/A1%20Full--Text%20Audit-Complete-success)](data/a1_live_note_audit_summary.json)

**Companion evidence repository for the survey manuscript under revision for the International Journal of Data Science and Analytics.**

</div>

---

## About

This repository is the machine-readable and auditable evidence register supporting the survey:

> **Khayoub, I., Chadi, M.-A., Mousannif, H., & Ait Mohamed, F. (2026).**  
> *LLM-Based Agents for Generalized Web Automation and Schema-Guided Data Extraction: A Survey.*

It exposes the systematic-mapping corpus, the strict citation-eligibility pool, paper-level notes, paper-specific synthesis sources, current-cycle full-text verification, remediation provenance, historical source-note snapshots, and explicit exceptions.

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
│   ├── a1_fulltext_rechecks.csv              # explicit A1 reread/reverification ledger
│   ├── a1_live_note_audit.csv                # one current A1 row per live paper note
│   ├── a1_live_note_audit_summary.json       # aggregate A1 closure check
│   ├── a1_evidence_batches/                  # paper-grounded remediation evidence
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
│   ├── apply_a1_evidence_batches.py
│   ├── apply_a1_fulltext_rechecks.py
│   └── materialize_paper_synthesis_sources.py
├── CITATION.cff
├── LICENSE.md
└── README.md
```

## A1 full-text remediation — completed 2026-09-11

The A1 remediation is complete under the repository's conservative reviewer-facing closure rule. Earlier repository states contained prospective language such as `When reading this paper, extract...` and historical records labeled `existing review archive audited; no current-cycle PDF verification`. Those states were not treated as evidence of completed reading.

The live corpus was remediated paper by paper. A record was moved out of the A1 queue only after its paper-specific methods/evaluation/results or benchmark properties, limitations, evidentiary role, and relevant evidence locations had been checked against a complete paper source at tier-appropriate depth. Historical source-note matching or file existence alone never counted as a reread.

The generated final audit in [`data/a1_live_note_audit_summary.json`](data/a1_live_note_audit_summary.json) reports:

| A1 closure check | Final state |
|---|---:|
| Live notes audited | **403** |
| Exact `When reading this paper...` TODOs | **0** |
| Generic evidence-template blocks | **0** |
| Accessible records without current-cycle full-text verification | **0** |
| Records still requiring A1 full-text remediation | **0** |
| Full-text access exceptions | **1** |

Accordingly, **402 accessible included records have documented current-cycle full-text analysis/verification**. **Record 249 is the sole full-text access exception** and remains blocked from claim-level synthesis. The repository does **not** claim that all 403 were read in full.

The authoritative A1 artifacts are:

- [`data/a1_live_note_audit_summary.json`](data/a1_live_note_audit_summary.json) — final aggregate closure state;
- [`data/a1_live_note_audit.csv`](data/a1_live_note_audit.csv) — one audit row per included paper;
- [`data/a1_fulltext_rechecks.csv`](data/a1_fulltext_rechecks.csv) — explicit reread/reverification ledger;
- [`data/a1_evidence_batches/`](data/a1_evidence_batches/) — paper-specific evidence used to replace incomplete live templates;
- [`data/paper_note_audit.csv`](data/paper_note_audit.csv) — provenance, full-text status, and claim-use state.

## What counts as a verified paper

A file being present in `notes/papers/` or `notes/original_sources/` does **not** by itself prove that the paper was read. Current-cycle verification requires paper-grounded evidence at the tier-specific standard.

For **P0/P1**, the standard is deep full-text critical analysis with concrete methods/results, limitations, evidentiary role, survey relevance, and evidence locations. For **P2/P3**, the standard is complete full-text reading with structured synthesis of relevance, methodology, concrete results or benchmark properties where applicable, contributions, limitations, and evidence locations. Generic summaries and future-reading checklists do not qualify.

## 403 normalized notes + 403 paper-specific synthesis files

The repository exposes two one-to-one file layers:

- **`notes/papers/` — 403 live normalized notes**, one per register record.
- **`notes/original_sources/` — 403 generated paper-specific synthesis-source files**, keyed by the same stable record IDs.

The second layer is generated from the live notes to improve traceability. It is not treated as independent proof of reading; A1 completion is determined by the explicit verification ledger and live-note audit.

## Historical provenance

The historical note audit found **335 reliable title/source mappings** resolving to **229 unique Markdown files** because 20 historical files were shared/merged syntheses. Exact historical snapshots are retained under `notes/historical_source_snapshots/` and in the immutable provenance commit `83aca98913e2202d912778917ff7c5b92ff67399`.

Historical source-note matching establishes where prior review material came from; it does **not** prove a current-cycle full-text reread. This distinction is why the historical archive is kept separate from the current A1 verification evidence.

The earlier structural audit also identified 68 records without a reliable historical source-note match and performed an initial remediation pass. Those historical counts remain reproducible, but A1 closure is based on the stricter final 403-note audit above.

## Full-text access exception

**Record 249**, *Meta-Agent-Workflow: Streamlining Tool Usage in LLMs through Workflow Construction, Retrieval, and Refinement*, remains the sole full-text access exception. Publisher/bibliographic metadata and the authors' public implementation are available, but a complete verifiable manuscript has not been obtained after renewed publisher, bibliographic, repository, exact-title, preprint, and author searches. The record is retained for traceability but blocked from claim-level synthesis rather than reconstructed from metadata or code. See [`docs/FULL_TEXT_ACCESS_EXCEPTIONS.md`](docs/FULL_TEXT_ACCESS_EXCEPTIONS.md).

## Separate publication-status revalidation flags

Records **323** and **419** were read and verified from complete available paper versions during A1, so they are **not** full-text access exceptions. Their claim-use status is separately blocked pending publication-status revalidation. This is a bibliographic/citation-eligibility issue, not an A1 reading-completeness issue, and it is reported separately in `data/summary.json`.

## Methodological protocol

Candidate studies are classified P0–P4 after full-text eligibility assessment. P4 records are excluded. P0/P1 receive deep critical reading; P2/P3 receive complete full-text reading with lighter structured synthesis. Priority is an evidence-use/analysis-depth classification, not a risk-of-bias score.

The A1 audit was introduced specifically to prevent the intended protocol from being reported as completed unless the live evidence trail supports it. See [`docs/METHODOLOGY_AND_VERSIONING.md`](docs/METHODOLOGY_AND_VERSIONING.md).

## Key audit artifacts

| Artifact | Purpose |
|---|---|
| `data/a1_live_note_audit_summary.json` | Final aggregate A1 closure state |
| `data/a1_live_note_audit.csv` | One final A1 status row per live paper note |
| `data/a1_fulltext_rechecks.csv` | Explicit current-cycle reread/reverification ledger |
| `data/a1_evidence_batches/` | Paper-grounded evidence used in remediation |
| `data/paper_note_audit.csv` | Paper-level provenance/full-text/claim-use state |
| `notes/papers/` | 403 canonical live notes |
| `notes/original_sources/` | 403 generated one-paper-per-file synthesis records |
| `notes/historical_source_snapshots/` | Exact historical provenance snapshots |
| `docs/FULL_TEXT_ACCESS_EXCEPTIONS.md` | Record 249 retrieval attempts and synthesis restriction |

## Validation status

| Check | Status |
|---|---|
| 805-study corpus unique IDs | ✅ 805 |
| Published/accepted pool | ✅ 403 register records |
| Normalized paper-note files | ✅ 403 |
| Generated paper-specific source files | ✅ 403 |
| Historical source mappings | ✅ 335 mappings → 229 exact files |
| Live TODO/template-free evidence corpus | ✅ **0 TODOs / 0 template blocks** |
| Current-cycle full-text verification for every accessible paper | ✅ **402/402 accessible records** |
| Full-text access exception | ⚠️ **Record 249 only; blocked from claim-level use** |
| Publication-status revalidation | ⚠️ Records **323 and 419** separately blocked pending revalidation |

The generated A1 audit is authoritative for reading-completeness status.

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

*Evidence register v1.2.0 · A1 full-text remediation complete · CC BY 4.0*

</div>
