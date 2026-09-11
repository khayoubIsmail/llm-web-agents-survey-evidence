# A2 — Reading-Depth Definitions and Manuscript Edit Plan

## Scope

A2 is the manuscript-facing correction for reading-depth terminology. A1 established the paper-level reading evidence and note audit. A2 defines the reading terms operationally, removes the inaccurate implication that every included study received the same depth of critical analysis, and provides the exact manuscript edits needed to make the paper consistent with the evidence repository.

A2 is intentionally separate from publication-status verification. The final corpus and tier counts remain placeholders until the hardened publication-status sweep and subsequent manual review are complete.

## Corpus terms used by A2

To avoid ambiguity between eligibility and actual synthesis use, A2 distinguishes two sets:

- `{{N_POOL}}` — the final publication-status-eligible P0–P3 pool after publication-status verification and manual adjudication.
- `{{N_SYNTH}}` — the subset of `{{N_POOL}}` admitted to qualitative synthesis after full-text availability and evidence-use checks.

Record 249 is currently publication-eligible but lacks a complete verified full text. It is retained in the register for traceability and is excluded from qualitative and claim-level synthesis.

**Important count rule:** record 249 must be excluded exactly once. If the publication-status sweep retains record 249 in `{{N_POOL}}`, then `{{N_SYNTH}}` excludes it. If the publication-status process itself removes record 249 from `{{N_POOL}}`, it must not be subtracted again when deriving `{{N_SYNTH}}`.

## Operational definitions for §2.4

Use the following protocol text in the Methods / Review Methodology section.

> **Reading protocol.** We distinguish three terms used throughout this review. *Full-text reading* means examination of the complete accessible article from beginning to end, including the methodological, evaluation/results, discussion, and limitation material relevant to the review; abstract-only or selected-section inspection does not qualify. *Deep critical analysis* (P0/P1) means full-text reading followed by structured notes recording the research problem, method, evaluation design, quantitative or qualitative findings, stated limitations, relationship to adjacent work, and the study's specific evidentiary role in this review. *Complete structured reading* (P2/P3) means full-text reading followed by lighter structured notes recording relevance to the review questions, methodological approach, principal findings or concrete benchmark properties where applicable, contributions, and limitations, without requiring the extended comparative and claim-level critical synthesis used for P0/P1 studies. **Priority determines analytical depth, not reading completeness, methodological quality, or risk of bias.**

Immediately after this protocol, add the synthesis-set clarification:

> All studies contributing to the final qualitative synthesis were read in full. One publication-eligible P3 record (record 249) could not be obtained as a complete verifiable full text despite documented retrieval attempts; it is retained in the register for traceability but excluded from qualitative and claim-level synthesis.

## Count placeholders

Do not freeze numerical values in the manuscript until publication-status verification is complete and the final synthesis set is rebuilt.

| Placeholder | Definition | Pre-verification value / state | Finalization rule |
|---|---|---:|---|
| `{{N_POOL}}` | final publication-status-eligible P0–P3 pool | 403 historical value | recompute after v2.2 + manual adjudication |
| `{{N_SYNTH}}` | final qualitative-synthesis set | unresolved | derive from final pool after evidence-use/full-text exclusions |
| `{{N_P0}}` | P0 records in synthesis set | unresolved | recompute from final synthesis membership |
| `{{N_P1}}` | P1 records in synthesis set | unresolved | recompute from final synthesis membership |
| `{{N_P2}}` | P2 records in synthesis set | unresolved | recompute from final synthesis membership |
| `{{N_P3}}` | P3 records in synthesis set | unresolved | recompute from final synthesis membership |
| `{{N_DEEP}}` | `{{N_P0}} + {{N_P1}}` | historical value 116 | recompute from final synthesis membership |
| `{{N_STRUCT}}` | `{{N_P2}} + {{N_P3}}` | historical value 287 before synthesis exclusion reconciliation | recompute from final synthesis membership |

The historical 116/287 split describes the 403-record pre-finalization register and must not be copied forward blindly after status and synthesis-set reconciliation.

## Manuscript edit map

The submitted `sn-article.tex` contains eight locations that either assert uniform in-depth reading or carry the old fixed count. Apply the wording changes below as one coordinated manuscript pass after the final counts are known.

### 1. Abstract — submitted source line 35

**Current**

> ...403 published or accepted studies form the final included evidence set and were read in full and reviewed in depth by the two primary reviewers.

**Replace with**

> ...{{N_POOL}} published or accepted studies form the final publication-eligible pool, of which {{N_SYNTH}} contribute to the qualitative synthesis. All studies contributing to the final qualitative synthesis were read in full by the two primary reviewers, with recorded analysis following two documented depth levels.

**Reason:** removes the false implication of uniform in-depth analysis and distinguishes the eligible pool from the actual synthesis set.

### 2. §2.4 reviewers paragraph — submitted source line 267

**Current**

> Both reviewers read the full text of every paper in the final 403-study included evidence set and reviewed each paper in depth. They compared decisions and jointly re-examined disagreements until reaching a shared decision.

**A2 replacement for the reading-depth portion**

> Both reviewers read the full text of every study contributing to the final qualitative synthesis. Recorded analysis followed two tiers: {{N_DEEP}} P0/P1 records received deep critical analysis and {{N_STRUCT}} P2/P3 records received complete structured reading, as defined above.

The reviewer-process sentence in this paragraph also belongs to D1. When D1 is resolved, rewrite the paragraph once so the final prose simultaneously reflects reading depth and the actual collaborative/independent-review procedure.

### 3. §2.4 priority paragraph — submitted source line 269

**Current**

> All 403 included studies received full-text, in-depth reading irrespective of tier.

**Replace with**

> All studies contributing to the final qualitative synthesis received full-text reading irrespective of tier; the depth of recorded analysis varied by tier as defined above.

**Reason:** this is the clearest direct contradiction of the documented tier protocol.

### 4. Figure 2 caption — submitted source line 310

**Current**

> Primary thematic distribution of the 403 fully read, published or accepted studies.

**Replace with**

> Primary thematic distribution of the {{N_SYNTH}} studies contributing to the final qualitative synthesis.

**Reason:** the figure should describe the population actually represented in the thematic synthesis rather than carry an unnecessary reading-process claim.

**Required data/figure action:** this is not a caption-only edit. After `{{N_SYNTH}}` is frozen, rebuild the thematic/category statistics from the actual final synthesis-membership table, regenerate every Figure 2 bar from those statistics, and verify that the bars sum exactly to `{{N_SYNTH}}`. Any historical 403-based statistics artifact must be regenerated rather than merely renamed or relabeled. If a manuscript-workspace file named `corpus_statistics_403.csv` is the current chart source, regenerate it from final membership and replace it with a count-neutral/finalized artifact; that file is not currently versioned in this evidence repository.

### 5. §3.1 taxonomy paragraph — submitted source line 323

**Current**

> ...rechecked against the full-text syntheses for the 403-study included evidence set.

**Replace with**

> ...rechecked against the full-text syntheses for the {{N_SYNTH}}-study qualitative-synthesis set.

**Reason:** “full-text syntheses” is acceptable; the set and count need to be accurate.

### 6. §10 Conclusion — submitted source line 881

**Current**

> This review mapped 805 studies and synthesized all 403 published or accepted works in the final included evidence set after full-text, in-depth reading.

**Replace with**

> This review mapped 805 studies, identified {{N_POOL}} studies in the final publication-eligible pool, and synthesized {{N_SYNTH}} studies using full-text reading followed by one of two documented levels of analysis.

### 7. §11 Limitations item 3 — submitted source line 893

**Current**

> Although the two primary reviewers read all 403 included papers in full and in depth, thematic coding, taxonomy construction, and evidence weighting still involve reviewer judgment.

**Replace with**

> Although the two primary reviewers read all studies contributing to the qualitative synthesis in full, recorded analysis was tiered by evidence-use priority, and thematic coding, taxonomy construction, and evidence weighting involve reviewer judgment.

### 8. Author contributions — submitted source line 911

**Current**

> ...and fully read and reviewed in depth all 403 included studies.

**Replace with**

> ...and read in full all studies contributing to the qualitative synthesis, recording analysis at the two documented depth levels.

## Record 249 — synthesis treatment

Record 249 (`Meta-Agent-Workflow: Streamlining Tool Usage in LLMs through Workflow Construction, Retrieval, and Refinement`) remains explicitly documented in `docs/FULL_TEXT_ACCESS_EXCEPTIONS.md`.

A2 adopts the following rule:

1. Keep the record in the master register while it remains otherwise eligible, so the search/screening history is not erased.
2. Exclude it from qualitative, quantitative, taxonomy-support, and claim-level synthesis until a complete verifiable full text is obtained and analyzed.
3. Do not describe it as fully read.
4. Do not subtract it twice during final corpus reconciliation. Its synthesis exclusion is applied only if it is still present in the final publication-eligible pool.

This yields the stronger defensible statement: **All studies contributing to the final qualitative synthesis were read in full.**

## Reviewer-response text for A2

> Thank you for requesting more precise definitions of the reading procedure. We have revised the Methods section to distinguish reading completeness from analytical depth. We now define full-text reading as examination of the complete accessible article rather than abstract-only or selected-section inspection. P0/P1 studies received deep critical analysis, including structured recording of the research problem, methods, evaluation design, findings, limitations, relationship to adjacent work, and evidentiary role. P2/P3 studies received complete structured reading, including relevance, methodological approach, principal findings or benchmark properties, contributions, and limitations, but without the extended comparative and claim-level critical synthesis required for P0/P1 studies. Priority therefore determines analytical depth, not reading completeness, methodological quality, or risk of bias.
>
> We also corrected every manuscript statement that previously implied uniform “in-depth” review of the entire included pool. The revised wording distinguishes the final publication-eligible pool from the subset contributing to qualitative synthesis. One otherwise publication-eligible P3 record (record 249) could not be obtained as a complete verifiable full text despite documented retrieval attempts. It is retained in the register for traceability but excluded from qualitative and claim-level synthesis. Consequently, all studies contributing to the final qualitative synthesis have documented full-text reading, with analysis recorded at one of the two defined depth levels.
>
> The repository now provides an A2 reading-depth audit that enumerates each affected manuscript location, the prior wording, the reason for correction, the replacement wording, and the supporting evidence artifact. Figure 2 will also be regenerated from the final synthesis membership rather than merely relabeled, so that its category bars and total reflect the same `{{N_SYNTH}}` population. Final numerical counts will be inserted after the ongoing publication-status verification and corpus reconciliation are complete.

## Coordination with D1 and E1

A2, D1, and E1 remain separate evidence tasks because they answer different reviewer concerns:

- **A2:** what “full-text,” “deep critical analysis,” and “complete structured reading” mean, and which records received each treatment;
- **D1:** whether review/coding decisions were independent or collaborative and what agreement statistics are supportable;
- **E1:** whether evidence weighting was a formal per-study quality/risk-of-bias appraisal or a holistic synthesis judgment.

However, all three touch the same §2.4 methods paragraph. The final manuscript should therefore receive one coordinated rewrite after the three methodological decisions are fixed, rather than three successive rewrites of the same paragraph.

## A2 completion criteria

A2 is closed only when all of the following are true:

- [x] operational definitions are fixed;
- [x] reading completeness is explicitly separated from analytical depth;
- [x] priority is explicitly stated not to be methodological quality or risk-of-bias scoring;
- [x] record 249 has a clean synthesis-exclusion rule;
- [x] all eight affected manuscript claims have mapped replacement text;
- [x] repository audit artifact exists;
- [ ] publication-status verification and manual adjudication are complete;
- [ ] `{{N_POOL}}`, `{{N_SYNTH}}`, `{{N_P0}}`–`{{N_P3}}`, `{{N_DEEP}}`, and `{{N_STRUCT}}` are recomputed from final membership;
- [ ] thematic statistics are rebuilt from final `{{N_SYNTH}}` membership and Figure 2 is regenerated, with bar totals verified to equal `{{N_SYNTH}}`;
- [ ] the eight manuscript edits are applied to the final LaTeX source;
- [ ] A3 confirms that manuscript, response letter, repository artifacts, figures/statistics, and counts agree.

Until the unchecked items are complete, A2 is **methodologically drafted and auditable, but not numerically frozen**.
