# A2 — Reading-Depth Definitions and Final Manuscript Closure

## Final status

**A2 is complete and numerically frozen.** Publication-status verification, manual adjudication, synthesis-membership reconciliation, figure regeneration, manuscript editing, and the final A3 consistency audit have all been completed.

Frozen values:

- mapping corpus: **805** unique studies;
- publication-eligible pool (`N_POOL`): **454** archival published or accepted studies;
- historical normalized-note / synthesis-candidate set: **403** records;
- final qualitative synthesis (`N_SYNTH`): **385** studies;
- priority counts: **P0 = 18, P1 = 96, P2 = 189, P3 = 82**;
- deep critical analysis: **114 P0/P1 studies**;
- complete structured reading: **271 P2/P3 studies**;
- full-text exception: **record 249**, excluded once from `N_SYNTH`.

## Operational reading definitions

**Full-text reading** means examination of the complete accessible article from beginning to end, including the methodological, evaluation/results, discussion, and limitation material relevant to the review. Abstract-only or selected-section inspection does not qualify.

**Deep critical analysis (P0/P1)** means full-text reading followed by structured notes recording the research problem, method, evaluation design, quantitative or qualitative findings, stated limitations, relationship to adjacent work, and the study's specific evidentiary role in this review.

**Complete structured reading (P2/P3)** means full-text reading followed by lighter structured notes recording relevance to the review questions, methodological approach, principal findings or benchmark properties, contributions, and limitations, without requiring the extended comparative and claim-level critical synthesis used for P0/P1 studies.

**Priority determines analytical depth and evidence use; it is not a methodological-quality or risk-of-bias score.**

All **385** studies contributing to the final qualitative synthesis have documented full-text reading. Record 249 remains in the master register for traceability but is excluded from qualitative, quantitative, taxonomy-support, and claim-level synthesis because a complete verifiable full text could not be obtained.

## Final reconciliation

The historical 403-record synthesis-candidate set was not treated as the final synthesis count. After final publication-status adjudication:

- **17** of the 403 candidates no longer met the strict archival publication-eligibility rule;
- **386** publication-eligible candidates remained;
- record **249** was then excluded once for the documented full-text exception;
- final `N_SYNTH` = **385**.

The resulting depth split is **114 deep + 271 structured = 385**.

## Manuscript changes applied

The coordinated manuscript pass has been completed. The revised source now:

1. distinguishes the 805 mapping corpus, 454 publication-eligible pool, historical 403 candidate set, and 385 final synthesis;
2. removes the inaccurate implication that all included studies received identical in-depth analysis;
3. states the final **114 / 271** analytical-depth split;
4. describes the reviewer process as collaborative discussion/reconciliation rather than blinded independent coding;
5. excludes record 249 exactly once;
6. uses **385** in the qualitative-synthesis and taxonomy statements;
7. updates the conclusion, limitations, data availability, and author-contribution statements; and
8. regenerates the study-selection flow and thematic-distribution figure from the frozen corpus.

## Final Figure 2 statistics

The primary thematic bars were rebuilt from `data/final_synthesis_membership.csv` and sum exactly to **385**:

| Section | Theme | Count |
|---|---|---:|
| S2 | Agent foundations and pretraining | 45 |
| S3 | Agent architectures and memory | 78 |
| S4 | Web/GUI agent evolution | 31 |
| S5.1 | Benchmarks and environments | 58 |
| S5.2 | Perception and grounding | 25 |
| S5.3 | Planning and memory | 20 |
| S5.4 | Learning and adaptation | 57 |
| S5.5 | Failure modes and reliability | 11 |
| S6 | Extraction and data agents | 13 |
| S7 | Security and safety | 43 |
| S8 | Generalization and deployment | 4 |
|  | **Total** | **385** |

The authoritative machine-readable statistics are in:

- `data/final_synthesis_statistics.json`
- `data/corpus_statistics_final.csv`
- `data/final_synthesis_membership.csv`

## Reviewer-response text

> Thank you for requesting more precise definitions of the reading procedure. We revised the Methods section to distinguish reading completeness from analytical depth. All 385 studies contributing to the final qualitative synthesis were read in full. Of these, 114 P0/P1 studies received deep critical analysis and 271 P2/P3 studies received complete structured reading. Priority therefore determines analytical depth and evidentiary role, not methodological quality or risk of bias. We also separated the 454-study publication-eligible pool from the 385-study qualitative-synthesis set. One otherwise eligible P3 record (record 249) could not be obtained as a complete verifiable full text; it is retained in the master register for traceability but excluded from qualitative and claim-level synthesis. Figure 2 and all manuscript counts were regenerated from the final frozen membership rather than relabeling the historical 403-study statistics.

## Completion checklist

- [x] operational definitions fixed;
- [x] reading completeness separated from analytical depth;
- [x] priority explicitly not a quality/risk-of-bias score;
- [x] record 249 exclusion rule fixed and applied once;
- [x] publication-status verification complete;
- [x] all 297 flagged publication-status records manually adjudicated;
- [x] `N_POOL = 454` and `N_SYNTH = 385` frozen;
- [x] `P0 = 18`, `P1 = 96`, `P2 = 189`, `P3 = 82` recomputed;
- [x] `N_DEEP = 114`, `N_STRUCT = 271` recomputed;
- [x] thematic statistics rebuilt from final membership;
- [x] Figure 1 and Figure 2 regenerated;
- [x] final LaTeX manuscript edits applied;
- [x] A3 consistency audit passed.

**A2 final status: CLOSED.**