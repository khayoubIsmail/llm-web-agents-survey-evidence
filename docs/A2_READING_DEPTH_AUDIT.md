# A2 — Reading-Depth Audit

## Purpose

This artifact makes the A2 correction auditable. It records the operational reading definitions, the manuscript claims affected by the old uniform-depth wording, the replacement text, and the repository evidence used to support the correction.

A2 does **not** freeze the final corpus counts. Publication-status verification and subsequent manual adjudication must finish first.

## Operational reading definitions

| Term | Applies to | Operational requirement |
|---|---|---|
| Full-text reading | every study admitted to qualitative synthesis | Complete article examined from beginning to end; abstract-only or selected-section inspection does not qualify. |
| Deep critical analysis | P0/P1 synthesis records | Full-text reading plus structured analysis of problem, method, evaluation design, findings, limitations, adjacent work, and specific evidentiary role in the survey. |
| Complete structured reading | P2/P3 synthesis records | Full-text reading plus structured analysis of relevance, method, principal findings or benchmark properties, contributions, and limitations, without the extended comparative/evidentiary-role analysis required for P0/P1. |

**Interpretive rule:** priority determines analytical depth, not reading completeness, methodological quality, or risk of bias.

## Corpus-set definitions

| Symbol | Meaning | Status |
|---|---|---|
| `{{N_POOL}}` | final publication-status-eligible P0–P3 pool | pending publication-status v2.2 + manual adjudication |
| `{{N_SYNTH}}` | final full-text qualitative-synthesis set | pending final pool reconciliation |
| `{{N_P0}}` | P0 records in synthesis set | pending |
| `{{N_P1}}` | P1 records in synthesis set | pending |
| `{{N_P2}}` | P2 records in synthesis set | pending |
| `{{N_P3}}` | P3 records in synthesis set | pending |
| `{{N_DEEP}}` | `{{N_P0}} + {{N_P1}}` | pending |
| `{{N_STRUCT}}` | `{{N_P2}} + {{N_P3}}` | pending |

Historical pre-finalization values were 403 register records, 116 P0/P1, and 287 P2/P3. These values are retained only as provenance and must not be treated as final after corpus reconciliation.

## Record 249 rule

Record 249 is retained in the register while publication-eligible but excluded from qualitative and claim-level synthesis because a complete verified full text was not obtained during the A1 recheck.

**No-double-subtraction rule:**

- if record 249 remains in final `{{N_POOL}}`, remove it once when deriving `{{N_SYNTH}}`;
- if publication-status adjudication removes record 249 from `{{N_POOL}}`, do not remove it again;
- tier counts must be recomputed from actual final `{{N_SYNTH}}` membership rather than adjusted arithmetically from historical totals.

Repository evidence: `docs/FULL_TEXT_ACCESS_EXCEPTIONS.md`, `data/paper_note_audit.csv`, `notes/papers/0249.md`, and `notes/original_sources/0249.md`.

## Manuscript claim audit

| ID | Location | Old claim / wording | A2 issue | Required replacement | Evidence pointer | Status |
|---|---|---|---|---|---|---|
| A2-01 | Abstract, submitted source line 35 | “403 ... read in full and reviewed in depth” | conflates reading completeness with uniform analytical depth | distinguish `{{N_POOL}}` from `{{N_SYNTH}}`; state that all synthesis studies were read in full and analyzed at two documented levels | `docs/A1_MANUSCRIPT_AND_RESPONSE_TEXT.md`; `data/a1_reading_tier_summary.json` | wording ready; counts pending |
| A2-02 | §2.4 reviewers paragraph, line 267 | every final-set paper was “reviewed ... in depth” | unsupported uniform-depth claim | state full-text reading for every synthesis study and P0/P1 vs P2/P3 analysis depth | `data/a1_reading_tier_summary.json`; `data/a1_live_note_audit.csv` | wording ready; coordinate with D1 |
| A2-03 | §2.4 priority paragraph, line 269 | “All 403 ... full-text, in-depth reading irrespective of tier” | directly contradicts documented tiered analysis | state full-text reading irrespective of tier, with analysis depth varying by tier | `docs/METHODOLOGY_AND_VERSIONING.md`; `data/a1_reading_tier_summary.json` | wording ready |
| A2-04 | Figure 2 caption, line 310 | “403 fully read...” | figure population should match actual synthesis set; reading-process claim is unnecessary | describe thematic distribution of `{{N_SYNTH}}` synthesis studies | final synthesis membership + Figure 2 regeneration | wording ready; count pending |
| A2-05 | §3.1 taxonomy paragraph, line 323 | “full-text syntheses for the 403-study included evidence set” | set/count must match actual synthesis membership | replace with `{{N_SYNTH}}`-study qualitative-synthesis set | full-text synthesis notes + final membership | wording ready; count pending |
| A2-06 | §10 Conclusion, line 881 | “synthesized all 403 ... after full-text, in-depth reading” | conflates eligibility, synthesis membership, and depth | report mapped 805, `{{N_POOL}}` eligible, `{{N_SYNTH}}` synthesized, two documented depth levels | final publication-status summary + A2 definitions | wording ready; counts pending |
| A2-07 | §11 Limitations item 3, line 893 | “all 403 ... in full and in depth” | repeats unsupported uniform-depth claim | state all synthesis studies were read in full; analysis was tiered by evidence-use priority | A1 note audit + A2 definitions | wording ready |
| A2-08 | Author contributions, line 911 | “fully read and reviewed in depth all 403” | overstates uniform depth and ignores synthesis exclusion | state full reading of synthesis studies with two documented depth levels | A1 audit + final synthesis membership | wording ready |

A machine-readable companion containing the same eight rows is stored at `data/a2_reading_depth_claim_audit.csv`.

## Repository evidence supporting A2

- `docs/A1_MANUSCRIPT_AND_RESPONSE_TEXT.md` — A1 closure wording and historical 403/402/116/287 state.
- `docs/FULL_TEXT_ACCESS_EXCEPTIONS.md` — record 249 retrieval history and claim-use restriction.
- `docs/METHODOLOGY_AND_VERSIONING.md` — reading-tier protocol and repository methodology.
- `data/a1_live_note_audit.csv` and `data/a1_live_note_audit_summary.json` — final A1 note audit.
- `data/a1_reading_tier_summary.json` — historical P0/P1 and P2/P3 reading-standard counts.
- `data/a1_fulltext_rechecks.csv` — current-cycle full-text recheck ledger.
- `data/paper_note_audit.csv` — paper-level provenance, full-text status, and claim-use status.
- `notes/papers/` — normalized live notes.
- `notes/original_sources/` — paper-specific synthesis-source records.

## A3 mechanical checks enabled by this artifact

After final counts are frozen and manuscript edits are applied, A3 should verify all of the following:

1. No manuscript occurrence remains of `all 403 ... in depth`, `reviewed each paper in depth`, or equivalent uniform-depth wording.
2. Every number referring to the publication-eligible pool equals final `{{N_POOL}}`.
3. Every number referring to the qualitative-synthesis/taxonomy set equals final `{{N_SYNTH}}`.
4. `{{N_DEEP}} = {{N_P0}} + {{N_P1}}` and `{{N_STRUCT}} = {{N_P2}} + {{N_P3}}` from actual synthesis membership.
5. `{{N_SYNTH}} = {{N_P0}} + {{N_P1}} + {{N_P2}} + {{N_P3}}`.
6. Record 249 is absent from claim-level/taxonomy synthesis if it remains without a complete verified full text.
7. Record 249 is excluded at most once during reconciliation.
8. The response letter, Methods, Abstract, Figure 2 caption, Conclusion, Limitations, Author contributions, README/count summaries, and repository artifacts report the same final definitions and numbers.

## Closure state

Current A2 state: **definitions and edit map complete; numerical freeze and manuscript application pending**.

A2 should not be marked fully closed until the publication-status sweep/manual review is complete, final synthesis membership is rebuilt, placeholders are resolved, the LaTeX edits are applied, and A3 passes the consistency checks above.
