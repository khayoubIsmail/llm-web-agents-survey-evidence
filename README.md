# Evidence Register for the World Wide Web Survey

This repository accompanies the manuscript:

**LLM-Based Agents for Generalized Web Automation and Schema-Guided Data Extraction: A Survey**

## Contents

- `data/studies_805_mapping_corpus.csv`: the reconciled systematic-mapping corpus of 805 unique studies.
- `data/studies_403_published_accepted_pool.csv`: the 403 studies verified as published or accepted and therefore eligible for claim-level citation if used in the manuscript.
- `data/records_excluded_from_strict_pool.csv`: three records retained in the broader mapping landscape but excluded from the strict published/accepted pool after status verification.
- JSON equivalents for programmatic reuse.
- `data/summary.json`: corpus totals and category counts.
- `docs/DATA_DICTIONARY.md`: field definitions.
- `docs/METHODOLOGY_AND_VERSIONING.md`: relationship between the 805-study corpus and 403-study evidence pool.

## Important interpretation

The 403-study pool is **not** an additional screening stage. It is a publication-status and citation-eligibility layer inside the 805-study mapping corpus. Inclusion in the 403-study file does not mean a paper is automatically cited; the final bibliography remains claim-driven.

## Copyright and redistribution

This repository contains bibliographic metadata and review coding only. It does not redistribute third-party full-text PDFs.

## Citation

Citation metadata are provided in `CITATION.cff`. Please cite the accompanying survey manuscript and the repository release when reusing the registers or coding.

## License

The authors' original metadata, review coding, and documentation are available under the Creative Commons Attribution 4.0 International license. See `LICENSE.md`. Third-party material remains subject to its original rights.
