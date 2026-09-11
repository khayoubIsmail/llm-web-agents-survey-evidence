# D1 — Reviewer Process, Independence, and Agreement

## Scope

D1 corrects the manuscript's description of how screening, reading, coding, and synthesis decisions were produced by the primary reviewers. It is separate from A2 reading-depth definitions and E1 evidence-weighting methodology, but it shares the same §2.4 methods paragraph with A2 and should therefore be applied in one coordinated manuscript rewrite.

## Factual reviewer-process statement

The defensible description of the process is:

- review/coding decisions were made **collaboratively**, with discussion and reconciliation during the review;
- the two reviewers did **not** produce two blinded, independent duplicate coding sets for the full synthesis corpus;
- no preserved pair of independent parallel ratings exists from which a valid inter-rater reliability statistic can be calculated;
- therefore the manuscript must **not** report or imply Cohen's kappa, Krippendorff's alpha, percentage agreement, blinded coding, independent duplicate verification, or an independent sample audit unless such evidence actually exists for a separately documented stage;
- the absence of independent duplicate coding and external independent verification is a methodological limitation and should be stated plainly.

The appropriate framing is not that collaborative coding is equivalent to independent reliability assessment. Collaborative review supported iterative interpretation across a heterogeneous corpus, but it provides less protection against shared reviewer bias than blinded independent duplicate coding.

## Relationship to A2

A2 establishes that all studies contributing to the final qualitative synthesis were read in full and that recorded analysis had two depth levels. D1 establishes **how reviewer decisions were produced**.

The final §2.4 prose should therefore combine both facts once, rather than rewriting the paragraph separately for A2 and D1.

### Coordinated A2 + D1 replacement for §2.4

Use this as the base wording after the final count placeholders are resolved:

> Both primary reviewers read the full text of every study contributing to the final qualitative synthesis. Recorded analysis followed two tiers: {{N_DEEP}} P0/P1 records received deep critical analysis and {{N_STRUCT}} P2/P3 records received complete structured reading. Review and coding decisions were developed collaboratively through discussion and reconciliation rather than as two blinded, independently produced coding sets. Because independent parallel ratings were not generated for the synthesis corpus, no inter-rater reliability coefficient is reported.

This wording should later be coordinated with E1 if the same paragraph also describes evidence weighting.

## Manuscript locations confirmed from the submitted-source map

### D1-01 — §2.4 reviewer-process paragraph, submitted source line 267

**Current wording captured in the A2 source map**

> Both reviewers read the full text of every paper in the final 403-study included evidence set and reviewed each paper in depth. They compared decisions and jointly re-examined disagreements until reaching a shared decision.

**Problem**

The sentence describes discussion/reconciliation but does not say whether the underlying decisions were independently produced. In the context of a systematic review, readers may reasonably interpret “both reviewers” and “disagreements” as independent duplicate coding unless the manuscript says otherwise.

**Required correction**

Use the coordinated A2 + D1 replacement above. Explicitly say **collaborative**, explicitly say **not blinded independent duplicate coding**, and explicitly state why no inter-rater coefficient is reported.

### D1-02 — §11 limitations item, submitted source line 893

The existing limitation already acknowledges reviewer judgment but does not state the more important design limitation: coding/taxonomy decisions were collaborative rather than independently duplicated.

**Recommended coordinated A2 + D1 limitation wording**

> Although both primary reviewers read all studies contributing to the qualitative synthesis in full, coding, taxonomy construction, and synthesis judgments were developed collaboratively rather than through blinded independent duplicate coding. Consequently, no inter-rater reliability statistic is available for the synthesis coding, and the resulting taxonomy and evidence interpretation remain susceptible to shared reviewer judgment. No reviewer outside the author team independently recoded a sample blind to the original labels. We therefore make the coding procedure explicit and expose the underlying paper-level evidence and audit artifacts for external inspection.

This is stronger than implying an agreement statistic or external verification that the study design cannot support.

## Global manuscript consistency search

The final LaTeX source is not currently versioned in this evidence repository, so D1 does not invent additional line locations. During the final manuscript pass, search the complete source for each of the following terms and manually inspect every hit:

- `independent`
- `independently`
- `blind`
- `blinded`
- `inter-rater`
- `interrater`
- `agreement`
- `disagreement`
- `Cohen`
- `kappa`
- `Krippendorff`
- `alpha`
- `two reviewers`
- `both reviewers`
- `verification`
- `independent audit`
- `independently verified`
- `external validation`
- `spot-check`

Any wording that implies independent duplicate coding or external independent verification must either be supported by stage-specific evidence or corrected to the collaborative process actually used.

## What must not be done

D1 must **not** be “fixed” by retrospectively manufacturing an agreement statistic from the final consensus labels. Consensus labels are not independent ratings, so computing kappa or percentage agreement from them would be methodologically invalid.

Similarly, do not reconstruct supposed independent labels from commit history, final notes, disagreement discussions, or a post hoc author-only spot-check unless contemporaneous reviewer-specific decisions actually exist and can be shown to have been produced independently before reconciliation.

## Reviewer-response text for D1

> Thank you for asking us to clarify reviewer independence and agreement. We have revised the Methods section because the previous wording could be read as implying independent duplicate coding. The review used a collaborative process: the two primary reviewers discussed and reconciled screening, coding, and synthesis decisions rather than producing two blinded, independently coded versions of the full synthesis corpus. Consequently, the study did not generate the independent parallel ratings required for a valid inter-rater reliability coefficient, and we do not report or retrospectively construct Cohen's kappa or a comparable statistic.
>
> We now state this process explicitly in the Methods and add the absence of independent duplicate coding and external independent verification as limitations. The collaborative approach supported iterative interpretation across a heterogeneous evidence base, but we acknowledge that it provides less protection against shared reviewer bias than blinded independent coding. To improve auditability, the revised evidence repository exposes the paper-level notes, synthesis-source records, reading-depth audit, and other decision artifacts used in the review.

## D1 audit rules

D1 passes only if all of the following are true:

1. the manuscript does not describe the full synthesis coding as independent or blinded;
2. the manuscript clearly labels the process as collaborative;
3. no inter-rater coefficient or percentage agreement is reported for the collaborative synthesis coding;
4. the absence of independent duplicate coding and external independent verification is stated as a limitation;
5. §2.4 is rewritten once in coordination with A2 (and later E1), rather than with contradictory successive edits;
6. a global search of the final LaTeX source finds no unsupported independence/agreement/audit claims;
7. the response letter uses the same description as the manuscript and repository.

## Closure state

Current D1 state: **methodological correction and replacement text drafted; final-LaTeX global consistency search and coordinated §2.4/§11 application pending**.
