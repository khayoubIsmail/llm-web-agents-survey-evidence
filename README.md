<div align="center">

# Evidence Register for<br>LLM-Based Agents for Generalized Web Automation<br>and Schema-Guided Data Extraction: A Survey

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightblue.svg)](https://creativecommons.org/licenses/by/4.0/)
[![Studies: 805](https://img.shields.io/badge/Mapping%20Corpus-805%20studies-4c8cbf)](data/summary.json)
[![Evidence Pool: 403](https://img.shields.io/badge/Published%2FAccepted%20Pool-403%20studies-2e7d32)](data/summary.json)
[![Checksums: verified](https://img.shields.io/badge/SHA--256%20Checksums-Verified-success)](data/summary.json)

**Companion data repository for the survey manuscript submitted to the World Wide Web (WWW) conference.**

</div>

---

## 📋 About

This repository is the **evidence register** — the machine-readable, auditable corpus — that underpins all empirical claims made in the survey:

> **Khayoub, I., Chadi, M.-A., Mousannif, H., & Ait Mohamed, F. (2026).**  
> *LLM-Based Agents for Generalized Web Automation and Schema-Guided Data Extraction: A Survey.*  
> Submitted to the World Wide Web (WWW) Journal.

It provides full transparency into the study selection pipeline, evidence-use tiers, publication-status verification, and strict exclusion decisions, enabling readers and reviewers to independently audit every citation in the manuscript.

---

## 📊 Corpus at a Glance

| Layer | Count |
|---|---|
| Identification ledger (author-approved) | 3,462 |
| After normalization & deduplication | 3,455 |
| Excluded during screening / eligibility | 2,643 |
| Provisional inclusions | 812 |
| Post-inclusion reconciliation (duplicates / artifacts removed) | −7 |
| **Final systematic-mapping corpus** | **805** |
| Published / accepted citation-eligibility pool | **403** |
| Strict pool exclusions after final validation | 3 |

### Priority tier distribution

| Tier | Meaning | Mapping (805) | Eligible (403) |
|---|---|---|---|
| **P0** | Cornerstone — directly defines scope or method | 20 | 18 |
| **P1** | Primary — directly cited for a specific claim | 179 | 98 |
| **P2** | Supporting / extending — cited for context or comparison | 444 | 204 |
| **P3** | Peripheral / historical / recency context | 162 | 83 |

### Publication status (mapping corpus)

| Status category | Count |
|---|---|
| Archival published | 374 |
| Preprint / technical report | 367 |
| Workshop / conditional | 12 |
| Archival accepted | 29 |
| Unconfirmed / other | 23 |

---

## 🗂️ Repository Structure

```
llm-web-agents-survey-evidence/
│
├── data/
│   ├── summary.json                              # Corpus totals and category counts
│   ├── studies_805_mapping_corpus.csv            # Full 805-study reconciled corpus
│   ├── studies_805_mapping_corpus.json           # JSON equivalent
│   ├── studies_403_published_accepted_pool.csv   # 403 citation-eligible studies
│   ├── studies_403_published_accepted_pool.json  # JSON equivalent
│   ├── records_excluded_from_strict_pool.csv     # 3 strict exclusions (IDs: 432, 656, 686)
│   └── bibliographic_patch_log.csv               # Bibliographic correction audit log
│
├── docs/
│   ├── DATA_DICTIONARY.md                        # Field definitions for all CSV/JSON columns
│   └── METHODOLOGY_AND_VERSIONING.md             # Screening pipeline, reading depth, version policy
│
├── CITATION.cff                                  # Machine-readable citation metadata (CFF 1.2.0)
├── LICENSE.md                                    # CC BY 4.0
└── README.md                                     # This file
```

---

## 🔍 Data Files

### `data/studies_805_mapping_corpus.{csv,json}`
The **complete systematic-mapping corpus** of 805 unique studies. Every study that passed eligibility screening is represented here regardless of publication status — including preprints and workshop papers. This file is the authoritative source for all mapping claims in the manuscript.

### `data/studies_403_published_accepted_pool.{csv,json}`
The **strict citation-eligibility subset**: 403 studies confirmed as archival-published or formally accepted for publication. These are the only records eligible to support direct, citeable empirical claims in the final manuscript. This pool is a proper subset of the 805-study corpus.

### `data/records_excluded_from_strict_pool.csv`
Three records retained in the broader mapping landscape but removed from the strict published/accepted pool after final validation:

| Record ID | Exclusion reason |
|---|---|
| 432 | Could not confirm archival published / accepted status |
| 656 | Could not confirm archival published / accepted status |
| 686 | Could not confirm archival published / accepted status |

### `data/bibliographic_patch_log.csv`
Audit log of all bibliographic corrections applied after the initial screening round — including title normalizations, venue canonicalizations, year corrections, and identifier updates. Provides a full traceable history of metadata changes.

### `data/summary.json`
Machine-readable totals and category counts. Validated and committed directly. All SHA-256 checksums for the corpus files pass independently.

---

## 📖 Field Definitions

See [`docs/DATA_DICTIONARY.md`](docs/DATA_DICTIONARY.md) for full field-by-field definitions. Key fields:

| Field | Description |
|---|---|
| `record_id` | Stable integer ID within the 805-study corpus |
| `priority` | Evidence tier: P0 / P1 / P2 / P3 (not a risk-of-bias score) |
| `publication_status` | Full verified status (published, accepted, preprint, workshop, etc.) |
| `status_category` | Normalized category used in summary statistics |
| `bibliography_eligibility` | Whether record enters the strict 403 pool |
| `identifier` | DOI, OpenReview URL, arXiv ID, or other canonical identifier |
| `verification_source` | Audit trail for the metadata/status confirmation |

---

## ⚙️ Methodology Summary

The corpus was built through a **seven-stage pipeline**:

```
3,462 candidate records (author-approved ledger)
  └─ Normalization & deduplication ──► 3,455
       └─ Screening & eligibility ────► 812 provisional inclusions
            └─ Post-inclusion audit ──► 805 final unique studies
                 └─ Status verification ► 403 published/accepted pool
                      └─ Strict exclusions ► 3 records removed
```

P0/P1 studies received in-depth reading (methods, results, limitations, relevance). P2/P3 studies received rapid targeted reading. Screening, eligibility, coding, evidence extraction, and synthesis were conducted by **Ismail Khayoub** and **Firdaous Ait Mohamed**, cross-checked for consistency. **Mohamed-Amine Chadi** and **Hajar Mousannif** performed final analytical verification and audit.

See [`docs/METHODOLOGY_AND_VERSIONING.md`](docs/METHODOLOGY_AND_VERSIONING.md) for the full protocol.

---

## 🏷️ Validation Summary

All release artifacts were independently validated before this commit:

| Check | Result |
|---|---|
| 805-study corpus — record count | ✅ 805 unique IDs, no duplicates |
| 403-pool — subset of 805 | ✅ Fully contained within the 805-study corpus |
| Strict exclusions count | ✅ Exactly 3 (records 432, 656, 686) |
| CSV ↔ JSON identifier agreement | ✅ All IDs match |
| Duplicate record IDs | ✅ None |
| SHA-256 checksums | ✅ All pass |

---

## 📝 How to Cite

If you use this evidence register in your own research, please cite both the survey manuscript and this repository:

### Survey manuscript (BibTeX)
```bibtex
@article{khayoub2026llmwebagents,
  author    = {Khayoub, Ismail and Chadi, Mohamed-Amine and
               Mousannif, Hajar and {Ait Mohamed}, Firdaous},
  title     = {{LLM-Based Agents for Generalized Web Automation
                and Schema-Guided Data Extraction: A Survey}},
  journal   = {World Wide Web},
  year      = {2026},
  note      = {Submitted}
}
```

### Evidence register (BibTeX)
```bibtex
@dataset{khayoub2026evidenceregister,
  author    = {Khayoub, Ismail and Chadi, Mohamed-Amine and
               Mousannif, Hajar and {Ait Mohamed}, Firdaous},
  title     = {{Evidence Register for LLM-Based Agents for Generalized
                Web Automation and Schema-Guided Data Extraction: A Survey}},
  year      = {2026},
  version   = {1.0.0},
  publisher = {GitHub},
  url       = {https://github.com/khayoubIsmail/llm-web-agents-survey-evidence},
  license   = {CC BY 4.0}
}
```

Or use the `CITATION.cff` file in the root of this repository for automatic citation via GitHub's **Cite this repository** button.

---

## 👥 Authors

| Name | Role | ORCID |
|---|---|---|
| **Ismail Khayoub** | Lead author, corpus construction, screening, coding, evidence extraction | [0009-0009-5677-8392](https://orcid.org/0009-0009-5677-8392) |
| **Mohamed-Amine Chadi** | Co-author, analytical verification | [0000-0003-3260-0978](https://orcid.org/0000-0003-3260-0978) |
| **Hajar Mousannif** | Co-author, analytical verification | [0000-0002-1307-4215](https://orcid.org/0000-0002-1307-4215) |
| **Firdaous Ait Mohamed** | Co-author, screening, coding, evidence extraction | [0009-0009-6131-1439](https://orcid.org/0009-0009-6131-1439) |

---

## ⚖️ License

The bibliographic metadata, review coding, documentation, and other original material in this repository are licensed under the  
**[Creative Commons Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/)** license.

You may share and adapt this material for any purpose provided you give appropriate credit, supply a link to the license, and indicate changes.

> **Note:** This license does **not** apply to third-party works, abstracts, DOIs, or other identifiers for which the authors hold no copyright. No full-text papers are redistributed in this repository.

---

<div align="center">

*Evidence register v1.0.0 · Released 2026-07-26 · CC BY 4.0*

</div>
