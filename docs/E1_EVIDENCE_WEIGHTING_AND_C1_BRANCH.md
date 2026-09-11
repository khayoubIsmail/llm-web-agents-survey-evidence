# E1 — Evidence Weighting, Study Appraisal, and C1 Traceability

## Scope

E1 corrects the manuscript's description of evidence weighting. The submitted §2.4 sentence combines three distinct assertions:

1. no numerical risk-of-bias instrument was used;
2. evidence was weighted using six named criteria;
3. every load-bearing claim has a claim-level record of primary evidence, corroboration, contradictory/boundary evidence, quantitative results, limitations, and checked source locations.

The repository supports the first assertion. It supports holistic qualitative synthesis considerations for the second, but not a formal six-criterion per-study appraisal. The third assertion is a separate C1 traceability requirement.

## What the repository supports

The paper-level notes record real evidence such as methodological/empirical findings, limitations and boundaries, relevance to the survey, evidence locations or full-text basis, paper-specific synthesis statements, and publication-status context. These artifacts support **holistic qualitative synthesis judgment**.

They do not show a standardized six-criterion quality/risk-of-bias instrument applied consistently to every study. In particular, criteria such as baseline adequacy, reproducibility artifacts, and reporting completeness must not be represented as systematically scored per-study fields unless corresponding records actually exist.

The review therefore used **qualitative synthesis considerations**, not a formal per-study appraisal instrument.

## E1 manuscript correction

Use wording of this form in §2.4:

> We did not apply a numerical risk-of-bias or study-quality score. Instead, evidence strength was judged qualitatively and holistically during synthesis using the information documented in the paper-level notes, including empirical findings, limitations or boundary conditions, relevance to the review question, publication-status context, and traceability to the supporting source locations. These considerations informed synthesis judgment but were not scored as an independent per-study appraisal instrument.

P0–P3 priority must remain separate from study quality: priority governs evidence use and analysis depth, not methodological quality or risk of bias.

## Line 271: separate E1 from C1

The submitted line 271 must not remain one compound sentence.

### E1 portion

> No numerical risk-of-bias or study-quality instrument was applied. Evidence strength was judged qualitatively and holistically from the paper-level evidence recorded in the synthesis notes rather than by assigning per-study criterion scores.

### C1 portion — Option A selected

**Option A is now the selected branch.** The repository contains:

- `docs/C1_CLAIM_EVIDENCE_TRACEABILITY.md`
- `data/c1_claim_evidence_matrix.csv`
- `scripts/check_c1_claim_evidence_matrix.py`

C1 currently maps 11 load-bearing synthesis claims to stable register IDs, primary/corroborating/boundary evidence roles, quantitative evidence where applicable, and checked source locations.

After the C1 final membership/source-location gate passes, the manuscript may retain the stronger traceability sentence:

> For each load-bearing claim, the synthesis records the primary supporting evidence, corroborating evidence where available, contradictory or boundary evidence where identified, relevant quantitative results and limitations, and the checked source locations.

This sentence must remain gated until every C1 evidence record is revalidated against final `{{N_SYNTH}}` after publication-status/manual adjudication. A paper-level limitations section is not automatically treated as claim-level contradictory/boundary evidence; C1 records that relationship claim by claim.

## Coordinated A2 + D1 + E1 base paragraph

Use the following methodological core for the final §2.4 rewrite after counts are frozen:

> Both primary reviewers read the full text of every study contributing to the final qualitative synthesis. Recorded analysis followed two tiers: {{N_DEEP}} P0/P1 records received deep critical analysis and {{N_STRUCT}} P2/P3 records received complete structured reading. Review and coding decisions were developed collaboratively through discussion and reconciliation rather than as two blinded, independently produced coding sets; because independent parallel ratings were not generated, no inter-rater reliability coefficient is reported. We did not apply a numerical risk-of-bias or study-quality score. Evidence strength was judged qualitatively and holistically from the paper-level evidence recorded in the synthesis notes rather than by assigning per-study criterion scores.

Once C1 passes its final gate, append the selected C1 traceability sentence above. E2's external-independent-audit limitation belongs in §11, not in this methods paragraph.

## Limitation wording

> The review did not apply a formal numerical risk-of-bias or study-quality instrument across the heterogeneous evidence base. Evidence strength was judged qualitatively from the documented paper-level evidence, which permits contextual interpretation across diverse study types but introduces reviewer judgment and does not provide a standardized per-study quality score.

Do not describe P0–P3 as a substitute quality instrument.

## Reviewer-response text for E1

> Thank you for asking us to clarify how evidence quality was assessed. We revised the Methods section because the previous wording could be read as implying a formal six-criterion per-study appraisal that was not actually recorded as such. The review did not use a numerical risk-of-bias or study-quality instrument. Instead, evidence strength was judged qualitatively and holistically during synthesis using the paper-level information documented in the evidence notes, including empirical findings, limitations and boundary conditions, relevance to the review questions, publication-status context, and checked source locations. These considerations informed synthesis judgment but were not assigned numerical or categorical per-study quality scores.
>
> We also separated this issue from claim-level traceability. Paper-level limitations are not equivalent to claim-level contradictory or boundary evidence. We therefore created a claim-level evidence matrix linking the survey's load-bearing claims to primary supporting studies, corroborating evidence where available, claim-specific boundary or contradictory evidence, quantitative results where applicable, and checked source locations. The matrix is released in the evidence repository and is revalidated against the final synthesis membership before manuscript freeze.

## E1 audit rules

E1 passes only if all of the following are true:

1. the manuscript explicitly states that no numerical risk-of-bias or formal per-study quality score was used;
2. the six named criteria are not presented as a systematic per-study instrument unless corresponding records actually exist;
3. weighting is described as holistic qualitative synthesis judgment;
4. P0–P3 priority is not presented as a quality/risk-of-bias score;
5. line 271's claim-level artifact promise is separated from the weighting statement;
6. C1 Option A remains selected and its matrix passes the final `{{N_SYNTH}}` and source-location audit before the stronger traceability sentence is retained;
7. §2.4 is applied once in coordination with A2 and D1;
8. the limitations section and reviewer response use the same description.

## Closure state

Current E1 state: **weighting methodology corrected; C1 Option A selected and matrix built; final C1 membership/source-location gate and coordinated manuscript application pending.**
