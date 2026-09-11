# C1 — Load-Bearing Claim → Study → Source-Location Traceability

## Purpose

Reviewer 2 requested an explicit mapping from the survey's major/load-bearing claims to the studies and source locations that support them. This artifact provides that mapping at the **claim level**, rather than treating paper-level notes as a substitute for claim-level evidence.

C1 is deliberately narrower than a sentence-by-sentence citation audit. It covers the principal synthesis claims on which the survey's argument, taxonomy, extraction framework, evaluation framework, security conclusions, and research agenda depend. Ordinary descriptive literature-summary sentences remain governed by their manuscript citations and paper-specific notes.

## Current status and final-membership gate

This matrix is built from the current manuscript and the current evidence repository. Every listed study is linked by stable register ID to a normalized paper note.

However, the hardened publication-status review of the 805-study corpus is still being finalized. Therefore:

- the current C1 rows are **verified against the current notes and register**;
- no row is considered finally frozen until all of its evidence IDs are revalidated against final `{{N_SYNTH}}` membership;
- if a cited study leaves the final synthesis set, the row must either replace it with eligible evidence or weaken/remove the corresponding claim;
- record 249 is not permitted as C1 evidence while the full-text exception remains open.

## Evidence-role definitions

C1 uses three evidence roles.

- **Primary support:** the study or studies that most directly establish the claim.
- **Corroboration:** additional studies that independently support the same direction, mechanism, or empirical pattern.
- **Boundary / contradictory evidence:** evidence that limits the scope of the claim, exposes a failure mode, or shows a setting in which the claim does not generalize. A paper's generic limitations section is not automatically treated as claim-level boundary evidence; the limitation must be relevant to the specific claim.

`None identified` means no distinct contradictory study was required or located for that claim; it does **not** mean that the literature contains no contradiction.

## C1 claim matrix

### C1-01 — Benchmark coverage is fragmented

**Manuscript location:** Abstract; §1 recurring gaps; §5.1 Evaluation environments and benchmark coverage; Table 4.

**Normalized claim:** Representative Web/GUI/data-agent benchmarks cover different parts of the agent pipeline, but no representative benchmark jointly evaluates live or executable interaction, cross-site behavior, structured field/record correctness, field-level provenance, robustness, and operational concerns across the complete source-to-dataset pipeline.

**Primary support:**

- **337 — Mind2Web**: offline real-Web demonstrations with explicit cross-task/cross-website/cross-domain splits; useful for generalization but not live recovery/execution.
- **338 — WebArena**: reproducible self-hosted execution and functional end-state checking; does not directly evaluate field-level extraction/provenance.

**Corroboration:**

- **283 — WebVoyager**: live-Web multimodal interaction improves environmental realism but weakens controlled reproducibility.
- **346 — OSWorld**: expands interaction to real computer environments but remains task/interaction centered rather than a complete extraction contract.

**Boundary evidence:** Mind2Web and WebArena deliberately optimize different evaluation properties; this supports fragmentation rather than implying either benchmark is defective. The claim is about **joint coverage**, not absence of individual capabilities.

**Quantitative evidence:** Mind2Web contains 2,350 tasks across 137 websites and 31 domains. WebArena contains 812 realistic tasks generated from 241 templates; the paper reports a large agent-human success gap (about 14.41% versus 78.24% in the reviewed baseline comparison).

**Checked source locations:**

- 337: dataset construction; Figure 1/domain-task diversity; cross-task/cross-website/cross-domain protocol; MindAct pipeline; main result tables; limitations.
- 338: environment/task construction; observation and action spaces; task/evaluation design; main results table; error analysis; limitations.

**Evidence strength:** strong cross-benchmark synthesis.

---

### C1-02 — Grounding is a distinct bottleneck from high-level reasoning

**Manuscript location:** §3.4 Grounding and action interface; §5.2 Perception, representation, and content grounding.

**Normalized claim:** A multimodal model may formulate a plausible next Web action while still failing to execute it because mapping the intended action to the correct interface element is a separate grounding problem.

**Primary support:**

- **282 — SeeAct**: explicitly separates action generation from action grounding and measures the gap between automatic and oracle grounding.

**Corroboration:**

- **441 — SeeClick**: visual GUI grounding as a dedicated capability.
- **443 — OmniParser**: structured visual parsing for agents without direct DOM access.

**Boundary evidence:** SeeAct's oracle-grounding condition is an upper-bound diagnostic, not a deployable solution. Its online evaluation also shows that multiple valid trajectories make single-reference offline evaluation imperfect.

**Quantitative evidence:** In the reviewed SeeAct results, automatic grounding variants are roughly 32–42% step success versus about 62–65% with oracle grounding; online task success is about 37.8% for automatic Choice grounding versus 51.1% with oracle grounding.

**Checked source locations:** 282: Figure 1; §2.1 formulation; §2.2 action generation; §2.3 action grounding; Figure 2; Tables 2–4; online evaluation; error analysis; impact statement.

**Evidence strength:** strong direct empirical support.

---

### C1-03 — Current Web-agent training objectives are not extraction contracts

**Manuscript location:** §3.6 Learning and adaptation; §5.4 Learning, self-improvement, and generalization; §5.4.1 Open limitation; §9.2 research agenda.

**Normalized claim:** Reinforcement learning, reward modeling, demonstrations, and trajectory synthesis can substantially improve Web-agent task behavior, but the dominant training targets remain task/trajectory/action success rather than schema adherence, field support, provenance validity, and record completeness.

**Primary support:**

- **517 — WebRL**: trains Web agents with self-evolving curriculum RL and an outcome-oriented reward signal tied to task success.

**Corroboration:**

- **536 — Web-Shepherd**: process/reward modeling for Web trajectories.
- **571 — AgentRM**: reward modeling for agent generalization.

**Boundary evidence:** WebRL strongly improves long-horizon task success, so this row does not claim that navigation-centric training is ineffective. The boundary is that such success does not by itself establish field/schema/provenance correctness.

**Quantitative evidence:** WebRL reports large WebArena-Lite gains, including Llama-3.1-8B from 4.8% to 42.4% and GLM-4-9B from 6.1% to 43.0% in the reviewed evidence.

**Checked source locations:** 517: self-evolving curriculum and outcome-reward formulation; Figure 2 framework; main WebArena-Lite results; failure analysis; complexity/long-horizon figures; ablations and replay/stability analysis.

**Evidence strength:** strong for the distinction between task-success training and extraction-specific objectives.

---

### C1-04 — Clean benchmark success overstates deployment robustness

**Manuscript location:** §5.1 benchmark observations; §5.5 Failure modes and reliability; §7.5 Failure-aware evaluation.

**Normalized claim:** Standard Web-agent benchmark scores can hide substantial brittleness to network/server failures, delayed or dynamic content, misleading interfaces, and other perturbations; recovery therefore requires explicit fault-aware evaluation rather than clean-condition task success alone.

**Primary support:**

- **639 — WAREX**: injects infrastructure/page faults into existing Web-agent benchmarks and measures task-success degradation and recovery.

**Corroboration:**

- **640 — An Illusion of Progress**: cautions that apparent benchmark gains need not equal robust capability.
- **641 — Why Do LLM-based Web Agents Fail?**: decomposes Web-agent failures hierarchically across planning/execution stages.

**Boundary evidence:** WAREX itself covers a selected fault set and therefore is a robustness stress test, not a complete model of production failures.

**Quantitative evidence:** The reviewed WAREX evidence reports network-error success drops from 12.4% to 3.7% on WebArena, 17.0% to 4.5% on REAL, and 42.0% to 2.0% on WebVoyager.

**Checked source locations:** 639: proxy architecture (Figure 1 / p.3 in the reviewed paper); injected error examples (Figure 3 / p.4); success/latency/call/cost results (Figure 4 / p.7); retry mitigation (Figure 5 / p.8); malicious-popup analysis (Figure 7 and Table 1 / pp.8–9).

**Evidence strength:** strong direct robustness evidence.

---

### C1-05 — Structured extraction benefits from schemas and executable programs, but remains incomplete

**Manuscript location:** §6.1–§6.5; Table 5.

**Normalized claim:** Explicit schemas, reusable scripts/selectors, and separated extraction/reflection components improve inspectability and structured extraction, but current systems remain bounded by page/layout assumptions and do not by themselves establish generalized live-Web extraction with field-level provenance and verification.

**Primary support:**

- **661 — AutoScraper**: reusable scraper generation, progressive HTML understanding, and cross-page executability.
- **675 — OneKE**: schema-guided Schema/Extraction/Reflection-agent architecture over Web HTML/PDF inputs.

**Corroboration:**

- **667 — SCRIBES**: RL-trained reusable extraction scripts across structurally similar Web pages.

**Boundary evidence:** AutoScraper is fragile under major DOM/layout change and multi-valued fields; OneKE is a compact demonstration/system evaluation rather than a large-scale live-Web robustness study; SCRIBES depends on structural regularity and can reward structurally consistent but semantically wrong extraction.

**Quantitative evidence:** AutoScraper evaluates reusable extraction across SWDE/Extended-SWDE/DS1 and improves its reviewed executability results; SCRIBES reports >13% script-quality improvement over compared baselines and >4% downstream QA improvement for GPT-4o with extracted triples.

**Checked source locations:**

- 661: Figures 1–2; scraper-generation formulation; SWDE/Extended-SWDE/DS1 experiments; executability metric; Table 6 efficiency; error analysis.
- 675: system architecture (Schema/Extraction/Reflection agents); NER/RE benchmark evaluation; Web-news/PDF case studies; results/limitations.
- 667: Figures 1–3; Table 1 script results; Table 4 QA gains; Figure 5/Table 5 HTML deduplication; holdout/noisy-reward analyses.

**Evidence strength:** strong multi-method synthesis.

---

### C1-06 — Open-ended Web aggregation is not equivalent to schema-bound dataset extraction

**Manuscript location:** §5.6 Deep research and information-seeking agents; §6.3 source discovery; §6.6 provenance/verification.

**Normalized claim:** Search and aggregation agents can improve multi-source discovery and synthesis, but answer/report-level aggregation does not ensure schema-bound row coverage, field-level provenance, or complete dataset assembly.

**Primary support:**

- **663 — INFOGENT**: Navigator–Extractor–Aggregator framework under API/text and interactive visual access.

**Corroboration:**

- **692 — WiNELL**: continuous source discovery, update aggregation, citations, and human review for Wikipedia updating.

**Boundary evidence:** INFOGENT's evaluated output is answer-level aggregation rather than schema-bound row extraction; WiNELL is specialized to Wikipedia updating and relies on human review/historical-edit evaluation.

**Quantitative evidence:** INFOGENT reports a 7% improvement over its compared multi-agent search framework on FRAMES and a 4.3% improvement over the compared information-seeking Web agent on AssistantBench in the reviewed settings.

**Checked source locations:**

- 663: Figure 1 access modes and Navigator–Extractor–Aggregator loop; FRAMES/AssistantBench main results; component/action analysis; qualitative errors and limitations.
- 692: section-criteria induction; agentic update aggregation; fine-grained editing; historical evaluation; key findings and limitations in the complete reviewed paper.

**Evidence strength:** strong conceptual/empirical boundary between aggregation and extraction.

---

### C1-07 — Automatic agent evaluators are themselves fallible

**Manuscript location:** §5.1 evaluator discussion; §6.6 provenance and verification; §7.4 Evaluator validity and statistical reporting.

**Normalized claim:** Rule/programmatic checks and LLM judges each have blind spots; LLM judgment can add semantic flexibility but should supplement rather than replace deterministic checks when values, types, state, or source evidence can be verified programmatically.

**Primary support:**

- **356 — AgentRewardBench**: meta-evaluates automatic trajectory judges against expert annotations.

**Corroboration:**

- **731 — R-Judge**: shows remaining error in safety-risk recognition over multi-turn agent trajectories.

**Boundary evidence:** Rule-based evaluators can undercount valid alternative trajectories, whereas flexible LLM judges introduce prompt/model bias and lower determinism. Thus neither family is treated as universal ground truth.

**Quantitative evidence:** AgentRewardBench includes 1,302 trajectories from five benchmarks and four source agents/models, expert labels, and 12 automatic evaluators; no single LLM judge dominates every setting. R-Judge reports GPT-4o at 74.45 F1 on its safety-judgment task in the reviewed evidence.

**Checked source locations:**

- 356: benchmark construction; expert annotation protocol; automatic-judge comparison; correlation/accuracy analyses; error analysis and limitations.
- 731: dataset/risk taxonomy pp.1–5 and 13–16; eleven-model evaluation pp.5–8; failure analysis/limitations pp.8–9.

**Evidence strength:** strong meta-evaluation evidence.

---

### C1-08 — Web/environment content is an active security boundary

**Manuscript location:** §8.1 Prompt, visual, and environmental injection; Figure 7; Table 6.

**Normalized claim:** A Web agent must treat externally controlled page/environment content as untrusted because it can act simultaneously as task data and as an adversarial instruction or grounding channel, causing unsafe actions, privacy leakage, or target redirection.

**Primary support:**

- **695 — InjecAgent**: indirect prompt injection through externally retrieved/tool content.
- **702 — EIA**: environment-adapted Web injection for privacy leakage.

**Corroboration:**

- **709 — WebInject**: Web-agent prompt injection attacks.
- **713 — VisualTrap**: visual-grounding backdoor that redirects otherwise correct action plans.

**Boundary evidence:** Threat models differ. InjecAgent uses a finite tool/task universe; EIA assumes attacker influence over Web elements; VisualTrap assumes training/supply-chain poisoning rather than ordinary runtime page injection. These boundaries prevent treating any single attack success rate as universal.

**Quantitative evidence:** InjecAgent contains 1,054 test cases and evaluates 30 agent configurations; a reviewed ReAct/GPT-4 configuration is compromised in 24% of cases. EIA evaluates 177 PII-related action steps and reports up to 70% attack success for specific-PII theft in the reviewed setting. VisualTrap reports high grounding attack-success rates under its poisoning threat model.

**Checked source locations:**

- 695: benchmark construction; user/attacker-tool pairing; attack-intention classes; 30-agent evaluation; reinforced attack setting; defenses/limitations.
- 702: privacy threat model; 177 PII-related Mind2Web steps; specific-PII/full-request targets; stealth tests; defensive prompts; deployment-stage defenses.
- 713: poisoning design; Qwen/LLaVA experiments; clean accuracy; transfer; persistence after clean fine-tuning.

**Evidence strength:** strong across multiple independent threat models.

---

### C1-09 — Safety must control the execution loop, not only the final answer

**Manuscript location:** §8.3 Unsafe tools and policy enforcement; Table 6.

**Normalized claim:** Moderating only the final model response is insufficient for tool-using agents because unsafe choices or harmful tool calls can occur during input interpretation and execution; safety therefore requires controls at the tool/action boundary as well as output monitoring.

**Primary support:**

- **734 — ToolSword**: safety benchmark explicitly spanning input, execution, and output stages of tool use.

**Corroboration:**

- **731 — R-Judge**: trajectory-level risk monitoring shows safety recognition remains imperfect.
- **738 — GuardAgent**: illustrates an external policy-enforcement layer that translates natural-language rules into executable checks.

**Boundary evidence:** ToolSword isolates controlled scenarios and evaluates vulnerabilities rather than a complete defense. R-Judge is post-hoc monitoring, not prevention. GuardAgent performs strongly on author-defined benchmark rules but does not establish end-to-end security against adaptive attackers or incomplete logging.

**Quantitative evidence:** ToolSword uses 440 samples and 100 constructed tools; the reviewed results include GPT-4 at 63.64% attack success on unmodified malicious queries and an average unsafe-output rate of 65.45% in harmful-feedback tests. GuardAgent exceeds 98% label accuracy on EICU-AC and 83% on Mind2Web-SC depending on model, within its benchmark setting.

**Checked source locations:**

- 734: benchmark/scenario construction pp.1–4; model setup and input/execution/output results pp.4–8; analysis/limitations pp.8–9.
- 731: dataset/risk taxonomy pp.1–5,13–16; model results pp.5–8; limitations pp.8–9.
- 738: architecture/workflow pp.1–5; benchmarks/metrics/ablations pp.3–9; conclusions/future work p.9.

**Evidence strength:** strong for lifecycle-stage safety; moderate for specific defense generalization.

---

### C1-10 — A plausible trajectory or final state does not establish data integrity

**Manuscript location:** §5.5 Failure modes and reliability; §6.5–§6.6 field extraction/provenance; §8.4 Output integrity and observability.

**Normalized claim:** An agent trajectory can appear behaviorally normal or terminate successfully while the resulting structured data remain incomplete, mis-associated, unsupported, or corrupted; extraction reliability therefore requires field/source/schema checks in addition to trajectory monitoring.

**Primary support:**

- **659 — Detecting Silent Failures in Multi-Agentic AI Trajectories**: demonstrates drift, cycles, missing-detail, tool, and context-propagation failures that may not surface as explicit errors.

**Corroboration:**

- **639 — WAREX**: shows that execution reliability deteriorates under realistic faults and that apparent clean-condition competence is not robust.
- **675 — OneKE**: schema/reflection structure demonstrates that structured extraction itself needs explicit checking beyond navigation.

**Boundary evidence:** Record 659 is a short work-in-progress-style conference paper over two non-browser multi-agent applications, so it supports the existence of silent trajectory anomalies but not a universal field-integrity detector. The field-level integrity conclusion is a synthesis step combining failure-monitoring evidence with extraction-system requirements.

**Quantitative evidence:** The reviewed Silent Failures study analyzes 4,275 traces in one application and 894 in another; supervised/semi-supervised detectors achieve high in-domain accuracy while subtle drift remains difficult.

**Checked source locations:**

- 659: complete seven-page current-cycle full-text extraction; dataset construction, trace-feature methodology, failure taxonomy, model results, and limitations.
- 639: injected-fault performance and recovery analyses listed in C1-04.
- 675: schema/extraction/reflection architecture and empirical case studies listed in C1-05.

**Evidence strength:** moderate cross-domain synthesis; wording should remain about the need for layered checks rather than claiming a proven universal detector.

---

### C1-11 — No reviewed system closes the complete generalized-extraction contract

**Manuscript location:** §6.8 Comparative synthesis; Table 5; Abstract/Conclusion central argument.

**Normalized claim:** Across the representative reviewed systems, no single system jointly demonstrates all of the following as an end-to-end evaluated capability: unfamiliar-site navigation, explicit schema coverage, field-level provenance, unsupported-value control, cross-site transfer, and complete dataset assembly.

**Evidence type:** cross-study absence/boundary synthesis. This claim cannot be established by one paper; it is supported by comparing what each representative system does and, critically, what it does not evaluate.

**Primary comparison set:**

- **661 — AutoScraper:** executable reusable extraction, but site/layout regularity and field-handling limits; not a generalized interactive provenance-aware pipeline.
- **675 — OneKE:** explicit schema-guided agentic extraction, but compact demo evaluation without large-scale live-Web robustness or field-level provenance.
- **667 — SCRIBES:** cross-page reusable scripts and holdout evaluation, but semi-structured/layout-dependent and not an interactive source-to-dataset agent.
- **663 — INFOGENT:** multi-source navigation/aggregation, but answer-level rather than schema-bound row/field extraction.
- **692 — WiNELL:** continuous citation-aware updating, but Wikipedia-specific and human-reviewed rather than generalized structured Web extraction.
- **338 — WebArena:** realistic executable navigation and functional end-state checks, but not field-level extraction/provenance/dataset assembly.

**Corroboration:** Table 4/benchmark fragmentation (C1-01) and evaluator limitations (C1-07) reinforce the absence of a benchmark/system demonstration covering the entire contract jointly.

**Contradictory / boundary evidence:** Each system demonstrates substantial pieces of the contract; therefore the claim must remain **joint/complete-coverage**, not “no system supports schemas/provenance/generalization.” Future systems or updated versions can falsify the claim, so it is bounded by the April 2026 review cutoff and final synthesis membership.

**Quantitative evidence:** quantitative results remain attached to the component studies (e.g., AutoScraper executability, SCRIBES script/QA gains, INFOGENT benchmark gains, WebArena task results). They should not be collapsed into a synthetic numeric score because the tasks and metrics are heterogeneous.

**Checked source locations:** use the C1-01, C1-05, and C1-06 source-location entries for the six systems above, plus manuscript Table 5's explicit cross-system strength/weakness comparison.

**Evidence strength:** strong cross-study qualitative synthesis, conditional on final membership and the review cutoff.

## Machine-readable artifact

`data/c1_claim_evidence_matrix.csv` contains the same 11 claims in a machine-readable form for final membership checks and A3 consistency validation.

## C1 finalization rules

C1 is fully closed only when all of the following pass:

1. every load-bearing claim has a stable `C1-XX` ID;
2. every study ID resolves to the 805-study register and an available evidence note;
3. every supporting study belongs to final `{{N_SYNTH}}` or is explicitly marked as contextual/non-load-bearing;
4. every primary evidence item has a checked paper location or an explicit location-resolution TODO before submission;
5. claim-level boundary/contradictory evidence is recorded where material rather than inferred from generic paper limitations;
6. quantitative values are tied to the study that reported them and are not compared across incompatible benchmarks as if commensurate;
7. the strongest absence claims (especially C1-11) are rechecked after final membership/status reconciliation;
8. the manuscript's §2.4 claim about claim-level evidence is retained only after this matrix passes the final audit;
9. the reviewer response links this matrix as the requested claim → study → source-location artifact.

## Current closure state

**C1 is structurally built and evidence-mapped against the current manuscript/current repository. Final publication-status and `{{N_SYNTH}}` membership revalidation is pending.**
