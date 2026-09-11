# E1 — Evidence Weighting, Study Appraisal, and the C1 Claim-Level Branch

## Scope

E1 corrects the manuscript's description of evidence weighting. The submitted §2.4 sentence currently combines three distinct assertions that must be separated:

1. no numerical risk-of-bias instrument was used;
2. evidence was weighted using six named criteria;
3. every load-bearing claim has a claim-level record of primary evidence, corroboration, contradictory/boundary evidence, quantitative results, limitations, and checked source locations.

The repository supports the first assertion and part of the qualitative basis for the second, but it does **not** currently support the second as a per-study scored appraisal and it does **not** yet contain the claim-level matrix promised by the third assertion.

## What the repository actually supports

The paper-level notes contain real evidence fields such as:

- methodological and empirical findings;
- limitations and boundaries;
- relevance to the survey;
- evidence locations checked in the source;
- paper-specific synthesis statements;
- publication-status metadata.

These artifacts support a **holistic qualitative synthesis judgment**. They do not constitute a six-criterion per-study quality/risk-of-bias instrument unless the six criteria were explicitly and consistently recorded for every study, which the current repository does not show.

Accordingly, E1 must distinguish between:

- **considerations used during synthesis**, which may include publication status, empirical grounding, limitations, relevance, and source-level evidence;
- **formal per-study appraisal**, which would require an explicit instrument, per-study fields, reproducible decision rules, and recorded judgments for every study.

The review used the former, not the latter.

## Core E1 correction

### Unsupported interpretation to avoid

Do not describe the review as if each study received a formal six-dimension appraisal or score when no such per-study artifact exists.

Do not retrospectively create scores merely to match the submitted prose. If a formal study-appraisal instrument is introduced now, it would be a post hoc methodology addition and would need to be performed transparently for the full final synthesis set rather than inferred from existing prose notes.

### Defensible manuscript wording

Use wording of this form in §2.4:

> We did not apply a numerical risk-of-bias or study-quality score. Instead, evidence strength was judged qualitatively and holistically during synthesis, using the information documented in the paper-level notes, including publication status, empirical grounding, reported results, limitations or boundary conditions, relevance to the review question, and the traceability of the supporting source locations. These considerations informed synthesis judgment but were not scored as an independent per-study appraisal instrument.

If the exact submitted six-item list differs from the examples above, preserve only items that are actually evidenced in the repository; do not retain unsupported criteria such as baseline adequacy, reproducibility artifacts, or reporting completeness as if each had been systematically recorded for every study.

## Line 271 must be split into E1 and C1

The submitted line 271 should not remain one compound sentence because its final clause is not an E1 weighting claim; it is a C1 artifact claim.

### E1 portion

Keep the two defensible statements:

> No numerical risk-of-bias or study-quality instrument was applied. Evidence strength was judged qualitatively and holistically from the paper-level evidence recorded in the synthesis notes rather than by assigning per-study criterion scores.

### C1-dependent portion — two valid branches

#### Option A — Build C1 and keep the stronger claim **(recommended)**

Build a claim-level evidence matrix with one row per load-bearing manuscript claim. At minimum, each row should contain:

- stable claim ID;
- manuscript section/location;
- claim text or normalized claim statement;
- primary supporting study IDs;
- corroborating study IDs, where applicable;
- contradictory, limiting, or boundary evidence IDs, where applicable;
- quantitative result(s), where the claim is quantitative;
- relevant limitations/boundaries;
- checked source location(s) for each cited evidence item;
- synthesis decision / strength note;
- status indicating whether the row has been manually verified.

Only after this artifact exists and is audited may the manuscript say:

> For each load-bearing claim, the synthesis records the primary supporting evidence, corroborating evidence where available, contradictory or boundary evidence where identified, relevant quantitative results and limitations, and the checked source locations.

Important: `contradictory or boundary evidence` must be recorded **per claim**. A paper-level limitations section is not, by itself, evidence that disconfirming or boundary evidence was identified for every manuscript claim.

#### Option B — Do not build C1 and weaken the manuscript

If no claim-level matrix will be built, replace the unsupported promise with wording limited to the existing paper-level artifacts:

> The synthesis draws on paper-level notes that record relevant results, limitations or boundary conditions, survey relevance, and checked source locations for the studies used as evidence.

This wording must **not** say that each load-bearing claim has separately recorded corroboration or contradictory evidence, because the current repository does not provide that structure.

## Recommendation

Use **Option A**. Reviewer 2 explicitly asked for claim-to-supporting-study/source-location traceability. Building the matrix solves both the C1 repository gap and the unsupported third clause at line 271. It also gives a defensible place to record contradictory/boundary evidence instead of trying to infer it from paper-level limitations.

This does not require editing the manuscript immediately. The schema and audit rules can be fixed now; the final §2.4 wording should be applied in the single coordinated A2 + D1 + E1 manuscript pass after C1's status is known.

## Coordinated A2 + D1 + E1 base paragraph

Use the following as the methodological core for the final §2.4 rewrite, with counts resolved later and the C1-dependent sentence selected separately:

> Both primary reviewers read the full text of every study contributing to the final qualitative synthesis. Recorded analysis followed two tiers: {{N_DEEP}} P0/P1 records received deep critical analysis and {{N_STRUCT}} P2/P3 records received complete structured reading. Review and coding decisions were developed collaboratively through discussion and reconciliation rather than as two blinded, independently produced coding sets; because independent parallel ratings were not generated, no inter-rater reliability coefficient is reported. We did not apply a numerical risk-of-bias or study-quality score. Evidence strength was judged qualitatively and holistically from the paper-level evidence recorded in the synthesis notes rather than by assigning per-study criterion scores.

Then append either the Option A or Option B C1 sentence above.

## Limitation wording

The manuscript should acknowledge the absence of a formal per-study quality/risk-of-bias instrument. Suggested wording for the limitations section:

> The review did not apply a formal numerical risk-of-bias or study-quality instrument across the heterogeneous evidence base. Evidence strength was judged qualitatively from the documented paper-level evidence, which allows contextual interpretation across diverse study types but introduces reviewer judgment and does not provide a standardized per-study quality score.

Do not frame this limitation as if the P0–P3 priority tiers substitute for quality assessment. A2 already establishes that priority reflects evidence-use/analysis depth, not methodological quality or risk of bias.

## Reviewer-response text for E1

> Thank you for asking us to clarify how evidence quality was assessed. We revised the Methods section because the previous wording could be read as implying a formal six-criterion per-study appraisal that was not actually recorded as such. The review did not use a numerical risk-of-bias or study-quality instrument. Instead, evidence strength was judged qualitatively and holistically during synthesis using the paper-level information documented in the evidence notes, including empirical findings, limitations and boundary conditions, relevance to the review questions, publication-status context, and checked source locations. These considerations informed synthesis judgment but were not assigned numerical or categorical per-study quality scores.
>
> We also separated this issue from the manuscript's claim-level traceability statement. Paper-level limitations are not equivalent to claim-level contradictory or boundary evidence. We therefore [**Option A:** provide a claim-level evidence matrix linking each load-bearing claim to its primary support, corroboration, contradictory/boundary evidence where identified, quantitative results, limitations, and checked source locations / **Option B:** revised the manuscript to describe only the paper-level evidence fields that are actually recorded in the repository].

## E1 audit rules

E1 passes only if all of the following are true:

1. the manuscript explicitly states that no numerical risk-of-bias or formal per-study quality score was used;
2. the six named criteria are not presented as a systematic per-study instrument unless corresponding per-study records actually exist;
3. weighting is described as holistic qualitative synthesis judgment;
4. P0–P3 priority is not presented as a quality/risk-of-bias score;
5. line 271's claim-level artifact promise is separated from the weighting statement;
6. if C1 Option A is chosen, the claim-level matrix exists and is audited before the stronger claim is retained;
7. if C1 Option B is chosen, all wording implying per-claim corroboration/contradictory-evidence records is removed;
8. §2.4 is applied once in coordination with A2 and D1;
9. the limitations section and reviewer response use the same description.

## Closure state

Current E1 state: **weighting methodology correction drafted and auditable; C1-dependent third clause has two explicit branches; final §2.4/limitations application pending.**
