# S4 - P2 Papers (Merged)

> **Generated on:** 2026-05-08 21:01:52
> **Total files merged:** 82

---

<!-- ========== FILE: S4_P2\paper_first_notes\README.md ========== -->

## Source: `S4_P2\paper_first_notes\README.md`

# S4 P2 Paper-First Detailed Notes

This ZIP contains one markdown file per S4 P2 paper.

Structure:
1. Metadata
2. Simple understanding
3. Core idea
4. Key finding
5. Key evidence
6. Limitations
7. Relation to S4
8. Relation to thesis
9. How to use in literature review
10. Reading decision
11. One-sentence summary
12. BibTeX placeholder


---

<!-- ========== FILE: S4_P2\paper_first_notes\S4_P2_01_Mapping_Natural_Language_Instructions_to_Mobile_UI_Action_Sequences.md ========== -->

## Source: `S4_P2\paper_first_notes\S4_P2_01_Mapping_Natural_Language_Instructions_to_Mobile_UI_Action_Sequences.md`

# S4 P2 Paper 01 — Mapping Natural Language Instructions to Mobile UI Action Sequences

## Metadata

- **Title:** Mapping Natural Language Instructions to Mobile UI Action Sequences
- **Year:** 2020
- **Venue / status:** ACL 2020 main conference
- **Peer-reviewed status:** Yes
- **Publication type:** Peer-reviewed conference paper
- **Thesis section:** S4 — LLM-based web, GUI, mobile, and computer-use agents
- **Category:** mobile UI instruction grounding / action sequence prediction
- **Priority:** P2
- **BibTeX key:** `mappingnaturallanguageinstructionst2020`

---

## Simple understanding

This paper studies how to map a natural-language instruction into a sequence of mobile UI actions. It is an early foundation for mobile GUI agents because it frames phone automation as instruction understanding plus UI action prediction.

In simple terms:

```text
Problem → how can an AI agent interact with a web, GUI, mobile, desktop, or application environment?
Method → add perception, planning, action, memory, API/tool use, state tracking, or browser control.
Goal → complete real user tasks more flexibly than scripts or static chatbots.
```

This note explains the paper first, then connects it to S4 and your thesis.

---

## Core idea

Ground user instructions to concrete mobile interface actions, such as tapping, typing, and navigating through app screens.

The paper is mainly about:

```text
mobile UI instruction grounding / action sequence prediction
```

It contributes to the larger agent loop:

```text
observe → understand state → plan → act → receive feedback → verify / recover → complete task
```

---

## Key finding / main claim

The paper shows that mobile task automation can be modeled as predicting action sequences over UI states, creating a foundation for later LLM-powered mobile GUI agents.

For S4, the important question is not only whether the method works on its benchmark, but **which part of web/GUI agency it improves**:

- perception and grounding,
- planning and reasoning,
- action execution,
- API/tool use,
- memory/state tracking,
- recovery and verification,
- or deployment/evaluation.

---

## Key evidence to extract from the paper

When reading the paper, extract these points:

- **Dataset/task formulation mapping instructions to mobile UI actions.**
- **Model setup for action sequence prediction.**
- **Evaluation of instruction-to-action grounding accuracy.**

These are the most useful parts for writing a literature-review paragraph.

---

## Limitations

- **Limitation 1:** It predates modern LLM/VLM agent architectures and therefore does not use strong multimodal reasoning models.
- **Limitation 2:** It focuses on mobile UI action prediction rather than open-ended web/browser automation.
- **Limitation 3:** It depends on datasets and UI representations that may not generalize to all real-world apps.

General thesis-level limitation:

```text
Improving one agent component is not enough for generalized web automation.
A robust web agent still needs grounding, planning, execution, verification, recovery, and safety.
```

---

## Relation to S4

This paper belongs in S4 because S4 discusses **LLM-based agents for web/GUI/mobile/computer automation**.

Its role in S4 is:

```text
Mapping Natural Language Instructions to Mobile UI Action Sequences
→ mobile UI instruction grounding / action sequence prediction
→ supporting P2 source for web/GUI/computer-use agent discussion
```

Use it after explaining what the paper does. Do not introduce it only as “P2”; introduce the method or idea first.

---

## Relation to thesis topic

Your thesis topic is:

```text
LLM-based agents for generalized web automation and data extraction
```

This paper matters because:

It provides historical grounding for the transition from classical/mobile UI automation to LLM-powered phone agents.

For generalized web automation, the connection is:

```text
web / GUI / mobile / computer-use interaction
→ agent observes a digital environment
→ agent chooses actions
→ agent extracts information or completes a workflow
```

Even when the paper is not directly about data extraction, it still helps explain the automation layer needed before extraction can be generalized.

---

## How to use this paper in the literature review

Recommended use:

- Use as **P2 support**, not as the central backbone.
- Use for one precise idea, architecture, benchmark, or limitation.
- If peer-reviewed, it can support stronger claims.
- If preprint/workshop/technical report, use it for recent trends and emerging directions.

Suggested sentence:

> Mapping Natural Language Instructions to Mobile UI Action Sequences shows how mobile UI instruction grounding / action sequence prediction contributes to the development of LLM-based agents for digital task automation, but its limitations indicate that generalized web automation still requires stronger grounding, verification, and recovery mechanisms.

---

## Reading decision

- **Keep in S4 P2:** Yes
- **Read fully?** Yes or selected sections carefully
- **Depth needed:** Medium to high
- **Main use:** Support S4 discussion of mobile UI instruction grounding / action sequence prediction
- **Most important parts:**
  - Abstract
  - Introduction
  - Main architecture / method figure
  - Dataset or benchmark section
  - Results table
  - Limitations / discussion

---

## One-sentence summary

Mapping Natural Language Instructions to Mobile UI Action Sequences is a P2 supporting paper for S4 because it explains **mobile UI instruction grounding / action sequence prediction**, but it should be cited according to its venue/status and not overused beyond its evidence.

---

## BibTeX placeholder

```bibtex
@misc{mappingnaturallanguageinstructionst2020,
  title = {Mapping Natural Language Instructions to Mobile UI Action Sequences},
  year = {2020},
  note = {ACL 2020 main conference; Peer-reviewed conference paper. Verify final bibliographic metadata before thesis submission.}
}
```


---

<!-- ========== FILE: S4_P2\paper_first_notes\S4_P2_02_Grounding_Open-Domain_Instructions_to_Automate_Web_Support_Tasks.md ========== -->

## Source: `S4_P2\paper_first_notes\S4_P2_02_Grounding_Open-Domain_Instructions_to_Automate_Web_Support_Tasks.md`

# S4 P2 Paper 02 — Grounding Open-Domain Instructions to Automate Web Support Tasks

## Metadata

- **Title:** Grounding Open-Domain Instructions to Automate Web Support Tasks
- **Year:** 2021
- **Venue / status:** NAACL-HLT 2021 main conference
- **Peer-reviewed status:** Yes
- **Publication type:** Peer-reviewed conference paper
- **Thesis section:** S4 — LLM-based web automation and web agents
- **Category:** open-domain web-support automation
- **Priority:** P2
- **BibTeX key:** `groundingopendomaininstructionstoau2021`

---

## Simple understanding

This paper studies how to ground open-domain user instructions into executable steps for web support tasks. It is important because it moves beyond fixed scripts toward instruction-driven web task automation.

In simple terms:

```text
Problem → how can an AI agent interact with a web, GUI, mobile, desktop, or application environment?
Method → add perception, planning, action, memory, API/tool use, state tracking, or browser control.
Goal → complete real user tasks more flexibly than scripts or static chatbots.
```

This note explains the paper first, then connects it to S4 and your thesis.

---

## Core idea

Translate natural-language support instructions into structured actions that can be executed on websites.

The paper is mainly about:

```text
open-domain web-support automation
```

It contributes to the larger agent loop:

```text
observe → understand state → plan → act → receive feedback → verify / recover → complete task
```

---

## Key finding / main claim

The work shows that grounding open-domain web instructions requires connecting language understanding with web state, task representation, and executable action generation.

For S4, the important question is not only whether the method works on its benchmark, but **which part of web/GUI agency it improves**:

- perception and grounding,
- planning and reasoning,
- action execution,
- API/tool use,
- memory/state tracking,
- recovery and verification,
- or deployment/evaluation.

---

## Key evidence to extract from the paper

When reading the paper, extract these points:

- **Task definition for open-domain web support automation.**
- **Grounding method from instructions to executable representations.**
- **Evaluation on web-support task completion or grounding accuracy.**

These are the most useful parts for writing a literature-review paragraph.

---

## Limitations

- **Limitation 1:** The system is more structured and task-specific than later general web agents.
- **Limitation 2:** It does not use modern multimodal LLMs or visual browser grounding.
- **Limitation 3:** It is mainly about support-task grounding, not generalized web automation across arbitrary sites.

General thesis-level limitation:

```text
Improving one agent component is not enough for generalized web automation.
A robust web agent still needs grounding, planning, execution, verification, recovery, and safety.
```

---

## Relation to S4

This paper belongs in S4 because S4 discusses **LLM-based agents for web/GUI/mobile/computer automation**.

Its role in S4 is:

```text
Grounding Open-Domain Instructions to Automate Web Support Tasks
→ open-domain web-support automation
→ supporting P2 source for web/GUI/computer-use agent discussion
```

Use it after explaining what the paper does. Do not introduce it only as “P2”; introduce the method or idea first.

---

## Relation to thesis topic

Your thesis topic is:

```text
LLM-based agents for generalized web automation and data extraction
```

This paper matters because:

It is an early peer-reviewed source showing how web automation can be framed as language grounding plus executable web actions.

For generalized web automation, the connection is:

```text
web / GUI / mobile / computer-use interaction
→ agent observes a digital environment
→ agent chooses actions
→ agent extracts information or completes a workflow
```

Even when the paper is not directly about data extraction, it still helps explain the automation layer needed before extraction can be generalized.

---

## How to use this paper in the literature review

Recommended use:

- Use as **P2 support**, not as the central backbone.
- Use for one precise idea, architecture, benchmark, or limitation.
- If peer-reviewed, it can support stronger claims.
- If preprint/workshop/technical report, use it for recent trends and emerging directions.

Suggested sentence:

> Grounding Open-Domain Instructions to Automate Web Support Tasks shows how open-domain web-support automation contributes to the development of LLM-based agents for digital task automation, but its limitations indicate that generalized web automation still requires stronger grounding, verification, and recovery mechanisms.

---

## Reading decision

- **Keep in S4 P2:** Yes
- **Read fully?** Yes or selected sections carefully
- **Depth needed:** Medium to high
- **Main use:** Support S4 discussion of open-domain web-support automation
- **Most important parts:**
  - Abstract
  - Introduction
  - Main architecture / method figure
  - Dataset or benchmark section
  - Results table
  - Limitations / discussion

---

## One-sentence summary

Grounding Open-Domain Instructions to Automate Web Support Tasks is a P2 supporting paper for S4 because it explains **open-domain web-support automation**, but it should be cited according to its venue/status and not overused beyond its evidence.

---

## BibTeX placeholder

```bibtex
@misc{groundingopendomaininstructionstoau2021,
  title = {Grounding Open-Domain Instructions to Automate Web Support Tasks},
  year = {2021},
  note = {NAACL-HLT 2021 main conference; Peer-reviewed conference paper. Verify final bibliographic metadata before thesis submission.}
}
```


---

<!-- ========== FILE: S4_P2\paper_first_notes\S4_P2_03_SYNAPSE_Leveraging_Few-Shot_Exemplars_for_Human-Level_Computer_Control.md ========== -->

## Source: `S4_P2\paper_first_notes\S4_P2_03_SYNAPSE_Leveraging_Few-Shot_Exemplars_for_Human-Level_Computer_Control.md`

# S4 P2 Paper 03 — SYNAPSE: Leveraging Few-Shot Exemplars for Human-Level Computer Control

## Metadata

- **Title:** SYNAPSE: Leveraging Few-Shot Exemplars for Human-Level Computer Control
- **Year:** 2023
- **Venue / status:** arXiv preprint
- **Peer-reviewed status:** No confirmed archival venue
- **Publication type:** Preprint
- **Thesis section:** S4 — computer-use and GUI-agent foundations
- **Category:** few-shot computer control / MiniWoB-style GUI automation
- **Priority:** P2
- **BibTeX key:** `synapseleveragingfewshotexemplarsfo2023`

---

## Simple understanding

SYNAPSE explores whether few-shot prompting can enable LLMs to control computers or web interfaces. It uses examples to guide action selection in interactive environments.

In simple terms:

```text
Problem → how can an AI agent interact with a web, GUI, mobile, desktop, or application environment?
Method → add perception, planning, action, memory, API/tool use, state tracking, or browser control.
Goal → complete real user tasks more flexibly than scripts or static chatbots.
```

This note explains the paper first, then connects it to S4 and your thesis.

---

## Core idea

Use few-shot exemplars to help an LLM infer how to perform computer-control tasks through actions.

The paper is mainly about:

```text
few-shot computer control / MiniWoB-style GUI automation
```

It contributes to the larger agent loop:

```text
observe → understand state → plan → act → receive feedback → verify / recover → complete task
```

---

## Key finding / main claim

Few-shot examples can improve action prediction and task completion in controlled computer-use environments.

For S4, the important question is not only whether the method works on its benchmark, but **which part of web/GUI agency it improves**:

- perception and grounding,
- planning and reasoning,
- action execution,
- API/tool use,
- memory/state tracking,
- recovery and verification,
- or deployment/evaluation.

---

## Key evidence to extract from the paper

When reading the paper, extract these points:

- **Prompting design with few-shot exemplars.**
- **Computer-control benchmark results.**
- **Analysis of where exemplar-based control succeeds or fails.**

These are the most useful parts for writing a literature-review paragraph.

---

## Limitations

- **Limitation 1:** The uploaded/known status is preprint, so cite carefully.
- **Limitation 2:** Controlled benchmarks are simpler than real dynamic web environments.
- **Limitation 3:** Few-shot prompting alone may be brittle for long-horizon tasks and UI changes.

General thesis-level limitation:

```text
Improving one agent component is not enough for generalized web automation.
A robust web agent still needs grounding, planning, execution, verification, recovery, and safety.
```

---

## Relation to S4

This paper belongs in S4 because S4 discusses **LLM-based agents for web/GUI/mobile/computer automation**.

Its role in S4 is:

```text
SYNAPSE: Leveraging Few-Shot Exemplars for Human-Level Computer Control
→ few-shot computer control / MiniWoB-style GUI automation
→ supporting P2 source for web/GUI/computer-use agent discussion
```

Use it after explaining what the paper does. Do not introduce it only as “P2”; introduce the method or idea first.

---

## Relation to thesis topic

Your thesis topic is:

```text
LLM-based agents for generalized web automation and data extraction
```

This paper matters because:

It supports the transition from static LLM prompting to interactive computer-use agents.

For generalized web automation, the connection is:

```text
web / GUI / mobile / computer-use interaction
→ agent observes a digital environment
→ agent chooses actions
→ agent extracts information or completes a workflow
```

Even when the paper is not directly about data extraction, it still helps explain the automation layer needed before extraction can be generalized.

---

## How to use this paper in the literature review

Recommended use:

- Use as **P2 support**, not as the central backbone.
- Use for one precise idea, architecture, benchmark, or limitation.
- If peer-reviewed, it can support stronger claims.
- If preprint/workshop/technical report, use it for recent trends and emerging directions.

Suggested sentence:

> SYNAPSE: Leveraging Few-Shot Exemplars for Human-Level Computer Control shows how few-shot computer control / MiniWoB-style GUI automation contributes to the development of LLM-based agents for digital task automation, but its limitations indicate that generalized web automation still requires stronger grounding, verification, and recovery mechanisms.

---

## Reading decision

- **Keep in S4 P2:** Yes
- **Read fully?** No, selected sections are enough unless promoted later
- **Depth needed:** Low to medium
- **Main use:** Support S4 discussion of few-shot computer control / MiniWoB-style GUI automation
- **Most important parts:**
  - Abstract
  - Introduction
  - Main architecture / method figure
  - Dataset or benchmark section
  - Results table
  - Limitations / discussion

---

## One-sentence summary

SYNAPSE: Leveraging Few-Shot Exemplars for Human-Level Computer Control is a P2 supporting paper for S4 because it explains **few-shot computer control / MiniWoB-style GUI automation**, but it should be cited according to its venue/status and not overused beyond its evidence.

---

## BibTeX placeholder

```bibtex
@misc{synapseleveragingfewshotexemplarsfo2023,
  title = {SYNAPSE: Leveraging Few-Shot Exemplars for Human-Level Computer Control},
  year = {2023},
  note = {arXiv preprint; Preprint. Verify final bibliographic metadata before thesis submission.}
}
```


---

<!-- ========== FILE: S4_P2\paper_first_notes\S4_P2_04_WebGLM_Towards_an_Efficient_Web-Enhanced_Question_Answering_System_with_Human_Preferences.md ========== -->

## Source: `S4_P2\paper_first_notes\S4_P2_04_WebGLM_Towards_an_Efficient_Web-Enhanced_Question_Answering_System_with_Human_Preferences.md`

# S4 P2 Paper 04 — WebGLM: Towards an Efficient Web-Enhanced Question Answering System with Human Preferences

## Metadata

- **Title:** WebGLM: Towards an Efficient Web-Enhanced Question Answering System with Human Preferences
- **Year:** 2023
- **Venue / status:** KDD 2023
- **Peer-reviewed status:** Yes
- **Publication type:** Peer-reviewed conference paper
- **Thesis section:** S4 — web-enhanced LLM systems and information agents
- **Category:** web-enhanced QA / retrieval and browsing
- **Priority:** P2
- **BibTeX key:** `webglmtowardsanefficientwebenhanced2023`

---

## Simple understanding

WebGLM is a web-enhanced question answering system that uses web search and human preference alignment to answer questions more effectively.

In simple terms:

```text
Problem → how can an AI agent interact with a web, GUI, mobile, desktop, or application environment?
Method → add perception, planning, action, memory, API/tool use, state tracking, or browser control.
Goal → complete real user tasks more flexibly than scripts or static chatbots.
```

This note explains the paper first, then connects it to S4 and your thesis.

---

## Core idea

Combine LLM generation with web retrieval/browsing and human preference optimization for web-grounded QA.

The paper is mainly about:

```text
web-enhanced QA / retrieval and browsing
```

It contributes to the larger agent loop:

```text
observe → understand state → plan → act → receive feedback → verify / recover → complete task
```

---

## Key finding / main claim

Web-enhanced systems can improve answer factuality and usefulness by grounding generation in online information.

For S4, the important question is not only whether the method works on its benchmark, but **which part of web/GUI agency it improves**:

- perception and grounding,
- planning and reasoning,
- action execution,
- API/tool use,
- memory/state tracking,
- recovery and verification,
- or deployment/evaluation.

---

## Key evidence to extract from the paper

When reading the paper, extract these points:

- **System pipeline for web-enhanced QA.**
- **Human preference or alignment component.**
- **KDD evaluation results comparing web-enhanced answers.**

These are the most useful parts for writing a literature-review paragraph.

---

## Limitations

- **Limitation 1:** It is mainly QA-oriented, not a general web-control or browser-action agent.
- **Limitation 2:** It does not focus on completing transactional web tasks like forms, carts, or account operations.
- **Limitation 3:** Web retrieval quality and source reliability still constrain output quality.

General thesis-level limitation:

```text
Improving one agent component is not enough for generalized web automation.
A robust web agent still needs grounding, planning, execution, verification, recovery, and safety.
```

---

## Relation to S4

This paper belongs in S4 because S4 discusses **LLM-based agents for web/GUI/mobile/computer automation**.

Its role in S4 is:

```text
WebGLM: Towards an Efficient Web-Enhanced Question Answering System with Human Preferences
→ web-enhanced QA / retrieval and browsing
→ supporting P2 source for web/GUI/computer-use agent discussion
```

Use it after explaining what the paper does. Do not introduce it only as “P2”; introduce the method or idea first.

---

## Relation to thesis topic

Your thesis topic is:

```text
LLM-based agents for generalized web automation and data extraction
```

This paper matters because:

It connects web retrieval and LLM generation, which is a foundation for later deep-research and web information agents.

For generalized web automation, the connection is:

```text
web / GUI / mobile / computer-use interaction
→ agent observes a digital environment
→ agent chooses actions
→ agent extracts information or completes a workflow
```

Even when the paper is not directly about data extraction, it still helps explain the automation layer needed before extraction can be generalized.

---

## How to use this paper in the literature review

Recommended use:

- Use as **P2 support**, not as the central backbone.
- Use for one precise idea, architecture, benchmark, or limitation.
- If peer-reviewed, it can support stronger claims.
- If preprint/workshop/technical report, use it for recent trends and emerging directions.

Suggested sentence:

> WebGLM: Towards an Efficient Web-Enhanced Question Answering System with Human Preferences shows how web-enhanced QA / retrieval and browsing contributes to the development of LLM-based agents for digital task automation, but its limitations indicate that generalized web automation still requires stronger grounding, verification, and recovery mechanisms.

---

## Reading decision

- **Keep in S4 P2:** Yes
- **Read fully?** Yes or selected sections carefully
- **Depth needed:** Medium to high
- **Main use:** Support S4 discussion of web-enhanced QA / retrieval and browsing
- **Most important parts:**
  - Abstract
  - Introduction
  - Main architecture / method figure
  - Dataset or benchmark section
  - Results table
  - Limitations / discussion

---

## One-sentence summary

WebGLM: Towards an Efficient Web-Enhanced Question Answering System with Human Preferences is a P2 supporting paper for S4 because it explains **web-enhanced QA / retrieval and browsing**, but it should be cited according to its venue/status and not overused beyond its evidence.

---

## BibTeX placeholder

```bibtex
@misc{webglmtowardsanefficientwebenhanced2023,
  title = {WebGLM: Towards an Efficient Web-Enhanced Question Answering System with Human Preferences},
  year = {2023},
  note = {KDD 2023; Peer-reviewed conference paper. Verify final bibliographic metadata before thesis submission.}
}
```


---

<!-- ========== FILE: S4_P2\paper_first_notes\S4_P2_05_A_Zero-Shot_Language_Agent_for_Computer_Control_with_Structured_Reflection.md ========== -->

## Source: `S4_P2\paper_first_notes\S4_P2_05_A_Zero-Shot_Language_Agent_for_Computer_Control_with_Structured_Reflection.md`

# S4 P2 Paper 05 — A Zero-Shot Language Agent for Computer Control with Structured Reflection

## Metadata

- **Title:** A Zero-Shot Language Agent for Computer Control with Structured Reflection
- **Year:** 2023
- **Venue / status:** arXiv preprint
- **Peer-reviewed status:** No confirmed archival venue
- **Publication type:** Preprint
- **Thesis section:** S4 — computer-use agents and reflective web/GUI control
- **Category:** zero-shot computer control / reflection
- **Priority:** P2
- **BibTeX key:** `azeroshotlanguageagentforcomputerco2023`

---

## Simple understanding

This paper studies a language agent that controls a computer using structured reflection without task-specific training.

In simple terms:

```text
Problem → how can an AI agent interact with a web, GUI, mobile, desktop, or application environment?
Method → add perception, planning, action, memory, API/tool use, state tracking, or browser control.
Goal → complete real user tasks more flexibly than scripts or static chatbots.
```

This note explains the paper first, then connects it to S4 and your thesis.

---

## Core idea

Use zero-shot LLM reasoning and structured reflection to select actions and improve future decisions during computer control.

The paper is mainly about:

```text
zero-shot computer control / reflection
```

It contributes to the larger agent loop:

```text
observe → understand state → plan → act → receive feedback → verify / recover → complete task
```

---

## Key finding / main claim

Reflection can improve interactive performance by helping the agent reason about previous actions and current state.

For S4, the important question is not only whether the method works on its benchmark, but **which part of web/GUI agency it improves**:

- perception and grounding,
- planning and reasoning,
- action execution,
- API/tool use,
- memory/state tracking,
- recovery and verification,
- or deployment/evaluation.

---

## Key evidence to extract from the paper

When reading the paper, extract these points:

- **Reflection structure used by the agent.**
- **Computer-control environment or benchmark results.**
- **Failure cases showing limits of reflection.**

These are the most useful parts for writing a literature-review paragraph.

---

## Limitations

- **Limitation 1:** Preprint status means it should be cited carefully.
- **Limitation 2:** Zero-shot reflection can still be wrong or ungrounded.
- **Limitation 3:** It may not scale reliably to complex real-world websites and desktop workflows.

General thesis-level limitation:

```text
Improving one agent component is not enough for generalized web automation.
A robust web agent still needs grounding, planning, execution, verification, recovery, and safety.
```

---

## Relation to S4

This paper belongs in S4 because S4 discusses **LLM-based agents for web/GUI/mobile/computer automation**.

Its role in S4 is:

```text
A Zero-Shot Language Agent for Computer Control with Structured Reflection
→ zero-shot computer control / reflection
→ supporting P2 source for web/GUI/computer-use agent discussion
```

Use it after explaining what the paper does. Do not introduce it only as “P2”; introduce the method or idea first.

---

## Relation to thesis topic

Your thesis topic is:

```text
LLM-based agents for generalized web automation and data extraction
```

This paper matters because:

It supports the idea that GUI/web agents need feedback and self-evaluation, not only action prediction.

For generalized web automation, the connection is:

```text
web / GUI / mobile / computer-use interaction
→ agent observes a digital environment
→ agent chooses actions
→ agent extracts information or completes a workflow
```

Even when the paper is not directly about data extraction, it still helps explain the automation layer needed before extraction can be generalized.

---

## How to use this paper in the literature review

Recommended use:

- Use as **P2 support**, not as the central backbone.
- Use for one precise idea, architecture, benchmark, or limitation.
- If peer-reviewed, it can support stronger claims.
- If preprint/workshop/technical report, use it for recent trends and emerging directions.

Suggested sentence:

> A Zero-Shot Language Agent for Computer Control with Structured Reflection shows how zero-shot computer control / reflection contributes to the development of LLM-based agents for digital task automation, but its limitations indicate that generalized web automation still requires stronger grounding, verification, and recovery mechanisms.

---

## Reading decision

- **Keep in S4 P2:** Yes
- **Read fully?** No, selected sections are enough unless promoted later
- **Depth needed:** Low to medium
- **Main use:** Support S4 discussion of zero-shot computer control / reflection
- **Most important parts:**
  - Abstract
  - Introduction
  - Main architecture / method figure
  - Dataset or benchmark section
  - Results table
  - Limitations / discussion

---

## One-sentence summary

A Zero-Shot Language Agent for Computer Control with Structured Reflection is a P2 supporting paper for S4 because it explains **zero-shot computer control / reflection**, but it should be cited according to its venue/status and not overused beyond its evidence.

---

## BibTeX placeholder

```bibtex
@misc{azeroshotlanguageagentforcomputerco2023,
  title = {A Zero-Shot Language Agent for Computer Control with Structured Reflection},
  year = {2023},
  note = {arXiv preprint; Preprint. Verify final bibliographic metadata before thesis submission.}
}
```


---

<!-- ========== FILE: S4_P2\paper_first_notes\S4_P2_06_GPT-4V_in_Wonderland_Large_Multimodal_Models_for_Zero-Shot_Smartphone_GUI_Navigation.md ========== -->

## Source: `S4_P2\paper_first_notes\S4_P2_06_GPT-4V_in_Wonderland_Large_Multimodal_Models_for_Zero-Shot_Smartphone_GUI_Navigation.md`

# S4 P2 Paper 06 — GPT-4V in Wonderland: Large Multimodal Models for Zero-Shot Smartphone GUI Navigation

## Metadata

- **Title:** GPT-4V in Wonderland: Large Multimodal Models for Zero-Shot Smartphone GUI Navigation
- **Year:** 2023
- **Venue / status:** arXiv preprint
- **Peer-reviewed status:** No confirmed archival venue
- **Publication type:** Preprint
- **Thesis section:** S4 — mobile GUI agents and multimodal interaction
- **Category:** multimodal smartphone GUI navigation
- **Priority:** P2
- **BibTeX key:** `gpt4vinwonderlandlargemultimodalmod2023`

---

## Simple understanding

This paper evaluates GPT-4V-style multimodal models for zero-shot smartphone GUI navigation. It is useful as an early study of vision-language models as mobile agents.

In simple terms:

```text
Problem → how can an AI agent interact with a web, GUI, mobile, desktop, or application environment?
Method → add perception, planning, action, memory, API/tool use, state tracking, or browser control.
Goal → complete real user tasks more flexibly than scripts or static chatbots.
```

This note explains the paper first, then connects it to S4 and your thesis.

---

## Core idea

Use a multimodal LLM to observe smartphone screens and choose GUI actions without task-specific training.

The paper is mainly about:

```text
multimodal smartphone GUI navigation
```

It contributes to the larger agent loop:

```text
observe → understand state → plan → act → receive feedback → verify / recover → complete task
```

---

## Key finding / main claim

Large multimodal models show promise for smartphone navigation, but still face grounding, robustness, and long-horizon interaction problems.

For S4, the important question is not only whether the method works on its benchmark, but **which part of web/GUI agency it improves**:

- perception and grounding,
- planning and reasoning,
- action execution,
- API/tool use,
- memory/state tracking,
- recovery and verification,
- or deployment/evaluation.

---

## Key evidence to extract from the paper

When reading the paper, extract these points:

- **Examples of screen observation and action prediction.**
- **Zero-shot GUI navigation results.**
- **Error analysis on visual grounding and planning failures.**

These are the most useful parts for writing a literature-review paragraph.

---

## Limitations

- **Limitation 1:** It is a preprint and should not carry strong claims alone.
- **Limitation 2:** Zero-shot performance may be sensitive to prompt design and screen complexity.
- **Limitation 3:** Smartphone GUI navigation is related to but not identical to web automation.

General thesis-level limitation:

```text
Improving one agent component is not enough for generalized web automation.
A robust web agent still needs grounding, planning, execution, verification, recovery, and safety.
```

---

## Relation to S4

This paper belongs in S4 because S4 discusses **LLM-based agents for web/GUI/mobile/computer automation**.

Its role in S4 is:

```text
GPT-4V in Wonderland: Large Multimodal Models for Zero-Shot Smartphone GUI Navigation
→ multimodal smartphone GUI navigation
→ supporting P2 source for web/GUI/computer-use agent discussion
```

Use it after explaining what the paper does. Do not introduce it only as “P2”; introduce the method or idea first.

---

## Relation to thesis topic

Your thesis topic is:

```text
LLM-based agents for generalized web automation and data extraction
```

This paper matters because:

It shows the move from text-only agents to vision-language agents that can act on screenshots.

For generalized web automation, the connection is:

```text
web / GUI / mobile / computer-use interaction
→ agent observes a digital environment
→ agent chooses actions
→ agent extracts information or completes a workflow
```

Even when the paper is not directly about data extraction, it still helps explain the automation layer needed before extraction can be generalized.

---

## How to use this paper in the literature review

Recommended use:

- Use as **P2 support**, not as the central backbone.
- Use for one precise idea, architecture, benchmark, or limitation.
- If peer-reviewed, it can support stronger claims.
- If preprint/workshop/technical report, use it for recent trends and emerging directions.

Suggested sentence:

> GPT-4V in Wonderland: Large Multimodal Models for Zero-Shot Smartphone GUI Navigation shows how multimodal smartphone GUI navigation contributes to the development of LLM-based agents for digital task automation, but its limitations indicate that generalized web automation still requires stronger grounding, verification, and recovery mechanisms.

---

## Reading decision

- **Keep in S4 P2:** Yes
- **Read fully?** No, selected sections are enough unless promoted later
- **Depth needed:** Low to medium
- **Main use:** Support S4 discussion of multimodal smartphone GUI navigation
- **Most important parts:**
  - Abstract
  - Introduction
  - Main architecture / method figure
  - Dataset or benchmark section
  - Results table
  - Limitations / discussion

---

## One-sentence summary

GPT-4V in Wonderland: Large Multimodal Models for Zero-Shot Smartphone GUI Navigation is a P2 supporting paper for S4 because it explains **multimodal smartphone GUI navigation**, but it should be cited according to its venue/status and not overused beyond its evidence.

---

## BibTeX placeholder

```bibtex
@misc{gpt4vinwonderlandlargemultimodalmod2023,
  title = {GPT-4V in Wonderland: Large Multimodal Models for Zero-Shot Smartphone GUI Navigation},
  year = {2023},
  note = {arXiv preprint; Preprint. Verify final bibliographic metadata before thesis submission.}
}
```


---

<!-- ========== FILE: S4_P2\paper_first_notes\S4_P2_07_AppAgent_Multimodal_Agents_as_Smartphone_Users.md ========== -->

## Source: `S4_P2\paper_first_notes\S4_P2_07_AppAgent_Multimodal_Agents_as_Smartphone_Users.md`

# S4 P2 Paper 07 — AppAgent: Multimodal Agents as Smartphone Users

## Metadata

- **Title:** AppAgent: Multimodal Agents as Smartphone Users
- **Year:** 2023
- **Venue / status:** arXiv preprint
- **Peer-reviewed status:** No confirmed archival venue
- **Publication type:** Preprint
- **Thesis section:** S4 — mobile GUI agents
- **Category:** smartphone agents / multimodal mobile automation
- **Priority:** P2
- **BibTeX key:** `appagentmultimodalagentsassmartphon2023`

---

## Simple understanding

AppAgent treats multimodal agents as smartphone users that can observe screens, understand tasks, and perform mobile actions.

In simple terms:

```text
Problem → how can an AI agent interact with a web, GUI, mobile, desktop, or application environment?
Method → add perception, planning, action, memory, API/tool use, state tracking, or browser control.
Goal → complete real user tasks more flexibly than scripts or static chatbots.
```

This note explains the paper first, then connects it to S4 and your thesis.

---

## Core idea

Build a mobile agent that uses screenshots, natural-language instructions, and a simplified action space to operate smartphone apps.

The paper is mainly about:

```text
smartphone agents / multimodal mobile automation
```

It contributes to the larger agent loop:

```text
observe → understand state → plan → act → receive feedback → verify / recover → complete task
```

---

## Key finding / main claim

Multimodal agents can complete smartphone tasks by combining visual perception, planning, and UI actions.

For S4, the important question is not only whether the method works on its benchmark, but **which part of web/GUI agency it improves**:

- perception and grounding,
- planning and reasoning,
- action execution,
- API/tool use,
- memory/state tracking,
- recovery and verification,
- or deployment/evaluation.

---

## Key evidence to extract from the paper

When reading the paper, extract these points:

- **Agent workflow and action space.**
- **Examples of smartphone app operation.**
- **Task success results and failure analysis.**

These are the most useful parts for writing a literature-review paragraph.

---

## Limitations

- **Limitation 1:** Preprint status; cite carefully.
- **Limitation 2:** Mobile apps differ from desktop web pages and APIs.
- **Limitation 3:** The agent may struggle with long-horizon tasks, dynamic layouts, and error recovery.

General thesis-level limitation:

```text
Improving one agent component is not enough for generalized web automation.
A robust web agent still needs grounding, planning, execution, verification, recovery, and safety.
```

---

## Relation to S4

This paper belongs in S4 because S4 discusses **LLM-based agents for web/GUI/mobile/computer automation**.

Its role in S4 is:

```text
AppAgent: Multimodal Agents as Smartphone Users
→ smartphone agents / multimodal mobile automation
→ supporting P2 source for web/GUI/computer-use agent discussion
```

Use it after explaining what the paper does. Do not introduce it only as “P2”; introduce the method or idea first.

---

## Relation to thesis topic

Your thesis topic is:

```text
LLM-based agents for generalized web automation and data extraction
```

This paper matters because:

It is a key early mobile-agent system, useful for explaining phone automation trends.

For generalized web automation, the connection is:

```text
web / GUI / mobile / computer-use interaction
→ agent observes a digital environment
→ agent chooses actions
→ agent extracts information or completes a workflow
```

Even when the paper is not directly about data extraction, it still helps explain the automation layer needed before extraction can be generalized.

---

## How to use this paper in the literature review

Recommended use:

- Use as **P2 support**, not as the central backbone.
- Use for one precise idea, architecture, benchmark, or limitation.
- If peer-reviewed, it can support stronger claims.
- If preprint/workshop/technical report, use it for recent trends and emerging directions.

Suggested sentence:

> AppAgent: Multimodal Agents as Smartphone Users shows how smartphone agents / multimodal mobile automation contributes to the development of LLM-based agents for digital task automation, but its limitations indicate that generalized web automation still requires stronger grounding, verification, and recovery mechanisms.

---

## Reading decision

- **Keep in S4 P2:** Yes
- **Read fully?** No, selected sections are enough unless promoted later
- **Depth needed:** Low to medium
- **Main use:** Support S4 discussion of smartphone agents / multimodal mobile automation
- **Most important parts:**
  - Abstract
  - Introduction
  - Main architecture / method figure
  - Dataset or benchmark section
  - Results table
  - Limitations / discussion

---

## One-sentence summary

AppAgent: Multimodal Agents as Smartphone Users is a P2 supporting paper for S4 because it explains **smartphone agents / multimodal mobile automation**, but it should be cited according to its venue/status and not overused beyond its evidence.

---

## BibTeX placeholder

```bibtex
@misc{appagentmultimodalagentsassmartphon2023,
  title = {AppAgent: Multimodal Agents as Smartphone Users},
  year = {2023},
  note = {arXiv preprint; Preprint. Verify final bibliographic metadata before thesis submission.}
}
```


---

<!-- ========== FILE: S4_P2\paper_first_notes\S4_P2_08_Mobile-Agent_Autonomous_Multi-Modal_Mobile_Device_Agent_with_Visual_Perception.md ========== -->

## Source: `S4_P2\paper_first_notes\S4_P2_08_Mobile-Agent_Autonomous_Multi-Modal_Mobile_Device_Agent_with_Visual_Perception.md`

# S4 P2 Paper 08 — Mobile-Agent: Autonomous Multi-Modal Mobile Device Agent with Visual Perception

## Metadata

- **Title:** Mobile-Agent: Autonomous Multi-Modal Mobile Device Agent with Visual Perception
- **Year:** 2024
- **Venue / status:** arXiv preprint / technical report
- **Peer-reviewed status:** No confirmed archival venue
- **Publication type:** Preprint / technical report
- **Thesis section:** S4 — mobile agents and GUI automation
- **Category:** autonomous multimodal mobile agents
- **Priority:** P2
- **BibTeX key:** `mobileagentautonomousmultimodalmobi2024`

---

## Simple understanding

Mobile-Agent is an autonomous mobile-device agent that uses visual perception to operate phone interfaces. It is a practical system showing how MLLMs can be used for mobile task automation.

In simple terms:

```text
Problem → how can an AI agent interact with a web, GUI, mobile, desktop, or application environment?
Method → add perception, planning, action, memory, API/tool use, state tracking, or browser control.
Goal → complete real user tasks more flexibly than scripts or static chatbots.
```

This note explains the paper first, then connects it to S4 and your thesis.

---

## Core idea

Use multimodal perception and action prediction to interact with mobile apps through screen observations.

The paper is mainly about:

```text
autonomous multimodal mobile agents
```

It contributes to the larger agent loop:

```text
observe → understand state → plan → act → receive feedback → verify / recover → complete task
```

---

## Key finding / main claim

The system demonstrates that visual mobile agents can perform multi-step phone tasks, but reliability remains a challenge.

For S4, the important question is not only whether the method works on its benchmark, but **which part of web/GUI agency it improves**:

- perception and grounding,
- planning and reasoning,
- action execution,
- API/tool use,
- memory/state tracking,
- recovery and verification,
- or deployment/evaluation.

---

## Key evidence to extract from the paper

When reading the paper, extract these points:

- **Mobile-agent architecture.**
- **Mobile-Eval or related benchmark results.**
- **Examples of visual perception and action execution.**

These are the most useful parts for writing a literature-review paragraph.

---

## Limitations

- **Limitation 1:** Preprint/technical-report status.
- **Limitation 2:** Mobile visual grounding is brittle under popups, layout changes, and small UI elements.
- **Limitation 3:** It is still not a general web automation solution.

General thesis-level limitation:

```text
Improving one agent component is not enough for generalized web automation.
A robust web agent still needs grounding, planning, execution, verification, recovery, and safety.
```

---

## Relation to S4

This paper belongs in S4 because S4 discusses **LLM-based agents for web/GUI/mobile/computer automation**.

Its role in S4 is:

```text
Mobile-Agent: Autonomous Multi-Modal Mobile Device Agent with Visual Perception
→ autonomous multimodal mobile agents
→ supporting P2 source for web/GUI/computer-use agent discussion
```

Use it after explaining what the paper does. Do not introduce it only as “P2”; introduce the method or idea first.

---

## Relation to thesis topic

Your thesis topic is:

```text
LLM-based agents for generalized web automation and data extraction
```

This paper matters because:

It provides a concrete mobile-agent baseline for comparing later systems like Mobile-Agent-E and Agent-SAMA.

For generalized web automation, the connection is:

```text
web / GUI / mobile / computer-use interaction
→ agent observes a digital environment
→ agent chooses actions
→ agent extracts information or completes a workflow
```

Even when the paper is not directly about data extraction, it still helps explain the automation layer needed before extraction can be generalized.

---

## How to use this paper in the literature review

Recommended use:

- Use as **P2 support**, not as the central backbone.
- Use for one precise idea, architecture, benchmark, or limitation.
- If peer-reviewed, it can support stronger claims.
- If preprint/workshop/technical report, use it for recent trends and emerging directions.

Suggested sentence:

> Mobile-Agent: Autonomous Multi-Modal Mobile Device Agent with Visual Perception shows how autonomous multimodal mobile agents contributes to the development of LLM-based agents for digital task automation, but its limitations indicate that generalized web automation still requires stronger grounding, verification, and recovery mechanisms.

---

## Reading decision

- **Keep in S4 P2:** Yes
- **Read fully?** No, selected sections are enough unless promoted later
- **Depth needed:** Low to medium
- **Main use:** Support S4 discussion of autonomous multimodal mobile agents
- **Most important parts:**
  - Abstract
  - Introduction
  - Main architecture / method figure
  - Dataset or benchmark section
  - Results table
  - Limitations / discussion

---

## One-sentence summary

Mobile-Agent: Autonomous Multi-Modal Mobile Device Agent with Visual Perception is a P2 supporting paper for S4 because it explains **autonomous multimodal mobile agents**, but it should be cited according to its venue/status and not overused beyond its evidence.

---

## BibTeX placeholder

```bibtex
@misc{mobileagentautonomousmultimodalmobi2024,
  title = {Mobile-Agent: Autonomous Multi-Modal Mobile Device Agent with Visual Perception},
  year = {2024},
  note = {arXiv preprint / technical report; Preprint / technical report. Verify final bibliographic metadata before thesis submission.}
}
```


---

<!-- ========== FILE: S4_P2\paper_first_notes\S4_P2_09_CRADLE_Empowering_Foundation_Agents_Towards_General_Computer_Control.md ========== -->

## Source: `S4_P2\paper_first_notes\S4_P2_09_CRADLE_Empowering_Foundation_Agents_Towards_General_Computer_Control.md`

# S4 P2 Paper 09 — CRADLE: Empowering Foundation Agents Towards General Computer Control

## Metadata

- **Title:** CRADLE: Empowering Foundation Agents Towards General Computer Control
- **Year:** 2024
- **Venue / status:** arXiv preprint / under review
- **Peer-reviewed status:** No
- **Publication type:** Preprint / under review
- **Thesis section:** S4 — computer-use agents
- **Category:** general computer control
- **Priority:** P2
- **BibTeX key:** `cradleempoweringfoundationagentstow2024`

---

## Simple understanding

CRADLE aims to empower foundation-model agents for general computer control. It addresses the broader problem of operating software environments beyond isolated web pages.

In simple terms:

```text
Problem → how can an AI agent interact with a web, GUI, mobile, desktop, or application environment?
Method → add perception, planning, action, memory, API/tool use, state tracking, or browser control.
Goal → complete real user tasks more flexibly than scripts or static chatbots.
```

This note explains the paper first, then connects it to S4 and your thesis.

---

## Core idea

Design an agent framework for general computer control using foundation models, perception, action, and feedback.

The paper is mainly about:

```text
general computer control
```

It contributes to the larger agent loop:

```text
observe → understand state → plan → act → receive feedback → verify / recover → complete task
```

---

## Key finding / main claim

Foundation agents can be extended toward more general computer-use tasks, but robust control remains difficult.

For S4, the important question is not only whether the method works on its benchmark, but **which part of web/GUI agency it improves**:

- perception and grounding,
- planning and reasoning,
- action execution,
- API/tool use,
- memory/state tracking,
- recovery and verification,
- or deployment/evaluation.

---

## Key evidence to extract from the paper

When reading the paper, extract these points:

- **Framework architecture for computer control.**
- **Task categories or benchmark results.**
- **Discussion of generality and limitations.**

These are the most useful parts for writing a literature-review paragraph.

---

## Limitations

- **Limitation 1:** Under-review/preprint status.
- **Limitation 2:** General computer control is broader than web automation and may include many environment-specific assumptions.
- **Limitation 3:** Reliability, safety, and reproducibility remain open concerns.

General thesis-level limitation:

```text
Improving one agent component is not enough for generalized web automation.
A robust web agent still needs grounding, planning, execution, verification, recovery, and safety.
```

---

## Relation to S4

This paper belongs in S4 because S4 discusses **LLM-based agents for web/GUI/mobile/computer automation**.

Its role in S4 is:

```text
CRADLE: Empowering Foundation Agents Towards General Computer Control
→ general computer control
→ supporting P2 source for web/GUI/computer-use agent discussion
```

Use it after explaining what the paper does. Do not introduce it only as “P2”; introduce the method or idea first.

---

## Relation to thesis topic

Your thesis topic is:

```text
LLM-based agents for generalized web automation and data extraction
```

This paper matters because:

It supports S4’s discussion of moving from web-only agents to general desktop/computer-use agents.

For generalized web automation, the connection is:

```text
web / GUI / mobile / computer-use interaction
→ agent observes a digital environment
→ agent chooses actions
→ agent extracts information or completes a workflow
```

Even when the paper is not directly about data extraction, it still helps explain the automation layer needed before extraction can be generalized.

---

## How to use this paper in the literature review

Recommended use:

- Use as **P2 support**, not as the central backbone.
- Use for one precise idea, architecture, benchmark, or limitation.
- If peer-reviewed, it can support stronger claims.
- If preprint/workshop/technical report, use it for recent trends and emerging directions.

Suggested sentence:

> CRADLE: Empowering Foundation Agents Towards General Computer Control shows how general computer control contributes to the development of LLM-based agents for digital task automation, but its limitations indicate that generalized web automation still requires stronger grounding, verification, and recovery mechanisms.

---

## Reading decision

- **Keep in S4 P2:** Yes
- **Read fully?** No, selected sections are enough unless promoted later
- **Depth needed:** Low to medium
- **Main use:** Support S4 discussion of general computer control
- **Most important parts:**
  - Abstract
  - Introduction
  - Main architecture / method figure
  - Dataset or benchmark section
  - Results table
  - Limitations / discussion

---

## One-sentence summary

CRADLE: Empowering Foundation Agents Towards General Computer Control is a P2 supporting paper for S4 because it explains **general computer control**, but it should be cited according to its venue/status and not overused beyond its evidence.

---

## BibTeX placeholder

```bibtex
@misc{cradleempoweringfoundationagentstow2024,
  title = {CRADLE: Empowering Foundation Agents Towards General Computer Control},
  year = {2024},
  note = {arXiv preprint / under review; Preprint / under review. Verify final bibliographic metadata before thesis submission.}
}
```


---

<!-- ========== FILE: S4_P2\paper_first_notes\S4_P2_10_ChatShop_Interactive_Information_Seeking_with_Language_Agents.md ========== -->

## Source: `S4_P2\paper_first_notes\S4_P2_10_ChatShop_Interactive_Information_Seeking_with_Language_Agents.md`

# S4 P2 Paper 10 — ChatShop: Interactive Information Seeking with Language Agents

## Metadata

- **Title:** ChatShop: Interactive Information Seeking with Language Agents
- **Year:** 2024
- **Venue / status:** arXiv preprint
- **Peer-reviewed status:** No confirmed archival venue
- **Publication type:** Preprint
- **Thesis section:** S4 — web agents for information seeking and e-commerce
- **Category:** interactive product search / shopping agents
- **Priority:** P2
- **BibTeX key:** `chatshopinteractiveinformationseeki2024`

---

## Simple understanding

ChatShop studies language agents for interactive information seeking, especially shopping or product-related search scenarios.

In simple terms:

```text
Problem → how can an AI agent interact with a web, GUI, mobile, desktop, or application environment?
Method → add perception, planning, action, memory, API/tool use, state tracking, or browser control.
Goal → complete real user tasks more flexibly than scripts or static chatbots.
```

This note explains the paper first, then connects it to S4 and your thesis.

---

## Core idea

Use a language agent to iteratively ask, search, refine, and retrieve information to satisfy user shopping/information needs.

The paper is mainly about:

```text
interactive product search / shopping agents
```

It contributes to the larger agent loop:

```text
observe → understand state → plan → act → receive feedback → verify / recover → complete task
```

---

## Key finding / main claim

Interactive agents can improve information seeking by engaging in multi-turn clarification and search.

For S4, the important question is not only whether the method works on its benchmark, but **which part of web/GUI agency it improves**:

- perception and grounding,
- planning and reasoning,
- action execution,
- API/tool use,
- memory/state tracking,
- recovery and verification,
- or deployment/evaluation.

---

## Key evidence to extract from the paper

When reading the paper, extract these points:

- **Interactive search protocol.**
- **Product-search or shopping evaluation.**
- **User/task examples showing clarification and search behavior.**

These are the most useful parts for writing a literature-review paragraph.

---

## Limitations

- **Limitation 1:** Preprint status.
- **Limitation 2:** Shopping/product tasks may not generalize to all web automation tasks.
- **Limitation 3:** Information seeking is different from executing high-stakes web actions.

General thesis-level limitation:

```text
Improving one agent component is not enough for generalized web automation.
A robust web agent still needs grounding, planning, execution, verification, recovery, and safety.
```

---

## Relation to S4

This paper belongs in S4 because S4 discusses **LLM-based agents for web/GUI/mobile/computer automation**.

Its role in S4 is:

```text
ChatShop: Interactive Information Seeking with Language Agents
→ interactive product search / shopping agents
→ supporting P2 source for web/GUI/computer-use agent discussion
```

Use it after explaining what the paper does. Do not introduce it only as “P2”; introduce the method or idea first.

---

## Relation to thesis topic

Your thesis topic is:

```text
LLM-based agents for generalized web automation and data extraction
```

This paper matters because:

It connects web agents with interactive search and product-oriented web tasks.

For generalized web automation, the connection is:

```text
web / GUI / mobile / computer-use interaction
→ agent observes a digital environment
→ agent chooses actions
→ agent extracts information or completes a workflow
```

Even when the paper is not directly about data extraction, it still helps explain the automation layer needed before extraction can be generalized.

---

## How to use this paper in the literature review

Recommended use:

- Use as **P2 support**, not as the central backbone.
- Use for one precise idea, architecture, benchmark, or limitation.
- If peer-reviewed, it can support stronger claims.
- If preprint/workshop/technical report, use it for recent trends and emerging directions.

Suggested sentence:

> ChatShop: Interactive Information Seeking with Language Agents shows how interactive product search / shopping agents contributes to the development of LLM-based agents for digital task automation, but its limitations indicate that generalized web automation still requires stronger grounding, verification, and recovery mechanisms.

---

## Reading decision

- **Keep in S4 P2:** Yes
- **Read fully?** No, selected sections are enough unless promoted later
- **Depth needed:** Low to medium
- **Main use:** Support S4 discussion of interactive product search / shopping agents
- **Most important parts:**
  - Abstract
  - Introduction
  - Main architecture / method figure
  - Dataset or benchmark section
  - Results table
  - Limitations / discussion

---

## One-sentence summary

ChatShop: Interactive Information Seeking with Language Agents is a P2 supporting paper for S4 because it explains **interactive product search / shopping agents**, but it should be cited according to its venue/status and not overused beyond its evidence.

---

## BibTeX placeholder

```bibtex
@misc{chatshopinteractiveinformationseeki2024,
  title = {ChatShop: Interactive Information Seeking with Language Agents},
  year = {2024},
  note = {arXiv preprint; Preprint. Verify final bibliographic metadata before thesis submission.}
}
```


---

<!-- ========== FILE: S4_P2\paper_first_notes\S4_P2_11_Grounded_Language_Agent_for_Product_Search_via_Intelligent_Web_Interactions.md ========== -->

## Source: `S4_P2\paper_first_notes\S4_P2_11_Grounded_Language_Agent_for_Product_Search_via_Intelligent_Web_Interactions.md`

# S4 P2 Paper 11 — Grounded Language Agent for Product Search via Intelligent Web Interactions

## Metadata

- **Title:** Grounded Language Agent for Product Search via Intelligent Web Interactions
- **Year:** 2024
- **Venue / status:** ACL Workshop CustomNLP4U 2024
- **Peer-reviewed status:** Yes, workshop
- **Publication type:** Workshop paper
- **Thesis section:** S4 — domain-specific web agents
- **Category:** grounded product-search web agent
- **Priority:** P2
- **BibTeX key:** `groundedlanguageagentforproductsear2024`

---

## Simple understanding

This paper proposes a grounded language agent for product search using intelligent web interactions. It is a domain-specific web-agent paper focused on e-commerce/product search.

In simple terms:

```text
Problem → how can an AI agent interact with a web, GUI, mobile, desktop, or application environment?
Method → add perception, planning, action, memory, API/tool use, state tracking, or browser control.
Goal → complete real user tasks more flexibly than scripts or static chatbots.
```

This note explains the paper first, then connects it to S4 and your thesis.

---

## Core idea

Train or design an agent that searches, navigates, and interacts with product pages to satisfy user product-search goals.

The paper is mainly about:

```text
grounded product-search web agent
```

It contributes to the larger agent loop:

```text
observe → understand state → plan → act → receive feedback → verify / recover → complete task
```

---

## Key finding / main claim

Grounded web interactions can improve product search by allowing agents to inspect and act within web environments rather than only rank static results.

For S4, the important question is not only whether the method works on its benchmark, but **which part of web/GUI agency it improves**:

- perception and grounding,
- planning and reasoning,
- action execution,
- API/tool use,
- memory/state tracking,
- recovery and verification,
- or deployment/evaluation.

---

## Key evidence to extract from the paper

When reading the paper, extract these points:

- **Agent architecture for product search.**
- **Web interaction/action design.**
- **Experimental comparison on product-search tasks.**

These are the most useful parts for writing a literature-review paragraph.

---

## Limitations

- **Limitation 1:** Workshop venue is useful but weaker than a main conference paper.
- **Limitation 2:** Product search is narrower than generalized web automation.
- **Limitation 3:** Evaluation may depend on WebShop-like assumptions.

General thesis-level limitation:

```text
Improving one agent component is not enough for generalized web automation.
A robust web agent still needs grounding, planning, execution, verification, recovery, and safety.
```

---

## Relation to S4

This paper belongs in S4 because S4 discusses **LLM-based agents for web/GUI/mobile/computer automation**.

Its role in S4 is:

```text
Grounded Language Agent for Product Search via Intelligent Web Interactions
→ grounded product-search web agent
→ supporting P2 source for web/GUI/computer-use agent discussion
```

Use it after explaining what the paper does. Do not introduce it only as “P2”; introduce the method or idea first.

---

## Relation to thesis topic

Your thesis topic is:

```text
LLM-based agents for generalized web automation and data extraction
```

This paper matters because:

It is useful for showing how web agents specialize in e-commerce and information-seeking tasks.

For generalized web automation, the connection is:

```text
web / GUI / mobile / computer-use interaction
→ agent observes a digital environment
→ agent chooses actions
→ agent extracts information or completes a workflow
```

Even when the paper is not directly about data extraction, it still helps explain the automation layer needed before extraction can be generalized.

---

## How to use this paper in the literature review

Recommended use:

- Use as **P2 support**, not as the central backbone.
- Use for one precise idea, architecture, benchmark, or limitation.
- If peer-reviewed, it can support stronger claims.
- If preprint/workshop/technical report, use it for recent trends and emerging directions.

Suggested sentence:

> Grounded Language Agent for Product Search via Intelligent Web Interactions shows how grounded product-search web agent contributes to the development of LLM-based agents for digital task automation, but its limitations indicate that generalized web automation still requires stronger grounding, verification, and recovery mechanisms.

---

## Reading decision

- **Keep in S4 P2:** Yes
- **Read fully?** Yes or selected sections carefully
- **Depth needed:** Medium to high
- **Main use:** Support S4 discussion of grounded product-search web agent
- **Most important parts:**
  - Abstract
  - Introduction
  - Main architecture / method figure
  - Dataset or benchmark section
  - Results table
  - Limitations / discussion

---

## One-sentence summary

Grounded Language Agent for Product Search via Intelligent Web Interactions is a P2 supporting paper for S4 because it explains **grounded product-search web agent**, but it should be cited according to its venue/status and not overused beyond its evidence.

---

## BibTeX placeholder

```bibtex
@misc{groundedlanguageagentforproductsear2024,
  title = {Grounded Language Agent for Product Search via Intelligent Web Interactions},
  year = {2024},
  note = {ACL Workshop CustomNLP4U 2024; Workshop paper. Verify final bibliographic metadata before thesis submission.}
}
```


---

<!-- ========== FILE: S4_P2\paper_first_notes\S4_P2_12_Automating_the_Enterprise_with_Foundation_Models.md ========== -->

## Source: `S4_P2\paper_first_notes\S4_P2_12_Automating_the_Enterprise_with_Foundation_Models.md`

# S4 P2 Paper 12 — Automating the Enterprise with Foundation Models

## Metadata

- **Title:** Automating the Enterprise with Foundation Models
- **Year:** 2024
- **Venue / status:** arXiv preprint
- **Peer-reviewed status:** No confirmed archival venue
- **Publication type:** Preprint
- **Thesis section:** S4 — enterprise web/computer automation
- **Category:** enterprise automation / foundation-model agents
- **Priority:** P2
- **BibTeX key:** `automatingtheenterprisewithfoundati2024`

---

## Simple understanding

This paper discusses enterprise automation using foundation models. It is useful for comparing LLM agents with classical RPA and workflow automation.

In simple terms:

```text
Problem → how can an AI agent interact with a web, GUI, mobile, desktop, or application environment?
Method → add perception, planning, action, memory, API/tool use, state tracking, or browser control.
Goal → complete real user tasks more flexibly than scripts or static chatbots.
```

This note explains the paper first, then connects it to S4 and your thesis.

---

## Core idea

Use foundation models to automate enterprise workflows that traditionally require scripts, APIs, or RPA.

The paper is mainly about:

```text
enterprise automation / foundation-model agents
```

It contributes to the larger agent loop:

```text
observe → understand state → plan → act → receive feedback → verify / recover → complete task
```

---

## Key finding / main claim

Foundation models can reduce manual development effort, but enterprise automation demands reliability, governance, and integration with existing systems.

For S4, the important question is not only whether the method works on its benchmark, but **which part of web/GUI agency it improves**:

- perception and grounding,
- planning and reasoning,
- action execution,
- API/tool use,
- memory/state tracking,
- recovery and verification,
- or deployment/evaluation.

---

## Key evidence to extract from the paper

When reading the paper, extract these points:

- **Enterprise automation use cases.**
- **Architecture or workflow examples.**
- **Comparison with RPA or traditional automation.**

These are the most useful parts for writing a literature-review paragraph.

---

## Limitations

- **Limitation 1:** Preprint status.
- **Limitation 2:** Enterprise settings are high-stakes and require stronger reliability than most research benchmarks.
- **Limitation 3:** The paper may be more vision/system-oriented than a rigorously evaluated benchmark paper.

General thesis-level limitation:

```text
Improving one agent component is not enough for generalized web automation.
A robust web agent still needs grounding, planning, execution, verification, recovery, and safety.
```

---

## Relation to S4

This paper belongs in S4 because S4 discusses **LLM-based agents for web/GUI/mobile/computer automation**.

Its role in S4 is:

```text
Automating the Enterprise with Foundation Models
→ enterprise automation / foundation-model agents
→ supporting P2 source for web/GUI/computer-use agent discussion
```

Use it after explaining what the paper does. Do not introduce it only as “P2”; introduce the method or idea first.

---

## Relation to thesis topic

Your thesis topic is:

```text
LLM-based agents for generalized web automation and data extraction
```

This paper matters because:

It helps position LLM agents in relation to RPA and business workflow automation.

For generalized web automation, the connection is:

```text
web / GUI / mobile / computer-use interaction
→ agent observes a digital environment
→ agent chooses actions
→ agent extracts information or completes a workflow
```

Even when the paper is not directly about data extraction, it still helps explain the automation layer needed before extraction can be generalized.

---

## How to use this paper in the literature review

Recommended use:

- Use as **P2 support**, not as the central backbone.
- Use for one precise idea, architecture, benchmark, or limitation.
- If peer-reviewed, it can support stronger claims.
- If preprint/workshop/technical report, use it for recent trends and emerging directions.

Suggested sentence:

> Automating the Enterprise with Foundation Models shows how enterprise automation / foundation-model agents contributes to the development of LLM-based agents for digital task automation, but its limitations indicate that generalized web automation still requires stronger grounding, verification, and recovery mechanisms.

---

## Reading decision

- **Keep in S4 P2:** Yes
- **Read fully?** No, selected sections are enough unless promoted later
- **Depth needed:** Low to medium
- **Main use:** Support S4 discussion of enterprise automation / foundation-model agents
- **Most important parts:**
  - Abstract
  - Introduction
  - Main architecture / method figure
  - Dataset or benchmark section
  - Results table
  - Limitations / discussion

---

## One-sentence summary

Automating the Enterprise with Foundation Models is a P2 supporting paper for S4 because it explains **enterprise automation / foundation-model agents**, but it should be cited according to its venue/status and not overused beyond its evidence.

---

## BibTeX placeholder

```bibtex
@misc{automatingtheenterprisewithfoundati2024,
  title = {Automating the Enterprise with Foundation Models},
  year = {2024},
  note = {arXiv preprint; Preprint. Verify final bibliographic metadata before thesis submission.}
}
```


---

<!-- ========== FILE: S4_P2\paper_first_notes\S4_P2_13_OpenWebAgent_An_Open_Toolkit_to_Enable_Web_Agents_on_Large_Language_Models.md ========== -->

## Source: `S4_P2\paper_first_notes\S4_P2_13_OpenWebAgent_An_Open_Toolkit_to_Enable_Web_Agents_on_Large_Language_Models.md`

# S4 P2 Paper 13 — OpenWebAgent: An Open Toolkit to Enable Web Agents on Large Language Models

## Metadata

- **Title:** OpenWebAgent: An Open Toolkit to Enable Web Agents on Large Language Models
- **Year:** 2024
- **Venue / status:** ACL 2024 System Demonstrations
- **Peer-reviewed status:** Yes, demo
- **Publication type:** System demonstration paper
- **Thesis section:** S4 — web-agent frameworks and toolkits
- **Category:** open web-agent toolkit
- **Priority:** P2
- **BibTeX key:** `openwebagentanopentoolkittoenablewe2024`

---

## Simple understanding

OpenWebAgent is an open toolkit for building web agents on top of LLMs. It provides infrastructure for web interaction, agent execution, and evaluation.

In simple terms:

```text
Problem → how can an AI agent interact with a web, GUI, mobile, desktop, or application environment?
Method → add perception, planning, action, memory, API/tool use, state tracking, or browser control.
Goal → complete real user tasks more flexibly than scripts or static chatbots.
```

This note explains the paper first, then connects it to S4 and your thesis.

---

## Core idea

Offer a reusable toolkit that enables LLMs to interact with websites as agents.

The paper is mainly about:

```text
open web-agent toolkit
```

It contributes to the larger agent loop:

```text
observe → understand state → plan → act → receive feedback → verify / recover → complete task
```

---

## Key finding / main claim

Open tooling helps standardize and accelerate web-agent research by making browser interaction and evaluation more accessible.

For S4, the important question is not only whether the method works on its benchmark, but **which part of web/GUI agency it improves**:

- perception and grounding,
- planning and reasoning,
- action execution,
- API/tool use,
- memory/state tracking,
- recovery and verification,
- or deployment/evaluation.

---

## Key evidence to extract from the paper

When reading the paper, extract these points:

- **Toolkit architecture.**
- **Supported web-agent components.**
- **Demonstration or evaluation examples.**

These are the most useful parts for writing a literature-review paragraph.

---

## Limitations

- **Limitation 1:** System demo papers are useful for tooling, but not always strong empirical evidence.
- **Limitation 2:** Toolkit performance depends on the underlying model and task setup.
- **Limitation 3:** It is infrastructure, not a single definitive agent algorithm.

General thesis-level limitation:

```text
Improving one agent component is not enough for generalized web automation.
A robust web agent still needs grounding, planning, execution, verification, recovery, and safety.
```

---

## Relation to S4

This paper belongs in S4 because S4 discusses **LLM-based agents for web/GUI/mobile/computer automation**.

Its role in S4 is:

```text
OpenWebAgent: An Open Toolkit to Enable Web Agents on Large Language Models
→ open web-agent toolkit
→ supporting P2 source for web/GUI/computer-use agent discussion
```

Use it after explaining what the paper does. Do not introduce it only as “P2”; introduce the method or idea first.

---

## Relation to thesis topic

Your thesis topic is:

```text
LLM-based agents for generalized web automation and data extraction
```

This paper matters because:

It is a strong practical reference for open web-agent infrastructure.

For generalized web automation, the connection is:

```text
web / GUI / mobile / computer-use interaction
→ agent observes a digital environment
→ agent chooses actions
→ agent extracts information or completes a workflow
```

Even when the paper is not directly about data extraction, it still helps explain the automation layer needed before extraction can be generalized.

---

## How to use this paper in the literature review

Recommended use:

- Use as **P2 support**, not as the central backbone.
- Use for one precise idea, architecture, benchmark, or limitation.
- If peer-reviewed, it can support stronger claims.
- If preprint/workshop/technical report, use it for recent trends and emerging directions.

Suggested sentence:

> OpenWebAgent: An Open Toolkit to Enable Web Agents on Large Language Models shows how open web-agent toolkit contributes to the development of LLM-based agents for digital task automation, but its limitations indicate that generalized web automation still requires stronger grounding, verification, and recovery mechanisms.

---

## Reading decision

- **Keep in S4 P2:** Yes
- **Read fully?** Yes or selected sections carefully
- **Depth needed:** Medium to high
- **Main use:** Support S4 discussion of open web-agent toolkit
- **Most important parts:**
  - Abstract
  - Introduction
  - Main architecture / method figure
  - Dataset or benchmark section
  - Results table
  - Limitations / discussion

---

## One-sentence summary

OpenWebAgent: An Open Toolkit to Enable Web Agents on Large Language Models is a P2 supporting paper for S4 because it explains **open web-agent toolkit**, but it should be cited according to its venue/status and not overused beyond its evidence.

---

## BibTeX placeholder

```bibtex
@misc{openwebagentanopentoolkittoenablewe2024,
  title = {OpenWebAgent: An Open Toolkit to Enable Web Agents on Large Language Models},
  year = {2024},
  note = {ACL 2024 System Demonstrations; System demonstration paper. Verify final bibliographic metadata before thesis submission.}
}
```


---

<!-- ========== FILE: S4_P2\paper_first_notes\S4_P2_14_Steward_Natural_Language_Web_Automation.md ========== -->

## Source: `S4_P2\paper_first_notes\S4_P2_14_Steward_Natural_Language_Web_Automation.md`

# S4 P2 Paper 14 — Steward: Natural Language Web Automation

## Metadata

- **Title:** Steward: Natural Language Web Automation
- **Year:** 2024
- **Venue / status:** arXiv preprint
- **Peer-reviewed status:** No confirmed archival venue
- **Publication type:** Preprint
- **Thesis section:** S4 — natural-language web automation
- **Category:** natural-language web automation
- **Priority:** P2
- **BibTeX key:** `stewardnaturallanguagewebautomation2024`

---

## Simple understanding

Steward is an LLM-powered web automation tool that takes natural-language tasks and executes browser actions through Playwright. It focuses on cost, runtime, action selection, and real website automation.

In simple terms:

```text
Problem → how can an AI agent interact with a web, GUI, mobile, desktop, or application environment?
Method → add perception, planning, action, memory, API/tool use, state tracking, or browser control.
Goal → complete real user tasks more flexibly than scripts or static chatbots.
```

This note explains the paper first, then connects it to S4 and your thesis.

---

## Core idea

Represent webpage state and use an LLM to iteratively select UI actions until a natural-language task is completed.

The paper is mainly about:

```text
natural-language web automation
```

It contributes to the larger agent loop:

```text
observe → understand state → plan → act → receive feedback → verify / recover → complete task
```

---

## Key finding / main claim

Steward reports practical execution on real websites, including top-1 action-element selection accuracy and task completion rates, while analyzing runtime/cost tradeoffs.

For S4, the important question is not only whether the method works on its benchmark, but **which part of web/GUI agency it improves**:

- perception and grounding,
- planning and reasoning,
- action execution,
- API/tool use,
- memory/state tracking,
- recovery and verification,
- or deployment/evaluation.

---

## Key evidence to extract from the paper

When reading the paper, extract these points:

- **Figure 1 showing iterative UI action selection.**
- **Reported metrics: 81.44% top-1 action+element selection for top elements, 46.70% per-step accuracy on Mind2Web, and 40% task completion.**
- **Runtime/cost analysis and caching mechanism.**

These are the most useful parts for writing a literature-review paragraph.

---

## Limitations

- **Limitation 1:** Preprint status.
- **Limitation 2:** Reported task completion on real websites is still limited and failures occur on long-horizon tasks.
- **Limitation 3:** State representation, completion detection, and UI drift remain difficult.

General thesis-level limitation:

```text
Improving one agent component is not enough for generalized web automation.
A robust web agent still needs grounding, planning, execution, verification, recovery, and safety.
```

---

## Relation to S4

This paper belongs in S4 because S4 discusses **LLM-based agents for web/GUI/mobile/computer automation**.

Its role in S4 is:

```text
Steward: Natural Language Web Automation
→ natural-language web automation
→ supporting P2 source for web/GUI/computer-use agent discussion
```

Use it after explaining what the paper does. Do not introduce it only as “P2”; introduce the method or idea first.

---

## Relation to thesis topic

Your thesis topic is:

```text
LLM-based agents for generalized web automation and data extraction
```

This paper matters because:

It is directly relevant to your thesis because it targets natural-language web automation with LLMs and browser automation.

For generalized web automation, the connection is:

```text
web / GUI / mobile / computer-use interaction
→ agent observes a digital environment
→ agent chooses actions
→ agent extracts information or completes a workflow
```

Even when the paper is not directly about data extraction, it still helps explain the automation layer needed before extraction can be generalized.

---

## How to use this paper in the literature review

Recommended use:

- Use as **P2 support**, not as the central backbone.
- Use for one precise idea, architecture, benchmark, or limitation.
- If peer-reviewed, it can support stronger claims.
- If preprint/workshop/technical report, use it for recent trends and emerging directions.

Suggested sentence:

> Steward: Natural Language Web Automation shows how natural-language web automation contributes to the development of LLM-based agents for digital task automation, but its limitations indicate that generalized web automation still requires stronger grounding, verification, and recovery mechanisms.

---

## Reading decision

- **Keep in S4 P2:** Yes
- **Read fully?** No, selected sections are enough unless promoted later
- **Depth needed:** Low to medium
- **Main use:** Support S4 discussion of natural-language web automation
- **Most important parts:**
  - Abstract
  - Introduction
  - Main architecture / method figure
  - Dataset or benchmark section
  - Results table
  - Limitations / discussion

---

## One-sentence summary

Steward: Natural Language Web Automation is a P2 supporting paper for S4 because it explains **natural-language web automation**, but it should be cited according to its venue/status and not overused beyond its evidence.

---

## BibTeX placeholder

```bibtex
@misc{stewardnaturallanguagewebautomation2024,
  title = {Steward: Natural Language Web Automation},
  year = {2024},
  note = {arXiv preprint; Preprint. Verify final bibliographic metadata before thesis submission.}
}
```


---

<!-- ========== FILE: S4_P2\paper_first_notes\S4_P2_15_AXIS_Efficient_Human-Agent-Computer_Interaction_with_API-First_LLM-Based_Agents.md ========== -->

## Source: `S4_P2\paper_first_notes\S4_P2_15_AXIS_Efficient_Human-Agent-Computer_Interaction_with_API-First_LLM-Based_Agents.md`

# S4 P2 Paper 15 — AXIS: Efficient Human-Agent-Computer Interaction with API-First LLM-Based Agents

## Metadata

- **Title:** AXIS: Efficient Human-Agent-Computer Interaction with API-First LLM-Based Agents
- **Year:** 2024/2025
- **Venue / status:** arXiv preprint
- **Peer-reviewed status:** No confirmed archival venue
- **Publication type:** Preprint
- **Thesis section:** S4 — API-first / hybrid web and computer agents
- **Category:** API-first GUI/computer agents
- **Priority:** P2
- **BibTeX key:** `axisefficienthumanagentcomputerinte2024/2025`

---

## Simple understanding

AXIS argues that LLM-based agents should prioritize APIs over human-like UI actions. It proposes an API-first framework for human-agent-computer interaction.

In simple terms:

```text
Problem → how can an AI agent interact with a web, GUI, mobile, desktop, or application environment?
Method → add perception, planning, action, memory, API/tool use, state tracking, or browser control.
Goal → complete real user tasks more flexibly than scripts or static chatbots.
```

This note explains the paper first, then connects it to S4 and your thesis.

---

## Core idea

Replace long sequential UI interactions with API calls where possible, while using UI actions only when APIs are unavailable.

The paper is mainly about:

```text
API-first GUI/computer agents
```

It contributes to the larger agent loop:

```text
observe → understand state → plan → act → receive feedback → verify / recover → complete task
```

---

## Key finding / main claim

On Microsoft Word tasks, AXIS reports large reductions in completion time and cognitive workload while maintaining high accuracy compared with humans.

For S4, the important question is not only whether the method works on its benchmark, but **which part of web/GUI agency it improves**:

- perception and grounding,
- planning and reasoning,
- action execution,
- API/tool use,
- memory/state tracking,
- recovery and verification,
- or deployment/evaluation.

---

## Key evidence to extract from the paper

When reading the paper, extract these points:

- **Figure 1 comparing manual operation, UI Agent, and AXIS API-call trajectory.**
- **Reported 65–70% task completion time reduction and 97–98% accuracy compared to humans.**
- **Discussion of HACI and Agent OS design.**

These are the most useful parts for writing a literature-review paragraph.

---

## Limitations

- **Limitation 1:** Preprint status.
- **Limitation 2:** Experiments focus on Microsoft Word, not the open web broadly.
- **Limitation 3:** API availability and documentation quality strongly determine effectiveness.

General thesis-level limitation:

```text
Improving one agent component is not enough for generalized web automation.
A robust web agent still needs grounding, planning, execution, verification, recovery, and safety.
```

---

## Relation to S4

This paper belongs in S4 because S4 discusses **LLM-based agents for web/GUI/mobile/computer automation**.

Its role in S4 is:

```text
AXIS: Efficient Human-Agent-Computer Interaction with API-First LLM-Based Agents
→ API-first GUI/computer agents
→ supporting P2 source for web/GUI/computer-use agent discussion
```

Use it after explaining what the paper does. Do not introduce it only as “P2”; introduce the method or idea first.

---

## Relation to thesis topic

Your thesis topic is:

```text
LLM-based agents for generalized web automation and data extraction
```

This paper matters because:

It supports a key S4 argument: agents should not always imitate human UI interaction when machine-native APIs are available.

For generalized web automation, the connection is:

```text
web / GUI / mobile / computer-use interaction
→ agent observes a digital environment
→ agent chooses actions
→ agent extracts information or completes a workflow
```

Even when the paper is not directly about data extraction, it still helps explain the automation layer needed before extraction can be generalized.

---

## How to use this paper in the literature review

Recommended use:

- Use as **P2 support**, not as the central backbone.
- Use for one precise idea, architecture, benchmark, or limitation.
- If peer-reviewed, it can support stronger claims.
- If preprint/workshop/technical report, use it for recent trends and emerging directions.

Suggested sentence:

> AXIS: Efficient Human-Agent-Computer Interaction with API-First LLM-Based Agents shows how API-first GUI/computer agents contributes to the development of LLM-based agents for digital task automation, but its limitations indicate that generalized web automation still requires stronger grounding, verification, and recovery mechanisms.

---

## Reading decision

- **Keep in S4 P2:** Yes
- **Read fully?** No, selected sections are enough unless promoted later
- **Depth needed:** Low to medium
- **Main use:** Support S4 discussion of API-first GUI/computer agents
- **Most important parts:**
  - Abstract
  - Introduction
  - Main architecture / method figure
  - Dataset or benchmark section
  - Results table
  - Limitations / discussion

---

## One-sentence summary

AXIS: Efficient Human-Agent-Computer Interaction with API-First LLM-Based Agents is a P2 supporting paper for S4 because it explains **API-first GUI/computer agents**, but it should be cited according to its venue/status and not overused beyond its evidence.

---

## BibTeX placeholder

```bibtex
@misc{axisefficienthumanagentcomputerinte2024/2025,
  title = {AXIS: Efficient Human-Agent-Computer Interaction with API-First LLM-Based Agents},
  year = {2024/2025},
  note = {arXiv preprint; Preprint. Verify final bibliographic metadata before thesis submission.}
}
```


---

<!-- ========== FILE: S4_P2\paper_first_notes\S4_P2_16_Foundations_and_Recent_Trends_in_Multimodal_Mobile_Agents_A_Survey.md ========== -->

## Source: `S4_P2\paper_first_notes\S4_P2_16_Foundations_and_Recent_Trends_in_Multimodal_Mobile_Agents_A_Survey.md`

# S4 P2 Paper 16 — Foundations and Recent Trends in Multimodal Mobile Agents: A Survey

## Metadata

- **Title:** Foundations and Recent Trends in Multimodal Mobile Agents: A Survey
- **Year:** 2024/2025
- **Venue / status:** arXiv survey
- **Peer-reviewed status:** No confirmed archival venue
- **Publication type:** Survey preprint
- **Thesis section:** S4 — mobile/GUI agent taxonomy
- **Category:** multimodal mobile-agent survey
- **Priority:** P2
- **BibTeX key:** `foundationsandrecenttrendsinmultimo2024/2025`

---

## Simple understanding

This survey reviews multimodal mobile agents, including prompt-based and training-based methods, benchmarks, components, and challenges.

In simple terms:

```text
Problem → how can an AI agent interact with a web, GUI, mobile, desktop, or application environment?
Method → add perception, planning, action, memory, API/tool use, state tracking, or browser control.
Goal → complete real user tasks more flexibly than scripts or static chatbots.
```

This note explains the paper first, then connects it to S4 and your thesis.

---

## Core idea

Organize mobile-agent research around perception, planning, action, memory, benchmarks, and deployment tradeoffs.

The paper is mainly about:

```text
multimodal mobile-agent survey
```

It contributes to the larger agent loop:

```text
observe → understand state → plan → act → receive feedback → verify / recover → complete task
```

---

## Key finding / main claim

Mobile agents are moving from prompt-based LLM control to multimodal/training-based systems, but resource efficiency, robustness, and realistic evaluation remain open.

For S4, the important question is not only whether the method works on its benchmark, but **which part of web/GUI agency it improves**:

- perception and grounding,
- planning and reasoning,
- action execution,
- API/tool use,
- memory/state tracking,
- recovery and verification,
- or deployment/evaluation.

---

## Key evidence to extract from the paper

When reading the paper, extract these points:

- **Section 2 taxonomy: perception, planning, action, memory.**
- **Distinction between prompt-based and training-based methods.**
- **Discussion of deployment cost and effectiveness.**

These are the most useful parts for writing a literature-review paragraph.

---

## Limitations

- **Limitation 1:** Survey preprint, not a primary empirical source.
- **Limitation 2:** It focuses on mobile agents, not all web agents.
- **Limitation 3:** Use mainly for taxonomy and background.

General thesis-level limitation:

```text
Improving one agent component is not enough for generalized web automation.
A robust web agent still needs grounding, planning, execution, verification, recovery, and safety.
```

---

## Relation to S4

This paper belongs in S4 because S4 discusses **LLM-based agents for web/GUI/mobile/computer automation**.

Its role in S4 is:

```text
Foundations and Recent Trends in Multimodal Mobile Agents: A Survey
→ multimodal mobile-agent survey
→ supporting P2 source for web/GUI/computer-use agent discussion
```

Use it after explaining what the paper does. Do not introduce it only as “P2”; introduce the method or idea first.

---

## Relation to thesis topic

Your thesis topic is:

```text
LLM-based agents for generalized web automation and data extraction
```

This paper matters because:

It gives a useful taxonomy for organizing phone/mobile agent systems in S4.

For generalized web automation, the connection is:

```text
web / GUI / mobile / computer-use interaction
→ agent observes a digital environment
→ agent chooses actions
→ agent extracts information or completes a workflow
```

Even when the paper is not directly about data extraction, it still helps explain the automation layer needed before extraction can be generalized.

---

## How to use this paper in the literature review

Recommended use:

- Use as **P2 support**, not as the central backbone.
- Use for one precise idea, architecture, benchmark, or limitation.
- If peer-reviewed, it can support stronger claims.
- If preprint/workshop/technical report, use it for recent trends and emerging directions.

Suggested sentence:

> Foundations and Recent Trends in Multimodal Mobile Agents: A Survey shows how multimodal mobile-agent survey contributes to the development of LLM-based agents for digital task automation, but its limitations indicate that generalized web automation still requires stronger grounding, verification, and recovery mechanisms.

---

## Reading decision

- **Keep in S4 P2:** Yes
- **Read fully?** No, selected sections are enough unless promoted later
- **Depth needed:** Low to medium
- **Main use:** Support S4 discussion of multimodal mobile-agent survey
- **Most important parts:**
  - Abstract
  - Introduction
  - Main architecture / method figure
  - Dataset or benchmark section
  - Results table
  - Limitations / discussion

---

## One-sentence summary

Foundations and Recent Trends in Multimodal Mobile Agents: A Survey is a P2 supporting paper for S4 because it explains **multimodal mobile-agent survey**, but it should be cited according to its venue/status and not overused beyond its evidence.

---

## BibTeX placeholder

```bibtex
@misc{foundationsandrecenttrendsinmultimo2024/2025,
  title = {Foundations and Recent Trends in Multimodal Mobile Agents: A Survey},
  year = {2024/2025},
  note = {arXiv survey; Survey preprint. Verify final bibliographic metadata before thesis submission.}
}
```


---

<!-- ========== FILE: S4_P2\paper_first_notes\S4_P2_17_The_Dawn_of_GUI_Agent_A_Preliminary_Case_Study_with_Claude_3.5_Computer_Use.md ========== -->

## Source: `S4_P2\paper_first_notes\S4_P2_17_The_Dawn_of_GUI_Agent_A_Preliminary_Case_Study_with_Claude_3.5_Computer_Use.md`

# S4 P2 Paper 17 — The Dawn of GUI Agent: A Preliminary Case Study with Claude 3.5 Computer Use

## Metadata

- **Title:** The Dawn of GUI Agent: A Preliminary Case Study with Claude 3.5 Computer Use
- **Year:** 2024
- **Venue / status:** arXiv preprint / under review
- **Peer-reviewed status:** No
- **Publication type:** Preprint / case study
- **Thesis section:** S4 — GUI/computer-use agents
- **Category:** GUI agent case study / Claude computer use
- **Priority:** P2
- **BibTeX key:** `thedawnofguiagentapreliminarycasest2024`

---

## Simple understanding

This paper studies Claude 3.5 Computer Use as an early public GUI-agent system. It evaluates its abilities and limitations across desktop tasks.

In simple terms:

```text
Problem → how can an AI agent interact with a web, GUI, mobile, desktop, or application environment?
Method → add perception, planning, action, memory, API/tool use, state tracking, or browser control.
Goal → complete real user tasks more flexibly than scripts or static chatbots.
```

This note explains the paper first, then connects it to S4 and your thesis.

---

## Core idea

Analyze an API-based GUI automation model through tasks involving web search, productivity, workflow, and entertainment domains.

The paper is mainly about:

```text
GUI agent case study / Claude computer use
```

It contributes to the larger agent loop:

```text
observe → understand state → plan → act → receive feedback → verify / recover → complete task
```

---

## Key finding / main claim

Claude Computer Use shows strong end-to-end language-to-desktop action ability but still has planning, action-grounding, and critic/recovery limitations.

For S4, the important question is not only whether the method works on its benchmark, but **which part of web/GUI agency it improves**:

- perception and grounding,
- planning and reasoning,
- action execution,
- API/tool use,
- memory/state tracking,
- recovery and verification,
- or deployment/evaluation.

---

## Key evidence to extract from the paper

When reading the paper, extract these points:

- **Three evaluation dimensions: planning, action, critic.**
- **Computer Use OOTB framework.**
- **System prompt/action tools shown in the paper.**

These are the most useful parts for writing a literature-review paragraph.

---

## Limitations

- **Limitation 1:** Preliminary case study, not a full benchmark paper.
- **Limitation 2:** Focused on one commercial model and its public beta behavior.
- **Limitation 3:** Results may change as the model/API changes.

General thesis-level limitation:

```text
Improving one agent component is not enough for generalized web automation.
A robust web agent still needs grounding, planning, execution, verification, recovery, and safety.
```

---

## Relation to S4

This paper belongs in S4 because S4 discusses **LLM-based agents for web/GUI/mobile/computer automation**.

Its role in S4 is:

```text
The Dawn of GUI Agent: A Preliminary Case Study with Claude 3.5 Computer Use
→ GUI agent case study / Claude computer use
→ supporting P2 source for web/GUI/computer-use agent discussion
```

Use it after explaining what the paper does. Do not introduce it only as “P2”; introduce the method or idea first.

---

## Relation to thesis topic

Your thesis topic is:

```text
LLM-based agents for generalized web automation and data extraction
```

This paper matters because:

It provides recent evidence on frontier commercial computer-use agents and their failure modes.

For generalized web automation, the connection is:

```text
web / GUI / mobile / computer-use interaction
→ agent observes a digital environment
→ agent chooses actions
→ agent extracts information or completes a workflow
```

Even when the paper is not directly about data extraction, it still helps explain the automation layer needed before extraction can be generalized.

---

## How to use this paper in the literature review

Recommended use:

- Use as **P2 support**, not as the central backbone.
- Use for one precise idea, architecture, benchmark, or limitation.
- If peer-reviewed, it can support stronger claims.
- If preprint/workshop/technical report, use it for recent trends and emerging directions.

Suggested sentence:

> The Dawn of GUI Agent: A Preliminary Case Study with Claude 3.5 Computer Use shows how GUI agent case study / Claude computer use contributes to the development of LLM-based agents for digital task automation, but its limitations indicate that generalized web automation still requires stronger grounding, verification, and recovery mechanisms.

---

## Reading decision

- **Keep in S4 P2:** Yes
- **Read fully?** No, selected sections are enough unless promoted later
- **Depth needed:** Low to medium
- **Main use:** Support S4 discussion of GUI agent case study / Claude computer use
- **Most important parts:**
  - Abstract
  - Introduction
  - Main architecture / method figure
  - Dataset or benchmark section
  - Results table
  - Limitations / discussion

---

## One-sentence summary

The Dawn of GUI Agent: A Preliminary Case Study with Claude 3.5 Computer Use is a P2 supporting paper for S4 because it explains **GUI agent case study / Claude computer use**, but it should be cited according to its venue/status and not overused beyond its evidence.

---

## BibTeX placeholder

```bibtex
@misc{thedawnofguiagentapreliminarycasest2024,
  title = {The Dawn of GUI Agent: A Preliminary Case Study with Claude 3.5 Computer Use},
  year = {2024},
  note = {arXiv preprint / under review; Preprint / case study. Verify final bibliographic metadata before thesis submission.}
}
```


---

<!-- ========== FILE: S4_P2\paper_first_notes\S4_P2_18_A_Comprehensive_Survey_of_Agents_for_Computer_Use_Foundations_Challenges_and_Future_Directions.md ========== -->

## Source: `S4_P2\paper_first_notes\S4_P2_18_A_Comprehensive_Survey_of_Agents_for_Computer_Use_Foundations_Challenges_and_Future_Directions.md`

# S4 P2 Paper 18 — A Comprehensive Survey of Agents for Computer Use: Foundations, Challenges, and Future Directions

## Metadata

- **Title:** A Comprehensive Survey of Agents for Computer Use: Foundations, Challenges, and Future Directions
- **Year:** 2025
- **Venue / status:** arXiv survey
- **Peer-reviewed status:** No confirmed archival venue
- **Publication type:** Survey preprint
- **Thesis section:** S4 — computer-use agent survey foundation
- **Category:** computer-use agent survey
- **Priority:** P2
- **BibTeX key:** `acomprehensivesurveyofagentsforcomp2025`

---

## Simple understanding

This survey reviews agents for computer use: systems that execute natural-language tasks on PCs or phones via UI actions.

In simple terms:

```text
Problem → how can an AI agent interact with a web, GUI, mobile, desktop, or application environment?
Method → add perception, planning, action, memory, API/tool use, state tracking, or browser control.
Goal → complete real user tasks more flexibly than scripts or static chatbots.
```

This note explains the paper first, then connects it to S4 and your thesis.

---

## Core idea

Provide a taxonomy of computer-use agents across domain, interaction, and agent perspectives.

The paper is mainly about:

```text
computer-use agent survey
```

It contributes to the larger agent loop:

```text
observe → understand state → plan → act → receive feedback → verify / recover → complete task
```

---

## Key finding / main claim

The field is shifting from specialized agents toward foundation-model-based agents, from text to image observations, and toward behavior cloning, while generalization and planning remain open problems.

For S4, the important question is not only whether the method works on its benchmark, but **which part of web/GUI agency it improves**:

- perception and grounding,
- planning and reasoning,
- action execution,
- API/tool use,
- memory/state tracking,
- recovery and verification,
- or deployment/evaluation.

---

## Key evidence to extract from the paper

When reading the paper, extract these points:

- **Taxonomy in Figure 1: domain, interaction, and agent perspectives.**
- **Review of 87 ACU papers and 33 datasets.**
- **Six gaps: generalization, inefficient learning, limited planning, low task complexity, non-standard evaluation, deployment mismatch.**

These are the most useful parts for writing a literature-review paragraph.

---

## Limitations

- **Limitation 1:** Survey preprint with about one-third preprint sources, according to its own methodology.
- **Limitation 2:** Not a primary method paper.
- **Limitation 3:** Use for taxonomy and research gaps, not central empirical claims.

General thesis-level limitation:

```text
Improving one agent component is not enough for generalized web automation.
A robust web agent still needs grounding, planning, execution, verification, recovery, and safety.
```

---

## Relation to S4

This paper belongs in S4 because S4 discusses **LLM-based agents for web/GUI/mobile/computer automation**.

Its role in S4 is:

```text
A Comprehensive Survey of Agents for Computer Use: Foundations, Challenges, and Future Directions
→ computer-use agent survey
→ supporting P2 source for web/GUI/computer-use agent discussion
```

Use it after explaining what the paper does. Do not introduce it only as “P2”; introduce the method or idea first.

---

## Relation to thesis topic

Your thesis topic is:

```text
LLM-based agents for generalized web automation and data extraction
```

This paper matters because:

It is highly useful for framing S4’s broader computer-use agent landscape.

For generalized web automation, the connection is:

```text
web / GUI / mobile / computer-use interaction
→ agent observes a digital environment
→ agent chooses actions
→ agent extracts information or completes a workflow
```

Even when the paper is not directly about data extraction, it still helps explain the automation layer needed before extraction can be generalized.

---

## How to use this paper in the literature review

Recommended use:

- Use as **P2 support**, not as the central backbone.
- Use for one precise idea, architecture, benchmark, or limitation.
- If peer-reviewed, it can support stronger claims.
- If preprint/workshop/technical report, use it for recent trends and emerging directions.

Suggested sentence:

> A Comprehensive Survey of Agents for Computer Use: Foundations, Challenges, and Future Directions shows how computer-use agent survey contributes to the development of LLM-based agents for digital task automation, but its limitations indicate that generalized web automation still requires stronger grounding, verification, and recovery mechanisms.

---

## Reading decision

- **Keep in S4 P2:** Yes
- **Read fully?** No, selected sections are enough unless promoted later
- **Depth needed:** Low to medium
- **Main use:** Support S4 discussion of computer-use agent survey
- **Most important parts:**
  - Abstract
  - Introduction
  - Main architecture / method figure
  - Dataset or benchmark section
  - Results table
  - Limitations / discussion

---

## One-sentence summary

A Comprehensive Survey of Agents for Computer Use: Foundations, Challenges, and Future Directions is a P2 supporting paper for S4 because it explains **computer-use agent survey**, but it should be cited according to its venue/status and not overused beyond its evidence.

---

## BibTeX placeholder

```bibtex
@misc{acomprehensivesurveyofagentsforcomp2025,
  title = {A Comprehensive Survey of Agents for Computer Use: Foundations, Challenges, and Future Directions},
  year = {2025},
  note = {arXiv survey; Survey preprint. Verify final bibliographic metadata before thesis submission.}
}
```


---

<!-- ========== FILE: S4_P2\paper_first_notes\S4_P2_19_Mobile-Agent-E_Self-Evolving_Mobile_Assistant_for_Complex_Tasks.md ========== -->

## Source: `S4_P2\paper_first_notes\S4_P2_19_Mobile-Agent-E_Self-Evolving_Mobile_Assistant_for_Complex_Tasks.md`

# S4 P2 Paper 19 — Mobile-Agent-E: Self-Evolving Mobile Assistant for Complex Tasks

## Metadata

- **Title:** Mobile-Agent-E: Self-Evolving Mobile Assistant for Complex Tasks
- **Year:** 2025
- **Venue / status:** arXiv preprint; SEA @ NeurIPS 2025 workshop oral
- **Peer-reviewed status:** Workshop
- **Publication type:** Workshop / preprint
- **Thesis section:** S4 — mobile agents, memory, and self-evolution
- **Category:** self-evolving mobile agents / hierarchical multi-agent mobile assistant
- **Priority:** P2
- **BibTeX key:** `mobileagenteselfevolvingmobileassis2025`

---

## Simple understanding

Mobile-Agent-E is a hierarchical multi-agent mobile assistant that separates high-level planning from low-level action and learns from past experience using Tips and Shortcuts.

In simple terms:

```text
Problem → how can an AI agent interact with a web, GUI, mobile, desktop, or application environment?
Method → add perception, planning, action, memory, API/tool use, state tracking, or browser control.
Goal → complete real user tasks more flexibly than scripts or static chatbots.
```

This note explains the paper first, then connects it to S4 and your thesis.

---

## Core idea

Use a Manager plus Perceptor, Operator, Action Reflector, and Notetaker agents, with self-evolution memory that stores reusable Tips and Shortcuts.

The paper is mainly about:

```text
self-evolving mobile agents / hierarchical multi-agent mobile assistant
```

It contributes to the larger agent loop:

```text
observe → understand state → plan → act → receive feedback → verify / recover → complete task
```

---

## Key finding / main claim

The paper reports that self-evolution improves performance and efficiency on complex real-world mobile tasks.

For S4, the important question is not only whether the method works on its benchmark, but **which part of web/GUI agency it improves**:

- perception and grounding,
- planning and reasoning,
- action execution,
- API/tool use,
- memory/state tracking,
- recovery and verification,
- or deployment/evaluation.

---

## Key evidence to extract from the paper

When reading the paper, extract these points:

- **Figure 1 showing hierarchical agents and self-evolution memory.**
- **Mobile-Eval-E benchmark for long-horizon multi-app tasks.**
- **Reported 22% absolute improvement over previous SOTA across model backbones.**

These are the most useful parts for writing a literature-review paragraph.

---

## Limitations

- **Limitation 1:** Workshop/preprint status, not main archival NeurIPS.
- **Limitation 2:** Mobile tasks are related to but not identical to web automation.
- **Limitation 3:** Persistent shortcuts can become stale when apps change.

General thesis-level limitation:

```text
Improving one agent component is not enough for generalized web automation.
A robust web agent still needs grounding, planning, execution, verification, recovery, and safety.
```

---

## Relation to S4

This paper belongs in S4 because S4 discusses **LLM-based agents for web/GUI/mobile/computer automation**.

Its role in S4 is:

```text
Mobile-Agent-E: Self-Evolving Mobile Assistant for Complex Tasks
→ self-evolving mobile agents / hierarchical multi-agent mobile assistant
→ supporting P2 source for web/GUI/computer-use agent discussion
```

Use it after explaining what the paper does. Do not introduce it only as “P2”; introduce the method or idea first.

---

## Relation to thesis topic

Your thesis topic is:

```text
LLM-based agents for generalized web automation and data extraction
```

This paper matters because:

It is useful for showing how mobile agents move beyond reactive action selection toward memory and reusable experience.

For generalized web automation, the connection is:

```text
web / GUI / mobile / computer-use interaction
→ agent observes a digital environment
→ agent chooses actions
→ agent extracts information or completes a workflow
```

Even when the paper is not directly about data extraction, it still helps explain the automation layer needed before extraction can be generalized.

---

## How to use this paper in the literature review

Recommended use:

- Use as **P2 support**, not as the central backbone.
- Use for one precise idea, architecture, benchmark, or limitation.
- If peer-reviewed, it can support stronger claims.
- If preprint/workshop/technical report, use it for recent trends and emerging directions.

Suggested sentence:

> Mobile-Agent-E: Self-Evolving Mobile Assistant for Complex Tasks shows how self-evolving mobile agents / hierarchical multi-agent mobile assistant contributes to the development of LLM-based agents for digital task automation, but its limitations indicate that generalized web automation still requires stronger grounding, verification, and recovery mechanisms.

---

## Reading decision

- **Keep in S4 P2:** Yes
- **Read fully?** No, selected sections are enough unless promoted later
- **Depth needed:** Low to medium
- **Main use:** Support S4 discussion of self-evolving mobile agents / hierarchical multi-agent mobile assistant
- **Most important parts:**
  - Abstract
  - Introduction
  - Main architecture / method figure
  - Dataset or benchmark section
  - Results table
  - Limitations / discussion

---

## One-sentence summary

Mobile-Agent-E: Self-Evolving Mobile Assistant for Complex Tasks is a P2 supporting paper for S4 because it explains **self-evolving mobile agents / hierarchical multi-agent mobile assistant**, but it should be cited according to its venue/status and not overused beyond its evidence.

---

## BibTeX placeholder

```bibtex
@misc{mobileagenteselfevolvingmobileassis2025,
  title = {Mobile-Agent-E: Self-Evolving Mobile Assistant for Complex Tasks},
  year = {2025},
  note = {arXiv preprint; SEA @ NeurIPS 2025 workshop oral; Workshop / preprint. Verify final bibliographic metadata before thesis submission.}
}
```


---

<!-- ========== FILE: S4_P2\paper_first_notes\S4_P2_20_ReachAgent_Enhancing_Mobile_Agent_via_Page_Reaching_and_Page_Operation.md ========== -->

## Source: `S4_P2\paper_first_notes\S4_P2_20_ReachAgent_Enhancing_Mobile_Agent_via_Page_Reaching_and_Page_Operation.md`

# S4 P2 Paper 20 — ReachAgent: Enhancing Mobile Agent via Page Reaching and Page Operation

## Metadata

- **Title:** ReachAgent: Enhancing Mobile Agent via Page Reaching and Page Operation
- **Year:** 2025
- **Venue / status:** NAACL 2025 long paper
- **Peer-reviewed status:** Yes
- **Publication type:** Peer-reviewed conference paper
- **Thesis section:** S4 — mobile GUI agent training
- **Category:** mobile agent training / page reaching and operation
- **Priority:** P2
- **BibTeX key:** `reachagentenhancingmobileagentviapa2025`

---

## Simple understanding

ReachAgent improves mobile agents by decomposing tasks into page-reaching and page-operation subtasks. It focuses on the whole GUI flow, not just the most relevant current element.

In simple terms:

```text
Problem → how can an AI agent interact with a web, GUI, mobile, desktop, or application environment?
Method → add perception, planning, action, memory, API/tool use, state tracking, or browser control.
Goal → complete real user tasks more flexibly than scripts or static chatbots.
```

This note explains the paper first, then connects it to S4 and your thesis.

---

## Core idea

Train mobile agents to reach target pages and perform specified operations, using MobileReach and reward-based preference GUI flows.

The paper is mainly about:

```text
mobile agent training / page reaching and operation
```

It contributes to the larger agent loop:

```text
observe → understand state → plan → act → receive feedback → verify / recover → complete task
```

---

## Key finding / main claim

ReachAgent improves step-level and task-level action accuracy over prior mobile agents by focusing on subtask completion and GUI flow quality.

For S4, the important question is not only whether the method works on its benchmark, but **which part of web/GUI agency it improves**:

- perception and grounding,
- planning and reasoning,
- action execution,
- API/tool use,
- memory/state tracking,
- recovery and verification,
- or deployment/evaluation.

---

## Key evidence to extract from the paper

When reading the paper, extract these points:

- **Figure 1/2 showing task decomposition into Reach and Operate subtasks.**
- **MobileReach dataset.**
- **Reported IoU and text accuracy improvements over SOTA.**

These are the most useful parts for writing a literature-review paragraph.

---

## Limitations

- **Limitation 1:** It is mobile-specific, not a general web-browser agent.
- **Limitation 2:** Training data and action alignment may depend on mobile app structure.
- **Limitation 3:** Page reaching/operation helps but does not solve all long-horizon planning failures.

General thesis-level limitation:

```text
Improving one agent component is not enough for generalized web automation.
A robust web agent still needs grounding, planning, execution, verification, recovery, and safety.
```

---

## Relation to S4

This paper belongs in S4 because S4 discusses **LLM-based agents for web/GUI/mobile/computer automation**.

Its role in S4 is:

```text
ReachAgent: Enhancing Mobile Agent via Page Reaching and Page Operation
→ mobile agent training / page reaching and operation
→ supporting P2 source for web/GUI/computer-use agent discussion
```

Use it after explaining what the paper does. Do not introduce it only as “P2”; introduce the method or idea first.

---

## Relation to thesis topic

Your thesis topic is:

```text
LLM-based agents for generalized web automation and data extraction
```

This paper matters because:

It is a strong peer-reviewed paper for the mobile-agent subsection of S4.

For generalized web automation, the connection is:

```text
web / GUI / mobile / computer-use interaction
→ agent observes a digital environment
→ agent chooses actions
→ agent extracts information or completes a workflow
```

Even when the paper is not directly about data extraction, it still helps explain the automation layer needed before extraction can be generalized.

---

## How to use this paper in the literature review

Recommended use:

- Use as **P2 support**, not as the central backbone.
- Use for one precise idea, architecture, benchmark, or limitation.
- If peer-reviewed, it can support stronger claims.
- If preprint/workshop/technical report, use it for recent trends and emerging directions.

Suggested sentence:

> ReachAgent: Enhancing Mobile Agent via Page Reaching and Page Operation shows how mobile agent training / page reaching and operation contributes to the development of LLM-based agents for digital task automation, but its limitations indicate that generalized web automation still requires stronger grounding, verification, and recovery mechanisms.

---

## Reading decision

- **Keep in S4 P2:** Yes
- **Read fully?** Yes or selected sections carefully
- **Depth needed:** Medium to high
- **Main use:** Support S4 discussion of mobile agent training / page reaching and operation
- **Most important parts:**
  - Abstract
  - Introduction
  - Main architecture / method figure
  - Dataset or benchmark section
  - Results table
  - Limitations / discussion

---

## One-sentence summary

ReachAgent: Enhancing Mobile Agent via Page Reaching and Page Operation is a P2 supporting paper for S4 because it explains **mobile agent training / page reaching and operation**, but it should be cited according to its venue/status and not overused beyond its evidence.

---

## BibTeX placeholder

```bibtex
@misc{reachagentenhancingmobileagentviapa2025,
  title = {ReachAgent: Enhancing Mobile Agent via Page Reaching and Page Operation},
  year = {2025},
  note = {NAACL 2025 long paper; Peer-reviewed conference paper. Verify final bibliographic metadata before thesis submission.}
}
```


---

<!-- ========== FILE: S4_P2\paper_first_notes\S4_P2_21_LiteWebAgent_The_Open-Source_Suite_for_VLM-Based_Web-Agent_Applications.md ========== -->

## Source: `S4_P2\paper_first_notes\S4_P2_21_LiteWebAgent_The_Open-Source_Suite_for_VLM-Based_Web-Agent_Applications.md`

# S4 P2 Paper 21 — LiteWebAgent: The Open-Source Suite for VLM-Based Web-Agent Applications

## Metadata

- **Title:** LiteWebAgent: The Open-Source Suite for VLM-Based Web-Agent Applications
- **Year:** 2025
- **Venue / status:** NAACL 2025 System Demonstrations
- **Peer-reviewed status:** Yes, demo
- **Publication type:** System demonstration paper
- **Thesis section:** S4 — web-agent frameworks and deployment
- **Category:** open-source VLM web-agent suite
- **Priority:** P2
- **BibTeX key:** `litewebagenttheopensourcesuiteforvl2025`

---

## Simple understanding

LiteWebAgent is an open-source suite for VLM-based web-agent applications. It provides a core agent framework plus deployable web app and Chrome extension.

In simple terms:

```text
Problem → how can an AI agent interact with a web, GUI, mobile, desktop, or application environment?
Method → add perception, planning, action, memory, API/tool use, state tracking, or browser control.
Goal → complete real user tasks more flexibly than scripts or static chatbots.
```

This note explains the paper first, then connects it to S4 and your thesis.

---

## Core idea

Build a modular web-agent framework with planning, memory, tree search, recursive function calling, and decoupled action generation/grounding.

The paper is mainly about:

```text
open-source VLM web-agent suite
```

It contributes to the larger agent loop:

```text
observe → understand state → plan → act → receive feedback → verify / recover → complete task
```

---

## Key finding / main claim

The paper addresses a tooling gap by offering an extensible, production-oriented web-agent suite for both research and deployment.

For S4, the important question is not only whether the method works on its benchmark, but **which part of web/GUI agency it improves**:

- perception and grounding,
- planning and reasoning,
- action execution,
- API/tool use,
- memory/state tracking,
- recovery and verification,
- or deployment/evaluation.

---

## Key evidence to extract from the paper

When reading the paper, extract these points:

- **Abstract describing planning, memory, and tree-search capabilities.**
- **Two deployment modes: Vercel remote browser and Chrome extension via CDP.**
- **Section 1.2 ecosystem categories and gap analysis.**

These are the most useful parts for writing a literature-review paragraph.

---

## Limitations

- **Limitation 1:** System demo paper, so it is more about infrastructure than a new benchmark-leading method.
- **Limitation 2:** Performance depends on connected VLMs and deployment settings.
- **Limitation 3:** Production-readiness does not guarantee robust performance on arbitrary websites.

General thesis-level limitation:

```text
Improving one agent component is not enough for generalized web automation.
A robust web agent still needs grounding, planning, execution, verification, recovery, and safety.
```

---

## Relation to S4

This paper belongs in S4 because S4 discusses **LLM-based agents for web/GUI/mobile/computer automation**.

Its role in S4 is:

```text
LiteWebAgent: The Open-Source Suite for VLM-Based Web-Agent Applications
→ open-source VLM web-agent suite
→ supporting P2 source for web/GUI/computer-use agent discussion
```

Use it after explaining what the paper does. Do not introduce it only as “P2”; introduce the method or idea first.

---

## Relation to thesis topic

Your thesis topic is:

```text
LLM-based agents for generalized web automation and data extraction
```

This paper matters because:

It is directly useful for your thesis because it connects web-agent research with practical deployment infrastructure.

For generalized web automation, the connection is:

```text
web / GUI / mobile / computer-use interaction
→ agent observes a digital environment
→ agent chooses actions
→ agent extracts information or completes a workflow
```

Even when the paper is not directly about data extraction, it still helps explain the automation layer needed before extraction can be generalized.

---

## How to use this paper in the literature review

Recommended use:

- Use as **P2 support**, not as the central backbone.
- Use for one precise idea, architecture, benchmark, or limitation.
- If peer-reviewed, it can support stronger claims.
- If preprint/workshop/technical report, use it for recent trends and emerging directions.

Suggested sentence:

> LiteWebAgent: The Open-Source Suite for VLM-Based Web-Agent Applications shows how open-source VLM web-agent suite contributes to the development of LLM-based agents for digital task automation, but its limitations indicate that generalized web automation still requires stronger grounding, verification, and recovery mechanisms.

---

## Reading decision

- **Keep in S4 P2:** Yes
- **Read fully?** Yes or selected sections carefully
- **Depth needed:** Medium to high
- **Main use:** Support S4 discussion of open-source VLM web-agent suite
- **Most important parts:**
  - Abstract
  - Introduction
  - Main architecture / method figure
  - Dataset or benchmark section
  - Results table
  - Limitations / discussion

---

## One-sentence summary

LiteWebAgent: The Open-Source Suite for VLM-Based Web-Agent Applications is a P2 supporting paper for S4 because it explains **open-source VLM web-agent suite**, but it should be cited according to its venue/status and not overused beyond its evidence.

---

## BibTeX placeholder

```bibtex
@misc{litewebagenttheopensourcesuiteforvl2025,
  title = {LiteWebAgent: The Open-Source Suite for VLM-Based Web-Agent Applications},
  year = {2025},
  note = {NAACL 2025 System Demonstrations; System demonstration paper. Verify final bibliographic metadata before thesis submission.}
}
```


---

<!-- ========== FILE: S4_P2\paper_first_notes\S4_P2_22_LLM-Powered_GUI_Agents_in_Phone_Automation_Surveying_Progress_and_Prospects.md ========== -->

## Source: `S4_P2\paper_first_notes\S4_P2_22_LLM-Powered_GUI_Agents_in_Phone_Automation_Surveying_Progress_and_Prospects.md`

# S4 P2 Paper 22 — LLM-Powered GUI Agents in Phone Automation: Surveying Progress and Prospects

## Metadata

- **Title:** LLM-Powered GUI Agents in Phone Automation: Surveying Progress and Prospects
- **Year:** 2025
- **Venue / status:** Transactions on Machine Learning Research, 11/2025
- **Peer-reviewed status:** Yes
- **Publication type:** Peer-reviewed TMLR survey
- **Thesis section:** S4 — phone GUI agents and mobile automation
- **Category:** phone GUI agent survey
- **Priority:** P2
- **BibTeX key:** `llmpoweredguiagentsinphoneautomatio2025`

---

## Simple understanding

This survey systematically reviews LLM-powered phone GUI agents, including frameworks, models, datasets, benchmarks, and open challenges.

In simple terms:

```text
Problem → how can an AI agent interact with a web, GUI, mobile, desktop, or application environment?
Method → add perception, planning, action, memory, API/tool use, state tracking, or browser control.
Goal → complete real user tasks more flexibly than scripts or static chatbots.
```

This note explains the paper first, then connects it to S4 and your thesis.

---

## Core idea

Provide a mobile-specific taxonomy covering single-agent, multi-agent, plan-then-act frameworks, prompt/training methods, and evaluation resources.

The paper is mainly about:

```text
phone GUI agent survey
```

It contributes to the larger agent loop:

```text
observe → understand state → plan → act → receive feedback → verify / recover → complete task
```

---

## Key finding / main claim

LLMs transform phone automation by improving intent understanding, multimodal perception, and decision-making, but challenges remain in data diversity, on-device efficiency, adaptation, and security.

For S4, the important question is not only whether the method works on its benchmark, but **which part of web/GUI agency it improves**:

- perception and grounding,
- planning and reasoning,
- action execution,
- API/tool use,
- memory/state tracking,
- recovery and verification,
- or deployment/evaluation.

---

## Key evidence to extract from the paper

When reading the paper, extract these points:

- **Figure 1 comparing conversational LLMs and phone GUI agents.**
- **Figure 2 comprehensive taxonomy of phone GUI agents.**
- **Table comparing this survey with prior GUI/RPA/LLM-agent surveys.**

These are the most useful parts for writing a literature-review paragraph.

---

## Limitations

- **Limitation 1:** Survey, not primary method.
- **Limitation 2:** Phone-specific focus may not cover all web/desktop agents in depth.
- **Limitation 3:** Recent field changes may quickly make some taxonomy parts outdated.

General thesis-level limitation:

```text
Improving one agent component is not enough for generalized web automation.
A robust web agent still needs grounding, planning, execution, verification, recovery, and safety.
```

---

## Relation to S4

This paper belongs in S4 because S4 discusses **LLM-based agents for web/GUI/mobile/computer automation**.

Its role in S4 is:

```text
LLM-Powered GUI Agents in Phone Automation: Surveying Progress and Prospects
→ phone GUI agent survey
→ supporting P2 source for web/GUI/computer-use agent discussion
```

Use it after explaining what the paper does. Do not introduce it only as “P2”; introduce the method or idea first.

---

## Relation to thesis topic

Your thesis topic is:

```text
LLM-based agents for generalized web automation and data extraction
```

This paper matters because:

It is one of the safest and strongest survey sources for the mobile/phone-agent part of S4.

For generalized web automation, the connection is:

```text
web / GUI / mobile / computer-use interaction
→ agent observes a digital environment
→ agent chooses actions
→ agent extracts information or completes a workflow
```

Even when the paper is not directly about data extraction, it still helps explain the automation layer needed before extraction can be generalized.

---

## How to use this paper in the literature review

Recommended use:

- Use as **P2 support**, not as the central backbone.
- Use for one precise idea, architecture, benchmark, or limitation.
- If peer-reviewed, it can support stronger claims.
- If preprint/workshop/technical report, use it for recent trends and emerging directions.

Suggested sentence:

> LLM-Powered GUI Agents in Phone Automation: Surveying Progress and Prospects shows how phone GUI agent survey contributes to the development of LLM-based agents for digital task automation, but its limitations indicate that generalized web automation still requires stronger grounding, verification, and recovery mechanisms.

---

## Reading decision

- **Keep in S4 P2:** Yes
- **Read fully?** Yes or selected sections carefully
- **Depth needed:** Medium to high
- **Main use:** Support S4 discussion of phone GUI agent survey
- **Most important parts:**
  - Abstract
  - Introduction
  - Main architecture / method figure
  - Dataset or benchmark section
  - Results table
  - Limitations / discussion

---

## One-sentence summary

LLM-Powered GUI Agents in Phone Automation: Surveying Progress and Prospects is a P2 supporting paper for S4 because it explains **phone GUI agent survey**, but it should be cited according to its venue/status and not overused beyond its evidence.

---

## BibTeX placeholder

```bibtex
@misc{llmpoweredguiagentsinphoneautomatio2025,
  title = {LLM-Powered GUI Agents in Phone Automation: Surveying Progress and Prospects},
  year = {2025},
  note = {Transactions on Machine Learning Research, 11/2025; Peer-reviewed TMLR survey. Verify final bibliographic metadata before thesis submission.}
}
```


---

<!-- ========== FILE: S4_P2\paper_first_notes\S4_P2_23_WebThinker_Empowering_Large_Reasoning_Models_with_Deep_Research_Capability.md ========== -->

## Source: `S4_P2\paper_first_notes\S4_P2_23_WebThinker_Empowering_Large_Reasoning_Models_with_Deep_Research_Capability.md`

# S4 P2 Paper 23 — WebThinker: Empowering Large Reasoning Models with Deep Research Capability

## Metadata

- **Title:** WebThinker: Empowering Large Reasoning Models with Deep Research Capability
- **Year:** 2025
- **Venue / status:** NeurIPS 2025
- **Peer-reviewed status:** Yes
- **Publication type:** Peer-reviewed conference paper
- **Thesis section:** S4 — deep research web agents
- **Category:** deep research web agents / reasoning with tools
- **Priority:** P2
- **BibTeX key:** `webthinkerempoweringlargereasoningm2025`

---

## Simple understanding

WebThinker gives large reasoning models deep research capability by allowing them to search, navigate web pages, extract information, and draft reports during reasoning.

In simple terms:

```text
Problem → how can an AI agent interact with a web, GUI, mobile, desktop, or application environment?
Method → add perception, planning, action, memory, API/tool use, state tracking, or browser control.
Goal → complete real user tasks more flexibly than scripts or static chatbots.
```

This note explains the paper first, then connects it to S4 and your thesis.

---

## Core idea

Integrate a Deep Web Explorer and Autonomous Think-Search-and-Draft strategy into LRMs, with online DPO training for research-tool use.

The paper is mainly about:

```text
deep research web agents / reasoning with tools
```

It contributes to the larger agent loop:

```text
observe → understand state → plan → act → receive feedback → verify / recover → complete task
```

---

## Key finding / main claim

WebThinker outperforms prior methods on complex reasoning benchmarks and scientific report generation tasks by interleaving reasoning, search, navigation, and drafting.

For S4, the important question is not only whether the method works on its benchmark, but **which part of web/GUI agency it improves**:

- perception and grounding,
- planning and reasoning,
- action execution,
- API/tool use,
- memory/state tracking,
- recovery and verification,
- or deployment/evaluation.

---

## Key evidence to extract from the paper

When reading the paper, extract these points:

- **Figure 2 comparing Standard RAG, predefined workflow RAG, and WebThinker.**
- **Figure 3 showing Problem-Solving and Report-Generation modes.**
- **Reported gains on GPQA, GAIA, WebWalkerQA, HLE, and Glaive.**

These are the most useful parts for writing a literature-review paragraph.

---

## Limitations

- **Limitation 1:** Deep research differs from transactional web automation such as filling forms or booking services.
- **Limitation 2:** Performance depends on search quality and tool integration.
- **Limitation 3:** Report generation quality still requires factuality and citation verification.

General thesis-level limitation:

```text
Improving one agent component is not enough for generalized web automation.
A robust web agent still needs grounding, planning, execution, verification, recovery, and safety.
```

---

## Relation to S4

This paper belongs in S4 because S4 discusses **LLM-based agents for web/GUI/mobile/computer automation**.

Its role in S4 is:

```text
WebThinker: Empowering Large Reasoning Models with Deep Research Capability
→ deep research web agents / reasoning with tools
→ supporting P2 source for web/GUI/computer-use agent discussion
```

Use it after explaining what the paper does. Do not introduce it only as “P2”; introduce the method or idea first.

---

## Relation to thesis topic

Your thesis topic is:

```text
LLM-based agents for generalized web automation and data extraction
```

This paper matters because:

It is a strong peer-reviewed source for web agents that perform information gathering and research, close to your thesis theme of web data extraction.

For generalized web automation, the connection is:

```text
web / GUI / mobile / computer-use interaction
→ agent observes a digital environment
→ agent chooses actions
→ agent extracts information or completes a workflow
```

Even when the paper is not directly about data extraction, it still helps explain the automation layer needed before extraction can be generalized.

---

## How to use this paper in the literature review

Recommended use:

- Use as **P2 support**, not as the central backbone.
- Use for one precise idea, architecture, benchmark, or limitation.
- If peer-reviewed, it can support stronger claims.
- If preprint/workshop/technical report, use it for recent trends and emerging directions.

Suggested sentence:

> WebThinker: Empowering Large Reasoning Models with Deep Research Capability shows how deep research web agents / reasoning with tools contributes to the development of LLM-based agents for digital task automation, but its limitations indicate that generalized web automation still requires stronger grounding, verification, and recovery mechanisms.

---

## Reading decision

- **Keep in S4 P2:** Yes
- **Read fully?** Yes or selected sections carefully
- **Depth needed:** Medium to high
- **Main use:** Support S4 discussion of deep research web agents / reasoning with tools
- **Most important parts:**
  - Abstract
  - Introduction
  - Main architecture / method figure
  - Dataset or benchmark section
  - Results table
  - Limitations / discussion

---

## One-sentence summary

WebThinker: Empowering Large Reasoning Models with Deep Research Capability is a P2 supporting paper for S4 because it explains **deep research web agents / reasoning with tools**, but it should be cited according to its venue/status and not overused beyond its evidence.

---

## BibTeX placeholder

```bibtex
@misc{webthinkerempoweringlargereasoningm2025,
  title = {WebThinker: Empowering Large Reasoning Models with Deep Research Capability},
  year = {2025},
  note = {NeurIPS 2025; Peer-reviewed conference paper. Verify final bibliographic metadata before thesis submission.}
}
```


---

<!-- ========== FILE: S4_P2\paper_first_notes\S4_P2_24_Beyond_Browsing_API-Based_Web_Agents.md ========== -->

## Source: `S4_P2\paper_first_notes\S4_P2_24_Beyond_Browsing_API-Based_Web_Agents.md`

# S4 P2 Paper 24 — Beyond Browsing: API-Based Web Agents

## Metadata

- **Title:** Beyond Browsing: API-Based Web Agents
- **Year:** 2025
- **Venue / status:** arXiv preprint
- **Peer-reviewed status:** No confirmed archival venue
- **Publication type:** Preprint
- **Thesis section:** S4 — API vs browser web-agent design
- **Category:** API-based and hybrid web agents
- **Priority:** P2
- **BibTeX key:** `beyondbrowsingapibasedwebagents2025`

---

## Simple understanding

This paper asks whether web agents should use APIs instead of only browsing. It proposes API-only and hybrid agents and compares them with browsing-only agents on WebArena.

In simple terms:

```text
Problem → how can an AI agent interact with a web, GUI, mobile, desktop, or application environment?
Method → add perception, planning, action, memory, API/tool use, state tracking, or browser control.
Goal → complete real user tasks more flexibly than scripts or static chatbots.
```

This note explains the paper first, then connects it to S4 and your thesis.

---

## Core idea

Expand web-agent action spaces to include API calls and code execution, with a hybrid agent that dynamically interleaves browsing and API actions.

The paper is mainly about:

```text
API-based and hybrid web agents
```

It contributes to the larger agent loop:

```text
observe → understand state → plan → act → receive feedback → verify / recover → complete task
```

---

## Key finding / main claim

API-based agents outperform browsing-only agents on WebArena, and hybrid agents perform best, reaching 38.9% success in the reported setup.

For S4, the important question is not only whether the method works on its benchmark, but **which part of web/GUI agency it improves**:

- perception and grounding,
- planning and reasoning,
- action execution,
- API/tool use,
- memory/state tracking,
- recovery and verification,
- or deployment/evaluation.

---

## Key evidence to extract from the paper

When reading the paper, extract these points:

- **Figure 1 comparing browsing, API-based, and hybrid agents.**
- **Example where API calls solve a GitLab task in fewer steps than browsing.**
- **Reported average: browsing 14.8%, API-based 29.2%, hybrid 38.9%.**

These are the most useful parts for writing a literature-review paragraph.

---

## Limitations

- **Limitation 1:** Preprint status.
- **Limitation 2:** APIs are not always available, documented, or authorized.
- **Limitation 3:** The study focuses on text-only WebArena tasks and may not cover visual web tasks.

General thesis-level limitation:

```text
Improving one agent component is not enough for generalized web automation.
A robust web agent still needs grounding, planning, execution, verification, recovery, and safety.
```

---

## Relation to S4

This paper belongs in S4 because S4 discusses **LLM-based agents for web/GUI/mobile/computer automation**.

Its role in S4 is:

```text
Beyond Browsing: API-Based Web Agents
→ API-based and hybrid web agents
→ supporting P2 source for web/GUI/computer-use agent discussion
```

Use it after explaining what the paper does. Do not introduce it only as “P2”; introduce the method or idea first.

---

## Relation to thesis topic

Your thesis topic is:

```text
LLM-based agents for generalized web automation and data extraction
```

This paper matters because:

It is extremely relevant to your thesis because it challenges the assumption that generalized web agents should always act through human-facing browsers.

For generalized web automation, the connection is:

```text
web / GUI / mobile / computer-use interaction
→ agent observes a digital environment
→ agent chooses actions
→ agent extracts information or completes a workflow
```

Even when the paper is not directly about data extraction, it still helps explain the automation layer needed before extraction can be generalized.

---

## How to use this paper in the literature review

Recommended use:

- Use as **P2 support**, not as the central backbone.
- Use for one precise idea, architecture, benchmark, or limitation.
- If peer-reviewed, it can support stronger claims.
- If preprint/workshop/technical report, use it for recent trends and emerging directions.

Suggested sentence:

> Beyond Browsing: API-Based Web Agents shows how API-based and hybrid web agents contributes to the development of LLM-based agents for digital task automation, but its limitations indicate that generalized web automation still requires stronger grounding, verification, and recovery mechanisms.

---

## Reading decision

- **Keep in S4 P2:** Yes
- **Read fully?** No, selected sections are enough unless promoted later
- **Depth needed:** Low to medium
- **Main use:** Support S4 discussion of API-based and hybrid web agents
- **Most important parts:**
  - Abstract
  - Introduction
  - Main architecture / method figure
  - Dataset or benchmark section
  - Results table
  - Limitations / discussion

---

## One-sentence summary

Beyond Browsing: API-Based Web Agents is a P2 supporting paper for S4 because it explains **API-based and hybrid web agents**, but it should be cited according to its venue/status and not overused beyond its evidence.

---

## BibTeX placeholder

```bibtex
@misc{beyondbrowsingapibasedwebagents2025,
  title = {Beyond Browsing: API-Based Web Agents},
  year = {2025},
  note = {arXiv preprint; Preprint. Verify final bibliographic metadata before thesis submission.}
}
```


---

<!-- ========== FILE: S4_P2\paper_first_notes\S4_P2_25_GA_A_Comprehensive_Survey_on_LLM-based_GUI_Agent.md ========== -->

## Source: `S4_P2\paper_first_notes\S4_P2_25_GA_A_Comprehensive_Survey_on_LLM-based_GUI_Agent.md`

# S4 P2 Paper 25 — GA: A Comprehensive Survey on LLM-based GUI Agent

## Metadata

- **Title:** GA: A Comprehensive Survey on LLM-based GUI Agent
- **Year:** 2025
- **Venue / status:** TechRxiv / submitted manuscript
- **Peer-reviewed status:** Not peer-reviewed in uploaded version
- **Publication type:** TechRxiv survey / submitted preprint
- **Thesis section:** S4 — GUI-agent taxonomy
- **Category:** GUI-agent survey
- **Priority:** P2
- **BibTeX key:** `gaacomprehensivesurveyonllmbasedgui2025`

---

## Simple understanding

This survey reviews LLM-based GUI agents across environment understanding, device control, user interaction, personalization, collaboration, and task automation pipelines.

In simple terms:

```text
Problem → how can an AI agent interact with a web, GUI, mobile, desktop, or application environment?
Method → add perception, planning, action, memory, API/tool use, state tracking, or browser control.
Goal → complete real user tasks more flexibly than scripts or static chatbots.
```

This note explains the paper first, then connects it to S4 and your thesis.

---

## Core idea

Summarize GUI-agent capabilities and propose a taxonomy based on how agents understand GUI environments: vision-based, text-based, and hybrid text-vision.

The paper is mainly about:

```text
GUI-agent survey
```

It contributes to the larger agent loop:

```text
observe → understand state → plan → act → receive feedback → verify / recover → complete task
```

---

## Key finding / main claim

LLM-based GUI agents move beyond template-based automation by understanding GUI states in real time and selecting actions flexibly.

For S4, the important question is not only whether the method works on its benchmark, but **which part of web/GUI agency it improves**:

- perception and grounding,
- planning and reasoning,
- action execution,
- API/tool use,
- memory/state tracking,
- recovery and verification,
- or deployment/evaluation.

---

## Key evidence to extract from the paper

When reading the paper, extract these points:

- **Figure 1 basic GUI-agent task automation pipeline.**
- **Taxonomy into vision-based, text-based, and hybrid agents.**
- **Discussion of one-stage vs two-stage exploration-to-exploitation pipelines.**

These are the most useful parts for writing a literature-review paragraph.

---

## Limitations

- **Limitation 1:** TechRxiv explicitly marks the uploaded version as not peer reviewed.
- **Limitation 2:** Some content may change if accepted to a journal.
- **Limitation 3:** Use only as supplementary survey support.

General thesis-level limitation:

```text
Improving one agent component is not enough for generalized web automation.
A robust web agent still needs grounding, planning, execution, verification, recovery, and safety.
```

---

## Relation to S4

This paper belongs in S4 because S4 discusses **LLM-based agents for web/GUI/mobile/computer automation**.

Its role in S4 is:

```text
GA: A Comprehensive Survey on LLM-based GUI Agent
→ GUI-agent survey
→ supporting P2 source for web/GUI/computer-use agent discussion
```

Use it after explaining what the paper does. Do not introduce it only as “P2”; introduce the method or idea first.

---

## Relation to thesis topic

Your thesis topic is:

```text
LLM-based agents for generalized web automation and data extraction
```

This paper matters because:

It can help broaden S4’s taxonomy, but should not be used as a main authoritative citation.

For generalized web automation, the connection is:

```text
web / GUI / mobile / computer-use interaction
→ agent observes a digital environment
→ agent chooses actions
→ agent extracts information or completes a workflow
```

Even when the paper is not directly about data extraction, it still helps explain the automation layer needed before extraction can be generalized.

---

## How to use this paper in the literature review

Recommended use:

- Use as **P2 support**, not as the central backbone.
- Use for one precise idea, architecture, benchmark, or limitation.
- If peer-reviewed, it can support stronger claims.
- If preprint/workshop/technical report, use it for recent trends and emerging directions.

Suggested sentence:

> GA: A Comprehensive Survey on LLM-based GUI Agent shows how GUI-agent survey contributes to the development of LLM-based agents for digital task automation, but its limitations indicate that generalized web automation still requires stronger grounding, verification, and recovery mechanisms.

---

## Reading decision

- **Keep in S4 P2:** Yes
- **Read fully?** No, selected sections are enough unless promoted later
- **Depth needed:** Low to medium
- **Main use:** Support S4 discussion of GUI-agent survey
- **Most important parts:**
  - Abstract
  - Introduction
  - Main architecture / method figure
  - Dataset or benchmark section
  - Results table
  - Limitations / discussion

---

## One-sentence summary

GA: A Comprehensive Survey on LLM-based GUI Agent is a P2 supporting paper for S4 because it explains **GUI-agent survey**, but it should be cited according to its venue/status and not overused beyond its evidence.

---

## BibTeX placeholder

```bibtex
@misc{gaacomprehensivesurveyonllmbasedgui2025,
  title = {GA: A Comprehensive Survey on LLM-based GUI Agent},
  year = {2025},
  note = {TechRxiv / submitted manuscript; TechRxiv survey / submitted preprint. Verify final bibliographic metadata before thesis submission.}
}
```


---

<!-- ========== FILE: S4_P2\paper_first_notes\S4_P2_26_Build_the_Web_for_Agents_Not_Agents_for_the_Web.md ========== -->

## Source: `S4_P2\paper_first_notes\S4_P2_26_Build_the_Web_for_Agents_Not_Agents_for_the_Web.md`

# S4 P2 Paper 26 — Build the Web for Agents, Not Agents for the Web

## Metadata

- **Title:** Build the Web for Agents, Not Agents for the Web
- **Year:** 2025
- **Venue / status:** arXiv position paper / under review
- **Peer-reviewed status:** No
- **Publication type:** Position paper / preprint
- **Thesis section:** S4 — agentic web interface design
- **Category:** agentic web interface / position paper
- **Priority:** P2
- **BibTeX key:** `buildthewebforagentsnotagentsforthe2025`

---

## Simple understanding

This position paper argues that instead of forcing agents to adapt to human-designed websites, we should build web interfaces designed for agents.

In simple terms:

```text
Problem → how can an AI agent interact with a web, GUI, mobile, desktop, or application environment?
Method → add perception, planning, action, memory, API/tool use, state tracking, or browser control.
Goal → complete real user tasks more flexibly than scripts or static chatbots.
```

This note explains the paper first, then connects it to S4 and your thesis.

---

## Core idea

Introduce the idea of Agentic Web Interfaces (AWIs): standardized, machine-oriented interfaces for web agents.

The paper is mainly about:

```text
agentic web interface / position paper
```

It contributes to the larger agent loop:

```text
observe → understand state → plan → act → receive feedback → verify / recover → complete task
```

---

## Key finding / main claim

The paper argues that screenshots, DOMs, and developer-oriented APIs are all imperfect for web agents, motivating a new agent-native interaction layer.

For S4, the important question is not only whether the method works on its benchmark, but **which part of web/GUI agency it improves**:

- perception and grounding,
- planning and reasoning,
- action execution,
- API/tool use,
- memory/state tracking,
- recovery and verification,
- or deployment/evaluation.

---

## Key evidence to extract from the paper

When reading the paper, extract these points:

- **Definition of web agents as sequential decision-making systems.**
- **Critique of screenshot, DOM, and API interaction methods.**
- **Six guiding principles for AWI design.**

These are the most useful parts for writing a literature-review paragraph.

---

## Limitations

- **Limitation 1:** Position paper, not an implemented system or benchmark.
- **Limitation 2:** No prototype is provided by design.
- **Limitation 3:** Claims are conceptual and should be framed as a research direction.

General thesis-level limitation:

```text
Improving one agent component is not enough for generalized web automation.
A robust web agent still needs grounding, planning, execution, verification, recovery, and safety.
```

---

## Relation to S4

This paper belongs in S4 because S4 discusses **LLM-based agents for web/GUI/mobile/computer automation**.

Its role in S4 is:

```text
Build the Web for Agents, Not Agents for the Web
→ agentic web interface / position paper
→ supporting P2 source for web/GUI/computer-use agent discussion
```

Use it after explaining what the paper does. Do not introduce it only as “P2”; introduce the method or idea first.

---

## Relation to thesis topic

Your thesis topic is:

```text
LLM-based agents for generalized web automation and data extraction
```

This paper matters because:

It gives a strong conceptual argument for your thesis: generalized web automation may require redesigning the web, not only improving agents.

For generalized web automation, the connection is:

```text
web / GUI / mobile / computer-use interaction
→ agent observes a digital environment
→ agent chooses actions
→ agent extracts information or completes a workflow
```

Even when the paper is not directly about data extraction, it still helps explain the automation layer needed before extraction can be generalized.

---

## How to use this paper in the literature review

Recommended use:

- Use as **P2 support**, not as the central backbone.
- Use for one precise idea, architecture, benchmark, or limitation.
- If peer-reviewed, it can support stronger claims.
- If preprint/workshop/technical report, use it for recent trends and emerging directions.

Suggested sentence:

> Build the Web for Agents, Not Agents for the Web shows how agentic web interface / position paper contributes to the development of LLM-based agents for digital task automation, but its limitations indicate that generalized web automation still requires stronger grounding, verification, and recovery mechanisms.

---

## Reading decision

- **Keep in S4 P2:** Yes
- **Read fully?** No, selected sections are enough unless promoted later
- **Depth needed:** Low to medium
- **Main use:** Support S4 discussion of agentic web interface / position paper
- **Most important parts:**
  - Abstract
  - Introduction
  - Main architecture / method figure
  - Dataset or benchmark section
  - Results table
  - Limitations / discussion

---

## One-sentence summary

Build the Web for Agents, Not Agents for the Web is a P2 supporting paper for S4 because it explains **agentic web interface / position paper**, but it should be cited according to its venue/status and not overused beyond its evidence.

---

## BibTeX placeholder

```bibtex
@misc{buildthewebforagentsnotagentsforthe2025,
  title = {Build the Web for Agents, Not Agents for the Web},
  year = {2025},
  note = {arXiv position paper / under review; Position paper / preprint. Verify final bibliographic metadata before thesis submission.}
}
```


---

<!-- ========== FILE: S4_P2\paper_first_notes\S4_P2_27_Embodied_Web_Agents_Bridging_Physical-Digital_Realms_for_Integrated_Agent_Intelligence.md ========== -->

## Source: `S4_P2\paper_first_notes\S4_P2_27_Embodied_Web_Agents_Bridging_Physical-Digital_Realms_for_Integrated_Agent_Intelligence.md`

# S4 P2 Paper 27 — Embodied Web Agents: Bridging Physical-Digital Realms for Integrated Agent Intelligence

## Metadata

- **Title:** Embodied Web Agents: Bridging Physical-Digital Realms for Integrated Agent Intelligence
- **Year:** 2025
- **Venue / status:** arXiv preprint / under review
- **Peer-reviewed status:** No
- **Publication type:** Preprint / benchmark paper
- **Thesis section:** S4 — emerging web-agent paradigms
- **Category:** embodied web agents / physical-digital integration
- **Priority:** P2
- **BibTeX key:** `embodiedwebagentsbridgingphysicaldi2025`

---

## Simple understanding

This paper introduces embodied web agents: agents that combine physical embodied interaction with web-scale reasoning and online information access.

In simple terms:

```text
Problem → how can an AI agent interact with a web, GUI, mobile, desktop, or application environment?
Method → add perception, planning, action, memory, API/tool use, state tracking, or browser control.
Goal → complete real user tasks more flexibly than scripts or static chatbots.
```

This note explains the paper first, then connects it to S4 and your thesis.

---

## Core idea

Create environments and a benchmark where agents must coordinate between 3D physical environments and web interfaces.

The paper is mainly about:

```text
embodied web agents / physical-digital integration
```

It contributes to the larger agent loop:

```text
observe → understand state → plan → act → receive feedback → verify / recover → complete task
```

---

## Key finding / main claim

Current agents struggle with cross-domain integration between physical perception/action and web reasoning.

For S4, the important question is not only whether the method works on its benchmark, but **which part of web/GUI agency it improves**:

- perception and grounding,
- planning and reasoning,
- action execution,
- API/tool use,
- memory/state tracking,
- recovery and verification,
- or deployment/evaluation.

---

## Key evidence to extract from the paper

When reading the paper, extract these points:

- **Figure 1 examples: traveling, cooking, and geolocation tasks crossing web and embodied environments.**
- **Unified simulation platform integrating AI2-THOR, Google Earth, and web interfaces.**
- **Benchmark with about 1.5k tasks across cooking, navigation, shopping, tourism, and geolocation.**

These are the most useful parts for writing a literature-review paragraph.

---

## Limitations

- **Limitation 1:** Preprint/under-review status.
- **Limitation 2:** The paradigm is broader than web automation and requires simulated physical environments.
- **Limitation 3:** Benchmark results may not directly transfer to browser-only data extraction.

General thesis-level limitation:

```text
Improving one agent component is not enough for generalized web automation.
A robust web agent still needs grounding, planning, execution, verification, recovery, and safety.
```

---

## Relation to S4

This paper belongs in S4 because S4 discusses **LLM-based agents for web/GUI/mobile/computer automation**.

Its role in S4 is:

```text
Embodied Web Agents: Bridging Physical-Digital Realms for Integrated Agent Intelligence
→ embodied web agents / physical-digital integration
→ supporting P2 source for web/GUI/computer-use agent discussion
```

Use it after explaining what the paper does. Do not introduce it only as “P2”; introduce the method or idea first.

---

## Relation to thesis topic

Your thesis topic is:

```text
LLM-based agents for generalized web automation and data extraction
```

This paper matters because:

It helps show that web agents may become part of broader physical-digital agent systems.

For generalized web automation, the connection is:

```text
web / GUI / mobile / computer-use interaction
→ agent observes a digital environment
→ agent chooses actions
→ agent extracts information or completes a workflow
```

Even when the paper is not directly about data extraction, it still helps explain the automation layer needed before extraction can be generalized.

---

## How to use this paper in the literature review

Recommended use:

- Use as **P2 support**, not as the central backbone.
- Use for one precise idea, architecture, benchmark, or limitation.
- If peer-reviewed, it can support stronger claims.
- If preprint/workshop/technical report, use it for recent trends and emerging directions.

Suggested sentence:

> Embodied Web Agents: Bridging Physical-Digital Realms for Integrated Agent Intelligence shows how embodied web agents / physical-digital integration contributes to the development of LLM-based agents for digital task automation, but its limitations indicate that generalized web automation still requires stronger grounding, verification, and recovery mechanisms.

---

## Reading decision

- **Keep in S4 P2:** Yes
- **Read fully?** No, selected sections are enough unless promoted later
- **Depth needed:** Low to medium
- **Main use:** Support S4 discussion of embodied web agents / physical-digital integration
- **Most important parts:**
  - Abstract
  - Introduction
  - Main architecture / method figure
  - Dataset or benchmark section
  - Results table
  - Limitations / discussion

---

## One-sentence summary

Embodied Web Agents: Bridging Physical-Digital Realms for Integrated Agent Intelligence is a P2 supporting paper for S4 because it explains **embodied web agents / physical-digital integration**, but it should be cited according to its venue/status and not overused beyond its evidence.

---

## BibTeX placeholder

```bibtex
@misc{embodiedwebagentsbridgingphysicaldi2025,
  title = {Embodied Web Agents: Bridging Physical-Digital Realms for Integrated Agent Intelligence},
  year = {2025},
  note = {arXiv preprint / under review; Preprint / benchmark paper. Verify final bibliographic metadata before thesis submission.}
}
```


---

<!-- ========== FILE: S4_P2\paper_first_notes\S4_P2_28_Agentic_Web_Weaving_the_Next_Web_with_AI_Agents.md ========== -->

## Source: `S4_P2\paper_first_notes\S4_P2_28_Agentic_Web_Weaving_the_Next_Web_with_AI_Agents.md`

# S4 P2 Paper 28 — Agentic Web: Weaving the Next Web with AI Agents

## Metadata

- **Title:** Agentic Web: Weaving the Next Web with AI Agents
- **Year:** 2025
- **Venue / status:** arXiv survey / vision paper
- **Peer-reviewed status:** No confirmed archival venue
- **Publication type:** Survey / vision preprint
- **Thesis section:** S4 — Agentic Web framing
- **Category:** agentic web / web architecture and governance
- **Priority:** P2
- **BibTeX key:** `agenticwebweavingthenextwebwithaiag2025`

---

## Simple understanding

This paper presents a broad vision of the Agentic Web, where AI agents act, communicate, coordinate, and execute tasks across web services on behalf of users.

In simple terms:

```text
Problem → how can an AI agent interact with a web, GUI, mobile, desktop, or application environment?
Method → add perception, planning, action, memory, API/tool use, state tracking, or browser control.
Goal → complete real user tasks more flexibly than scripts or static chatbots.
```

This note explains the paper first, then connects it to S4 and your thesis.

---

## Core idea

Frame the Agentic Web through intelligence, interaction, and economics, including protocols, orchestration, applications, risks, and governance.

The paper is mainly about:

```text
agentic web / web architecture and governance
```

It contributes to the larger agent loop:

```text
observe → understand state → plan → act → receive feedback → verify / recover → complete task
```

---

## Key finding / main claim

The web may shift from human-driven browsing to agent-mediated workflows involving discovery, planning, inter-agent collaboration, and execution.

For S4, the important question is not only whether the method works on its benchmark, but **which part of web/GUI agency it improves**:

- perception and grounding,
- planning and reasoning,
- action execution,
- API/tool use,
- memory/state tracking,
- recovery and verification,
- or deployment/evaluation.

---

## Key evidence to extract from the paper

When reading the paper, extract these points:

- **Definition of Agentic Web.**
- **Figure 1 process cycle: user request → plan → agent discovery → inter-agent discussion → action → report.**
- **Discussion of MCP, A2A, agent attention economy, risks, and governance.**

These are the most useful parts for writing a literature-review paragraph.

---

## Limitations

- **Limitation 1:** Vision/survey preprint, not a primary empirical paper.
- **Limitation 2:** Broad scope means less depth on individual web-agent algorithms.
- **Limitation 3:** Future-looking claims should be phrased cautiously.

General thesis-level limitation:

```text
Improving one agent component is not enough for generalized web automation.
A robust web agent still needs grounding, planning, execution, verification, recovery, and safety.
```

---

## Relation to S4

This paper belongs in S4 because S4 discusses **LLM-based agents for web/GUI/mobile/computer automation**.

Its role in S4 is:

```text
Agentic Web: Weaving the Next Web with AI Agents
→ agentic web / web architecture and governance
→ supporting P2 source for web/GUI/computer-use agent discussion
```

Use it after explaining what the paper does. Do not introduce it only as “P2”; introduce the method or idea first.

---

## Relation to thesis topic

Your thesis topic is:

```text
LLM-based agents for generalized web automation and data extraction
```

This paper matters because:

It provides useful high-level framing for the future of web automation and web-agent ecosystems.

For generalized web automation, the connection is:

```text
web / GUI / mobile / computer-use interaction
→ agent observes a digital environment
→ agent chooses actions
→ agent extracts information or completes a workflow
```

Even when the paper is not directly about data extraction, it still helps explain the automation layer needed before extraction can be generalized.

---

## How to use this paper in the literature review

Recommended use:

- Use as **P2 support**, not as the central backbone.
- Use for one precise idea, architecture, benchmark, or limitation.
- If peer-reviewed, it can support stronger claims.
- If preprint/workshop/technical report, use it for recent trends and emerging directions.

Suggested sentence:

> Agentic Web: Weaving the Next Web with AI Agents shows how agentic web / web architecture and governance contributes to the development of LLM-based agents for digital task automation, but its limitations indicate that generalized web automation still requires stronger grounding, verification, and recovery mechanisms.

---

## Reading decision

- **Keep in S4 P2:** Yes
- **Read fully?** No, selected sections are enough unless promoted later
- **Depth needed:** Low to medium
- **Main use:** Support S4 discussion of agentic web / web architecture and governance
- **Most important parts:**
  - Abstract
  - Introduction
  - Main architecture / method figure
  - Dataset or benchmark section
  - Results table
  - Limitations / discussion

---

## One-sentence summary

Agentic Web: Weaving the Next Web with AI Agents is a P2 supporting paper for S4 because it explains **agentic web / web architecture and governance**, but it should be cited according to its venue/status and not overused beyond its evidence.

---

## BibTeX placeholder

```bibtex
@misc{agenticwebweavingthenextwebwithaiag2025,
  title = {Agentic Web: Weaving the Next Web with AI Agents},
  year = {2025},
  note = {arXiv survey / vision paper; Survey / vision preprint. Verify final bibliographic metadata before thesis submission.}
}
```


---

<!-- ========== FILE: S4_P2\paper_first_notes\S4_P2_29_CoAct-1_Computer-using_Agents_with_Coding_as_Actions.md ========== -->

## Source: `S4_P2\paper_first_notes\S4_P2_29_CoAct-1_Computer-using_Agents_with_Coding_as_Actions.md`

# S4 P2 Paper 29 — CoAct-1: Computer-using Agents with Coding as Actions

## Metadata

- **Title:** CoAct-1: Computer-using Agents with Coding as Actions
- **Year:** 2025
- **Venue / status:** arXiv preprint
- **Peer-reviewed status:** No confirmed archival venue
- **Publication type:** Preprint
- **Thesis section:** S4 — hybrid computer-use agents
- **Category:** computer-use agents / coding as actions
- **Priority:** P2
- **BibTeX key:** `coact1computerusingagentswithcoding2025`

---

## Simple understanding

CoAct-1 argues that computer-use agents should not rely only on GUI actions. It adds coding as an action, allowing agents to use Python or Bash when more reliable.

In simple terms:

```text
Problem → how can an AI agent interact with a web, GUI, mobile, desktop, or application environment?
Method → add perception, planning, action, memory, API/tool use, state tracking, or browser control.
Goal → complete real user tasks more flexibly than scripts or static chatbots.
```

This note explains the paper first, then connects it to S4 and your thesis.

---

## Core idea

Use a multi-agent system with an Orchestrator, Programmer, and GUI Operator to dynamically choose between GUI control and programmatic execution.

The paper is mainly about:

```text
computer-use agents / coding as actions
```

It contributes to the larger agent loop:

```text
observe → understand state → plan → act → receive feedback → verify / recover → complete task
```

---

## Key finding / main claim

CoAct-1 reports stronger OSWorld performance and fewer steps by replacing fragile GUI sequences with code when appropriate.

For S4, the important question is not only whether the method works on its benchmark, but **which part of web/GUI agency it improves**:

- perception and grounding,
- planning and reasoning,
- action execution,
- API/tool use,
- memory/state tracking,
- recovery and verification,
- or deployment/evaluation.

---

## Key evidence to extract from the paper

When reading the paper, extract these points:

- **Architecture with Orchestrator, Programmer, and GUI Operator.**
- **Reported OSWorld success rate of 60.76%.**
- **Average step reduction to 10.15 compared with about 15 for leading GUI agents.**

These are the most useful parts for writing a literature-review paragraph.

---

## Limitations

- **Limitation 1:** Preprint status.
- **Limitation 2:** Coding actions require sandboxing and security controls.
- **Limitation 3:** Some GUI tasks cannot be replaced by code, especially when APIs/files are inaccessible.

General thesis-level limitation:

```text
Improving one agent component is not enough for generalized web automation.
A robust web agent still needs grounding, planning, execution, verification, recovery, and safety.
```

---

## Relation to S4

This paper belongs in S4 because S4 discusses **LLM-based agents for web/GUI/mobile/computer automation**.

Its role in S4 is:

```text
CoAct-1: Computer-using Agents with Coding as Actions
→ computer-use agents / coding as actions
→ supporting P2 source for web/GUI/computer-use agent discussion
```

Use it after explaining what the paper does. Do not introduce it only as “P2”; introduce the method or idea first.

---

## Relation to thesis topic

Your thesis topic is:

```text
LLM-based agents for generalized web automation and data extraction
```

This paper matters because:

It supports the hybrid-action argument: generalized automation should combine GUI actions with code/tool execution.

For generalized web automation, the connection is:

```text
web / GUI / mobile / computer-use interaction
→ agent observes a digital environment
→ agent chooses actions
→ agent extracts information or completes a workflow
```

Even when the paper is not directly about data extraction, it still helps explain the automation layer needed before extraction can be generalized.

---

## How to use this paper in the literature review

Recommended use:

- Use as **P2 support**, not as the central backbone.
- Use for one precise idea, architecture, benchmark, or limitation.
- If peer-reviewed, it can support stronger claims.
- If preprint/workshop/technical report, use it for recent trends and emerging directions.

Suggested sentence:

> CoAct-1: Computer-using Agents with Coding as Actions shows how computer-use agents / coding as actions contributes to the development of LLM-based agents for digital task automation, but its limitations indicate that generalized web automation still requires stronger grounding, verification, and recovery mechanisms.

---

## Reading decision

- **Keep in S4 P2:** Yes
- **Read fully?** No, selected sections are enough unless promoted later
- **Depth needed:** Low to medium
- **Main use:** Support S4 discussion of computer-use agents / coding as actions
- **Most important parts:**
  - Abstract
  - Introduction
  - Main architecture / method figure
  - Dataset or benchmark section
  - Results table
  - Limitations / discussion

---

## One-sentence summary

CoAct-1: Computer-using Agents with Coding as Actions is a P2 supporting paper for S4 because it explains **computer-use agents / coding as actions**, but it should be cited according to its venue/status and not overused beyond its evidence.

---

## BibTeX placeholder

```bibtex
@misc{coact1computerusingagentswithcoding2025,
  title = {CoAct-1: Computer-using Agents with Coding as Actions},
  year = {2025},
  note = {arXiv preprint; Preprint. Verify final bibliographic metadata before thesis submission.}
}
```


---

<!-- ========== FILE: S4_P2\paper_first_notes\S4_P2_30_OpenCUA_Open_Foundations_for_Computer-Use_Agents.md ========== -->

## Source: `S4_P2\paper_first_notes\S4_P2_30_OpenCUA_Open_Foundations_for_Computer-Use_Agents.md`

# S4 P2 Paper 30 — OpenCUA: Open Foundations for Computer-Use Agents

## Metadata

- **Title:** OpenCUA: Open Foundations for Computer-Use Agents
- **Year:** 2025
- **Venue / status:** NeurIPS 2025
- **Peer-reviewed status:** Yes
- **Publication type:** Peer-reviewed conference paper
- **Thesis section:** S4 — computer-use agent foundations
- **Category:** open computer-use agent foundation / dataset and model
- **Priority:** P2
- **BibTeX key:** `opencuaopenfoundationsforcomputerus2025`

---

## Simple understanding

OpenCUA provides an open-source framework, dataset, benchmark, and models for computer-use agents. It addresses the lack of open foundations for CUA research.

In simple terms:

```text
Problem → how can an AI agent interact with a web, GUI, mobile, desktop, or application environment?
Method → add perception, planning, action, memory, API/tool use, state tracking, or browser control.
Goal → complete real user tasks more flexibly than scripts or static chatbots.
```

This note explains the paper first, then connects it to S4 and your thesis.

---

## Core idea

Collect large-scale human computer-use demonstrations, convert them into state-action trajectories with reflective CoT, and train open CUA models.

The paper is mainly about:

```text
open computer-use agent foundation / dataset and model
```

It contributes to the larger agent loop:

```text
observe → understand state → plan → act → receive feedback → verify / recover → complete task
```

---

## Key finding / main claim

OpenCUA reports state-of-the-art open-source performance on OSWorld-Verified and strong cross-domain generalization.

For S4, the important question is not only whether the method works on its benchmark, but **which part of web/GUI agency it improves**:

- perception and grounding,
- planning and reasoning,
- action execution,
- API/tool use,
- memory/state tracking,
- recovery and verification,
- or deployment/evaluation.

---

## Key evidence to extract from the paper

When reading the paper, extract these points:

- **Figure 2 overview of OpenCUA framework and AgentNet pipeline.**
- **AGENTNET dataset: 22.6K trajectories across 100+ applications and 200 websites across Windows, macOS, and Ubuntu.**
- **OpenCUA-72B reported 45.0% success on OSWorld-Verified.**

These are the most useful parts for writing a literature-review paragraph.

---

## Limitations

- **Limitation 1:** Computer-use agents are broader than web agents and include desktop applications.
- **Limitation 2:** Performance still remains far below perfect reliability.
- **Limitation 3:** Large-scale data collection and privacy controls are complex.

General thesis-level limitation:

```text
Improving one agent component is not enough for generalized web automation.
A robust web agent still needs grounding, planning, execution, verification, recovery, and safety.
```

---

## Relation to S4

This paper belongs in S4 because S4 discusses **LLM-based agents for web/GUI/mobile/computer automation**.

Its role in S4 is:

```text
OpenCUA: Open Foundations for Computer-Use Agents
→ open computer-use agent foundation / dataset and model
→ supporting P2 source for web/GUI/computer-use agent discussion
```

Use it after explaining what the paper does. Do not introduce it only as “P2”; introduce the method or idea first.

---

## Relation to thesis topic

Your thesis topic is:

```text
LLM-based agents for generalized web automation and data extraction
```

This paper matters because:

It is one of the strongest recent sources for open computer-use agent data, models, and evaluation.

For generalized web automation, the connection is:

```text
web / GUI / mobile / computer-use interaction
→ agent observes a digital environment
→ agent chooses actions
→ agent extracts information or completes a workflow
```

Even when the paper is not directly about data extraction, it still helps explain the automation layer needed before extraction can be generalized.

---

## How to use this paper in the literature review

Recommended use:

- Use as **P2 support**, not as the central backbone.
- Use for one precise idea, architecture, benchmark, or limitation.
- If peer-reviewed, it can support stronger claims.
- If preprint/workshop/technical report, use it for recent trends and emerging directions.

Suggested sentence:

> OpenCUA: Open Foundations for Computer-Use Agents shows how open computer-use agent foundation / dataset and model contributes to the development of LLM-based agents for digital task automation, but its limitations indicate that generalized web automation still requires stronger grounding, verification, and recovery mechanisms.

---

## Reading decision

- **Keep in S4 P2:** Yes
- **Read fully?** Yes or selected sections carefully
- **Depth needed:** Medium to high
- **Main use:** Support S4 discussion of open computer-use agent foundation / dataset and model
- **Most important parts:**
  - Abstract
  - Introduction
  - Main architecture / method figure
  - Dataset or benchmark section
  - Results table
  - Limitations / discussion

---

## One-sentence summary

OpenCUA: Open Foundations for Computer-Use Agents is a P2 supporting paper for S4 because it explains **open computer-use agent foundation / dataset and model**, but it should be cited according to its venue/status and not overused beyond its evidence.

---

## BibTeX placeholder

```bibtex
@misc{opencuaopenfoundationsforcomputerus2025,
  title = {OpenCUA: Open Foundations for Computer-Use Agents},
  year = {2025},
  note = {NeurIPS 2025; Peer-reviewed conference paper. Verify final bibliographic metadata before thesis submission.}
}
```


---

<!-- ========== FILE: S4_P2\paper_first_notes\S4_P2_31_Are_LLM_Agents_the_New_RPA_A_Comparative_Study_with_RPA_Across_Enterprise_Workflows.md ========== -->

## Source: `S4_P2\paper_first_notes\S4_P2_31_Are_LLM_Agents_the_New_RPA_A_Comparative_Study_with_RPA_Across_Enterprise_Workflows.md`

# S4 P2 Paper 31 — Are LLM Agents the New RPA? A Comparative Study with RPA Across Enterprise Workflows

## Metadata

- **Title:** Are LLM Agents the New RPA? A Comparative Study with RPA Across Enterprise Workflows
- **Year:** 2025
- **Venue / status:** Uploaded copy does not show confirmed venue
- **Peer-reviewed status:** Unclear / likely preprint or proceedings draft
- **Publication type:** Comparative study / unclear venue
- **Thesis section:** S4 — enterprise automation and RPA comparison
- **Category:** LLM agents vs RPA / enterprise automation
- **Priority:** P2
- **BibTeX key:** `arellmagentsthenewrpaacomparativest2025`

---

## Simple understanding

This paper compares LLM agents with traditional RPA across enterprise workflows such as data entry, monitoring, and document extraction.

In simple terms:

```text
Problem → how can an AI agent interact with a web, GUI, mobile, desktop, or application environment?
Method → add perception, planning, action, memory, API/tool use, state tracking, or browser control.
Goal → complete real user tasks more flexibly than scripts or static chatbots.
```

This note explains the paper first, then connects it to S4 and your thesis.

---

## Core idea

Empirically compare RPA tools and agentic automation with computer use in terms of speed, reliability, and development effort.

The paper is mainly about:

```text
LLM agents vs RPA / enterprise automation
```

It contributes to the larger agent loop:

```text
observe → understand state → plan → act → receive feedback → verify / recover → complete task
```

---

## Key finding / main claim

RPA remains faster and more reliable in stable repetitive environments, while LLM agents reduce development time and adapt more flexibly to dynamic interfaces.

For S4, the important question is not only whether the method works on its benchmark, but **which part of web/GUI agency it improves**:

- perception and grounding,
- planning and reasoning,
- action execution,
- API/tool use,
- memory/state tracking,
- recovery and verification,
- or deployment/evaluation.

---

## Key evidence to extract from the paper

When reading the paper, extract these points:

- **Three hypotheses comparing speed, reliability, and development time.**
- **Tasks from rpachallenge.com.**
- **Conclusion that AACU is promising but not yet production-ready compared with RPA.**

These are the most useful parts for writing a literature-review paragraph.

---

## Limitations

- **Limitation 1:** Final venue/status is unclear from the uploaded copy.
- **Limitation 2:** Evaluation covers only a small number of RPA-style workflows.
- **Limitation 3:** Current AACU tools may change rapidly, so results can become outdated.

General thesis-level limitation:

```text
Improving one agent component is not enough for generalized web automation.
A robust web agent still needs grounding, planning, execution, verification, recovery, and safety.
```

---

## Relation to S4

This paper belongs in S4 because S4 discusses **LLM-based agents for web/GUI/mobile/computer automation**.

Its role in S4 is:

```text
Are LLM Agents the New RPA? A Comparative Study with RPA Across Enterprise Workflows
→ LLM agents vs RPA / enterprise automation
→ supporting P2 source for web/GUI/computer-use agent discussion
```

Use it after explaining what the paper does. Do not introduce it only as “P2”; introduce the method or idea first.

---

## Relation to thesis topic

Your thesis topic is:

```text
LLM-based agents for generalized web automation and data extraction
```

This paper matters because:

It is useful for your thesis because it directly compares LLM agent automation with classical RPA.

For generalized web automation, the connection is:

```text
web / GUI / mobile / computer-use interaction
→ agent observes a digital environment
→ agent chooses actions
→ agent extracts information or completes a workflow
```

Even when the paper is not directly about data extraction, it still helps explain the automation layer needed before extraction can be generalized.

---

## How to use this paper in the literature review

Recommended use:

- Use as **P2 support**, not as the central backbone.
- Use for one precise idea, architecture, benchmark, or limitation.
- If peer-reviewed, it can support stronger claims.
- If preprint/workshop/technical report, use it for recent trends and emerging directions.

Suggested sentence:

> Are LLM Agents the New RPA? A Comparative Study with RPA Across Enterprise Workflows shows how LLM agents vs RPA / enterprise automation contributes to the development of LLM-based agents for digital task automation, but its limitations indicate that generalized web automation still requires stronger grounding, verification, and recovery mechanisms.

---

## Reading decision

- **Keep in S4 P2:** Yes
- **Read fully?** No, selected sections are enough unless promoted later
- **Depth needed:** Low to medium
- **Main use:** Support S4 discussion of LLM agents vs RPA / enterprise automation
- **Most important parts:**
  - Abstract
  - Introduction
  - Main architecture / method figure
  - Dataset or benchmark section
  - Results table
  - Limitations / discussion

---

## One-sentence summary

Are LLM Agents the New RPA? A Comparative Study with RPA Across Enterprise Workflows is a P2 supporting paper for S4 because it explains **LLM agents vs RPA / enterprise automation**, but it should be cited according to its venue/status and not overused beyond its evidence.

---

## BibTeX placeholder

```bibtex
@misc{arellmagentsthenewrpaacomparativest2025,
  title = {Are LLM Agents the New RPA? A Comparative Study with RPA Across Enterprise Workflows},
  year = {2025},
  note = {Uploaded copy does not show confirmed venue; Comparative study / unclear venue. Verify final bibliographic metadata before thesis submission.}
}
```


---

<!-- ========== FILE: S4_P2\paper_first_notes\S4_P2_32_BrowserAgent_Building_Web_Agents_with_Human-Inspired_Web_Browsing_Actions.md ========== -->

## Source: `S4_P2\paper_first_notes\S4_P2_32_BrowserAgent_Building_Web_Agents_with_Human-Inspired_Web_Browsing_Actions.md`

# S4 P2 Paper 32 — BrowserAgent: Building Web Agents with Human-Inspired Web Browsing Actions

## Metadata

- **Title:** BrowserAgent: Building Web Agents with Human-Inspired Web Browsing Actions
- **Year:** 2025
- **Venue / status:** arXiv preprint / work in progress
- **Peer-reviewed status:** No
- **Publication type:** Work-in-progress preprint
- **Thesis section:** S4 — browser-native web agents
- **Category:** browser-native web agents
- **Priority:** P2
- **BibTeX key:** `browseragentbuildingwebagentswithhu2025`

---

## Simple understanding

BrowserAgent trains web agents to use human-inspired browser actions such as scrolling, clicking, typing, and tab management rather than relying on static text extraction.

In simple terms:

```text
Problem → how can an AI agent interact with a web, GUI, mobile, desktop, or application environment?
Method → add perception, planning, action, memory, API/tool use, state tracking, or browser control.
Goal → complete real user tasks more flexibly than scripts or static chatbots.
```

This note explains the paper first, then connects it to S4 and your thesis.

---

## Core idea

Build a browser-native agent framework that interacts with raw web pages through Playwright and trains with SFT followed by rejection fine-tuning.

The paper is mainly about:

```text
browser-native web agents
```

It contributes to the larger agent loop:

```text
observe → understand state → plan → act → receive feedback → verify / recover → complete task
```

---

## Key finding / main claim

BrowserAgent reports strong results on open QA and multi-hop QA tasks while using less training data than some search-agent baselines.

For S4, the important question is not only whether the method works on its benchmark, but **which part of web/GUI agency it improves**:

- perception and grounding,
- planning and reasoning,
- action execution,
- API/tool use,
- memory/state tracking,
- recovery and verification,
- or deployment/evaluation.

---

## Key evidence to extract from the paper

When reading the paper, extract these points:

- **Figure 2 comparing BrowserAgent with traditional deep research pipeline.**
- **Action set: click, type, scroll, hover, goto, and tab/browser operations.**
- **Reported around 20% improvement over Search-R1 on multi-hop QA tasks.**

These are the most useful parts for writing a literature-review paragraph.

---

## Limitations

- **Limitation 1:** Marked Work in Progress, so cite carefully.
- **Limitation 2:** QA-focused browser interaction differs from transactional web automation.
- **Limitation 3:** Results depend on browser orchestration infrastructure and training data quality.

General thesis-level limitation:

```text
Improving one agent component is not enough for generalized web automation.
A robust web agent still needs grounding, planning, execution, verification, recovery, and safety.
```

---

## Relation to S4

This paper belongs in S4 because S4 discusses **LLM-based agents for web/GUI/mobile/computer automation**.

Its role in S4 is:

```text
BrowserAgent: Building Web Agents with Human-Inspired Web Browsing Actions
→ browser-native web agents
→ supporting P2 source for web/GUI/computer-use agent discussion
```

Use it after explaining what the paper does. Do not introduce it only as “P2”; introduce the method or idea first.

---

## Relation to thesis topic

Your thesis topic is:

```text
LLM-based agents for generalized web automation and data extraction
```

This paper matters because:

It supports a recent trend: training agents to interact with the live browser instead of only processed HTML or search summaries.

For generalized web automation, the connection is:

```text
web / GUI / mobile / computer-use interaction
→ agent observes a digital environment
→ agent chooses actions
→ agent extracts information or completes a workflow
```

Even when the paper is not directly about data extraction, it still helps explain the automation layer needed before extraction can be generalized.

---

## How to use this paper in the literature review

Recommended use:

- Use as **P2 support**, not as the central backbone.
- Use for one precise idea, architecture, benchmark, or limitation.
- If peer-reviewed, it can support stronger claims.
- If preprint/workshop/technical report, use it for recent trends and emerging directions.

Suggested sentence:

> BrowserAgent: Building Web Agents with Human-Inspired Web Browsing Actions shows how browser-native web agents contributes to the development of LLM-based agents for digital task automation, but its limitations indicate that generalized web automation still requires stronger grounding, verification, and recovery mechanisms.

---

## Reading decision

- **Keep in S4 P2:** Yes
- **Read fully?** No, selected sections are enough unless promoted later
- **Depth needed:** Low to medium
- **Main use:** Support S4 discussion of browser-native web agents
- **Most important parts:**
  - Abstract
  - Introduction
  - Main architecture / method figure
  - Dataset or benchmark section
  - Results table
  - Limitations / discussion

---

## One-sentence summary

BrowserAgent: Building Web Agents with Human-Inspired Web Browsing Actions is a P2 supporting paper for S4 because it explains **browser-native web agents**, but it should be cited according to its venue/status and not overused beyond its evidence.

---

## BibTeX placeholder

```bibtex
@misc{browseragentbuildingwebagentswithhu2025,
  title = {BrowserAgent: Building Web Agents with Human-Inspired Web Browsing Actions},
  year = {2025},
  note = {arXiv preprint / work in progress; Work-in-progress preprint. Verify final bibliographic metadata before thesis submission.}
}
```


---

<!-- ========== FILE: S4_P2\paper_first_notes\S4_P2_33_UltraCUA_A_Foundation_Model_for_Computer_Use_Agents_with_Hybrid_Action.md ========== -->

## Source: `S4_P2\paper_first_notes\S4_P2_33_UltraCUA_A_Foundation_Model_for_Computer_Use_Agents_with_Hybrid_Action.md`

# S4 P2 Paper 33 — UltraCUA: A Foundation Model for Computer Use Agents with Hybrid Action

## Metadata

- **Title:** UltraCUA: A Foundation Model for Computer Use Agents with Hybrid Action
- **Year:** 2025
- **Venue / status:** arXiv preprint
- **Peer-reviewed status:** No confirmed archival venue
- **Publication type:** Preprint
- **Thesis section:** S4 — hybrid computer-use agents
- **Category:** hybrid-action computer-use foundation model
- **Priority:** P2
- **BibTeX key:** `ultracuaafoundationmodelforcomputer2025`

---

## Simple understanding

UltraCUA proposes a foundation model for computer-use agents that can use both low-level GUI actions and high-level programmatic tool calls.

In simple terms:

```text
Problem → how can an AI agent interact with a web, GUI, mobile, desktop, or application environment?
Method → add perception, planning, action, memory, API/tool use, state tracking, or browser control.
Goal → complete real user tasks more flexibly than scripts or static chatbots.
```

This note explains the paper first, then connects it to S4 and your thesis.

---

## Core idea

Train CUA models with hybrid action trajectories so they learn when to click/type/scroll and when to call tools.

The paper is mainly about:

```text
hybrid-action computer-use foundation model
```

It contributes to the larger agent loop:

```text
observe → understand state → plan → act → receive feedback → verify / recover → complete task
```

---

## Key finding / main claim

UltraCUA reports improved OSWorld and WindowsAgentArena performance, arguing that hybrid action reduces cascading GUI errors.

For S4, the important question is not only whether the method works on its benchmark, but **which part of web/GUI agency it improves**:

- perception and grounding,
- planning and reasoning,
- action execution,
- API/tool use,
- memory/state tracking,
- recovery and verification,
- or deployment/evaluation.

---

## Key evidence to extract from the paper

When reading the paper, extract these points:

- **Figure 1 comparing GUI-only cascade errors with hybrid tool calls.**
- **Figure 2 showing tool collection, task synthesis, trajectory collection, and SFT/RL training.**
- **Reported OSWorld and WindowsAgentArena gains.**

These are the most useful parts for writing a literature-review paragraph.

---

## Limitations

- **Limitation 1:** Preprint status.
- **Limitation 2:** Tool extraction and hybrid trajectory generation may be difficult to reproduce.
- **Limitation 3:** Hybrid action requires safe tool execution and reliable tool availability.

General thesis-level limitation:

```text
Improving one agent component is not enough for generalized web automation.
A robust web agent still needs grounding, planning, execution, verification, recovery, and safety.
```

---

## Relation to S4

This paper belongs in S4 because S4 discusses **LLM-based agents for web/GUI/mobile/computer automation**.

Its role in S4 is:

```text
UltraCUA: A Foundation Model for Computer Use Agents with Hybrid Action
→ hybrid-action computer-use foundation model
→ supporting P2 source for web/GUI/computer-use agent discussion
```

Use it after explaining what the paper does. Do not introduce it only as “P2”; introduce the method or idea first.

---

## Relation to thesis topic

Your thesis topic is:

```text
LLM-based agents for generalized web automation and data extraction
```

This paper matters because:

It reinforces the argument that future agents should combine GUI universality with API/tool precision.

For generalized web automation, the connection is:

```text
web / GUI / mobile / computer-use interaction
→ agent observes a digital environment
→ agent chooses actions
→ agent extracts information or completes a workflow
```

Even when the paper is not directly about data extraction, it still helps explain the automation layer needed before extraction can be generalized.

---

## How to use this paper in the literature review

Recommended use:

- Use as **P2 support**, not as the central backbone.
- Use for one precise idea, architecture, benchmark, or limitation.
- If peer-reviewed, it can support stronger claims.
- If preprint/workshop/technical report, use it for recent trends and emerging directions.

Suggested sentence:

> UltraCUA: A Foundation Model for Computer Use Agents with Hybrid Action shows how hybrid-action computer-use foundation model contributes to the development of LLM-based agents for digital task automation, but its limitations indicate that generalized web automation still requires stronger grounding, verification, and recovery mechanisms.

---

## Reading decision

- **Keep in S4 P2:** Yes
- **Read fully?** No, selected sections are enough unless promoted later
- **Depth needed:** Low to medium
- **Main use:** Support S4 discussion of hybrid-action computer-use foundation model
- **Most important parts:**
  - Abstract
  - Introduction
  - Main architecture / method figure
  - Dataset or benchmark section
  - Results table
  - Limitations / discussion

---

## One-sentence summary

UltraCUA: A Foundation Model for Computer Use Agents with Hybrid Action is a P2 supporting paper for S4 because it explains **hybrid-action computer-use foundation model**, but it should be cited according to its venue/status and not overused beyond its evidence.

---

## BibTeX placeholder

```bibtex
@misc{ultracuaafoundationmodelforcomputer2025,
  title = {UltraCUA: A Foundation Model for Computer Use Agents with Hybrid Action},
  year = {2025},
  note = {arXiv preprint; Preprint. Verify final bibliographic metadata before thesis submission.}
}
```


---

<!-- ========== FILE: S4_P2\paper_first_notes\S4_P2_34_Agent-SAMA_State-Aware_Mobile_Assistant.md ========== -->

## Source: `S4_P2\paper_first_notes\S4_P2_34_Agent-SAMA_State-Aware_Mobile_Assistant.md`

# S4 P2 Paper 34 — Agent-SAMA: State-Aware Mobile Assistant

## Metadata

- **Title:** Agent-SAMA: State-Aware Mobile Assistant
- **Year:** 2025
- **Venue / status:** arXiv preprint
- **Peer-reviewed status:** No confirmed archival venue
- **Publication type:** Preprint
- **Thesis section:** S4 — state-aware GUI/mobile agents
- **Category:** state-aware mobile agents / FSM memory
- **Priority:** P2
- **BibTeX key:** `agentsamastateawaremobileassistant2025`

---

## Simple understanding

Agent-SAMA is a state-aware mobile assistant that models mobile app execution as a finite state machine. It uses app states and transitions for planning, verification, and recovery.

In simple terms:

```text
Problem → how can an AI agent interact with a web, GUI, mobile, desktop, or application environment?
Method → add perception, planning, action, memory, API/tool use, state tracking, or browser control.
Goal → complete real user tasks more flexibly than scripts or static chatbots.
```

This note explains the paper first, then connects it to S4 and your thesis.

---

## Core idea

Use four agents to build and exploit FSMs in real time: planning, screen parsing/state modeling, acting, reflection/recovery, and memory retention.

The paper is mainly about:

```text
state-aware mobile agents / FSM memory
```

It contributes to the larger agent loop:

```text
observe → understand state → plan → act → receive feedback → verify / recover → complete task
```

---

## Key finding / main claim

Agent-SAMA reports higher success and recovery rates on Mobile-Eval-E, SPA-Bench, and AndroidWorld by using structured state modeling.

For S4, the important question is not only whether the method works on its benchmark, but **which part of web/GUI agency it improves**:

- perception and grounding,
- planning and reasoning,
- action execution,
- API/tool use,
- memory/state tracking,
- recovery and verification,
- or deployment/evaluation.

---

## Key evidence to extract from the paper

When reading the paper, extract these points:

- **FSM formulation: UI screens as states and actions as transitions.**
- **Reported 84.0% success and 71.9% recovery on Mobile-Eval-E.**
- **Four phases: planning, execution, error recovery/verification, and knowledge retention.**

These are the most useful parts for writing a literature-review paragraph.

---

## Limitations

- **Limitation 1:** Preprint status.
- **Limitation 2:** FSM construction may be imperfect when screens are visually similar or highly dynamic.
- **Limitation 3:** Mobile app state modeling may not directly transfer to web pages with complex DOM states.

General thesis-level limitation:

```text
Improving one agent component is not enough for generalized web automation.
A robust web agent still needs grounding, planning, execution, verification, recovery, and safety.
```

---

## Relation to S4

This paper belongs in S4 because S4 discusses **LLM-based agents for web/GUI/mobile/computer automation**.

Its role in S4 is:

```text
Agent-SAMA: State-Aware Mobile Assistant
→ state-aware mobile agents / FSM memory
→ supporting P2 source for web/GUI/computer-use agent discussion
```

Use it after explaining what the paper does. Do not introduce it only as “P2”; introduce the method or idea first.

---

## Relation to thesis topic

Your thesis topic is:

```text
LLM-based agents for generalized web automation and data extraction
```

This paper matters because:

It is useful for discussing memory/state tracking as a solution to reactive GUI-agent limitations.

For generalized web automation, the connection is:

```text
web / GUI / mobile / computer-use interaction
→ agent observes a digital environment
→ agent chooses actions
→ agent extracts information or completes a workflow
```

Even when the paper is not directly about data extraction, it still helps explain the automation layer needed before extraction can be generalized.

---

## How to use this paper in the literature review

Recommended use:

- Use as **P2 support**, not as the central backbone.
- Use for one precise idea, architecture, benchmark, or limitation.
- If peer-reviewed, it can support stronger claims.
- If preprint/workshop/technical report, use it for recent trends and emerging directions.

Suggested sentence:

> Agent-SAMA: State-Aware Mobile Assistant shows how state-aware mobile agents / FSM memory contributes to the development of LLM-based agents for digital task automation, but its limitations indicate that generalized web automation still requires stronger grounding, verification, and recovery mechanisms.

---

## Reading decision

- **Keep in S4 P2:** Yes
- **Read fully?** No, selected sections are enough unless promoted later
- **Depth needed:** Low to medium
- **Main use:** Support S4 discussion of state-aware mobile agents / FSM memory
- **Most important parts:**
  - Abstract
  - Introduction
  - Main architecture / method figure
  - Dataset or benchmark section
  - Results table
  - Limitations / discussion

---

## One-sentence summary

Agent-SAMA: State-Aware Mobile Assistant is a P2 supporting paper for S4 because it explains **state-aware mobile agents / FSM memory**, but it should be cited according to its venue/status and not overused beyond its evidence.

---

## BibTeX placeholder

```bibtex
@misc{agentsamastateawaremobileassistant2025,
  title = {Agent-SAMA: State-Aware Mobile Assistant},
  year = {2025},
  note = {arXiv preprint; Preprint. Verify final bibliographic metadata before thesis submission.}
}
```


---

<!-- ========== FILE: S4_P2\paper_first_notes\S4_P2_35_Building_the_Web_for_Agents_A_Declarative_Framework_for_AgentWeb_Interaction.md ========== -->

## Source: `S4_P2\paper_first_notes\S4_P2_35_Building_the_Web_for_Agents_A_Declarative_Framework_for_AgentWeb_Interaction.md`

# S4 P2 Paper 35 — Building the Web for Agents: A Declarative Framework for Agent–Web Interaction

## Metadata

- **Title:** Building the Web for Agents: A Declarative Framework for Agent–Web Interaction
- **Year:** 2025
- **Venue / status:** arXiv preprint
- **Peer-reviewed status:** No confirmed archival venue
- **Publication type:** Preprint
- **Thesis section:** S4 — agentic web interface design
- **Category:** declarative agent-web interface / VOIX
- **Priority:** P2
- **BibTeX key:** `buildingthewebforagentsadeclarative2025`

---

## Simple understanding

This paper proposes VOIX, a declarative framework that lets websites expose machine-readable tools and context to AI agents using HTML tags.

In simple terms:

```text
Problem → how can an AI agent interact with a web, GUI, mobile, desktop, or application environment?
Method → add perception, planning, action, memory, API/tool use, state tracking, or browser control.
Goal → complete real user tasks more flexibly than scripts or static chatbots.
```

This note explains the paper first, then connects it to S4 and your thesis.

---

## Core idea

Introduce <tool> and <context> tags so developers can explicitly define available actions and relevant state for agents.

The paper is mainly about:

```text
declarative agent-web interface / VOIX
```

It contributes to the larger agent loop:

```text
observe → understand state → plan → act → receive feedback → verify / recover → complete task
```

---

## Key finding / main claim

The paper argues that declarative agent-web contracts can improve reliability, auditability, privacy, and developer control compared with scraping DOM/screenshots.

For S4, the important question is not only whether the method works on its benchmark, but **which part of web/GUI agency it improves**:

- perception and grounding,
- planning and reasoning,
- action execution,
- API/tool use,
- memory/state tracking,
- recovery and verification,
- or deployment/evaluation.

---

## Key evidence to extract from the paper

When reading the paper, extract these points:

- **VOIX mechanism with <tool> and <context> tags.**
- **Three-day hackathon study with 16 developers.**
- **Argument that machine-native affordances reduce brittle inference from human UI.**

These are the most useful parts for writing a literature-review paragraph.

---

## Limitations

- **Limitation 1:** Preprint status.
- **Limitation 2:** Hackathon evaluation with 16 developers is useful but limited.
- **Limitation 3:** Standard adoption would require ecosystem-level agreement.

General thesis-level limitation:

```text
Improving one agent component is not enough for generalized web automation.
A robust web agent still needs grounding, planning, execution, verification, recovery, and safety.
```

---

## Relation to S4

This paper belongs in S4 because S4 discusses **LLM-based agents for web/GUI/mobile/computer automation**.

Its role in S4 is:

```text
Building the Web for Agents: A Declarative Framework for Agent–Web Interaction
→ declarative agent-web interface / VOIX
→ supporting P2 source for web/GUI/computer-use agent discussion
```

Use it after explaining what the paper does. Do not introduce it only as “P2”; introduce the method or idea first.

---

## Relation to thesis topic

Your thesis topic is:

```text
LLM-based agents for generalized web automation and data extraction
```

This paper matters because:

It operationalizes the Agentic Web idea with a concrete declarative framework, directly relevant to generalized web automation.

For generalized web automation, the connection is:

```text
web / GUI / mobile / computer-use interaction
→ agent observes a digital environment
→ agent chooses actions
→ agent extracts information or completes a workflow
```

Even when the paper is not directly about data extraction, it still helps explain the automation layer needed before extraction can be generalized.

---

## How to use this paper in the literature review

Recommended use:

- Use as **P2 support**, not as the central backbone.
- Use for one precise idea, architecture, benchmark, or limitation.
- If peer-reviewed, it can support stronger claims.
- If preprint/workshop/technical report, use it for recent trends and emerging directions.

Suggested sentence:

> Building the Web for Agents: A Declarative Framework for Agent–Web Interaction shows how declarative agent-web interface / VOIX contributes to the development of LLM-based agents for digital task automation, but its limitations indicate that generalized web automation still requires stronger grounding, verification, and recovery mechanisms.

---

## Reading decision

- **Keep in S4 P2:** Yes
- **Read fully?** No, selected sections are enough unless promoted later
- **Depth needed:** Low to medium
- **Main use:** Support S4 discussion of declarative agent-web interface / VOIX
- **Most important parts:**
  - Abstract
  - Introduction
  - Main architecture / method figure
  - Dataset or benchmark section
  - Results table
  - Limitations / discussion

---

## One-sentence summary

Building the Web for Agents: A Declarative Framework for Agent–Web Interaction is a P2 supporting paper for S4 because it explains **declarative agent-web interface / VOIX**, but it should be cited according to its venue/status and not overused beyond its evidence.

---

## BibTeX placeholder

```bibtex
@misc{buildingthewebforagentsadeclarative2025,
  title = {Building the Web for Agents: A Declarative Framework for Agent–Web Interaction},
  year = {2025},
  note = {arXiv preprint; Preprint. Verify final bibliographic metadata before thesis submission.}
}
```


---

<!-- ========== FILE: S4_P2\paper_first_notes\S4_P2_36_LegalWebAgent_Empowering_Access_to_Justice_via_LLM-Based_Web_Agents.md ========== -->

## Source: `S4_P2\paper_first_notes\S4_P2_36_LegalWebAgent_Empowering_Access_to_Justice_via_LLM-Based_Web_Agents.md`

# S4 P2 Paper 36 — LegalWebAgent: Empowering Access to Justice via LLM-Based Web Agents

## Metadata

- **Title:** LegalWebAgent: Empowering Access to Justice via LLM-Based Web Agents
- **Year:** 2025
- **Venue / status:** AI4A2J Workshop 2025, to appear
- **Peer-reviewed status:** Workshop / pending final proceedings
- **Publication type:** Workshop paper / domain case study
- **Thesis section:** S4 — domain-specific web agents
- **Category:** domain-specific legal web agent
- **Priority:** P2
- **BibTeX key:** `legalwebagentempoweringaccesstojust2025`

---

## Simple understanding

LegalWebAgent is a multimodal web-agent framework for legal access-to-justice tasks. It helps users search legal information, navigate websites, fill forms, and book appointments.

In simple terms:

```text
Problem → how can an AI agent interact with a web, GUI, mobile, desktop, or application environment?
Method → add perception, planning, action, memory, API/tool use, state tracking, or browser control.
Goal → complete real user tasks more flexibly than scripts or static chatbots.
```

This note explains the paper first, then connects it to S4 and your thesis.

---

## Core idea

Use Ask, Browse, and Act modules to understand user needs, navigate legal websites using HTML and screenshots, and perform concrete web actions.

The paper is mainly about:

```text
domain-specific legal web agent
```

It contributes to the larger agent loop:

```text
observe → understand state → plan → act → receive feedback → verify / recover → complete task
```

---

## Key finding / main claim

The paper reports high task success on a benchmark of Québec civil-law web tasks.

For S4, the important question is not only whether the method works on its benchmark, but **which part of web/GUI agency it improves**:

- perception and grounding,
- planning and reasoning,
- action execution,
- API/tool use,
- memory/state tracking,
- recovery and verification,
- or deployment/evaluation.

---

## Key evidence to extract from the paper

When reading the paper, extract these points:

- **Figure 1 workflow: Ask → Browse → Act modules with web browser environment.**
- **Benchmark of 15 Québec civil-law tasks.**
- **Reported peak success rate 86.7% and average 84.4% across tested models.**

These are the most useful parts for writing a literature-review paragraph.

---

## Limitations

- **Limitation 1:** Workshop/pending venue; cite carefully.
- **Limitation 2:** Legal tasks are high-stakes and require strong legal validation and human oversight.
- **Limitation 3:** The benchmark has only 15 real-world tasks, so generalization is limited.

General thesis-level limitation:

```text
Improving one agent component is not enough for generalized web automation.
A robust web agent still needs grounding, planning, execution, verification, recovery, and safety.
```

---

## Relation to S4

This paper belongs in S4 because S4 discusses **LLM-based agents for web/GUI/mobile/computer automation**.

Its role in S4 is:

```text
LegalWebAgent: Empowering Access to Justice via LLM-Based Web Agents
→ domain-specific legal web agent
→ supporting P2 source for web/GUI/computer-use agent discussion
```

Use it after explaining what the paper does. Do not introduce it only as “P2”; introduce the method or idea first.

---

## Relation to thesis topic

Your thesis topic is:

```text
LLM-based agents for generalized web automation and data extraction
```

This paper matters because:

It is useful as an applied example showing web agents for access-to-justice and form/navigation assistance.

For generalized web automation, the connection is:

```text
web / GUI / mobile / computer-use interaction
→ agent observes a digital environment
→ agent chooses actions
→ agent extracts information or completes a workflow
```

Even when the paper is not directly about data extraction, it still helps explain the automation layer needed before extraction can be generalized.

---

## How to use this paper in the literature review

Recommended use:

- Use as **P2 support**, not as the central backbone.
- Use for one precise idea, architecture, benchmark, or limitation.
- If peer-reviewed, it can support stronger claims.
- If preprint/workshop/technical report, use it for recent trends and emerging directions.

Suggested sentence:

> LegalWebAgent: Empowering Access to Justice via LLM-Based Web Agents shows how domain-specific legal web agent contributes to the development of LLM-based agents for digital task automation, but its limitations indicate that generalized web automation still requires stronger grounding, verification, and recovery mechanisms.

---

## Reading decision

- **Keep in S4 P2:** Yes
- **Read fully?** No, selected sections are enough unless promoted later
- **Depth needed:** Low to medium
- **Main use:** Support S4 discussion of domain-specific legal web agent
- **Most important parts:**
  - Abstract
  - Introduction
  - Main architecture / method figure
  - Dataset or benchmark section
  - Results table
  - Limitations / discussion

---

## One-sentence summary

LegalWebAgent: Empowering Access to Justice via LLM-Based Web Agents is a P2 supporting paper for S4 because it explains **domain-specific legal web agent**, but it should be cited according to its venue/status and not overused beyond its evidence.

---

## BibTeX placeholder

```bibtex
@misc{legalwebagentempoweringaccesstojust2025,
  title = {LegalWebAgent: Empowering Access to Justice via LLM-Based Web Agents},
  year = {2025},
  note = {AI4A2J Workshop 2025, to appear; Workshop paper / domain case study. Verify final bibliographic metadata before thesis submission.}
}
```


---

<!-- ========== FILE: S4_P2\paper_first_notes\S4_P2_37_NetGent_Agent-Based_Automation_of_Network_Application_Workflows.md ========== -->

## Source: `S4_P2\paper_first_notes\S4_P2_37_NetGent_Agent-Based_Automation_of_Network_Application_Workflows.md`

# S4 P2 Paper 37 — NetGent: Agent-Based Automation of Network Application Workflows

## Metadata

- **Title:** NetGent: Agent-Based Automation of Network Application Workflows
- **Year:** 2025
- **Venue / status:** arXiv preprint
- **Peer-reviewed status:** No confirmed archival venue
- **Publication type:** Preprint
- **Thesis section:** S4 — workflow automation and scalable web interaction
- **Category:** workflow automation / network application data generation
- **Priority:** P2
- **BibTeX key:** `netgentagentbasedautomationofnetwor2025`

---

## Simple understanding

NetGent automates web/network application workflows to generate realistic network traffic datasets. It combines natural-language workflow specification with compiled deterministic execution.

In simple terms:

```text
Problem → how can an AI agent interact with a web, GUI, mobile, desktop, or application environment?
Method → add perception, planning, action, memory, API/tool use, state tracking, or browser control.
Goal → complete real user tasks more flexibly than scripts or static chatbots.
```

This note explains the paper first, then connects it to S4 and your thesis.

---

## Core idea

Compile natural-language state-dependent rules into nondeterministic finite automata and reusable executable code for robust replay.

The paper is mainly about:

```text
workflow automation / network application data generation
```

It contributes to the larger agent loop:

```text
observe → understand state → plan → act → receive feedback → verify / recover → complete task
```

---

## Key finding / main claim

NetGent automates 50+ workflows across streaming, conferencing, social media, and web scraping while improving repeatability, robustness, and efficiency.

For S4, the important question is not only whether the method works on its benchmark, but **which part of web/GUI agency it improves**:

- perception and grounding,
- planning and reasoning,
- action execution,
- API/tool use,
- memory/state tracking,
- recovery and verification,
- or deployment/evaluation.

---

## Key evidence to extract from the paper

When reading the paper, extract these points:

- **Abstract NFA → concrete NFA → cache/replay design.**
- **Evaluation across 50+ workflows.**
- **Claims about reducing redundant LLM calls through state caching and deterministic replay.**

These are the most useful parts for writing a literature-review paragraph.

---

## Limitations

- **Limitation 1:** Preprint status.
- **Limitation 2:** Its target is networking dataset generation, not user-facing web automation generally.
- **Limitation 3:** Workflow compilation still requires robust state detectors and handling UI drift.

General thesis-level limitation:

```text
Improving one agent component is not enough for generalized web automation.
A robust web agent still needs grounding, planning, execution, verification, recovery, and safety.
```

---

## Relation to S4

This paper belongs in S4 because S4 discusses **LLM-based agents for web/GUI/mobile/computer automation**.

Its role in S4 is:

```text
NetGent: Agent-Based Automation of Network Application Workflows
→ workflow automation / network application data generation
→ supporting P2 source for web/GUI/computer-use agent discussion
```

Use it after explaining what the paper does. Do not introduce it only as “P2”; introduce the method or idea first.

---

## Relation to thesis topic

Your thesis topic is:

```text
LLM-based agents for generalized web automation and data extraction
```

This paper matters because:

It gives a useful hybrid design pattern: language-based flexibility plus compiled execution reliability.

For generalized web automation, the connection is:

```text
web / GUI / mobile / computer-use interaction
→ agent observes a digital environment
→ agent chooses actions
→ agent extracts information or completes a workflow
```

Even when the paper is not directly about data extraction, it still helps explain the automation layer needed before extraction can be generalized.

---

## How to use this paper in the literature review

Recommended use:

- Use as **P2 support**, not as the central backbone.
- Use for one precise idea, architecture, benchmark, or limitation.
- If peer-reviewed, it can support stronger claims.
- If preprint/workshop/technical report, use it for recent trends and emerging directions.

Suggested sentence:

> NetGent: Agent-Based Automation of Network Application Workflows shows how workflow automation / network application data generation contributes to the development of LLM-based agents for digital task automation, but its limitations indicate that generalized web automation still requires stronger grounding, verification, and recovery mechanisms.

---

## Reading decision

- **Keep in S4 P2:** Yes
- **Read fully?** No, selected sections are enough unless promoted later
- **Depth needed:** Low to medium
- **Main use:** Support S4 discussion of workflow automation / network application data generation
- **Most important parts:**
  - Abstract
  - Introduction
  - Main architecture / method figure
  - Dataset or benchmark section
  - Results table
  - Limitations / discussion

---

## One-sentence summary

NetGent: Agent-Based Automation of Network Application Workflows is a P2 supporting paper for S4 because it explains **workflow automation / network application data generation**, but it should be cited according to its venue/status and not overused beyond its evidence.

---

## BibTeX placeholder

```bibtex
@misc{netgentagentbasedautomationofnetwor2025,
  title = {NetGent: Agent-Based Automation of Network Application Workflows},
  year = {2025},
  note = {arXiv preprint; Preprint. Verify final bibliographic metadata before thesis submission.}
}
```


---

<!-- ========== FILE: S4_P2\paper_first_notes\S4_P2_GLOBAL_SYNTHESIS.md ========== -->

## Source: `S4_P2\paper_first_notes\S4_P2_GLOBAL_SYNTHESIS.md`

# S4 P2 — Global Synthesis

## What S4 P2 papers cover

This S4 P2 batch covers:

1. early instruction-to-UI and web-support grounding,
2. mobile GUI agents,
3. web agents and browser-native agents,
4. computer-use agents,
5. API-first and hybrid-action agents,
6. agentic web interface proposals,
7. domain-specific web agents,
8. surveys and position papers on future web/GUI agents.

## How to use them

Use S4 P2 papers as supporting evidence:

```text
P0/P1 = central structure and core claims
P2 = breadth, recent examples, system variants, limitations, and trends
```

## Stronger papers

The stronger S4 P2 sources are the peer-reviewed or archival papers:

- ACL 2020 mobile UI action sequence paper
- NAACL 2021 web support task grounding
- KDD 2023 WebGLM
- ACL demo 2024 OpenWebAgent
- NAACL 2025 ReachAgent
- TMLR 2025 phone GUI agents survey
- NeurIPS 2025 WebThinker
- NeurIPS 2025 OpenCUA

## Main trend

The S4 P2 set shows a clear shift:

```text
scripted automation
→ instruction-grounded UI actions
→ LLM/VLM web and mobile agents
→ computer-use agents
→ API-first and hybrid-action agents
→ agent-native web interfaces
```

## Main caution

Many 2025 papers are arXiv preprints, under-review papers, TechRxiv reports, or work-in-progress papers. They are valuable for recent trends, but central claims should rely more on peer-reviewed papers.


---

<!-- ========== FILE: S4_P2\paper_first_notes\S4_P2_INDEX.md ========== -->

## Source: `S4_P2\paper_first_notes\S4_P2_INDEX.md`

# S4 P2 — Paper-First Detailed Notes Index

Each file follows the paper-first structure: understand the paper first, then connect it to S4/P2/thesis.

## Files

- [01. Mapping Natural Language Instructions to Mobile UI Action Sequences](./S4_P2_01_Mapping_Natural_Language_Instructions_to_Mobile_UI_Action_Sequences.md)
- [02. Grounding Open-Domain Instructions to Automate Web Support Tasks](./S4_P2_02_Grounding_Open-Domain_Instructions_to_Automate_Web_Support_Tasks.md)
- [03. SYNAPSE: Leveraging Few-Shot Exemplars for Human-Level Computer Control](./S4_P2_03_SYNAPSE_Leveraging_Few-Shot_Exemplars_for_Human-Level_Computer_Control.md)
- [04. WebGLM: Towards an Efficient Web-Enhanced Question Answering System with Human Preferences](./S4_P2_04_WebGLM_Towards_an_Efficient_Web-Enhanced_Question_Answering_System_with_Human_Preferences.md)
- [05. A Zero-Shot Language Agent for Computer Control with Structured Reflection](./S4_P2_05_A_Zero-Shot_Language_Agent_for_Computer_Control_with_Structured_Reflection.md)
- [06. GPT-4V in Wonderland: Large Multimodal Models for Zero-Shot Smartphone GUI Navigation](./S4_P2_06_GPT-4V_in_Wonderland_Large_Multimodal_Models_for_Zero-Shot_Smartphone_GUI_Navigation.md)
- [07. AppAgent: Multimodal Agents as Smartphone Users](./S4_P2_07_AppAgent_Multimodal_Agents_as_Smartphone_Users.md)
- [08. Mobile-Agent: Autonomous Multi-Modal Mobile Device Agent with Visual Perception](./S4_P2_08_Mobile-Agent_Autonomous_Multi-Modal_Mobile_Device_Agent_with_Visual_Perception.md)
- [09. CRADLE: Empowering Foundation Agents Towards General Computer Control](./S4_P2_09_CRADLE_Empowering_Foundation_Agents_Towards_General_Computer_Control.md)
- [10. ChatShop: Interactive Information Seeking with Language Agents](./S4_P2_10_ChatShop_Interactive_Information_Seeking_with_Language_Agents.md)
- [11. Grounded Language Agent for Product Search via Intelligent Web Interactions](./S4_P2_11_Grounded_Language_Agent_for_Product_Search_via_Intelligent_Web_Interactions.md)
- [12. Automating the Enterprise with Foundation Models](./S4_P2_12_Automating_the_Enterprise_with_Foundation_Models.md)
- [13. OpenWebAgent: An Open Toolkit to Enable Web Agents on Large Language Models](./S4_P2_13_OpenWebAgent_An_Open_Toolkit_to_Enable_Web_Agents_on_Large_Language_Models.md)
- [14. Steward: Natural Language Web Automation](./S4_P2_14_Steward_Natural_Language_Web_Automation.md)
- [15. AXIS: Efficient Human-Agent-Computer Interaction with API-First LLM-Based Agents](./S4_P2_15_AXIS_Efficient_Human-Agent-Computer_Interaction_with_API-First_LLM-Based_Agents.md)
- [16. Foundations and Recent Trends in Multimodal Mobile Agents: A Survey](./S4_P2_16_Foundations_and_Recent_Trends_in_Multimodal_Mobile_Agents_A_Survey.md)
- [17. The Dawn of GUI Agent: A Preliminary Case Study with Claude 3.5 Computer Use](./S4_P2_17_The_Dawn_of_GUI_Agent_A_Preliminary_Case_Study_with_Claude_3.5_Computer_Use.md)
- [18. A Comprehensive Survey of Agents for Computer Use: Foundations, Challenges, and Future Directions](./S4_P2_18_A_Comprehensive_Survey_of_Agents_for_Computer_Use_Foundations_Challenges_and_Future_Directions.md)
- [19. Mobile-Agent-E: Self-Evolving Mobile Assistant for Complex Tasks](./S4_P2_19_Mobile-Agent-E_Self-Evolving_Mobile_Assistant_for_Complex_Tasks.md)
- [20. ReachAgent: Enhancing Mobile Agent via Page Reaching and Page Operation](./S4_P2_20_ReachAgent_Enhancing_Mobile_Agent_via_Page_Reaching_and_Page_Operation.md)
- [21. LiteWebAgent: The Open-Source Suite for VLM-Based Web-Agent Applications](./S4_P2_21_LiteWebAgent_The_Open-Source_Suite_for_VLM-Based_Web-Agent_Applications.md)
- [22. LLM-Powered GUI Agents in Phone Automation: Surveying Progress and Prospects](./S4_P2_22_LLM-Powered_GUI_Agents_in_Phone_Automation_Surveying_Progress_and_Prospects.md)
- [23. WebThinker: Empowering Large Reasoning Models with Deep Research Capability](./S4_P2_23_WebThinker_Empowering_Large_Reasoning_Models_with_Deep_Research_Capability.md)
- [24. Beyond Browsing: API-Based Web Agents](./S4_P2_24_Beyond_Browsing_API-Based_Web_Agents.md)
- [25. GA: A Comprehensive Survey on LLM-based GUI Agent](./S4_P2_25_GA_A_Comprehensive_Survey_on_LLM-based_GUI_Agent.md)
- [26. Build the Web for Agents, Not Agents for the Web](./S4_P2_26_Build_the_Web_for_Agents_Not_Agents_for_the_Web.md)
- [27. Embodied Web Agents: Bridging Physical-Digital Realms for Integrated Agent Intelligence](./S4_P2_27_Embodied_Web_Agents_Bridging_Physical-Digital_Realms_for_Integrated_Agent_Intelligence.md)
- [28. Agentic Web: Weaving the Next Web with AI Agents](./S4_P2_28_Agentic_Web_Weaving_the_Next_Web_with_AI_Agents.md)
- [29. CoAct-1: Computer-using Agents with Coding as Actions](./S4_P2_29_CoAct-1_Computer-using_Agents_with_Coding_as_Actions.md)
- [30. OpenCUA: Open Foundations for Computer-Use Agents](./S4_P2_30_OpenCUA_Open_Foundations_for_Computer-Use_Agents.md)
- [31. Are LLM Agents the New RPA? A Comparative Study with RPA Across Enterprise Workflows](./S4_P2_31_Are_LLM_Agents_the_New_RPA_A_Comparative_Study_with_RPA_Across_Enterprise_Workflows.md)
- [32. BrowserAgent: Building Web Agents with Human-Inspired Web Browsing Actions](./S4_P2_32_BrowserAgent_Building_Web_Agents_with_Human-Inspired_Web_Browsing_Actions.md)
- [33. UltraCUA: A Foundation Model for Computer Use Agents with Hybrid Action](./S4_P2_33_UltraCUA_A_Foundation_Model_for_Computer_Use_Agents_with_Hybrid_Action.md)
- [34. Agent-SAMA: State-Aware Mobile Assistant](./S4_P2_34_Agent-SAMA_State-Aware_Mobile_Assistant.md)
- [35. Building the Web for Agents: A Declarative Framework for Agent–Web Interaction](./S4_P2_35_Building_the_Web_for_Agents_A_Declarative_Framework_for_AgentWeb_Interaction.md)
- [36. LegalWebAgent: Empowering Access to Justice via LLM-Based Web Agents](./S4_P2_36_LegalWebAgent_Empowering_Access_to_Justice_via_LLM-Based_Web_Agents.md)
- [37. NetGent: Agent-Based Automation of Network Application Workflows](./S4_P2_37_NetGent_Agent-Based_Automation_of_Network_Application_Workflows.md)


---

<!-- ========== FILE: S4_P2_deep_internet_venue_verification_arxiv_preprints.md ========== -->

## Source: `S4_P2_deep_internet_venue_verification_arxiv_preprints.md`

# S4 P2 — Deep Internet Verification of arXiv / Preprint Papers

This report checks only the S4 P2 items that were previously marked as arXiv, preprint, technical report, under review, workshop, or unclear.

## Main corrections

The first venue report was conservative. After internet verification, several papers should be upgraded from “arXiv/preprint” to confirmed peer-reviewed or workshop status.

### Upgraded to confirmed peer-reviewed / archival

- **A Zero-Shot Language Agent for Computer Control with Structured Reflection** → Findings of EMNLP 2023.
- **AppAgent: Multimodal Agents as Smartphone Users** → CHI 2025 / ACM DL.
- **CRADLE: Empowering Foundation Agents Towards General Computer Control** → ICML 2025 / PMLR v267.
- **Automating the Enterprise with Foundation Models** → PVLDB Vol. 17.
- **AXIS: Efficient Human-Agent-Computer Interaction with API-First LLM-Based Agents** → ACL 2025 main conference.
- **A Comprehensive Survey of Agents for Computer Use** → JAIR 2026.
- **Beyond Browsing: API-Based Web Agents** → Findings of ACL 2025.
- **BrowserAgent: Building Web Agents with Human-Inspired Web Browsing Actions** → TMLR accepted / DBLP lists TMLR 2026.
- **Agent-SAMA: State-Aware Mobile Assistant** → AAAI 2026.

### Confirmed workshop only

- **Mobile-Agent: Autonomous Multi-Modal Mobile Device Agent with Visual Perception** → arXiv; MobileAgent project says ICLR 2024 Workshop.
- **ChatShop: Interactive Information Seeking with Language Agents** → arXiv; SouthNLP workshop poster found.
- **Mobile-Agent-E: Self-Evolving Mobile Assistant for Complex Tasks** → SEA @ NeurIPS 2025 Workshop Oral.
- **LegalWebAgent: Empowering Access to Justice via LLM-Based Web Agents** → AI4A2J Workshop at JURIX 2025.

### Still arXiv / preprint / no confirmed venue found

- **SYNAPSE / Synapse: Trajectory-as-Exemplar Prompting with Memory for Computer Control** → arXiv + OpenReview page.
- **GPT-4V in Wonderland / MM-Navigator** → arXiv + project/GitHub pages.
- **Steward: Natural Language Web Automation** → arXiv only.
- **Foundations and Recent Trends in Multimodal Mobile Agents: A Survey** → arXiv only.
- **The Dawn of GUI Agent: A Preliminary Case Study with Claude 3.5 Computer Use** → arXiv only.
- **GA: A Comprehensive Survey on LLM-based GUI Agent** → TechRxiv / submitted manuscript.
- **Build the Web for Agents, Not Agents for the Web** → arXiv position paper / under review.
- **Embodied Web Agents: Bridging Physical-Digital Realms for Integrated Agent Intelligence** → arXiv/OpenReview under-review style page.
- **Agentic Web: Weaving the Next Web with AI Agents** → arXiv survey/vision paper.
- **CoAct-1: Computer-using Agents with Coding as Actions** → arXiv/OpenReview submission.
- **Are LLM Agents the New RPA? A Comparative Study with RPA Across Enterprise Workflows** → arXiv only.
- **UltraCUA: A Foundation Model for Computer Use Agents with Hybrid Action** → arXiv/OpenReview submission.
- **Building the Web for Agents: A Declarative Framework for Agent-Web Interaction** → arXiv only.
- **NetGent: Agent-Based Automation of Network Application Workflows** → arXiv/OpenReview submission.

## Full verification table

| # | Paper | Current verified venue/status | Peer-reviewed? | Corrected action | Notes |
|---:|---|---|---|---|---|
| 1 | **SYNAPSE / Synapse: Trajectory-as-Exemplar Prompting with Memory for Computer Control** | arXiv + OpenReview page | No confirmed peer-reviewed venue found | Keep as preprint | Search found arXiv and OpenReview/project pages, but no ACL/NeurIPS/ICLR/ICML/AAAI/CHI archival record. |
| 2 | **A Zero-Shot Language Agent for Computer Control with Structured Reflection** | Findings of EMNLP 2023 | Yes | Upgrade from preprint to peer-reviewed Findings paper | ACL Anthology record exists: 2023.findings-emnlp.753. |
| 3 | **GPT-4V in Wonderland / MM-Navigator** | arXiv + project/GitHub pages | No confirmed peer-reviewed venue found | Keep as preprint | Search found arXiv, GitHub, and Semantic Scholar only; no final conference/journal record confirmed. |
| 4 | **AppAgent: Multimodal Agents as Smartphone Users** | CHI 2025 / ACM DL | Yes | Upgrade from preprint to peer-reviewed CHI paper | ACM DL and CHI program record found. |
| 5 | **Mobile-Agent: Autonomous Multi-Modal Mobile Device Agent with Visual Perception** | arXiv; MobileAgent project says ICLR 2024 Workshop | Workshop only / not main archival | Keep as workshop/preprint | Project page says Mobile-Agent accepted by ICLR 2024 Workshop; no main conference/journal version found. |
| 6 | **CRADLE: Empowering Foundation Agents Towards General Computer Control** | ICML 2025 / PMLR v267 | Yes | Upgrade to peer-reviewed ICML paper | PMLR proceedings record found. |
| 7 | **ChatShop: Interactive Information Seeking with Language Agents** | arXiv; SouthNLP workshop poster found | Workshop/preprint only | Keep as preprint/workshop poster | DukeNLP lists it as arXiv; SouthNLP poster PDF found, no main archival venue confirmed. |
| 8 | **Automating the Enterprise with Foundation Models** | PVLDB Vol. 17 | Yes | Upgrade to peer-reviewed/archival PVLDB paper | VLDB PDF record found. |
| 9 | **Steward: Natural Language Web Automation** | arXiv only | No confirmed peer-reviewed venue found | Keep as preprint | GitHub citation still lists arXiv preprint; no final venue found. |
| 10 | **AXIS: Efficient Human-Agent-Computer Interaction with API-First LLM-Based Agents** | ACL 2025 main conference | Yes | Upgrade to peer-reviewed ACL long paper | ACL Anthology record exists: 2025.acl-long.381. |
| 11 | **Foundations and Recent Trends in Multimodal Mobile Agents: A Survey** | arXiv only | No confirmed peer-reviewed venue found | Keep as survey preprint | Author GitHub citation lists arXiv preprint. |
| 12 | **The Dawn of GUI Agent: A Preliminary Case Study with Claude 3.5 Computer Use** | arXiv only | No confirmed peer-reviewed venue found | Keep as preprint/case study | Search found arXiv/project pages only. |
| 13 | **A Comprehensive Survey of Agents for Computer Use** | JAIR 2026 | Yes | Upgrade to peer-reviewed journal article | JAIR article page found. |
| 14 | **Mobile-Agent-E: Self-Evolving Mobile Assistant for Complex Tasks** | SEA @ NeurIPS 2025 Workshop Oral | Workshop | Keep as workshop/preprint, not main NeurIPS | SEA workshop/OpenReview page confirms NeurIPS 2025 workshop oral. |
| 15 | **Beyond Browsing: API-Based Web Agents** | Findings of ACL 2025 | Yes | Upgrade to peer-reviewed Findings paper | ACL Anthology record exists: 2025.findings-acl.577. |
| 16 | **GA: A Comprehensive Survey on LLM-based GUI Agent** | TechRxiv / submitted manuscript | No | Keep as non-peer-reviewed preprint | TechRxiv page and uploaded copy indicate preliminary/not peer-reviewed. |
| 17 | **Build the Web for Agents, Not Agents for the Web** | arXiv position paper / under review | No confirmed peer-reviewed venue found | Keep as position preprint | Search found arXiv only. |
| 18 | **Embodied Web Agents: Bridging Physical-Digital Realms for Integrated Agent Intelligence** | arXiv/OpenReview under-review style page | No confirmed peer-reviewed venue found | Keep as preprint/under-review | Search found project/arXiv/OpenReview page, no accepted venue confirmed. |
| 19 | **Agentic Web: Weaving the Next Web with AI Agents** | arXiv survey/vision paper | No confirmed peer-reviewed venue found | Keep as survey/vision preprint | GitHub citation lists arXiv preprint. |
| 20 | **CoAct-1: Computer-using Agents with Coding as Actions** | arXiv/OpenReview submission | No confirmed accepted venue found | Keep as preprint/submission | Search found arXiv, project, OpenReview submission; no accepted venue confirmed. |
| 21 | **Are LLM Agents the New RPA? A Comparative Study with RPA Across Enterprise Workflows** | arXiv only | No confirmed peer-reviewed venue found | Keep as preprint | Search found arXiv/ResearchGate/Semantic Scholar only. |
| 22 | **BrowserAgent: Building Web Agents with Human-Inspired Web Browsing Actions** | TMLR accepted / DBLP lists TMLR 2026 | Yes, but final citation likely 2026 | Upgrade from work-in-progress to TMLR accepted | GitHub/OpenReview profile/DBLP indicate TMLR acceptance; use TMLR 2026 if final metadata confirms. |
| 23 | **UltraCUA: A Foundation Model for Computer Use Agents with Hybrid Action** | arXiv/OpenReview submission | No confirmed accepted venue found | Keep as preprint/submission | Search found arXiv/HuggingFace/OpenReview submission only. |
| 24 | **Agent-SAMA: State-Aware Mobile Assistant** | AAAI 2026 | Yes | Upgrade from preprint to peer-reviewed AAAI paper | Zenodo says AAAI26 accepted; AAAI/OJS PDF record found. |
| 25 | **Building the Web for Agents: A Declarative Framework for Agent-Web Interaction** | arXiv only | No confirmed peer-reviewed venue found | Keep as preprint | Search found arXiv only. |
| 26 | **LegalWebAgent: Empowering Access to Justice via LLM-Based Web Agents** | AI4A2J Workshop at JURIX 2025 | Workshop | Keep as workshop paper | Workshop website lists the paper; arXiv exists. |
| 27 | **NetGent: Agent-Based Automation of Network Application Workflows** | arXiv/OpenReview submission | No confirmed accepted venue found | Keep as preprint/submission | Search found arXiv/OpenReview PDF and project/blog pages, no accepted venue confirmed. |

## Corrected S4 P2 citation strategy

### Safe for stronger claims after correction

- A Zero-Shot Language Agent for Computer Control with Structured Reflection — Findings of EMNLP 2023
- AppAgent — CHI 2025
- CRADLE — ICML 2025
- Automating the Enterprise with Foundation Models — PVLDB Vol. 17
- AXIS — ACL 2025
- A Comprehensive Survey of Agents for Computer Use — JAIR 2026
- Beyond Browsing — Findings of ACL 2025
- BrowserAgent — TMLR accepted / likely TMLR 2026 final citation
- Agent-SAMA — AAAI 2026

### Use as workshop/system/support sources

- Mobile-Agent — ICLR 2024 Workshop
- Mobile-Agent-E — SEA @ NeurIPS 2025 Workshop Oral
- LegalWebAgent — AI4A2J Workshop at JURIX 2025

### Keep as preprint / recent trend only

- SYNAPSE / Synapse: Trajectory-as-Exemplar Prompting with Memory for Computer Control
- GPT-4V in Wonderland / MM-Navigator
- ChatShop: Interactive Information Seeking with Language Agents
- Steward: Natural Language Web Automation
- Foundations and Recent Trends in Multimodal Mobile Agents: A Survey
- The Dawn of GUI Agent: A Preliminary Case Study with Claude 3.5 Computer Use
- GA: A Comprehensive Survey on LLM-based GUI Agent
- Build the Web for Agents, Not Agents for the Web
- Embodied Web Agents: Bridging Physical-Digital Realms for Integrated Agent Intelligence
- Agentic Web: Weaving the Next Web with AI Agents
- CoAct-1: Computer-using Agents with Coding as Actions
- Are LLM Agents the New RPA? A Comparative Study with RPA Across Enterprise Workflows
- UltraCUA: A Foundation Model for Computer Use Agents with Hybrid Action
- Building the Web for Agents: A Declarative Framework for Agent-Web Interaction
- NetGent: Agent-Based Automation of Network Application Workflows

## Final note

For the thesis bibliography, use the confirmed venue version when available, not the arXiv version. For papers still listed only as arXiv/TechRxiv/OpenReview submissions, cite them explicitly as preprints or workshop papers.


---

<!-- ========== FILE: S4_P2_paper_first_detailed_markdown_notes\README.md ========== -->

## Source: `S4_P2_paper_first_detailed_markdown_notes\README.md`

# S4 P2 Paper-First Detailed Notes

This ZIP contains one markdown file per S4 P2 paper.

Structure:
1. Metadata
2. Simple understanding
3. Core idea
4. Key finding
5. Key evidence
6. Limitations
7. Relation to S4
8. Relation to thesis
9. How to use in literature review
10. Reading decision
11. One-sentence summary
12. BibTeX placeholder


---

<!-- ========== FILE: S4_P2_paper_first_detailed_markdown_notes\S4_P2_01_Mapping_Natural_Language_Instructions_to_Mobile_UI_Action_Sequences.md ========== -->

## Source: `S4_P2_paper_first_detailed_markdown_notes\S4_P2_01_Mapping_Natural_Language_Instructions_to_Mobile_UI_Action_Sequences.md`

# S4 P2 Paper 01 — Mapping Natural Language Instructions to Mobile UI Action Sequences

## Metadata

- **Title:** Mapping Natural Language Instructions to Mobile UI Action Sequences
- **Year:** 2020
- **Venue / status:** ACL 2020 main conference
- **Peer-reviewed status:** Yes
- **Publication type:** Peer-reviewed conference paper
- **Thesis section:** S4 — LLM-based web, GUI, mobile, and computer-use agents
- **Category:** mobile UI instruction grounding / action sequence prediction
- **Priority:** P2
- **BibTeX key:** `mappingnaturallanguageinstructionst2020`

---

## Simple understanding

This paper studies how to map a natural-language instruction into a sequence of mobile UI actions. It is an early foundation for mobile GUI agents because it frames phone automation as instruction understanding plus UI action prediction.

In simple terms:

```text
Problem → how can an AI agent interact with a web, GUI, mobile, desktop, or application environment?
Method → add perception, planning, action, memory, API/tool use, state tracking, or browser control.
Goal → complete real user tasks more flexibly than scripts or static chatbots.
```

This note explains the paper first, then connects it to S4 and your thesis.

---

## Core idea

Ground user instructions to concrete mobile interface actions, such as tapping, typing, and navigating through app screens.

The paper is mainly about:

```text
mobile UI instruction grounding / action sequence prediction
```

It contributes to the larger agent loop:

```text
observe → understand state → plan → act → receive feedback → verify / recover → complete task
```

---

## Key finding / main claim

The paper shows that mobile task automation can be modeled as predicting action sequences over UI states, creating a foundation for later LLM-powered mobile GUI agents.

For S4, the important question is not only whether the method works on its benchmark, but **which part of web/GUI agency it improves**:

- perception and grounding,
- planning and reasoning,
- action execution,
- API/tool use,
- memory/state tracking,
- recovery and verification,
- or deployment/evaluation.

---

## Key evidence to extract from the paper

When reading the paper, extract these points:

- **Dataset/task formulation mapping instructions to mobile UI actions.**
- **Model setup for action sequence prediction.**
- **Evaluation of instruction-to-action grounding accuracy.**

These are the most useful parts for writing a literature-review paragraph.

---

## Limitations

- **Limitation 1:** It predates modern LLM/VLM agent architectures and therefore does not use strong multimodal reasoning models.
- **Limitation 2:** It focuses on mobile UI action prediction rather than open-ended web/browser automation.
- **Limitation 3:** It depends on datasets and UI representations that may not generalize to all real-world apps.

General thesis-level limitation:

```text
Improving one agent component is not enough for generalized web automation.
A robust web agent still needs grounding, planning, execution, verification, recovery, and safety.
```

---

## Relation to S4

This paper belongs in S4 because S4 discusses **LLM-based agents for web/GUI/mobile/computer automation**.

Its role in S4 is:

```text
Mapping Natural Language Instructions to Mobile UI Action Sequences
→ mobile UI instruction grounding / action sequence prediction
→ supporting P2 source for web/GUI/computer-use agent discussion
```

Use it after explaining what the paper does. Do not introduce it only as “P2”; introduce the method or idea first.

---

## Relation to thesis topic

Your thesis topic is:

```text
LLM-based agents for generalized web automation and data extraction
```

This paper matters because:

It provides historical grounding for the transition from classical/mobile UI automation to LLM-powered phone agents.

For generalized web automation, the connection is:

```text
web / GUI / mobile / computer-use interaction
→ agent observes a digital environment
→ agent chooses actions
→ agent extracts information or completes a workflow
```

Even when the paper is not directly about data extraction, it still helps explain the automation layer needed before extraction can be generalized.

---

## How to use this paper in the literature review

Recommended use:

- Use as **P2 support**, not as the central backbone.
- Use for one precise idea, architecture, benchmark, or limitation.
- If peer-reviewed, it can support stronger claims.
- If preprint/workshop/technical report, use it for recent trends and emerging directions.

Suggested sentence:

> Mapping Natural Language Instructions to Mobile UI Action Sequences shows how mobile UI instruction grounding / action sequence prediction contributes to the development of LLM-based agents for digital task automation, but its limitations indicate that generalized web automation still requires stronger grounding, verification, and recovery mechanisms.

---

## Reading decision

- **Keep in S4 P2:** Yes
- **Read fully?** Yes or selected sections carefully
- **Depth needed:** Medium to high
- **Main use:** Support S4 discussion of mobile UI instruction grounding / action sequence prediction
- **Most important parts:**
  - Abstract
  - Introduction
  - Main architecture / method figure
  - Dataset or benchmark section
  - Results table
  - Limitations / discussion

---

## One-sentence summary

Mapping Natural Language Instructions to Mobile UI Action Sequences is a P2 supporting paper for S4 because it explains **mobile UI instruction grounding / action sequence prediction**, but it should be cited according to its venue/status and not overused beyond its evidence.

---

## BibTeX placeholder

```bibtex
@misc{mappingnaturallanguageinstructionst2020,
  title = {Mapping Natural Language Instructions to Mobile UI Action Sequences},
  year = {2020},
  note = {ACL 2020 main conference; Peer-reviewed conference paper. Verify final bibliographic metadata before thesis submission.}
}
```


---

<!-- ========== FILE: S4_P2_paper_first_detailed_markdown_notes\S4_P2_02_Grounding_Open-Domain_Instructions_to_Automate_Web_Support_Tasks.md ========== -->

## Source: `S4_P2_paper_first_detailed_markdown_notes\S4_P2_02_Grounding_Open-Domain_Instructions_to_Automate_Web_Support_Tasks.md`

# S4 P2 Paper 02 — Grounding Open-Domain Instructions to Automate Web Support Tasks

## Metadata

- **Title:** Grounding Open-Domain Instructions to Automate Web Support Tasks
- **Year:** 2021
- **Venue / status:** NAACL-HLT 2021 main conference
- **Peer-reviewed status:** Yes
- **Publication type:** Peer-reviewed conference paper
- **Thesis section:** S4 — LLM-based web automation and web agents
- **Category:** open-domain web-support automation
- **Priority:** P2
- **BibTeX key:** `groundingopendomaininstructionstoau2021`

---

## Simple understanding

This paper studies how to ground open-domain user instructions into executable steps for web support tasks. It is important because it moves beyond fixed scripts toward instruction-driven web task automation.

In simple terms:

```text
Problem → how can an AI agent interact with a web, GUI, mobile, desktop, or application environment?
Method → add perception, planning, action, memory, API/tool use, state tracking, or browser control.
Goal → complete real user tasks more flexibly than scripts or static chatbots.
```

This note explains the paper first, then connects it to S4 and your thesis.

---

## Core idea

Translate natural-language support instructions into structured actions that can be executed on websites.

The paper is mainly about:

```text
open-domain web-support automation
```

It contributes to the larger agent loop:

```text
observe → understand state → plan → act → receive feedback → verify / recover → complete task
```

---

## Key finding / main claim

The work shows that grounding open-domain web instructions requires connecting language understanding with web state, task representation, and executable action generation.

For S4, the important question is not only whether the method works on its benchmark, but **which part of web/GUI agency it improves**:

- perception and grounding,
- planning and reasoning,
- action execution,
- API/tool use,
- memory/state tracking,
- recovery and verification,
- or deployment/evaluation.

---

## Key evidence to extract from the paper

When reading the paper, extract these points:

- **Task definition for open-domain web support automation.**
- **Grounding method from instructions to executable representations.**
- **Evaluation on web-support task completion or grounding accuracy.**

These are the most useful parts for writing a literature-review paragraph.

---

## Limitations

- **Limitation 1:** The system is more structured and task-specific than later general web agents.
- **Limitation 2:** It does not use modern multimodal LLMs or visual browser grounding.
- **Limitation 3:** It is mainly about support-task grounding, not generalized web automation across arbitrary sites.

General thesis-level limitation:

```text
Improving one agent component is not enough for generalized web automation.
A robust web agent still needs grounding, planning, execution, verification, recovery, and safety.
```

---

## Relation to S4

This paper belongs in S4 because S4 discusses **LLM-based agents for web/GUI/mobile/computer automation**.

Its role in S4 is:

```text
Grounding Open-Domain Instructions to Automate Web Support Tasks
→ open-domain web-support automation
→ supporting P2 source for web/GUI/computer-use agent discussion
```

Use it after explaining what the paper does. Do not introduce it only as “P2”; introduce the method or idea first.

---

## Relation to thesis topic

Your thesis topic is:

```text
LLM-based agents for generalized web automation and data extraction
```

This paper matters because:

It is an early peer-reviewed source showing how web automation can be framed as language grounding plus executable web actions.

For generalized web automation, the connection is:

```text
web / GUI / mobile / computer-use interaction
→ agent observes a digital environment
→ agent chooses actions
→ agent extracts information or completes a workflow
```

Even when the paper is not directly about data extraction, it still helps explain the automation layer needed before extraction can be generalized.

---

## How to use this paper in the literature review

Recommended use:

- Use as **P2 support**, not as the central backbone.
- Use for one precise idea, architecture, benchmark, or limitation.
- If peer-reviewed, it can support stronger claims.
- If preprint/workshop/technical report, use it for recent trends and emerging directions.

Suggested sentence:

> Grounding Open-Domain Instructions to Automate Web Support Tasks shows how open-domain web-support automation contributes to the development of LLM-based agents for digital task automation, but its limitations indicate that generalized web automation still requires stronger grounding, verification, and recovery mechanisms.

---

## Reading decision

- **Keep in S4 P2:** Yes
- **Read fully?** Yes or selected sections carefully
- **Depth needed:** Medium to high
- **Main use:** Support S4 discussion of open-domain web-support automation
- **Most important parts:**
  - Abstract
  - Introduction
  - Main architecture / method figure
  - Dataset or benchmark section
  - Results table
  - Limitations / discussion

---

## One-sentence summary

Grounding Open-Domain Instructions to Automate Web Support Tasks is a P2 supporting paper for S4 because it explains **open-domain web-support automation**, but it should be cited according to its venue/status and not overused beyond its evidence.

---

## BibTeX placeholder

```bibtex
@misc{groundingopendomaininstructionstoau2021,
  title = {Grounding Open-Domain Instructions to Automate Web Support Tasks},
  year = {2021},
  note = {NAACL-HLT 2021 main conference; Peer-reviewed conference paper. Verify final bibliographic metadata before thesis submission.}
}
```


---

<!-- ========== FILE: S4_P2_paper_first_detailed_markdown_notes\S4_P2_03_SYNAPSE_Leveraging_Few-Shot_Exemplars_for_Human-Level_Computer_Control.md ========== -->

## Source: `S4_P2_paper_first_detailed_markdown_notes\S4_P2_03_SYNAPSE_Leveraging_Few-Shot_Exemplars_for_Human-Level_Computer_Control.md`

# S4 P2 Paper 03 — SYNAPSE: Leveraging Few-Shot Exemplars for Human-Level Computer Control

## Metadata

- **Title:** SYNAPSE: Leveraging Few-Shot Exemplars for Human-Level Computer Control
- **Year:** 2023
- **Venue / status:** arXiv preprint
- **Peer-reviewed status:** No confirmed archival venue
- **Publication type:** Preprint
- **Thesis section:** S4 — computer-use and GUI-agent foundations
- **Category:** few-shot computer control / MiniWoB-style GUI automation
- **Priority:** P2
- **BibTeX key:** `synapseleveragingfewshotexemplarsfo2023`

---

## Simple understanding

SYNAPSE explores whether few-shot prompting can enable LLMs to control computers or web interfaces. It uses examples to guide action selection in interactive environments.

In simple terms:

```text
Problem → how can an AI agent interact with a web, GUI, mobile, desktop, or application environment?
Method → add perception, planning, action, memory, API/tool use, state tracking, or browser control.
Goal → complete real user tasks more flexibly than scripts or static chatbots.
```

This note explains the paper first, then connects it to S4 and your thesis.

---

## Core idea

Use few-shot exemplars to help an LLM infer how to perform computer-control tasks through actions.

The paper is mainly about:

```text
few-shot computer control / MiniWoB-style GUI automation
```

It contributes to the larger agent loop:

```text
observe → understand state → plan → act → receive feedback → verify / recover → complete task
```

---

## Key finding / main claim

Few-shot examples can improve action prediction and task completion in controlled computer-use environments.

For S4, the important question is not only whether the method works on its benchmark, but **which part of web/GUI agency it improves**:

- perception and grounding,
- planning and reasoning,
- action execution,
- API/tool use,
- memory/state tracking,
- recovery and verification,
- or deployment/evaluation.

---

## Key evidence to extract from the paper

When reading the paper, extract these points:

- **Prompting design with few-shot exemplars.**
- **Computer-control benchmark results.**
- **Analysis of where exemplar-based control succeeds or fails.**

These are the most useful parts for writing a literature-review paragraph.

---

## Limitations

- **Limitation 1:** The uploaded/known status is preprint, so cite carefully.
- **Limitation 2:** Controlled benchmarks are simpler than real dynamic web environments.
- **Limitation 3:** Few-shot prompting alone may be brittle for long-horizon tasks and UI changes.

General thesis-level limitation:

```text
Improving one agent component is not enough for generalized web automation.
A robust web agent still needs grounding, planning, execution, verification, recovery, and safety.
```

---

## Relation to S4

This paper belongs in S4 because S4 discusses **LLM-based agents for web/GUI/mobile/computer automation**.

Its role in S4 is:

```text
SYNAPSE: Leveraging Few-Shot Exemplars for Human-Level Computer Control
→ few-shot computer control / MiniWoB-style GUI automation
→ supporting P2 source for web/GUI/computer-use agent discussion
```

Use it after explaining what the paper does. Do not introduce it only as “P2”; introduce the method or idea first.

---

## Relation to thesis topic

Your thesis topic is:

```text
LLM-based agents for generalized web automation and data extraction
```

This paper matters because:

It supports the transition from static LLM prompting to interactive computer-use agents.

For generalized web automation, the connection is:

```text
web / GUI / mobile / computer-use interaction
→ agent observes a digital environment
→ agent chooses actions
→ agent extracts information or completes a workflow
```

Even when the paper is not directly about data extraction, it still helps explain the automation layer needed before extraction can be generalized.

---

## How to use this paper in the literature review

Recommended use:

- Use as **P2 support**, not as the central backbone.
- Use for one precise idea, architecture, benchmark, or limitation.
- If peer-reviewed, it can support stronger claims.
- If preprint/workshop/technical report, use it for recent trends and emerging directions.

Suggested sentence:

> SYNAPSE: Leveraging Few-Shot Exemplars for Human-Level Computer Control shows how few-shot computer control / MiniWoB-style GUI automation contributes to the development of LLM-based agents for digital task automation, but its limitations indicate that generalized web automation still requires stronger grounding, verification, and recovery mechanisms.

---

## Reading decision

- **Keep in S4 P2:** Yes
- **Read fully?** No, selected sections are enough unless promoted later
- **Depth needed:** Low to medium
- **Main use:** Support S4 discussion of few-shot computer control / MiniWoB-style GUI automation
- **Most important parts:**
  - Abstract
  - Introduction
  - Main architecture / method figure
  - Dataset or benchmark section
  - Results table
  - Limitations / discussion

---

## One-sentence summary

SYNAPSE: Leveraging Few-Shot Exemplars for Human-Level Computer Control is a P2 supporting paper for S4 because it explains **few-shot computer control / MiniWoB-style GUI automation**, but it should be cited according to its venue/status and not overused beyond its evidence.

---

## BibTeX placeholder

```bibtex
@misc{synapseleveragingfewshotexemplarsfo2023,
  title = {SYNAPSE: Leveraging Few-Shot Exemplars for Human-Level Computer Control},
  year = {2023},
  note = {arXiv preprint; Preprint. Verify final bibliographic metadata before thesis submission.}
}
```


---

<!-- ========== FILE: S4_P2_paper_first_detailed_markdown_notes\S4_P2_04_WebGLM_Towards_an_Efficient_Web-Enhanced_Question_Answering_System_with_Human_Preferences.md ========== -->

## Source: `S4_P2_paper_first_detailed_markdown_notes\S4_P2_04_WebGLM_Towards_an_Efficient_Web-Enhanced_Question_Answering_System_with_Human_Preferences.md`

# S4 P2 Paper 04 — WebGLM: Towards an Efficient Web-Enhanced Question Answering System with Human Preferences

## Metadata

- **Title:** WebGLM: Towards an Efficient Web-Enhanced Question Answering System with Human Preferences
- **Year:** 2023
- **Venue / status:** KDD 2023
- **Peer-reviewed status:** Yes
- **Publication type:** Peer-reviewed conference paper
- **Thesis section:** S4 — web-enhanced LLM systems and information agents
- **Category:** web-enhanced QA / retrieval and browsing
- **Priority:** P2
- **BibTeX key:** `webglmtowardsanefficientwebenhanced2023`

---

## Simple understanding

WebGLM is a web-enhanced question answering system that uses web search and human preference alignment to answer questions more effectively.

In simple terms:

```text
Problem → how can an AI agent interact with a web, GUI, mobile, desktop, or application environment?
Method → add perception, planning, action, memory, API/tool use, state tracking, or browser control.
Goal → complete real user tasks more flexibly than scripts or static chatbots.
```

This note explains the paper first, then connects it to S4 and your thesis.

---

## Core idea

Combine LLM generation with web retrieval/browsing and human preference optimization for web-grounded QA.

The paper is mainly about:

```text
web-enhanced QA / retrieval and browsing
```

It contributes to the larger agent loop:

```text
observe → understand state → plan → act → receive feedback → verify / recover → complete task
```

---

## Key finding / main claim

Web-enhanced systems can improve answer factuality and usefulness by grounding generation in online information.

For S4, the important question is not only whether the method works on its benchmark, but **which part of web/GUI agency it improves**:

- perception and grounding,
- planning and reasoning,
- action execution,
- API/tool use,
- memory/state tracking,
- recovery and verification,
- or deployment/evaluation.

---

## Key evidence to extract from the paper

When reading the paper, extract these points:

- **System pipeline for web-enhanced QA.**
- **Human preference or alignment component.**
- **KDD evaluation results comparing web-enhanced answers.**

These are the most useful parts for writing a literature-review paragraph.

---

## Limitations

- **Limitation 1:** It is mainly QA-oriented, not a general web-control or browser-action agent.
- **Limitation 2:** It does not focus on completing transactional web tasks like forms, carts, or account operations.
- **Limitation 3:** Web retrieval quality and source reliability still constrain output quality.

General thesis-level limitation:

```text
Improving one agent component is not enough for generalized web automation.
A robust web agent still needs grounding, planning, execution, verification, recovery, and safety.
```

---

## Relation to S4

This paper belongs in S4 because S4 discusses **LLM-based agents for web/GUI/mobile/computer automation**.

Its role in S4 is:

```text
WebGLM: Towards an Efficient Web-Enhanced Question Answering System with Human Preferences
→ web-enhanced QA / retrieval and browsing
→ supporting P2 source for web/GUI/computer-use agent discussion
```

Use it after explaining what the paper does. Do not introduce it only as “P2”; introduce the method or idea first.

---

## Relation to thesis topic

Your thesis topic is:

```text
LLM-based agents for generalized web automation and data extraction
```

This paper matters because:

It connects web retrieval and LLM generation, which is a foundation for later deep-research and web information agents.

For generalized web automation, the connection is:

```text
web / GUI / mobile / computer-use interaction
→ agent observes a digital environment
→ agent chooses actions
→ agent extracts information or completes a workflow
```

Even when the paper is not directly about data extraction, it still helps explain the automation layer needed before extraction can be generalized.

---

## How to use this paper in the literature review

Recommended use:

- Use as **P2 support**, not as the central backbone.
- Use for one precise idea, architecture, benchmark, or limitation.
- If peer-reviewed, it can support stronger claims.
- If preprint/workshop/technical report, use it for recent trends and emerging directions.

Suggested sentence:

> WebGLM: Towards an Efficient Web-Enhanced Question Answering System with Human Preferences shows how web-enhanced QA / retrieval and browsing contributes to the development of LLM-based agents for digital task automation, but its limitations indicate that generalized web automation still requires stronger grounding, verification, and recovery mechanisms.

---

## Reading decision

- **Keep in S4 P2:** Yes
- **Read fully?** Yes or selected sections carefully
- **Depth needed:** Medium to high
- **Main use:** Support S4 discussion of web-enhanced QA / retrieval and browsing
- **Most important parts:**
  - Abstract
  - Introduction
  - Main architecture / method figure
  - Dataset or benchmark section
  - Results table
  - Limitations / discussion

---

## One-sentence summary

WebGLM: Towards an Efficient Web-Enhanced Question Answering System with Human Preferences is a P2 supporting paper for S4 because it explains **web-enhanced QA / retrieval and browsing**, but it should be cited according to its venue/status and not overused beyond its evidence.

---

## BibTeX placeholder

```bibtex
@misc{webglmtowardsanefficientwebenhanced2023,
  title = {WebGLM: Towards an Efficient Web-Enhanced Question Answering System with Human Preferences},
  year = {2023},
  note = {KDD 2023; Peer-reviewed conference paper. Verify final bibliographic metadata before thesis submission.}
}
```


---

<!-- ========== FILE: S4_P2_paper_first_detailed_markdown_notes\S4_P2_05_A_Zero-Shot_Language_Agent_for_Computer_Control_with_Structured_Reflection.md ========== -->

## Source: `S4_P2_paper_first_detailed_markdown_notes\S4_P2_05_A_Zero-Shot_Language_Agent_for_Computer_Control_with_Structured_Reflection.md`

# S4 P2 Paper 05 — A Zero-Shot Language Agent for Computer Control with Structured Reflection

## Metadata

- **Title:** A Zero-Shot Language Agent for Computer Control with Structured Reflection
- **Year:** 2023
- **Venue / status:** arXiv preprint
- **Peer-reviewed status:** No confirmed archival venue
- **Publication type:** Preprint
- **Thesis section:** S4 — computer-use agents and reflective web/GUI control
- **Category:** zero-shot computer control / reflection
- **Priority:** P2
- **BibTeX key:** `azeroshotlanguageagentforcomputerco2023`

---

## Simple understanding

This paper studies a language agent that controls a computer using structured reflection without task-specific training.

In simple terms:

```text
Problem → how can an AI agent interact with a web, GUI, mobile, desktop, or application environment?
Method → add perception, planning, action, memory, API/tool use, state tracking, or browser control.
Goal → complete real user tasks more flexibly than scripts or static chatbots.
```

This note explains the paper first, then connects it to S4 and your thesis.

---

## Core idea

Use zero-shot LLM reasoning and structured reflection to select actions and improve future decisions during computer control.

The paper is mainly about:

```text
zero-shot computer control / reflection
```

It contributes to the larger agent loop:

```text
observe → understand state → plan → act → receive feedback → verify / recover → complete task
```

---

## Key finding / main claim

Reflection can improve interactive performance by helping the agent reason about previous actions and current state.

For S4, the important question is not only whether the method works on its benchmark, but **which part of web/GUI agency it improves**:

- perception and grounding,
- planning and reasoning,
- action execution,
- API/tool use,
- memory/state tracking,
- recovery and verification,
- or deployment/evaluation.

---

## Key evidence to extract from the paper

When reading the paper, extract these points:

- **Reflection structure used by the agent.**
- **Computer-control environment or benchmark results.**
- **Failure cases showing limits of reflection.**

These are the most useful parts for writing a literature-review paragraph.

---

## Limitations

- **Limitation 1:** Preprint status means it should be cited carefully.
- **Limitation 2:** Zero-shot reflection can still be wrong or ungrounded.
- **Limitation 3:** It may not scale reliably to complex real-world websites and desktop workflows.

General thesis-level limitation:

```text
Improving one agent component is not enough for generalized web automation.
A robust web agent still needs grounding, planning, execution, verification, recovery, and safety.
```

---

## Relation to S4

This paper belongs in S4 because S4 discusses **LLM-based agents for web/GUI/mobile/computer automation**.

Its role in S4 is:

```text
A Zero-Shot Language Agent for Computer Control with Structured Reflection
→ zero-shot computer control / reflection
→ supporting P2 source for web/GUI/computer-use agent discussion
```

Use it after explaining what the paper does. Do not introduce it only as “P2”; introduce the method or idea first.

---

## Relation to thesis topic

Your thesis topic is:

```text
LLM-based agents for generalized web automation and data extraction
```

This paper matters because:

It supports the idea that GUI/web agents need feedback and self-evaluation, not only action prediction.

For generalized web automation, the connection is:

```text
web / GUI / mobile / computer-use interaction
→ agent observes a digital environment
→ agent chooses actions
→ agent extracts information or completes a workflow
```

Even when the paper is not directly about data extraction, it still helps explain the automation layer needed before extraction can be generalized.

---

## How to use this paper in the literature review

Recommended use:

- Use as **P2 support**, not as the central backbone.
- Use for one precise idea, architecture, benchmark, or limitation.
- If peer-reviewed, it can support stronger claims.
- If preprint/workshop/technical report, use it for recent trends and emerging directions.

Suggested sentence:

> A Zero-Shot Language Agent for Computer Control with Structured Reflection shows how zero-shot computer control / reflection contributes to the development of LLM-based agents for digital task automation, but its limitations indicate that generalized web automation still requires stronger grounding, verification, and recovery mechanisms.

---

## Reading decision

- **Keep in S4 P2:** Yes
- **Read fully?** No, selected sections are enough unless promoted later
- **Depth needed:** Low to medium
- **Main use:** Support S4 discussion of zero-shot computer control / reflection
- **Most important parts:**
  - Abstract
  - Introduction
  - Main architecture / method figure
  - Dataset or benchmark section
  - Results table
  - Limitations / discussion

---

## One-sentence summary

A Zero-Shot Language Agent for Computer Control with Structured Reflection is a P2 supporting paper for S4 because it explains **zero-shot computer control / reflection**, but it should be cited according to its venue/status and not overused beyond its evidence.

---

## BibTeX placeholder

```bibtex
@misc{azeroshotlanguageagentforcomputerco2023,
  title = {A Zero-Shot Language Agent for Computer Control with Structured Reflection},
  year = {2023},
  note = {arXiv preprint; Preprint. Verify final bibliographic metadata before thesis submission.}
}
```


---

<!-- ========== FILE: S4_P2_paper_first_detailed_markdown_notes\S4_P2_06_GPT-4V_in_Wonderland_Large_Multimodal_Models_for_Zero-Shot_Smartphone_GUI_Navigation.md ========== -->

## Source: `S4_P2_paper_first_detailed_markdown_notes\S4_P2_06_GPT-4V_in_Wonderland_Large_Multimodal_Models_for_Zero-Shot_Smartphone_GUI_Navigation.md`

# S4 P2 Paper 06 — GPT-4V in Wonderland: Large Multimodal Models for Zero-Shot Smartphone GUI Navigation

## Metadata

- **Title:** GPT-4V in Wonderland: Large Multimodal Models for Zero-Shot Smartphone GUI Navigation
- **Year:** 2023
- **Venue / status:** arXiv preprint
- **Peer-reviewed status:** No confirmed archival venue
- **Publication type:** Preprint
- **Thesis section:** S4 — mobile GUI agents and multimodal interaction
- **Category:** multimodal smartphone GUI navigation
- **Priority:** P2
- **BibTeX key:** `gpt4vinwonderlandlargemultimodalmod2023`

---

## Simple understanding

This paper evaluates GPT-4V-style multimodal models for zero-shot smartphone GUI navigation. It is useful as an early study of vision-language models as mobile agents.

In simple terms:

```text
Problem → how can an AI agent interact with a web, GUI, mobile, desktop, or application environment?
Method → add perception, planning, action, memory, API/tool use, state tracking, or browser control.
Goal → complete real user tasks more flexibly than scripts or static chatbots.
```

This note explains the paper first, then connects it to S4 and your thesis.

---

## Core idea

Use a multimodal LLM to observe smartphone screens and choose GUI actions without task-specific training.

The paper is mainly about:

```text
multimodal smartphone GUI navigation
```

It contributes to the larger agent loop:

```text
observe → understand state → plan → act → receive feedback → verify / recover → complete task
```

---

## Key finding / main claim

Large multimodal models show promise for smartphone navigation, but still face grounding, robustness, and long-horizon interaction problems.

For S4, the important question is not only whether the method works on its benchmark, but **which part of web/GUI agency it improves**:

- perception and grounding,
- planning and reasoning,
- action execution,
- API/tool use,
- memory/state tracking,
- recovery and verification,
- or deployment/evaluation.

---

## Key evidence to extract from the paper

When reading the paper, extract these points:

- **Examples of screen observation and action prediction.**
- **Zero-shot GUI navigation results.**
- **Error analysis on visual grounding and planning failures.**

These are the most useful parts for writing a literature-review paragraph.

---

## Limitations

- **Limitation 1:** It is a preprint and should not carry strong claims alone.
- **Limitation 2:** Zero-shot performance may be sensitive to prompt design and screen complexity.
- **Limitation 3:** Smartphone GUI navigation is related to but not identical to web automation.

General thesis-level limitation:

```text
Improving one agent component is not enough for generalized web automation.
A robust web agent still needs grounding, planning, execution, verification, recovery, and safety.
```

---

## Relation to S4

This paper belongs in S4 because S4 discusses **LLM-based agents for web/GUI/mobile/computer automation**.

Its role in S4 is:

```text
GPT-4V in Wonderland: Large Multimodal Models for Zero-Shot Smartphone GUI Navigation
→ multimodal smartphone GUI navigation
→ supporting P2 source for web/GUI/computer-use agent discussion
```

Use it after explaining what the paper does. Do not introduce it only as “P2”; introduce the method or idea first.

---

## Relation to thesis topic

Your thesis topic is:

```text
LLM-based agents for generalized web automation and data extraction
```

This paper matters because:

It shows the move from text-only agents to vision-language agents that can act on screenshots.

For generalized web automation, the connection is:

```text
web / GUI / mobile / computer-use interaction
→ agent observes a digital environment
→ agent chooses actions
→ agent extracts information or completes a workflow
```

Even when the paper is not directly about data extraction, it still helps explain the automation layer needed before extraction can be generalized.

---

## How to use this paper in the literature review

Recommended use:

- Use as **P2 support**, not as the central backbone.
- Use for one precise idea, architecture, benchmark, or limitation.
- If peer-reviewed, it can support stronger claims.
- If preprint/workshop/technical report, use it for recent trends and emerging directions.

Suggested sentence:

> GPT-4V in Wonderland: Large Multimodal Models for Zero-Shot Smartphone GUI Navigation shows how multimodal smartphone GUI navigation contributes to the development of LLM-based agents for digital task automation, but its limitations indicate that generalized web automation still requires stronger grounding, verification, and recovery mechanisms.

---

## Reading decision

- **Keep in S4 P2:** Yes
- **Read fully?** No, selected sections are enough unless promoted later
- **Depth needed:** Low to medium
- **Main use:** Support S4 discussion of multimodal smartphone GUI navigation
- **Most important parts:**
  - Abstract
  - Introduction
  - Main architecture / method figure
  - Dataset or benchmark section
  - Results table
  - Limitations / discussion

---

## One-sentence summary

GPT-4V in Wonderland: Large Multimodal Models for Zero-Shot Smartphone GUI Navigation is a P2 supporting paper for S4 because it explains **multimodal smartphone GUI navigation**, but it should be cited according to its venue/status and not overused beyond its evidence.

---

## BibTeX placeholder

```bibtex
@misc{gpt4vinwonderlandlargemultimodalmod2023,
  title = {GPT-4V in Wonderland: Large Multimodal Models for Zero-Shot Smartphone GUI Navigation},
  year = {2023},
  note = {arXiv preprint; Preprint. Verify final bibliographic metadata before thesis submission.}
}
```


---

<!-- ========== FILE: S4_P2_paper_first_detailed_markdown_notes\S4_P2_07_AppAgent_Multimodal_Agents_as_Smartphone_Users.md ========== -->

## Source: `S4_P2_paper_first_detailed_markdown_notes\S4_P2_07_AppAgent_Multimodal_Agents_as_Smartphone_Users.md`

# S4 P2 Paper 07 — AppAgent: Multimodal Agents as Smartphone Users

## Metadata

- **Title:** AppAgent: Multimodal Agents as Smartphone Users
- **Year:** 2023
- **Venue / status:** arXiv preprint
- **Peer-reviewed status:** No confirmed archival venue
- **Publication type:** Preprint
- **Thesis section:** S4 — mobile GUI agents
- **Category:** smartphone agents / multimodal mobile automation
- **Priority:** P2
- **BibTeX key:** `appagentmultimodalagentsassmartphon2023`

---

## Simple understanding

AppAgent treats multimodal agents as smartphone users that can observe screens, understand tasks, and perform mobile actions.

In simple terms:

```text
Problem → how can an AI agent interact with a web, GUI, mobile, desktop, or application environment?
Method → add perception, planning, action, memory, API/tool use, state tracking, or browser control.
Goal → complete real user tasks more flexibly than scripts or static chatbots.
```

This note explains the paper first, then connects it to S4 and your thesis.

---

## Core idea

Build a mobile agent that uses screenshots, natural-language instructions, and a simplified action space to operate smartphone apps.

The paper is mainly about:

```text
smartphone agents / multimodal mobile automation
```

It contributes to the larger agent loop:

```text
observe → understand state → plan → act → receive feedback → verify / recover → complete task
```

---

## Key finding / main claim

Multimodal agents can complete smartphone tasks by combining visual perception, planning, and UI actions.

For S4, the important question is not only whether the method works on its benchmark, but **which part of web/GUI agency it improves**:

- perception and grounding,
- planning and reasoning,
- action execution,
- API/tool use,
- memory/state tracking,
- recovery and verification,
- or deployment/evaluation.

---

## Key evidence to extract from the paper

When reading the paper, extract these points:

- **Agent workflow and action space.**
- **Examples of smartphone app operation.**
- **Task success results and failure analysis.**

These are the most useful parts for writing a literature-review paragraph.

---

## Limitations

- **Limitation 1:** Preprint status; cite carefully.
- **Limitation 2:** Mobile apps differ from desktop web pages and APIs.
- **Limitation 3:** The agent may struggle with long-horizon tasks, dynamic layouts, and error recovery.

General thesis-level limitation:

```text
Improving one agent component is not enough for generalized web automation.
A robust web agent still needs grounding, planning, execution, verification, recovery, and safety.
```

---

## Relation to S4

This paper belongs in S4 because S4 discusses **LLM-based agents for web/GUI/mobile/computer automation**.

Its role in S4 is:

```text
AppAgent: Multimodal Agents as Smartphone Users
→ smartphone agents / multimodal mobile automation
→ supporting P2 source for web/GUI/computer-use agent discussion
```

Use it after explaining what the paper does. Do not introduce it only as “P2”; introduce the method or idea first.

---

## Relation to thesis topic

Your thesis topic is:

```text
LLM-based agents for generalized web automation and data extraction
```

This paper matters because:

It is a key early mobile-agent system, useful for explaining phone automation trends.

For generalized web automation, the connection is:

```text
web / GUI / mobile / computer-use interaction
→ agent observes a digital environment
→ agent chooses actions
→ agent extracts information or completes a workflow
```

Even when the paper is not directly about data extraction, it still helps explain the automation layer needed before extraction can be generalized.

---

## How to use this paper in the literature review

Recommended use:

- Use as **P2 support**, not as the central backbone.
- Use for one precise idea, architecture, benchmark, or limitation.
- If peer-reviewed, it can support stronger claims.
- If preprint/workshop/technical report, use it for recent trends and emerging directions.

Suggested sentence:

> AppAgent: Multimodal Agents as Smartphone Users shows how smartphone agents / multimodal mobile automation contributes to the development of LLM-based agents for digital task automation, but its limitations indicate that generalized web automation still requires stronger grounding, verification, and recovery mechanisms.

---

## Reading decision

- **Keep in S4 P2:** Yes
- **Read fully?** No, selected sections are enough unless promoted later
- **Depth needed:** Low to medium
- **Main use:** Support S4 discussion of smartphone agents / multimodal mobile automation
- **Most important parts:**
  - Abstract
  - Introduction
  - Main architecture / method figure
  - Dataset or benchmark section
  - Results table
  - Limitations / discussion

---

## One-sentence summary

AppAgent: Multimodal Agents as Smartphone Users is a P2 supporting paper for S4 because it explains **smartphone agents / multimodal mobile automation**, but it should be cited according to its venue/status and not overused beyond its evidence.

---

## BibTeX placeholder

```bibtex
@misc{appagentmultimodalagentsassmartphon2023,
  title = {AppAgent: Multimodal Agents as Smartphone Users},
  year = {2023},
  note = {arXiv preprint; Preprint. Verify final bibliographic metadata before thesis submission.}
}
```


---

<!-- ========== FILE: S4_P2_paper_first_detailed_markdown_notes\S4_P2_08_Mobile-Agent_Autonomous_Multi-Modal_Mobile_Device_Agent_with_Visual_Perception.md ========== -->

## Source: `S4_P2_paper_first_detailed_markdown_notes\S4_P2_08_Mobile-Agent_Autonomous_Multi-Modal_Mobile_Device_Agent_with_Visual_Perception.md`

# S4 P2 Paper 08 — Mobile-Agent: Autonomous Multi-Modal Mobile Device Agent with Visual Perception

## Metadata

- **Title:** Mobile-Agent: Autonomous Multi-Modal Mobile Device Agent with Visual Perception
- **Year:** 2024
- **Venue / status:** arXiv preprint / technical report
- **Peer-reviewed status:** No confirmed archival venue
- **Publication type:** Preprint / technical report
- **Thesis section:** S4 — mobile agents and GUI automation
- **Category:** autonomous multimodal mobile agents
- **Priority:** P2
- **BibTeX key:** `mobileagentautonomousmultimodalmobi2024`

---

## Simple understanding

Mobile-Agent is an autonomous mobile-device agent that uses visual perception to operate phone interfaces. It is a practical system showing how MLLMs can be used for mobile task automation.

In simple terms:

```text
Problem → how can an AI agent interact with a web, GUI, mobile, desktop, or application environment?
Method → add perception, planning, action, memory, API/tool use, state tracking, or browser control.
Goal → complete real user tasks more flexibly than scripts or static chatbots.
```

This note explains the paper first, then connects it to S4 and your thesis.

---

## Core idea

Use multimodal perception and action prediction to interact with mobile apps through screen observations.

The paper is mainly about:

```text
autonomous multimodal mobile agents
```

It contributes to the larger agent loop:

```text
observe → understand state → plan → act → receive feedback → verify / recover → complete task
```

---

## Key finding / main claim

The system demonstrates that visual mobile agents can perform multi-step phone tasks, but reliability remains a challenge.

For S4, the important question is not only whether the method works on its benchmark, but **which part of web/GUI agency it improves**:

- perception and grounding,
- planning and reasoning,
- action execution,
- API/tool use,
- memory/state tracking,
- recovery and verification,
- or deployment/evaluation.

---

## Key evidence to extract from the paper

When reading the paper, extract these points:

- **Mobile-agent architecture.**
- **Mobile-Eval or related benchmark results.**
- **Examples of visual perception and action execution.**

These are the most useful parts for writing a literature-review paragraph.

---

## Limitations

- **Limitation 1:** Preprint/technical-report status.
- **Limitation 2:** Mobile visual grounding is brittle under popups, layout changes, and small UI elements.
- **Limitation 3:** It is still not a general web automation solution.

General thesis-level limitation:

```text
Improving one agent component is not enough for generalized web automation.
A robust web agent still needs grounding, planning, execution, verification, recovery, and safety.
```

---

## Relation to S4

This paper belongs in S4 because S4 discusses **LLM-based agents for web/GUI/mobile/computer automation**.

Its role in S4 is:

```text
Mobile-Agent: Autonomous Multi-Modal Mobile Device Agent with Visual Perception
→ autonomous multimodal mobile agents
→ supporting P2 source for web/GUI/computer-use agent discussion
```

Use it after explaining what the paper does. Do not introduce it only as “P2”; introduce the method or idea first.

---

## Relation to thesis topic

Your thesis topic is:

```text
LLM-based agents for generalized web automation and data extraction
```

This paper matters because:

It provides a concrete mobile-agent baseline for comparing later systems like Mobile-Agent-E and Agent-SAMA.

For generalized web automation, the connection is:

```text
web / GUI / mobile / computer-use interaction
→ agent observes a digital environment
→ agent chooses actions
→ agent extracts information or completes a workflow
```

Even when the paper is not directly about data extraction, it still helps explain the automation layer needed before extraction can be generalized.

---

## How to use this paper in the literature review

Recommended use:

- Use as **P2 support**, not as the central backbone.
- Use for one precise idea, architecture, benchmark, or limitation.
- If peer-reviewed, it can support stronger claims.
- If preprint/workshop/technical report, use it for recent trends and emerging directions.

Suggested sentence:

> Mobile-Agent: Autonomous Multi-Modal Mobile Device Agent with Visual Perception shows how autonomous multimodal mobile agents contributes to the development of LLM-based agents for digital task automation, but its limitations indicate that generalized web automation still requires stronger grounding, verification, and recovery mechanisms.

---

## Reading decision

- **Keep in S4 P2:** Yes
- **Read fully?** No, selected sections are enough unless promoted later
- **Depth needed:** Low to medium
- **Main use:** Support S4 discussion of autonomous multimodal mobile agents
- **Most important parts:**
  - Abstract
  - Introduction
  - Main architecture / method figure
  - Dataset or benchmark section
  - Results table
  - Limitations / discussion

---

## One-sentence summary

Mobile-Agent: Autonomous Multi-Modal Mobile Device Agent with Visual Perception is a P2 supporting paper for S4 because it explains **autonomous multimodal mobile agents**, but it should be cited according to its venue/status and not overused beyond its evidence.

---

## BibTeX placeholder

```bibtex
@misc{mobileagentautonomousmultimodalmobi2024,
  title = {Mobile-Agent: Autonomous Multi-Modal Mobile Device Agent with Visual Perception},
  year = {2024},
  note = {arXiv preprint / technical report; Preprint / technical report. Verify final bibliographic metadata before thesis submission.}
}
```


---

<!-- ========== FILE: S4_P2_paper_first_detailed_markdown_notes\S4_P2_09_CRADLE_Empowering_Foundation_Agents_Towards_General_Computer_Control.md ========== -->

## Source: `S4_P2_paper_first_detailed_markdown_notes\S4_P2_09_CRADLE_Empowering_Foundation_Agents_Towards_General_Computer_Control.md`

# S4 P2 Paper 09 — CRADLE: Empowering Foundation Agents Towards General Computer Control

## Metadata

- **Title:** CRADLE: Empowering Foundation Agents Towards General Computer Control
- **Year:** 2024
- **Venue / status:** arXiv preprint / under review
- **Peer-reviewed status:** No
- **Publication type:** Preprint / under review
- **Thesis section:** S4 — computer-use agents
- **Category:** general computer control
- **Priority:** P2
- **BibTeX key:** `cradleempoweringfoundationagentstow2024`

---

## Simple understanding

CRADLE aims to empower foundation-model agents for general computer control. It addresses the broader problem of operating software environments beyond isolated web pages.

In simple terms:

```text
Problem → how can an AI agent interact with a web, GUI, mobile, desktop, or application environment?
Method → add perception, planning, action, memory, API/tool use, state tracking, or browser control.
Goal → complete real user tasks more flexibly than scripts or static chatbots.
```

This note explains the paper first, then connects it to S4 and your thesis.

---

## Core idea

Design an agent framework for general computer control using foundation models, perception, action, and feedback.

The paper is mainly about:

```text
general computer control
```

It contributes to the larger agent loop:

```text
observe → understand state → plan → act → receive feedback → verify / recover → complete task
```

---

## Key finding / main claim

Foundation agents can be extended toward more general computer-use tasks, but robust control remains difficult.

For S4, the important question is not only whether the method works on its benchmark, but **which part of web/GUI agency it improves**:

- perception and grounding,
- planning and reasoning,
- action execution,
- API/tool use,
- memory/state tracking,
- recovery and verification,
- or deployment/evaluation.

---

## Key evidence to extract from the paper

When reading the paper, extract these points:

- **Framework architecture for computer control.**
- **Task categories or benchmark results.**
- **Discussion of generality and limitations.**

These are the most useful parts for writing a literature-review paragraph.

---

## Limitations

- **Limitation 1:** Under-review/preprint status.
- **Limitation 2:** General computer control is broader than web automation and may include many environment-specific assumptions.
- **Limitation 3:** Reliability, safety, and reproducibility remain open concerns.

General thesis-level limitation:

```text
Improving one agent component is not enough for generalized web automation.
A robust web agent still needs grounding, planning, execution, verification, recovery, and safety.
```

---

## Relation to S4

This paper belongs in S4 because S4 discusses **LLM-based agents for web/GUI/mobile/computer automation**.

Its role in S4 is:

```text
CRADLE: Empowering Foundation Agents Towards General Computer Control
→ general computer control
→ supporting P2 source for web/GUI/computer-use agent discussion
```

Use it after explaining what the paper does. Do not introduce it only as “P2”; introduce the method or idea first.

---

## Relation to thesis topic

Your thesis topic is:

```text
LLM-based agents for generalized web automation and data extraction
```

This paper matters because:

It supports S4’s discussion of moving from web-only agents to general desktop/computer-use agents.

For generalized web automation, the connection is:

```text
web / GUI / mobile / computer-use interaction
→ agent observes a digital environment
→ agent chooses actions
→ agent extracts information or completes a workflow
```

Even when the paper is not directly about data extraction, it still helps explain the automation layer needed before extraction can be generalized.

---

## How to use this paper in the literature review

Recommended use:

- Use as **P2 support**, not as the central backbone.
- Use for one precise idea, architecture, benchmark, or limitation.
- If peer-reviewed, it can support stronger claims.
- If preprint/workshop/technical report, use it for recent trends and emerging directions.

Suggested sentence:

> CRADLE: Empowering Foundation Agents Towards General Computer Control shows how general computer control contributes to the development of LLM-based agents for digital task automation, but its limitations indicate that generalized web automation still requires stronger grounding, verification, and recovery mechanisms.

---

## Reading decision

- **Keep in S4 P2:** Yes
- **Read fully?** No, selected sections are enough unless promoted later
- **Depth needed:** Low to medium
- **Main use:** Support S4 discussion of general computer control
- **Most important parts:**
  - Abstract
  - Introduction
  - Main architecture / method figure
  - Dataset or benchmark section
  - Results table
  - Limitations / discussion

---

## One-sentence summary

CRADLE: Empowering Foundation Agents Towards General Computer Control is a P2 supporting paper for S4 because it explains **general computer control**, but it should be cited according to its venue/status and not overused beyond its evidence.

---

## BibTeX placeholder

```bibtex
@misc{cradleempoweringfoundationagentstow2024,
  title = {CRADLE: Empowering Foundation Agents Towards General Computer Control},
  year = {2024},
  note = {arXiv preprint / under review; Preprint / under review. Verify final bibliographic metadata before thesis submission.}
}
```


---

<!-- ========== FILE: S4_P2_paper_first_detailed_markdown_notes\S4_P2_10_ChatShop_Interactive_Information_Seeking_with_Language_Agents.md ========== -->

## Source: `S4_P2_paper_first_detailed_markdown_notes\S4_P2_10_ChatShop_Interactive_Information_Seeking_with_Language_Agents.md`

# S4 P2 Paper 10 — ChatShop: Interactive Information Seeking with Language Agents

## Metadata

- **Title:** ChatShop: Interactive Information Seeking with Language Agents
- **Year:** 2024
- **Venue / status:** arXiv preprint
- **Peer-reviewed status:** No confirmed archival venue
- **Publication type:** Preprint
- **Thesis section:** S4 — web agents for information seeking and e-commerce
- **Category:** interactive product search / shopping agents
- **Priority:** P2
- **BibTeX key:** `chatshopinteractiveinformationseeki2024`

---

## Simple understanding

ChatShop studies language agents for interactive information seeking, especially shopping or product-related search scenarios.

In simple terms:

```text
Problem → how can an AI agent interact with a web, GUI, mobile, desktop, or application environment?
Method → add perception, planning, action, memory, API/tool use, state tracking, or browser control.
Goal → complete real user tasks more flexibly than scripts or static chatbots.
```

This note explains the paper first, then connects it to S4 and your thesis.

---

## Core idea

Use a language agent to iteratively ask, search, refine, and retrieve information to satisfy user shopping/information needs.

The paper is mainly about:

```text
interactive product search / shopping agents
```

It contributes to the larger agent loop:

```text
observe → understand state → plan → act → receive feedback → verify / recover → complete task
```

---

## Key finding / main claim

Interactive agents can improve information seeking by engaging in multi-turn clarification and search.

For S4, the important question is not only whether the method works on its benchmark, but **which part of web/GUI agency it improves**:

- perception and grounding,
- planning and reasoning,
- action execution,
- API/tool use,
- memory/state tracking,
- recovery and verification,
- or deployment/evaluation.

---

## Key evidence to extract from the paper

When reading the paper, extract these points:

- **Interactive search protocol.**
- **Product-search or shopping evaluation.**
- **User/task examples showing clarification and search behavior.**

These are the most useful parts for writing a literature-review paragraph.

---

## Limitations

- **Limitation 1:** Preprint status.
- **Limitation 2:** Shopping/product tasks may not generalize to all web automation tasks.
- **Limitation 3:** Information seeking is different from executing high-stakes web actions.

General thesis-level limitation:

```text
Improving one agent component is not enough for generalized web automation.
A robust web agent still needs grounding, planning, execution, verification, recovery, and safety.
```

---

## Relation to S4

This paper belongs in S4 because S4 discusses **LLM-based agents for web/GUI/mobile/computer automation**.

Its role in S4 is:

```text
ChatShop: Interactive Information Seeking with Language Agents
→ interactive product search / shopping agents
→ supporting P2 source for web/GUI/computer-use agent discussion
```

Use it after explaining what the paper does. Do not introduce it only as “P2”; introduce the method or idea first.

---

## Relation to thesis topic

Your thesis topic is:

```text
LLM-based agents for generalized web automation and data extraction
```

This paper matters because:

It connects web agents with interactive search and product-oriented web tasks.

For generalized web automation, the connection is:

```text
web / GUI / mobile / computer-use interaction
→ agent observes a digital environment
→ agent chooses actions
→ agent extracts information or completes a workflow
```

Even when the paper is not directly about data extraction, it still helps explain the automation layer needed before extraction can be generalized.

---

## How to use this paper in the literature review

Recommended use:

- Use as **P2 support**, not as the central backbone.
- Use for one precise idea, architecture, benchmark, or limitation.
- If peer-reviewed, it can support stronger claims.
- If preprint/workshop/technical report, use it for recent trends and emerging directions.

Suggested sentence:

> ChatShop: Interactive Information Seeking with Language Agents shows how interactive product search / shopping agents contributes to the development of LLM-based agents for digital task automation, but its limitations indicate that generalized web automation still requires stronger grounding, verification, and recovery mechanisms.

---

## Reading decision

- **Keep in S4 P2:** Yes
- **Read fully?** No, selected sections are enough unless promoted later
- **Depth needed:** Low to medium
- **Main use:** Support S4 discussion of interactive product search / shopping agents
- **Most important parts:**
  - Abstract
  - Introduction
  - Main architecture / method figure
  - Dataset or benchmark section
  - Results table
  - Limitations / discussion

---

## One-sentence summary

ChatShop: Interactive Information Seeking with Language Agents is a P2 supporting paper for S4 because it explains **interactive product search / shopping agents**, but it should be cited according to its venue/status and not overused beyond its evidence.

---

## BibTeX placeholder

```bibtex
@misc{chatshopinteractiveinformationseeki2024,
  title = {ChatShop: Interactive Information Seeking with Language Agents},
  year = {2024},
  note = {arXiv preprint; Preprint. Verify final bibliographic metadata before thesis submission.}
}
```


---

<!-- ========== FILE: S4_P2_paper_first_detailed_markdown_notes\S4_P2_11_Grounded_Language_Agent_for_Product_Search_via_Intelligent_Web_Interactions.md ========== -->

## Source: `S4_P2_paper_first_detailed_markdown_notes\S4_P2_11_Grounded_Language_Agent_for_Product_Search_via_Intelligent_Web_Interactions.md`

# S4 P2 Paper 11 — Grounded Language Agent for Product Search via Intelligent Web Interactions

## Metadata

- **Title:** Grounded Language Agent for Product Search via Intelligent Web Interactions
- **Year:** 2024
- **Venue / status:** ACL Workshop CustomNLP4U 2024
- **Peer-reviewed status:** Yes, workshop
- **Publication type:** Workshop paper
- **Thesis section:** S4 — domain-specific web agents
- **Category:** grounded product-search web agent
- **Priority:** P2
- **BibTeX key:** `groundedlanguageagentforproductsear2024`

---

## Simple understanding

This paper proposes a grounded language agent for product search using intelligent web interactions. It is a domain-specific web-agent paper focused on e-commerce/product search.

In simple terms:

```text
Problem → how can an AI agent interact with a web, GUI, mobile, desktop, or application environment?
Method → add perception, planning, action, memory, API/tool use, state tracking, or browser control.
Goal → complete real user tasks more flexibly than scripts or static chatbots.
```

This note explains the paper first, then connects it to S4 and your thesis.

---

## Core idea

Train or design an agent that searches, navigates, and interacts with product pages to satisfy user product-search goals.

The paper is mainly about:

```text
grounded product-search web agent
```

It contributes to the larger agent loop:

```text
observe → understand state → plan → act → receive feedback → verify / recover → complete task
```

---

## Key finding / main claim

Grounded web interactions can improve product search by allowing agents to inspect and act within web environments rather than only rank static results.

For S4, the important question is not only whether the method works on its benchmark, but **which part of web/GUI agency it improves**:

- perception and grounding,
- planning and reasoning,
- action execution,
- API/tool use,
- memory/state tracking,
- recovery and verification,
- or deployment/evaluation.

---

## Key evidence to extract from the paper

When reading the paper, extract these points:

- **Agent architecture for product search.**
- **Web interaction/action design.**
- **Experimental comparison on product-search tasks.**

These are the most useful parts for writing a literature-review paragraph.

---

## Limitations

- **Limitation 1:** Workshop venue is useful but weaker than a main conference paper.
- **Limitation 2:** Product search is narrower than generalized web automation.
- **Limitation 3:** Evaluation may depend on WebShop-like assumptions.

General thesis-level limitation:

```text
Improving one agent component is not enough for generalized web automation.
A robust web agent still needs grounding, planning, execution, verification, recovery, and safety.
```

---

## Relation to S4

This paper belongs in S4 because S4 discusses **LLM-based agents for web/GUI/mobile/computer automation**.

Its role in S4 is:

```text
Grounded Language Agent for Product Search via Intelligent Web Interactions
→ grounded product-search web agent
→ supporting P2 source for web/GUI/computer-use agent discussion
```

Use it after explaining what the paper does. Do not introduce it only as “P2”; introduce the method or idea first.

---

## Relation to thesis topic

Your thesis topic is:

```text
LLM-based agents for generalized web automation and data extraction
```

This paper matters because:

It is useful for showing how web agents specialize in e-commerce and information-seeking tasks.

For generalized web automation, the connection is:

```text
web / GUI / mobile / computer-use interaction
→ agent observes a digital environment
→ agent chooses actions
→ agent extracts information or completes a workflow
```

Even when the paper is not directly about data extraction, it still helps explain the automation layer needed before extraction can be generalized.

---

## How to use this paper in the literature review

Recommended use:

- Use as **P2 support**, not as the central backbone.
- Use for one precise idea, architecture, benchmark, or limitation.
- If peer-reviewed, it can support stronger claims.
- If preprint/workshop/technical report, use it for recent trends and emerging directions.

Suggested sentence:

> Grounded Language Agent for Product Search via Intelligent Web Interactions shows how grounded product-search web agent contributes to the development of LLM-based agents for digital task automation, but its limitations indicate that generalized web automation still requires stronger grounding, verification, and recovery mechanisms.

---

## Reading decision

- **Keep in S4 P2:** Yes
- **Read fully?** Yes or selected sections carefully
- **Depth needed:** Medium to high
- **Main use:** Support S4 discussion of grounded product-search web agent
- **Most important parts:**
  - Abstract
  - Introduction
  - Main architecture / method figure
  - Dataset or benchmark section
  - Results table
  - Limitations / discussion

---

## One-sentence summary

Grounded Language Agent for Product Search via Intelligent Web Interactions is a P2 supporting paper for S4 because it explains **grounded product-search web agent**, but it should be cited according to its venue/status and not overused beyond its evidence.

---

## BibTeX placeholder

```bibtex
@misc{groundedlanguageagentforproductsear2024,
  title = {Grounded Language Agent for Product Search via Intelligent Web Interactions},
  year = {2024},
  note = {ACL Workshop CustomNLP4U 2024; Workshop paper. Verify final bibliographic metadata before thesis submission.}
}
```


---

<!-- ========== FILE: S4_P2_paper_first_detailed_markdown_notes\S4_P2_12_Automating_the_Enterprise_with_Foundation_Models.md ========== -->

## Source: `S4_P2_paper_first_detailed_markdown_notes\S4_P2_12_Automating_the_Enterprise_with_Foundation_Models.md`

# S4 P2 Paper 12 — Automating the Enterprise with Foundation Models

## Metadata

- **Title:** Automating the Enterprise with Foundation Models
- **Year:** 2024
- **Venue / status:** arXiv preprint
- **Peer-reviewed status:** No confirmed archival venue
- **Publication type:** Preprint
- **Thesis section:** S4 — enterprise web/computer automation
- **Category:** enterprise automation / foundation-model agents
- **Priority:** P2
- **BibTeX key:** `automatingtheenterprisewithfoundati2024`

---

## Simple understanding

This paper discusses enterprise automation using foundation models. It is useful for comparing LLM agents with classical RPA and workflow automation.

In simple terms:

```text
Problem → how can an AI agent interact with a web, GUI, mobile, desktop, or application environment?
Method → add perception, planning, action, memory, API/tool use, state tracking, or browser control.
Goal → complete real user tasks more flexibly than scripts or static chatbots.
```

This note explains the paper first, then connects it to S4 and your thesis.

---

## Core idea

Use foundation models to automate enterprise workflows that traditionally require scripts, APIs, or RPA.

The paper is mainly about:

```text
enterprise automation / foundation-model agents
```

It contributes to the larger agent loop:

```text
observe → understand state → plan → act → receive feedback → verify / recover → complete task
```

---

## Key finding / main claim

Foundation models can reduce manual development effort, but enterprise automation demands reliability, governance, and integration with existing systems.

For S4, the important question is not only whether the method works on its benchmark, but **which part of web/GUI agency it improves**:

- perception and grounding,
- planning and reasoning,
- action execution,
- API/tool use,
- memory/state tracking,
- recovery and verification,
- or deployment/evaluation.

---

## Key evidence to extract from the paper

When reading the paper, extract these points:

- **Enterprise automation use cases.**
- **Architecture or workflow examples.**
- **Comparison with RPA or traditional automation.**

These are the most useful parts for writing a literature-review paragraph.

---

## Limitations

- **Limitation 1:** Preprint status.
- **Limitation 2:** Enterprise settings are high-stakes and require stronger reliability than most research benchmarks.
- **Limitation 3:** The paper may be more vision/system-oriented than a rigorously evaluated benchmark paper.

General thesis-level limitation:

```text
Improving one agent component is not enough for generalized web automation.
A robust web agent still needs grounding, planning, execution, verification, recovery, and safety.
```

---

## Relation to S4

This paper belongs in S4 because S4 discusses **LLM-based agents for web/GUI/mobile/computer automation**.

Its role in S4 is:

```text
Automating the Enterprise with Foundation Models
→ enterprise automation / foundation-model agents
→ supporting P2 source for web/GUI/computer-use agent discussion
```

Use it after explaining what the paper does. Do not introduce it only as “P2”; introduce the method or idea first.

---

## Relation to thesis topic

Your thesis topic is:

```text
LLM-based agents for generalized web automation and data extraction
```

This paper matters because:

It helps position LLM agents in relation to RPA and business workflow automation.

For generalized web automation, the connection is:

```text
web / GUI / mobile / computer-use interaction
→ agent observes a digital environment
→ agent chooses actions
→ agent extracts information or completes a workflow
```

Even when the paper is not directly about data extraction, it still helps explain the automation layer needed before extraction can be generalized.

---

## How to use this paper in the literature review

Recommended use:

- Use as **P2 support**, not as the central backbone.
- Use for one precise idea, architecture, benchmark, or limitation.
- If peer-reviewed, it can support stronger claims.
- If preprint/workshop/technical report, use it for recent trends and emerging directions.

Suggested sentence:

> Automating the Enterprise with Foundation Models shows how enterprise automation / foundation-model agents contributes to the development of LLM-based agents for digital task automation, but its limitations indicate that generalized web automation still requires stronger grounding, verification, and recovery mechanisms.

---

## Reading decision

- **Keep in S4 P2:** Yes
- **Read fully?** No, selected sections are enough unless promoted later
- **Depth needed:** Low to medium
- **Main use:** Support S4 discussion of enterprise automation / foundation-model agents
- **Most important parts:**
  - Abstract
  - Introduction
  - Main architecture / method figure
  - Dataset or benchmark section
  - Results table
  - Limitations / discussion

---

## One-sentence summary

Automating the Enterprise with Foundation Models is a P2 supporting paper for S4 because it explains **enterprise automation / foundation-model agents**, but it should be cited according to its venue/status and not overused beyond its evidence.

---

## BibTeX placeholder

```bibtex
@misc{automatingtheenterprisewithfoundati2024,
  title = {Automating the Enterprise with Foundation Models},
  year = {2024},
  note = {arXiv preprint; Preprint. Verify final bibliographic metadata before thesis submission.}
}
```


---

<!-- ========== FILE: S4_P2_paper_first_detailed_markdown_notes\S4_P2_13_OpenWebAgent_An_Open_Toolkit_to_Enable_Web_Agents_on_Large_Language_Models.md ========== -->

## Source: `S4_P2_paper_first_detailed_markdown_notes\S4_P2_13_OpenWebAgent_An_Open_Toolkit_to_Enable_Web_Agents_on_Large_Language_Models.md`

# S4 P2 Paper 13 — OpenWebAgent: An Open Toolkit to Enable Web Agents on Large Language Models

## Metadata

- **Title:** OpenWebAgent: An Open Toolkit to Enable Web Agents on Large Language Models
- **Year:** 2024
- **Venue / status:** ACL 2024 System Demonstrations
- **Peer-reviewed status:** Yes, demo
- **Publication type:** System demonstration paper
- **Thesis section:** S4 — web-agent frameworks and toolkits
- **Category:** open web-agent toolkit
- **Priority:** P2
- **BibTeX key:** `openwebagentanopentoolkittoenablewe2024`

---

## Simple understanding

OpenWebAgent is an open toolkit for building web agents on top of LLMs. It provides infrastructure for web interaction, agent execution, and evaluation.

In simple terms:

```text
Problem → how can an AI agent interact with a web, GUI, mobile, desktop, or application environment?
Method → add perception, planning, action, memory, API/tool use, state tracking, or browser control.
Goal → complete real user tasks more flexibly than scripts or static chatbots.
```

This note explains the paper first, then connects it to S4 and your thesis.

---

## Core idea

Offer a reusable toolkit that enables LLMs to interact with websites as agents.

The paper is mainly about:

```text
open web-agent toolkit
```

It contributes to the larger agent loop:

```text
observe → understand state → plan → act → receive feedback → verify / recover → complete task
```

---

## Key finding / main claim

Open tooling helps standardize and accelerate web-agent research by making browser interaction and evaluation more accessible.

For S4, the important question is not only whether the method works on its benchmark, but **which part of web/GUI agency it improves**:

- perception and grounding,
- planning and reasoning,
- action execution,
- API/tool use,
- memory/state tracking,
- recovery and verification,
- or deployment/evaluation.

---

## Key evidence to extract from the paper

When reading the paper, extract these points:

- **Toolkit architecture.**
- **Supported web-agent components.**
- **Demonstration or evaluation examples.**

These are the most useful parts for writing a literature-review paragraph.

---

## Limitations

- **Limitation 1:** System demo papers are useful for tooling, but not always strong empirical evidence.
- **Limitation 2:** Toolkit performance depends on the underlying model and task setup.
- **Limitation 3:** It is infrastructure, not a single definitive agent algorithm.

General thesis-level limitation:

```text
Improving one agent component is not enough for generalized web automation.
A robust web agent still needs grounding, planning, execution, verification, recovery, and safety.
```

---

## Relation to S4

This paper belongs in S4 because S4 discusses **LLM-based agents for web/GUI/mobile/computer automation**.

Its role in S4 is:

```text
OpenWebAgent: An Open Toolkit to Enable Web Agents on Large Language Models
→ open web-agent toolkit
→ supporting P2 source for web/GUI/computer-use agent discussion
```

Use it after explaining what the paper does. Do not introduce it only as “P2”; introduce the method or idea first.

---

## Relation to thesis topic

Your thesis topic is:

```text
LLM-based agents for generalized web automation and data extraction
```

This paper matters because:

It is a strong practical reference for open web-agent infrastructure.

For generalized web automation, the connection is:

```text
web / GUI / mobile / computer-use interaction
→ agent observes a digital environment
→ agent chooses actions
→ agent extracts information or completes a workflow
```

Even when the paper is not directly about data extraction, it still helps explain the automation layer needed before extraction can be generalized.

---

## How to use this paper in the literature review

Recommended use:

- Use as **P2 support**, not as the central backbone.
- Use for one precise idea, architecture, benchmark, or limitation.
- If peer-reviewed, it can support stronger claims.
- If preprint/workshop/technical report, use it for recent trends and emerging directions.

Suggested sentence:

> OpenWebAgent: An Open Toolkit to Enable Web Agents on Large Language Models shows how open web-agent toolkit contributes to the development of LLM-based agents for digital task automation, but its limitations indicate that generalized web automation still requires stronger grounding, verification, and recovery mechanisms.

---

## Reading decision

- **Keep in S4 P2:** Yes
- **Read fully?** Yes or selected sections carefully
- **Depth needed:** Medium to high
- **Main use:** Support S4 discussion of open web-agent toolkit
- **Most important parts:**
  - Abstract
  - Introduction
  - Main architecture / method figure
  - Dataset or benchmark section
  - Results table
  - Limitations / discussion

---

## One-sentence summary

OpenWebAgent: An Open Toolkit to Enable Web Agents on Large Language Models is a P2 supporting paper for S4 because it explains **open web-agent toolkit**, but it should be cited according to its venue/status and not overused beyond its evidence.

---

## BibTeX placeholder

```bibtex
@misc{openwebagentanopentoolkittoenablewe2024,
  title = {OpenWebAgent: An Open Toolkit to Enable Web Agents on Large Language Models},
  year = {2024},
  note = {ACL 2024 System Demonstrations; System demonstration paper. Verify final bibliographic metadata before thesis submission.}
}
```


---

<!-- ========== FILE: S4_P2_paper_first_detailed_markdown_notes\S4_P2_14_Steward_Natural_Language_Web_Automation.md ========== -->

## Source: `S4_P2_paper_first_detailed_markdown_notes\S4_P2_14_Steward_Natural_Language_Web_Automation.md`

# S4 P2 Paper 14 — Steward: Natural Language Web Automation

## Metadata

- **Title:** Steward: Natural Language Web Automation
- **Year:** 2024
- **Venue / status:** arXiv preprint
- **Peer-reviewed status:** No confirmed archival venue
- **Publication type:** Preprint
- **Thesis section:** S4 — natural-language web automation
- **Category:** natural-language web automation
- **Priority:** P2
- **BibTeX key:** `stewardnaturallanguagewebautomation2024`

---

## Simple understanding

Steward is an LLM-powered web automation tool that takes natural-language tasks and executes browser actions through Playwright. It focuses on cost, runtime, action selection, and real website automation.

In simple terms:

```text
Problem → how can an AI agent interact with a web, GUI, mobile, desktop, or application environment?
Method → add perception, planning, action, memory, API/tool use, state tracking, or browser control.
Goal → complete real user tasks more flexibly than scripts or static chatbots.
```

This note explains the paper first, then connects it to S4 and your thesis.

---

## Core idea

Represent webpage state and use an LLM to iteratively select UI actions until a natural-language task is completed.

The paper is mainly about:

```text
natural-language web automation
```

It contributes to the larger agent loop:

```text
observe → understand state → plan → act → receive feedback → verify / recover → complete task
```

---

## Key finding / main claim

Steward reports practical execution on real websites, including top-1 action-element selection accuracy and task completion rates, while analyzing runtime/cost tradeoffs.

For S4, the important question is not only whether the method works on its benchmark, but **which part of web/GUI agency it improves**:

- perception and grounding,
- planning and reasoning,
- action execution,
- API/tool use,
- memory/state tracking,
- recovery and verification,
- or deployment/evaluation.

---

## Key evidence to extract from the paper

When reading the paper, extract these points:

- **Figure 1 showing iterative UI action selection.**
- **Reported metrics: 81.44% top-1 action+element selection for top elements, 46.70% per-step accuracy on Mind2Web, and 40% task completion.**
- **Runtime/cost analysis and caching mechanism.**

These are the most useful parts for writing a literature-review paragraph.

---

## Limitations

- **Limitation 1:** Preprint status.
- **Limitation 2:** Reported task completion on real websites is still limited and failures occur on long-horizon tasks.
- **Limitation 3:** State representation, completion detection, and UI drift remain difficult.

General thesis-level limitation:

```text
Improving one agent component is not enough for generalized web automation.
A robust web agent still needs grounding, planning, execution, verification, recovery, and safety.
```

---

## Relation to S4

This paper belongs in S4 because S4 discusses **LLM-based agents for web/GUI/mobile/computer automation**.

Its role in S4 is:

```text
Steward: Natural Language Web Automation
→ natural-language web automation
→ supporting P2 source for web/GUI/computer-use agent discussion
```

Use it after explaining what the paper does. Do not introduce it only as “P2”; introduce the method or idea first.

---

## Relation to thesis topic

Your thesis topic is:

```text
LLM-based agents for generalized web automation and data extraction
```

This paper matters because:

It is directly relevant to your thesis because it targets natural-language web automation with LLMs and browser automation.

For generalized web automation, the connection is:

```text
web / GUI / mobile / computer-use interaction
→ agent observes a digital environment
→ agent chooses actions
→ agent extracts information or completes a workflow
```

Even when the paper is not directly about data extraction, it still helps explain the automation layer needed before extraction can be generalized.

---

## How to use this paper in the literature review

Recommended use:

- Use as **P2 support**, not as the central backbone.
- Use for one precise idea, architecture, benchmark, or limitation.
- If peer-reviewed, it can support stronger claims.
- If preprint/workshop/technical report, use it for recent trends and emerging directions.

Suggested sentence:

> Steward: Natural Language Web Automation shows how natural-language web automation contributes to the development of LLM-based agents for digital task automation, but its limitations indicate that generalized web automation still requires stronger grounding, verification, and recovery mechanisms.

---

## Reading decision

- **Keep in S4 P2:** Yes
- **Read fully?** No, selected sections are enough unless promoted later
- **Depth needed:** Low to medium
- **Main use:** Support S4 discussion of natural-language web automation
- **Most important parts:**
  - Abstract
  - Introduction
  - Main architecture / method figure
  - Dataset or benchmark section
  - Results table
  - Limitations / discussion

---

## One-sentence summary

Steward: Natural Language Web Automation is a P2 supporting paper for S4 because it explains **natural-language web automation**, but it should be cited according to its venue/status and not overused beyond its evidence.

---

## BibTeX placeholder

```bibtex
@misc{stewardnaturallanguagewebautomation2024,
  title = {Steward: Natural Language Web Automation},
  year = {2024},
  note = {arXiv preprint; Preprint. Verify final bibliographic metadata before thesis submission.}
}
```


---

<!-- ========== FILE: S4_P2_paper_first_detailed_markdown_notes\S4_P2_15_AXIS_Efficient_Human-Agent-Computer_Interaction_with_API-First_LLM-Based_Agents.md ========== -->

## Source: `S4_P2_paper_first_detailed_markdown_notes\S4_P2_15_AXIS_Efficient_Human-Agent-Computer_Interaction_with_API-First_LLM-Based_Agents.md`

# S4 P2 Paper 15 — AXIS: Efficient Human-Agent-Computer Interaction with API-First LLM-Based Agents

## Metadata

- **Title:** AXIS: Efficient Human-Agent-Computer Interaction with API-First LLM-Based Agents
- **Year:** 2024/2025
- **Venue / status:** arXiv preprint
- **Peer-reviewed status:** No confirmed archival venue
- **Publication type:** Preprint
- **Thesis section:** S4 — API-first / hybrid web and computer agents
- **Category:** API-first GUI/computer agents
- **Priority:** P2
- **BibTeX key:** `axisefficienthumanagentcomputerinte2024/2025`

---

## Simple understanding

AXIS argues that LLM-based agents should prioritize APIs over human-like UI actions. It proposes an API-first framework for human-agent-computer interaction.

In simple terms:

```text
Problem → how can an AI agent interact with a web, GUI, mobile, desktop, or application environment?
Method → add perception, planning, action, memory, API/tool use, state tracking, or browser control.
Goal → complete real user tasks more flexibly than scripts or static chatbots.
```

This note explains the paper first, then connects it to S4 and your thesis.

---

## Core idea

Replace long sequential UI interactions with API calls where possible, while using UI actions only when APIs are unavailable.

The paper is mainly about:

```text
API-first GUI/computer agents
```

It contributes to the larger agent loop:

```text
observe → understand state → plan → act → receive feedback → verify / recover → complete task
```

---

## Key finding / main claim

On Microsoft Word tasks, AXIS reports large reductions in completion time and cognitive workload while maintaining high accuracy compared with humans.

For S4, the important question is not only whether the method works on its benchmark, but **which part of web/GUI agency it improves**:

- perception and grounding,
- planning and reasoning,
- action execution,
- API/tool use,
- memory/state tracking,
- recovery and verification,
- or deployment/evaluation.

---

## Key evidence to extract from the paper

When reading the paper, extract these points:

- **Figure 1 comparing manual operation, UI Agent, and AXIS API-call trajectory.**
- **Reported 65–70% task completion time reduction and 97–98% accuracy compared to humans.**
- **Discussion of HACI and Agent OS design.**

These are the most useful parts for writing a literature-review paragraph.

---

## Limitations

- **Limitation 1:** Preprint status.
- **Limitation 2:** Experiments focus on Microsoft Word, not the open web broadly.
- **Limitation 3:** API availability and documentation quality strongly determine effectiveness.

General thesis-level limitation:

```text
Improving one agent component is not enough for generalized web automation.
A robust web agent still needs grounding, planning, execution, verification, recovery, and safety.
```

---

## Relation to S4

This paper belongs in S4 because S4 discusses **LLM-based agents for web/GUI/mobile/computer automation**.

Its role in S4 is:

```text
AXIS: Efficient Human-Agent-Computer Interaction with API-First LLM-Based Agents
→ API-first GUI/computer agents
→ supporting P2 source for web/GUI/computer-use agent discussion
```

Use it after explaining what the paper does. Do not introduce it only as “P2”; introduce the method or idea first.

---

## Relation to thesis topic

Your thesis topic is:

```text
LLM-based agents for generalized web automation and data extraction
```

This paper matters because:

It supports a key S4 argument: agents should not always imitate human UI interaction when machine-native APIs are available.

For generalized web automation, the connection is:

```text
web / GUI / mobile / computer-use interaction
→ agent observes a digital environment
→ agent chooses actions
→ agent extracts information or completes a workflow
```

Even when the paper is not directly about data extraction, it still helps explain the automation layer needed before extraction can be generalized.

---

## How to use this paper in the literature review

Recommended use:

- Use as **P2 support**, not as the central backbone.
- Use for one precise idea, architecture, benchmark, or limitation.
- If peer-reviewed, it can support stronger claims.
- If preprint/workshop/technical report, use it for recent trends and emerging directions.

Suggested sentence:

> AXIS: Efficient Human-Agent-Computer Interaction with API-First LLM-Based Agents shows how API-first GUI/computer agents contributes to the development of LLM-based agents for digital task automation, but its limitations indicate that generalized web automation still requires stronger grounding, verification, and recovery mechanisms.

---

## Reading decision

- **Keep in S4 P2:** Yes
- **Read fully?** No, selected sections are enough unless promoted later
- **Depth needed:** Low to medium
- **Main use:** Support S4 discussion of API-first GUI/computer agents
- **Most important parts:**
  - Abstract
  - Introduction
  - Main architecture / method figure
  - Dataset or benchmark section
  - Results table
  - Limitations / discussion

---

## One-sentence summary

AXIS: Efficient Human-Agent-Computer Interaction with API-First LLM-Based Agents is a P2 supporting paper for S4 because it explains **API-first GUI/computer agents**, but it should be cited according to its venue/status and not overused beyond its evidence.

---

## BibTeX placeholder

```bibtex
@misc{axisefficienthumanagentcomputerinte2024/2025,
  title = {AXIS: Efficient Human-Agent-Computer Interaction with API-First LLM-Based Agents},
  year = {2024/2025},
  note = {arXiv preprint; Preprint. Verify final bibliographic metadata before thesis submission.}
}
```


---

<!-- ========== FILE: S4_P2_paper_first_detailed_markdown_notes\S4_P2_16_Foundations_and_Recent_Trends_in_Multimodal_Mobile_Agents_A_Survey.md ========== -->

## Source: `S4_P2_paper_first_detailed_markdown_notes\S4_P2_16_Foundations_and_Recent_Trends_in_Multimodal_Mobile_Agents_A_Survey.md`

# S4 P2 Paper 16 — Foundations and Recent Trends in Multimodal Mobile Agents: A Survey

## Metadata

- **Title:** Foundations and Recent Trends in Multimodal Mobile Agents: A Survey
- **Year:** 2024/2025
- **Venue / status:** arXiv survey
- **Peer-reviewed status:** No confirmed archival venue
- **Publication type:** Survey preprint
- **Thesis section:** S4 — mobile/GUI agent taxonomy
- **Category:** multimodal mobile-agent survey
- **Priority:** P2
- **BibTeX key:** `foundationsandrecenttrendsinmultimo2024/2025`

---

## Simple understanding

This survey reviews multimodal mobile agents, including prompt-based and training-based methods, benchmarks, components, and challenges.

In simple terms:

```text
Problem → how can an AI agent interact with a web, GUI, mobile, desktop, or application environment?
Method → add perception, planning, action, memory, API/tool use, state tracking, or browser control.
Goal → complete real user tasks more flexibly than scripts or static chatbots.
```

This note explains the paper first, then connects it to S4 and your thesis.

---

## Core idea

Organize mobile-agent research around perception, planning, action, memory, benchmarks, and deployment tradeoffs.

The paper is mainly about:

```text
multimodal mobile-agent survey
```

It contributes to the larger agent loop:

```text
observe → understand state → plan → act → receive feedback → verify / recover → complete task
```

---

## Key finding / main claim

Mobile agents are moving from prompt-based LLM control to multimodal/training-based systems, but resource efficiency, robustness, and realistic evaluation remain open.

For S4, the important question is not only whether the method works on its benchmark, but **which part of web/GUI agency it improves**:

- perception and grounding,
- planning and reasoning,
- action execution,
- API/tool use,
- memory/state tracking,
- recovery and verification,
- or deployment/evaluation.

---

## Key evidence to extract from the paper

When reading the paper, extract these points:

- **Section 2 taxonomy: perception, planning, action, memory.**
- **Distinction between prompt-based and training-based methods.**
- **Discussion of deployment cost and effectiveness.**

These are the most useful parts for writing a literature-review paragraph.

---

## Limitations

- **Limitation 1:** Survey preprint, not a primary empirical source.
- **Limitation 2:** It focuses on mobile agents, not all web agents.
- **Limitation 3:** Use mainly for taxonomy and background.

General thesis-level limitation:

```text
Improving one agent component is not enough for generalized web automation.
A robust web agent still needs grounding, planning, execution, verification, recovery, and safety.
```

---

## Relation to S4

This paper belongs in S4 because S4 discusses **LLM-based agents for web/GUI/mobile/computer automation**.

Its role in S4 is:

```text
Foundations and Recent Trends in Multimodal Mobile Agents: A Survey
→ multimodal mobile-agent survey
→ supporting P2 source for web/GUI/computer-use agent discussion
```

Use it after explaining what the paper does. Do not introduce it only as “P2”; introduce the method or idea first.

---

## Relation to thesis topic

Your thesis topic is:

```text
LLM-based agents for generalized web automation and data extraction
```

This paper matters because:

It gives a useful taxonomy for organizing phone/mobile agent systems in S4.

For generalized web automation, the connection is:

```text
web / GUI / mobile / computer-use interaction
→ agent observes a digital environment
→ agent chooses actions
→ agent extracts information or completes a workflow
```

Even when the paper is not directly about data extraction, it still helps explain the automation layer needed before extraction can be generalized.

---

## How to use this paper in the literature review

Recommended use:

- Use as **P2 support**, not as the central backbone.
- Use for one precise idea, architecture, benchmark, or limitation.
- If peer-reviewed, it can support stronger claims.
- If preprint/workshop/technical report, use it for recent trends and emerging directions.

Suggested sentence:

> Foundations and Recent Trends in Multimodal Mobile Agents: A Survey shows how multimodal mobile-agent survey contributes to the development of LLM-based agents for digital task automation, but its limitations indicate that generalized web automation still requires stronger grounding, verification, and recovery mechanisms.

---

## Reading decision

- **Keep in S4 P2:** Yes
- **Read fully?** No, selected sections are enough unless promoted later
- **Depth needed:** Low to medium
- **Main use:** Support S4 discussion of multimodal mobile-agent survey
- **Most important parts:**
  - Abstract
  - Introduction
  - Main architecture / method figure
  - Dataset or benchmark section
  - Results table
  - Limitations / discussion

---

## One-sentence summary

Foundations and Recent Trends in Multimodal Mobile Agents: A Survey is a P2 supporting paper for S4 because it explains **multimodal mobile-agent survey**, but it should be cited according to its venue/status and not overused beyond its evidence.

---

## BibTeX placeholder

```bibtex
@misc{foundationsandrecenttrendsinmultimo2024/2025,
  title = {Foundations and Recent Trends in Multimodal Mobile Agents: A Survey},
  year = {2024/2025},
  note = {arXiv survey; Survey preprint. Verify final bibliographic metadata before thesis submission.}
}
```


---

<!-- ========== FILE: S4_P2_paper_first_detailed_markdown_notes\S4_P2_17_The_Dawn_of_GUI_Agent_A_Preliminary_Case_Study_with_Claude_3.5_Computer_Use.md ========== -->

## Source: `S4_P2_paper_first_detailed_markdown_notes\S4_P2_17_The_Dawn_of_GUI_Agent_A_Preliminary_Case_Study_with_Claude_3.5_Computer_Use.md`

# S4 P2 Paper 17 — The Dawn of GUI Agent: A Preliminary Case Study with Claude 3.5 Computer Use

## Metadata

- **Title:** The Dawn of GUI Agent: A Preliminary Case Study with Claude 3.5 Computer Use
- **Year:** 2024
- **Venue / status:** arXiv preprint / under review
- **Peer-reviewed status:** No
- **Publication type:** Preprint / case study
- **Thesis section:** S4 — GUI/computer-use agents
- **Category:** GUI agent case study / Claude computer use
- **Priority:** P2
- **BibTeX key:** `thedawnofguiagentapreliminarycasest2024`

---

## Simple understanding

This paper studies Claude 3.5 Computer Use as an early public GUI-agent system. It evaluates its abilities and limitations across desktop tasks.

In simple terms:

```text
Problem → how can an AI agent interact with a web, GUI, mobile, desktop, or application environment?
Method → add perception, planning, action, memory, API/tool use, state tracking, or browser control.
Goal → complete real user tasks more flexibly than scripts or static chatbots.
```

This note explains the paper first, then connects it to S4 and your thesis.

---

## Core idea

Analyze an API-based GUI automation model through tasks involving web search, productivity, workflow, and entertainment domains.

The paper is mainly about:

```text
GUI agent case study / Claude computer use
```

It contributes to the larger agent loop:

```text
observe → understand state → plan → act → receive feedback → verify / recover → complete task
```

---

## Key finding / main claim

Claude Computer Use shows strong end-to-end language-to-desktop action ability but still has planning, action-grounding, and critic/recovery limitations.

For S4, the important question is not only whether the method works on its benchmark, but **which part of web/GUI agency it improves**:

- perception and grounding,
- planning and reasoning,
- action execution,
- API/tool use,
- memory/state tracking,
- recovery and verification,
- or deployment/evaluation.

---

## Key evidence to extract from the paper

When reading the paper, extract these points:

- **Three evaluation dimensions: planning, action, critic.**
- **Computer Use OOTB framework.**
- **System prompt/action tools shown in the paper.**

These are the most useful parts for writing a literature-review paragraph.

---

## Limitations

- **Limitation 1:** Preliminary case study, not a full benchmark paper.
- **Limitation 2:** Focused on one commercial model and its public beta behavior.
- **Limitation 3:** Results may change as the model/API changes.

General thesis-level limitation:

```text
Improving one agent component is not enough for generalized web automation.
A robust web agent still needs grounding, planning, execution, verification, recovery, and safety.
```

---

## Relation to S4

This paper belongs in S4 because S4 discusses **LLM-based agents for web/GUI/mobile/computer automation**.

Its role in S4 is:

```text
The Dawn of GUI Agent: A Preliminary Case Study with Claude 3.5 Computer Use
→ GUI agent case study / Claude computer use
→ supporting P2 source for web/GUI/computer-use agent discussion
```

Use it after explaining what the paper does. Do not introduce it only as “P2”; introduce the method or idea first.

---

## Relation to thesis topic

Your thesis topic is:

```text
LLM-based agents for generalized web automation and data extraction
```

This paper matters because:

It provides recent evidence on frontier commercial computer-use agents and their failure modes.

For generalized web automation, the connection is:

```text
web / GUI / mobile / computer-use interaction
→ agent observes a digital environment
→ agent chooses actions
→ agent extracts information or completes a workflow
```

Even when the paper is not directly about data extraction, it still helps explain the automation layer needed before extraction can be generalized.

---

## How to use this paper in the literature review

Recommended use:

- Use as **P2 support**, not as the central backbone.
- Use for one precise idea, architecture, benchmark, or limitation.
- If peer-reviewed, it can support stronger claims.
- If preprint/workshop/technical report, use it for recent trends and emerging directions.

Suggested sentence:

> The Dawn of GUI Agent: A Preliminary Case Study with Claude 3.5 Computer Use shows how GUI agent case study / Claude computer use contributes to the development of LLM-based agents for digital task automation, but its limitations indicate that generalized web automation still requires stronger grounding, verification, and recovery mechanisms.

---

## Reading decision

- **Keep in S4 P2:** Yes
- **Read fully?** No, selected sections are enough unless promoted later
- **Depth needed:** Low to medium
- **Main use:** Support S4 discussion of GUI agent case study / Claude computer use
- **Most important parts:**
  - Abstract
  - Introduction
  - Main architecture / method figure
  - Dataset or benchmark section
  - Results table
  - Limitations / discussion

---

## One-sentence summary

The Dawn of GUI Agent: A Preliminary Case Study with Claude 3.5 Computer Use is a P2 supporting paper for S4 because it explains **GUI agent case study / Claude computer use**, but it should be cited according to its venue/status and not overused beyond its evidence.

---

## BibTeX placeholder

```bibtex
@misc{thedawnofguiagentapreliminarycasest2024,
  title = {The Dawn of GUI Agent: A Preliminary Case Study with Claude 3.5 Computer Use},
  year = {2024},
  note = {arXiv preprint / under review; Preprint / case study. Verify final bibliographic metadata before thesis submission.}
}
```


---

<!-- ========== FILE: S4_P2_paper_first_detailed_markdown_notes\S4_P2_18_A_Comprehensive_Survey_of_Agents_for_Computer_Use_Foundations_Challenges_and_Future_Directions.md ========== -->

## Source: `S4_P2_paper_first_detailed_markdown_notes\S4_P2_18_A_Comprehensive_Survey_of_Agents_for_Computer_Use_Foundations_Challenges_and_Future_Directions.md`

# S4 P2 Paper 18 — A Comprehensive Survey of Agents for Computer Use: Foundations, Challenges, and Future Directions

## Metadata

- **Title:** A Comprehensive Survey of Agents for Computer Use: Foundations, Challenges, and Future Directions
- **Year:** 2025
- **Venue / status:** arXiv survey
- **Peer-reviewed status:** No confirmed archival venue
- **Publication type:** Survey preprint
- **Thesis section:** S4 — computer-use agent survey foundation
- **Category:** computer-use agent survey
- **Priority:** P2
- **BibTeX key:** `acomprehensivesurveyofagentsforcomp2025`

---

## Simple understanding

This survey reviews agents for computer use: systems that execute natural-language tasks on PCs or phones via UI actions.

In simple terms:

```text
Problem → how can an AI agent interact with a web, GUI, mobile, desktop, or application environment?
Method → add perception, planning, action, memory, API/tool use, state tracking, or browser control.
Goal → complete real user tasks more flexibly than scripts or static chatbots.
```

This note explains the paper first, then connects it to S4 and your thesis.

---

## Core idea

Provide a taxonomy of computer-use agents across domain, interaction, and agent perspectives.

The paper is mainly about:

```text
computer-use agent survey
```

It contributes to the larger agent loop:

```text
observe → understand state → plan → act → receive feedback → verify / recover → complete task
```

---

## Key finding / main claim

The field is shifting from specialized agents toward foundation-model-based agents, from text to image observations, and toward behavior cloning, while generalization and planning remain open problems.

For S4, the important question is not only whether the method works on its benchmark, but **which part of web/GUI agency it improves**:

- perception and grounding,
- planning and reasoning,
- action execution,
- API/tool use,
- memory/state tracking,
- recovery and verification,
- or deployment/evaluation.

---

## Key evidence to extract from the paper

When reading the paper, extract these points:

- **Taxonomy in Figure 1: domain, interaction, and agent perspectives.**
- **Review of 87 ACU papers and 33 datasets.**
- **Six gaps: generalization, inefficient learning, limited planning, low task complexity, non-standard evaluation, deployment mismatch.**

These are the most useful parts for writing a literature-review paragraph.

---

## Limitations

- **Limitation 1:** Survey preprint with about one-third preprint sources, according to its own methodology.
- **Limitation 2:** Not a primary method paper.
- **Limitation 3:** Use for taxonomy and research gaps, not central empirical claims.

General thesis-level limitation:

```text
Improving one agent component is not enough for generalized web automation.
A robust web agent still needs grounding, planning, execution, verification, recovery, and safety.
```

---

## Relation to S4

This paper belongs in S4 because S4 discusses **LLM-based agents for web/GUI/mobile/computer automation**.

Its role in S4 is:

```text
A Comprehensive Survey of Agents for Computer Use: Foundations, Challenges, and Future Directions
→ computer-use agent survey
→ supporting P2 source for web/GUI/computer-use agent discussion
```

Use it after explaining what the paper does. Do not introduce it only as “P2”; introduce the method or idea first.

---

## Relation to thesis topic

Your thesis topic is:

```text
LLM-based agents for generalized web automation and data extraction
```

This paper matters because:

It is highly useful for framing S4’s broader computer-use agent landscape.

For generalized web automation, the connection is:

```text
web / GUI / mobile / computer-use interaction
→ agent observes a digital environment
→ agent chooses actions
→ agent extracts information or completes a workflow
```

Even when the paper is not directly about data extraction, it still helps explain the automation layer needed before extraction can be generalized.

---

## How to use this paper in the literature review

Recommended use:

- Use as **P2 support**, not as the central backbone.
- Use for one precise idea, architecture, benchmark, or limitation.
- If peer-reviewed, it can support stronger claims.
- If preprint/workshop/technical report, use it for recent trends and emerging directions.

Suggested sentence:

> A Comprehensive Survey of Agents for Computer Use: Foundations, Challenges, and Future Directions shows how computer-use agent survey contributes to the development of LLM-based agents for digital task automation, but its limitations indicate that generalized web automation still requires stronger grounding, verification, and recovery mechanisms.

---

## Reading decision

- **Keep in S4 P2:** Yes
- **Read fully?** No, selected sections are enough unless promoted later
- **Depth needed:** Low to medium
- **Main use:** Support S4 discussion of computer-use agent survey
- **Most important parts:**
  - Abstract
  - Introduction
  - Main architecture / method figure
  - Dataset or benchmark section
  - Results table
  - Limitations / discussion

---

## One-sentence summary

A Comprehensive Survey of Agents for Computer Use: Foundations, Challenges, and Future Directions is a P2 supporting paper for S4 because it explains **computer-use agent survey**, but it should be cited according to its venue/status and not overused beyond its evidence.

---

## BibTeX placeholder

```bibtex
@misc{acomprehensivesurveyofagentsforcomp2025,
  title = {A Comprehensive Survey of Agents for Computer Use: Foundations, Challenges, and Future Directions},
  year = {2025},
  note = {arXiv survey; Survey preprint. Verify final bibliographic metadata before thesis submission.}
}
```


---

<!-- ========== FILE: S4_P2_paper_first_detailed_markdown_notes\S4_P2_19_Mobile-Agent-E_Self-Evolving_Mobile_Assistant_for_Complex_Tasks.md ========== -->

## Source: `S4_P2_paper_first_detailed_markdown_notes\S4_P2_19_Mobile-Agent-E_Self-Evolving_Mobile_Assistant_for_Complex_Tasks.md`

# S4 P2 Paper 19 — Mobile-Agent-E: Self-Evolving Mobile Assistant for Complex Tasks

## Metadata

- **Title:** Mobile-Agent-E: Self-Evolving Mobile Assistant for Complex Tasks
- **Year:** 2025
- **Venue / status:** arXiv preprint; SEA @ NeurIPS 2025 workshop oral
- **Peer-reviewed status:** Workshop
- **Publication type:** Workshop / preprint
- **Thesis section:** S4 — mobile agents, memory, and self-evolution
- **Category:** self-evolving mobile agents / hierarchical multi-agent mobile assistant
- **Priority:** P2
- **BibTeX key:** `mobileagenteselfevolvingmobileassis2025`

---

## Simple understanding

Mobile-Agent-E is a hierarchical multi-agent mobile assistant that separates high-level planning from low-level action and learns from past experience using Tips and Shortcuts.

In simple terms:

```text
Problem → how can an AI agent interact with a web, GUI, mobile, desktop, or application environment?
Method → add perception, planning, action, memory, API/tool use, state tracking, or browser control.
Goal → complete real user tasks more flexibly than scripts or static chatbots.
```

This note explains the paper first, then connects it to S4 and your thesis.

---

## Core idea

Use a Manager plus Perceptor, Operator, Action Reflector, and Notetaker agents, with self-evolution memory that stores reusable Tips and Shortcuts.

The paper is mainly about:

```text
self-evolving mobile agents / hierarchical multi-agent mobile assistant
```

It contributes to the larger agent loop:

```text
observe → understand state → plan → act → receive feedback → verify / recover → complete task
```

---

## Key finding / main claim

The paper reports that self-evolution improves performance and efficiency on complex real-world mobile tasks.

For S4, the important question is not only whether the method works on its benchmark, but **which part of web/GUI agency it improves**:

- perception and grounding,
- planning and reasoning,
- action execution,
- API/tool use,
- memory/state tracking,
- recovery and verification,
- or deployment/evaluation.

---

## Key evidence to extract from the paper

When reading the paper, extract these points:

- **Figure 1 showing hierarchical agents and self-evolution memory.**
- **Mobile-Eval-E benchmark for long-horizon multi-app tasks.**
- **Reported 22% absolute improvement over previous SOTA across model backbones.**

These are the most useful parts for writing a literature-review paragraph.

---

## Limitations

- **Limitation 1:** Workshop/preprint status, not main archival NeurIPS.
- **Limitation 2:** Mobile tasks are related to but not identical to web automation.
- **Limitation 3:** Persistent shortcuts can become stale when apps change.

General thesis-level limitation:

```text
Improving one agent component is not enough for generalized web automation.
A robust web agent still needs grounding, planning, execution, verification, recovery, and safety.
```

---

## Relation to S4

This paper belongs in S4 because S4 discusses **LLM-based agents for web/GUI/mobile/computer automation**.

Its role in S4 is:

```text
Mobile-Agent-E: Self-Evolving Mobile Assistant for Complex Tasks
→ self-evolving mobile agents / hierarchical multi-agent mobile assistant
→ supporting P2 source for web/GUI/computer-use agent discussion
```

Use it after explaining what the paper does. Do not introduce it only as “P2”; introduce the method or idea first.

---

## Relation to thesis topic

Your thesis topic is:

```text
LLM-based agents for generalized web automation and data extraction
```

This paper matters because:

It is useful for showing how mobile agents move beyond reactive action selection toward memory and reusable experience.

For generalized web automation, the connection is:

```text
web / GUI / mobile / computer-use interaction
→ agent observes a digital environment
→ agent chooses actions
→ agent extracts information or completes a workflow
```

Even when the paper is not directly about data extraction, it still helps explain the automation layer needed before extraction can be generalized.

---

## How to use this paper in the literature review

Recommended use:

- Use as **P2 support**, not as the central backbone.
- Use for one precise idea, architecture, benchmark, or limitation.
- If peer-reviewed, it can support stronger claims.
- If preprint/workshop/technical report, use it for recent trends and emerging directions.

Suggested sentence:

> Mobile-Agent-E: Self-Evolving Mobile Assistant for Complex Tasks shows how self-evolving mobile agents / hierarchical multi-agent mobile assistant contributes to the development of LLM-based agents for digital task automation, but its limitations indicate that generalized web automation still requires stronger grounding, verification, and recovery mechanisms.

---

## Reading decision

- **Keep in S4 P2:** Yes
- **Read fully?** No, selected sections are enough unless promoted later
- **Depth needed:** Low to medium
- **Main use:** Support S4 discussion of self-evolving mobile agents / hierarchical multi-agent mobile assistant
- **Most important parts:**
  - Abstract
  - Introduction
  - Main architecture / method figure
  - Dataset or benchmark section
  - Results table
  - Limitations / discussion

---

## One-sentence summary

Mobile-Agent-E: Self-Evolving Mobile Assistant for Complex Tasks is a P2 supporting paper for S4 because it explains **self-evolving mobile agents / hierarchical multi-agent mobile assistant**, but it should be cited according to its venue/status and not overused beyond its evidence.

---

## BibTeX placeholder

```bibtex
@misc{mobileagenteselfevolvingmobileassis2025,
  title = {Mobile-Agent-E: Self-Evolving Mobile Assistant for Complex Tasks},
  year = {2025},
  note = {arXiv preprint; SEA @ NeurIPS 2025 workshop oral; Workshop / preprint. Verify final bibliographic metadata before thesis submission.}
}
```


---

<!-- ========== FILE: S4_P2_paper_first_detailed_markdown_notes\S4_P2_20_ReachAgent_Enhancing_Mobile_Agent_via_Page_Reaching_and_Page_Operation.md ========== -->

## Source: `S4_P2_paper_first_detailed_markdown_notes\S4_P2_20_ReachAgent_Enhancing_Mobile_Agent_via_Page_Reaching_and_Page_Operation.md`

# S4 P2 Paper 20 — ReachAgent: Enhancing Mobile Agent via Page Reaching and Page Operation

## Metadata

- **Title:** ReachAgent: Enhancing Mobile Agent via Page Reaching and Page Operation
- **Year:** 2025
- **Venue / status:** NAACL 2025 long paper
- **Peer-reviewed status:** Yes
- **Publication type:** Peer-reviewed conference paper
- **Thesis section:** S4 — mobile GUI agent training
- **Category:** mobile agent training / page reaching and operation
- **Priority:** P2
- **BibTeX key:** `reachagentenhancingmobileagentviapa2025`

---

## Simple understanding

ReachAgent improves mobile agents by decomposing tasks into page-reaching and page-operation subtasks. It focuses on the whole GUI flow, not just the most relevant current element.

In simple terms:

```text
Problem → how can an AI agent interact with a web, GUI, mobile, desktop, or application environment?
Method → add perception, planning, action, memory, API/tool use, state tracking, or browser control.
Goal → complete real user tasks more flexibly than scripts or static chatbots.
```

This note explains the paper first, then connects it to S4 and your thesis.

---

## Core idea

Train mobile agents to reach target pages and perform specified operations, using MobileReach and reward-based preference GUI flows.

The paper is mainly about:

```text
mobile agent training / page reaching and operation
```

It contributes to the larger agent loop:

```text
observe → understand state → plan → act → receive feedback → verify / recover → complete task
```

---

## Key finding / main claim

ReachAgent improves step-level and task-level action accuracy over prior mobile agents by focusing on subtask completion and GUI flow quality.

For S4, the important question is not only whether the method works on its benchmark, but **which part of web/GUI agency it improves**:

- perception and grounding,
- planning and reasoning,
- action execution,
- API/tool use,
- memory/state tracking,
- recovery and verification,
- or deployment/evaluation.

---

## Key evidence to extract from the paper

When reading the paper, extract these points:

- **Figure 1/2 showing task decomposition into Reach and Operate subtasks.**
- **MobileReach dataset.**
- **Reported IoU and text accuracy improvements over SOTA.**

These are the most useful parts for writing a literature-review paragraph.

---

## Limitations

- **Limitation 1:** It is mobile-specific, not a general web-browser agent.
- **Limitation 2:** Training data and action alignment may depend on mobile app structure.
- **Limitation 3:** Page reaching/operation helps but does not solve all long-horizon planning failures.

General thesis-level limitation:

```text
Improving one agent component is not enough for generalized web automation.
A robust web agent still needs grounding, planning, execution, verification, recovery, and safety.
```

---

## Relation to S4

This paper belongs in S4 because S4 discusses **LLM-based agents for web/GUI/mobile/computer automation**.

Its role in S4 is:

```text
ReachAgent: Enhancing Mobile Agent via Page Reaching and Page Operation
→ mobile agent training / page reaching and operation
→ supporting P2 source for web/GUI/computer-use agent discussion
```

Use it after explaining what the paper does. Do not introduce it only as “P2”; introduce the method or idea first.

---

## Relation to thesis topic

Your thesis topic is:

```text
LLM-based agents for generalized web automation and data extraction
```

This paper matters because:

It is a strong peer-reviewed paper for the mobile-agent subsection of S4.

For generalized web automation, the connection is:

```text
web / GUI / mobile / computer-use interaction
→ agent observes a digital environment
→ agent chooses actions
→ agent extracts information or completes a workflow
```

Even when the paper is not directly about data extraction, it still helps explain the automation layer needed before extraction can be generalized.

---

## How to use this paper in the literature review

Recommended use:

- Use as **P2 support**, not as the central backbone.
- Use for one precise idea, architecture, benchmark, or limitation.
- If peer-reviewed, it can support stronger claims.
- If preprint/workshop/technical report, use it for recent trends and emerging directions.

Suggested sentence:

> ReachAgent: Enhancing Mobile Agent via Page Reaching and Page Operation shows how mobile agent training / page reaching and operation contributes to the development of LLM-based agents for digital task automation, but its limitations indicate that generalized web automation still requires stronger grounding, verification, and recovery mechanisms.

---

## Reading decision

- **Keep in S4 P2:** Yes
- **Read fully?** Yes or selected sections carefully
- **Depth needed:** Medium to high
- **Main use:** Support S4 discussion of mobile agent training / page reaching and operation
- **Most important parts:**
  - Abstract
  - Introduction
  - Main architecture / method figure
  - Dataset or benchmark section
  - Results table
  - Limitations / discussion

---

## One-sentence summary

ReachAgent: Enhancing Mobile Agent via Page Reaching and Page Operation is a P2 supporting paper for S4 because it explains **mobile agent training / page reaching and operation**, but it should be cited according to its venue/status and not overused beyond its evidence.

---

## BibTeX placeholder

```bibtex
@misc{reachagentenhancingmobileagentviapa2025,
  title = {ReachAgent: Enhancing Mobile Agent via Page Reaching and Page Operation},
  year = {2025},
  note = {NAACL 2025 long paper; Peer-reviewed conference paper. Verify final bibliographic metadata before thesis submission.}
}
```


---

<!-- ========== FILE: S4_P2_paper_first_detailed_markdown_notes\S4_P2_21_LiteWebAgent_The_Open-Source_Suite_for_VLM-Based_Web-Agent_Applications.md ========== -->

## Source: `S4_P2_paper_first_detailed_markdown_notes\S4_P2_21_LiteWebAgent_The_Open-Source_Suite_for_VLM-Based_Web-Agent_Applications.md`

# S4 P2 Paper 21 — LiteWebAgent: The Open-Source Suite for VLM-Based Web-Agent Applications

## Metadata

- **Title:** LiteWebAgent: The Open-Source Suite for VLM-Based Web-Agent Applications
- **Year:** 2025
- **Venue / status:** NAACL 2025 System Demonstrations
- **Peer-reviewed status:** Yes, demo
- **Publication type:** System demonstration paper
- **Thesis section:** S4 — web-agent frameworks and deployment
- **Category:** open-source VLM web-agent suite
- **Priority:** P2
- **BibTeX key:** `litewebagenttheopensourcesuiteforvl2025`

---

## Simple understanding

LiteWebAgent is an open-source suite for VLM-based web-agent applications. It provides a core agent framework plus deployable web app and Chrome extension.

In simple terms:

```text
Problem → how can an AI agent interact with a web, GUI, mobile, desktop, or application environment?
Method → add perception, planning, action, memory, API/tool use, state tracking, or browser control.
Goal → complete real user tasks more flexibly than scripts or static chatbots.
```

This note explains the paper first, then connects it to S4 and your thesis.

---

## Core idea

Build a modular web-agent framework with planning, memory, tree search, recursive function calling, and decoupled action generation/grounding.

The paper is mainly about:

```text
open-source VLM web-agent suite
```

It contributes to the larger agent loop:

```text
observe → understand state → plan → act → receive feedback → verify / recover → complete task
```

---

## Key finding / main claim

The paper addresses a tooling gap by offering an extensible, production-oriented web-agent suite for both research and deployment.

For S4, the important question is not only whether the method works on its benchmark, but **which part of web/GUI agency it improves**:

- perception and grounding,
- planning and reasoning,
- action execution,
- API/tool use,
- memory/state tracking,
- recovery and verification,
- or deployment/evaluation.

---

## Key evidence to extract from the paper

When reading the paper, extract these points:

- **Abstract describing planning, memory, and tree-search capabilities.**
- **Two deployment modes: Vercel remote browser and Chrome extension via CDP.**
- **Section 1.2 ecosystem categories and gap analysis.**

These are the most useful parts for writing a literature-review paragraph.

---

## Limitations

- **Limitation 1:** System demo paper, so it is more about infrastructure than a new benchmark-leading method.
- **Limitation 2:** Performance depends on connected VLMs and deployment settings.
- **Limitation 3:** Production-readiness does not guarantee robust performance on arbitrary websites.

General thesis-level limitation:

```text
Improving one agent component is not enough for generalized web automation.
A robust web agent still needs grounding, planning, execution, verification, recovery, and safety.
```

---

## Relation to S4

This paper belongs in S4 because S4 discusses **LLM-based agents for web/GUI/mobile/computer automation**.

Its role in S4 is:

```text
LiteWebAgent: The Open-Source Suite for VLM-Based Web-Agent Applications
→ open-source VLM web-agent suite
→ supporting P2 source for web/GUI/computer-use agent discussion
```

Use it after explaining what the paper does. Do not introduce it only as “P2”; introduce the method or idea first.

---

## Relation to thesis topic

Your thesis topic is:

```text
LLM-based agents for generalized web automation and data extraction
```

This paper matters because:

It is directly useful for your thesis because it connects web-agent research with practical deployment infrastructure.

For generalized web automation, the connection is:

```text
web / GUI / mobile / computer-use interaction
→ agent observes a digital environment
→ agent chooses actions
→ agent extracts information or completes a workflow
```

Even when the paper is not directly about data extraction, it still helps explain the automation layer needed before extraction can be generalized.

---

## How to use this paper in the literature review

Recommended use:

- Use as **P2 support**, not as the central backbone.
- Use for one precise idea, architecture, benchmark, or limitation.
- If peer-reviewed, it can support stronger claims.
- If preprint/workshop/technical report, use it for recent trends and emerging directions.

Suggested sentence:

> LiteWebAgent: The Open-Source Suite for VLM-Based Web-Agent Applications shows how open-source VLM web-agent suite contributes to the development of LLM-based agents for digital task automation, but its limitations indicate that generalized web automation still requires stronger grounding, verification, and recovery mechanisms.

---

## Reading decision

- **Keep in S4 P2:** Yes
- **Read fully?** Yes or selected sections carefully
- **Depth needed:** Medium to high
- **Main use:** Support S4 discussion of open-source VLM web-agent suite
- **Most important parts:**
  - Abstract
  - Introduction
  - Main architecture / method figure
  - Dataset or benchmark section
  - Results table
  - Limitations / discussion

---

## One-sentence summary

LiteWebAgent: The Open-Source Suite for VLM-Based Web-Agent Applications is a P2 supporting paper for S4 because it explains **open-source VLM web-agent suite**, but it should be cited according to its venue/status and not overused beyond its evidence.

---

## BibTeX placeholder

```bibtex
@misc{litewebagenttheopensourcesuiteforvl2025,
  title = {LiteWebAgent: The Open-Source Suite for VLM-Based Web-Agent Applications},
  year = {2025},
  note = {NAACL 2025 System Demonstrations; System demonstration paper. Verify final bibliographic metadata before thesis submission.}
}
```


---

<!-- ========== FILE: S4_P2_paper_first_detailed_markdown_notes\S4_P2_22_LLM-Powered_GUI_Agents_in_Phone_Automation_Surveying_Progress_and_Prospects.md ========== -->

## Source: `S4_P2_paper_first_detailed_markdown_notes\S4_P2_22_LLM-Powered_GUI_Agents_in_Phone_Automation_Surveying_Progress_and_Prospects.md`

# S4 P2 Paper 22 — LLM-Powered GUI Agents in Phone Automation: Surveying Progress and Prospects

## Metadata

- **Title:** LLM-Powered GUI Agents in Phone Automation: Surveying Progress and Prospects
- **Year:** 2025
- **Venue / status:** Transactions on Machine Learning Research, 11/2025
- **Peer-reviewed status:** Yes
- **Publication type:** Peer-reviewed TMLR survey
- **Thesis section:** S4 — phone GUI agents and mobile automation
- **Category:** phone GUI agent survey
- **Priority:** P2
- **BibTeX key:** `llmpoweredguiagentsinphoneautomatio2025`

---

## Simple understanding

This survey systematically reviews LLM-powered phone GUI agents, including frameworks, models, datasets, benchmarks, and open challenges.

In simple terms:

```text
Problem → how can an AI agent interact with a web, GUI, mobile, desktop, or application environment?
Method → add perception, planning, action, memory, API/tool use, state tracking, or browser control.
Goal → complete real user tasks more flexibly than scripts or static chatbots.
```

This note explains the paper first, then connects it to S4 and your thesis.

---

## Core idea

Provide a mobile-specific taxonomy covering single-agent, multi-agent, plan-then-act frameworks, prompt/training methods, and evaluation resources.

The paper is mainly about:

```text
phone GUI agent survey
```

It contributes to the larger agent loop:

```text
observe → understand state → plan → act → receive feedback → verify / recover → complete task
```

---

## Key finding / main claim

LLMs transform phone automation by improving intent understanding, multimodal perception, and decision-making, but challenges remain in data diversity, on-device efficiency, adaptation, and security.

For S4, the important question is not only whether the method works on its benchmark, but **which part of web/GUI agency it improves**:

- perception and grounding,
- planning and reasoning,
- action execution,
- API/tool use,
- memory/state tracking,
- recovery and verification,
- or deployment/evaluation.

---

## Key evidence to extract from the paper

When reading the paper, extract these points:

- **Figure 1 comparing conversational LLMs and phone GUI agents.**
- **Figure 2 comprehensive taxonomy of phone GUI agents.**
- **Table comparing this survey with prior GUI/RPA/LLM-agent surveys.**

These are the most useful parts for writing a literature-review paragraph.

---

## Limitations

- **Limitation 1:** Survey, not primary method.
- **Limitation 2:** Phone-specific focus may not cover all web/desktop agents in depth.
- **Limitation 3:** Recent field changes may quickly make some taxonomy parts outdated.

General thesis-level limitation:

```text
Improving one agent component is not enough for generalized web automation.
A robust web agent still needs grounding, planning, execution, verification, recovery, and safety.
```

---

## Relation to S4

This paper belongs in S4 because S4 discusses **LLM-based agents for web/GUI/mobile/computer automation**.

Its role in S4 is:

```text
LLM-Powered GUI Agents in Phone Automation: Surveying Progress and Prospects
→ phone GUI agent survey
→ supporting P2 source for web/GUI/computer-use agent discussion
```

Use it after explaining what the paper does. Do not introduce it only as “P2”; introduce the method or idea first.

---

## Relation to thesis topic

Your thesis topic is:

```text
LLM-based agents for generalized web automation and data extraction
```

This paper matters because:

It is one of the safest and strongest survey sources for the mobile/phone-agent part of S4.

For generalized web automation, the connection is:

```text
web / GUI / mobile / computer-use interaction
→ agent observes a digital environment
→ agent chooses actions
→ agent extracts information or completes a workflow
```

Even when the paper is not directly about data extraction, it still helps explain the automation layer needed before extraction can be generalized.

---

## How to use this paper in the literature review

Recommended use:

- Use as **P2 support**, not as the central backbone.
- Use for one precise idea, architecture, benchmark, or limitation.
- If peer-reviewed, it can support stronger claims.
- If preprint/workshop/technical report, use it for recent trends and emerging directions.

Suggested sentence:

> LLM-Powered GUI Agents in Phone Automation: Surveying Progress and Prospects shows how phone GUI agent survey contributes to the development of LLM-based agents for digital task automation, but its limitations indicate that generalized web automation still requires stronger grounding, verification, and recovery mechanisms.

---

## Reading decision

- **Keep in S4 P2:** Yes
- **Read fully?** Yes or selected sections carefully
- **Depth needed:** Medium to high
- **Main use:** Support S4 discussion of phone GUI agent survey
- **Most important parts:**
  - Abstract
  - Introduction
  - Main architecture / method figure
  - Dataset or benchmark section
  - Results table
  - Limitations / discussion

---

## One-sentence summary

LLM-Powered GUI Agents in Phone Automation: Surveying Progress and Prospects is a P2 supporting paper for S4 because it explains **phone GUI agent survey**, but it should be cited according to its venue/status and not overused beyond its evidence.

---

## BibTeX placeholder

```bibtex
@misc{llmpoweredguiagentsinphoneautomatio2025,
  title = {LLM-Powered GUI Agents in Phone Automation: Surveying Progress and Prospects},
  year = {2025},
  note = {Transactions on Machine Learning Research, 11/2025; Peer-reviewed TMLR survey. Verify final bibliographic metadata before thesis submission.}
}
```


---

<!-- ========== FILE: S4_P2_paper_first_detailed_markdown_notes\S4_P2_23_WebThinker_Empowering_Large_Reasoning_Models_with_Deep_Research_Capability.md ========== -->

## Source: `S4_P2_paper_first_detailed_markdown_notes\S4_P2_23_WebThinker_Empowering_Large_Reasoning_Models_with_Deep_Research_Capability.md`

# S4 P2 Paper 23 — WebThinker: Empowering Large Reasoning Models with Deep Research Capability

## Metadata

- **Title:** WebThinker: Empowering Large Reasoning Models with Deep Research Capability
- **Year:** 2025
- **Venue / status:** NeurIPS 2025
- **Peer-reviewed status:** Yes
- **Publication type:** Peer-reviewed conference paper
- **Thesis section:** S4 — deep research web agents
- **Category:** deep research web agents / reasoning with tools
- **Priority:** P2
- **BibTeX key:** `webthinkerempoweringlargereasoningm2025`

---

## Simple understanding

WebThinker gives large reasoning models deep research capability by allowing them to search, navigate web pages, extract information, and draft reports during reasoning.

In simple terms:

```text
Problem → how can an AI agent interact with a web, GUI, mobile, desktop, or application environment?
Method → add perception, planning, action, memory, API/tool use, state tracking, or browser control.
Goal → complete real user tasks more flexibly than scripts or static chatbots.
```

This note explains the paper first, then connects it to S4 and your thesis.

---

## Core idea

Integrate a Deep Web Explorer and Autonomous Think-Search-and-Draft strategy into LRMs, with online DPO training for research-tool use.

The paper is mainly about:

```text
deep research web agents / reasoning with tools
```

It contributes to the larger agent loop:

```text
observe → understand state → plan → act → receive feedback → verify / recover → complete task
```

---

## Key finding / main claim

WebThinker outperforms prior methods on complex reasoning benchmarks and scientific report generation tasks by interleaving reasoning, search, navigation, and drafting.

For S4, the important question is not only whether the method works on its benchmark, but **which part of web/GUI agency it improves**:

- perception and grounding,
- planning and reasoning,
- action execution,
- API/tool use,
- memory/state tracking,
- recovery and verification,
- or deployment/evaluation.

---

## Key evidence to extract from the paper

When reading the paper, extract these points:

- **Figure 2 comparing Standard RAG, predefined workflow RAG, and WebThinker.**
- **Figure 3 showing Problem-Solving and Report-Generation modes.**
- **Reported gains on GPQA, GAIA, WebWalkerQA, HLE, and Glaive.**

These are the most useful parts for writing a literature-review paragraph.

---

## Limitations

- **Limitation 1:** Deep research differs from transactional web automation such as filling forms or booking services.
- **Limitation 2:** Performance depends on search quality and tool integration.
- **Limitation 3:** Report generation quality still requires factuality and citation verification.

General thesis-level limitation:

```text
Improving one agent component is not enough for generalized web automation.
A robust web agent still needs grounding, planning, execution, verification, recovery, and safety.
```

---

## Relation to S4

This paper belongs in S4 because S4 discusses **LLM-based agents for web/GUI/mobile/computer automation**.

Its role in S4 is:

```text
WebThinker: Empowering Large Reasoning Models with Deep Research Capability
→ deep research web agents / reasoning with tools
→ supporting P2 source for web/GUI/computer-use agent discussion
```

Use it after explaining what the paper does. Do not introduce it only as “P2”; introduce the method or idea first.

---

## Relation to thesis topic

Your thesis topic is:

```text
LLM-based agents for generalized web automation and data extraction
```

This paper matters because:

It is a strong peer-reviewed source for web agents that perform information gathering and research, close to your thesis theme of web data extraction.

For generalized web automation, the connection is:

```text
web / GUI / mobile / computer-use interaction
→ agent observes a digital environment
→ agent chooses actions
→ agent extracts information or completes a workflow
```

Even when the paper is not directly about data extraction, it still helps explain the automation layer needed before extraction can be generalized.

---

## How to use this paper in the literature review

Recommended use:

- Use as **P2 support**, not as the central backbone.
- Use for one precise idea, architecture, benchmark, or limitation.
- If peer-reviewed, it can support stronger claims.
- If preprint/workshop/technical report, use it for recent trends and emerging directions.

Suggested sentence:

> WebThinker: Empowering Large Reasoning Models with Deep Research Capability shows how deep research web agents / reasoning with tools contributes to the development of LLM-based agents for digital task automation, but its limitations indicate that generalized web automation still requires stronger grounding, verification, and recovery mechanisms.

---

## Reading decision

- **Keep in S4 P2:** Yes
- **Read fully?** Yes or selected sections carefully
- **Depth needed:** Medium to high
- **Main use:** Support S4 discussion of deep research web agents / reasoning with tools
- **Most important parts:**
  - Abstract
  - Introduction
  - Main architecture / method figure
  - Dataset or benchmark section
  - Results table
  - Limitations / discussion

---

## One-sentence summary

WebThinker: Empowering Large Reasoning Models with Deep Research Capability is a P2 supporting paper for S4 because it explains **deep research web agents / reasoning with tools**, but it should be cited according to its venue/status and not overused beyond its evidence.

---

## BibTeX placeholder

```bibtex
@misc{webthinkerempoweringlargereasoningm2025,
  title = {WebThinker: Empowering Large Reasoning Models with Deep Research Capability},
  year = {2025},
  note = {NeurIPS 2025; Peer-reviewed conference paper. Verify final bibliographic metadata before thesis submission.}
}
```


---

<!-- ========== FILE: S4_P2_paper_first_detailed_markdown_notes\S4_P2_24_Beyond_Browsing_API-Based_Web_Agents.md ========== -->

## Source: `S4_P2_paper_first_detailed_markdown_notes\S4_P2_24_Beyond_Browsing_API-Based_Web_Agents.md`

# S4 P2 Paper 24 — Beyond Browsing: API-Based Web Agents

## Metadata

- **Title:** Beyond Browsing: API-Based Web Agents
- **Year:** 2025
- **Venue / status:** arXiv preprint
- **Peer-reviewed status:** No confirmed archival venue
- **Publication type:** Preprint
- **Thesis section:** S4 — API vs browser web-agent design
- **Category:** API-based and hybrid web agents
- **Priority:** P2
- **BibTeX key:** `beyondbrowsingapibasedwebagents2025`

---

## Simple understanding

This paper asks whether web agents should use APIs instead of only browsing. It proposes API-only and hybrid agents and compares them with browsing-only agents on WebArena.

In simple terms:

```text
Problem → how can an AI agent interact with a web, GUI, mobile, desktop, or application environment?
Method → add perception, planning, action, memory, API/tool use, state tracking, or browser control.
Goal → complete real user tasks more flexibly than scripts or static chatbots.
```

This note explains the paper first, then connects it to S4 and your thesis.

---

## Core idea

Expand web-agent action spaces to include API calls and code execution, with a hybrid agent that dynamically interleaves browsing and API actions.

The paper is mainly about:

```text
API-based and hybrid web agents
```

It contributes to the larger agent loop:

```text
observe → understand state → plan → act → receive feedback → verify / recover → complete task
```

---

## Key finding / main claim

API-based agents outperform browsing-only agents on WebArena, and hybrid agents perform best, reaching 38.9% success in the reported setup.

For S4, the important question is not only whether the method works on its benchmark, but **which part of web/GUI agency it improves**:

- perception and grounding,
- planning and reasoning,
- action execution,
- API/tool use,
- memory/state tracking,
- recovery and verification,
- or deployment/evaluation.

---

## Key evidence to extract from the paper

When reading the paper, extract these points:

- **Figure 1 comparing browsing, API-based, and hybrid agents.**
- **Example where API calls solve a GitLab task in fewer steps than browsing.**
- **Reported average: browsing 14.8%, API-based 29.2%, hybrid 38.9%.**

These are the most useful parts for writing a literature-review paragraph.

---

## Limitations

- **Limitation 1:** Preprint status.
- **Limitation 2:** APIs are not always available, documented, or authorized.
- **Limitation 3:** The study focuses on text-only WebArena tasks and may not cover visual web tasks.

General thesis-level limitation:

```text
Improving one agent component is not enough for generalized web automation.
A robust web agent still needs grounding, planning, execution, verification, recovery, and safety.
```

---

## Relation to S4

This paper belongs in S4 because S4 discusses **LLM-based agents for web/GUI/mobile/computer automation**.

Its role in S4 is:

```text
Beyond Browsing: API-Based Web Agents
→ API-based and hybrid web agents
→ supporting P2 source for web/GUI/computer-use agent discussion
```

Use it after explaining what the paper does. Do not introduce it only as “P2”; introduce the method or idea first.

---

## Relation to thesis topic

Your thesis topic is:

```text
LLM-based agents for generalized web automation and data extraction
```

This paper matters because:

It is extremely relevant to your thesis because it challenges the assumption that generalized web agents should always act through human-facing browsers.

For generalized web automation, the connection is:

```text
web / GUI / mobile / computer-use interaction
→ agent observes a digital environment
→ agent chooses actions
→ agent extracts information or completes a workflow
```

Even when the paper is not directly about data extraction, it still helps explain the automation layer needed before extraction can be generalized.

---

## How to use this paper in the literature review

Recommended use:

- Use as **P2 support**, not as the central backbone.
- Use for one precise idea, architecture, benchmark, or limitation.
- If peer-reviewed, it can support stronger claims.
- If preprint/workshop/technical report, use it for recent trends and emerging directions.

Suggested sentence:

> Beyond Browsing: API-Based Web Agents shows how API-based and hybrid web agents contributes to the development of LLM-based agents for digital task automation, but its limitations indicate that generalized web automation still requires stronger grounding, verification, and recovery mechanisms.

---

## Reading decision

- **Keep in S4 P2:** Yes
- **Read fully?** No, selected sections are enough unless promoted later
- **Depth needed:** Low to medium
- **Main use:** Support S4 discussion of API-based and hybrid web agents
- **Most important parts:**
  - Abstract
  - Introduction
  - Main architecture / method figure
  - Dataset or benchmark section
  - Results table
  - Limitations / discussion

---

## One-sentence summary

Beyond Browsing: API-Based Web Agents is a P2 supporting paper for S4 because it explains **API-based and hybrid web agents**, but it should be cited according to its venue/status and not overused beyond its evidence.

---

## BibTeX placeholder

```bibtex
@misc{beyondbrowsingapibasedwebagents2025,
  title = {Beyond Browsing: API-Based Web Agents},
  year = {2025},
  note = {arXiv preprint; Preprint. Verify final bibliographic metadata before thesis submission.}
}
```


---

<!-- ========== FILE: S4_P2_paper_first_detailed_markdown_notes\S4_P2_25_GA_A_Comprehensive_Survey_on_LLM-based_GUI_Agent.md ========== -->

## Source: `S4_P2_paper_first_detailed_markdown_notes\S4_P2_25_GA_A_Comprehensive_Survey_on_LLM-based_GUI_Agent.md`

# S4 P2 Paper 25 — GA: A Comprehensive Survey on LLM-based GUI Agent

## Metadata

- **Title:** GA: A Comprehensive Survey on LLM-based GUI Agent
- **Year:** 2025
- **Venue / status:** TechRxiv / submitted manuscript
- **Peer-reviewed status:** Not peer-reviewed in uploaded version
- **Publication type:** TechRxiv survey / submitted preprint
- **Thesis section:** S4 — GUI-agent taxonomy
- **Category:** GUI-agent survey
- **Priority:** P2
- **BibTeX key:** `gaacomprehensivesurveyonllmbasedgui2025`

---

## Simple understanding

This survey reviews LLM-based GUI agents across environment understanding, device control, user interaction, personalization, collaboration, and task automation pipelines.

In simple terms:

```text
Problem → how can an AI agent interact with a web, GUI, mobile, desktop, or application environment?
Method → add perception, planning, action, memory, API/tool use, state tracking, or browser control.
Goal → complete real user tasks more flexibly than scripts or static chatbots.
```

This note explains the paper first, then connects it to S4 and your thesis.

---

## Core idea

Summarize GUI-agent capabilities and propose a taxonomy based on how agents understand GUI environments: vision-based, text-based, and hybrid text-vision.

The paper is mainly about:

```text
GUI-agent survey
```

It contributes to the larger agent loop:

```text
observe → understand state → plan → act → receive feedback → verify / recover → complete task
```

---

## Key finding / main claim

LLM-based GUI agents move beyond template-based automation by understanding GUI states in real time and selecting actions flexibly.

For S4, the important question is not only whether the method works on its benchmark, but **which part of web/GUI agency it improves**:

- perception and grounding,
- planning and reasoning,
- action execution,
- API/tool use,
- memory/state tracking,
- recovery and verification,
- or deployment/evaluation.

---

## Key evidence to extract from the paper

When reading the paper, extract these points:

- **Figure 1 basic GUI-agent task automation pipeline.**
- **Taxonomy into vision-based, text-based, and hybrid agents.**
- **Discussion of one-stage vs two-stage exploration-to-exploitation pipelines.**

These are the most useful parts for writing a literature-review paragraph.

---

## Limitations

- **Limitation 1:** TechRxiv explicitly marks the uploaded version as not peer reviewed.
- **Limitation 2:** Some content may change if accepted to a journal.
- **Limitation 3:** Use only as supplementary survey support.

General thesis-level limitation:

```text
Improving one agent component is not enough for generalized web automation.
A robust web agent still needs grounding, planning, execution, verification, recovery, and safety.
```

---

## Relation to S4

This paper belongs in S4 because S4 discusses **LLM-based agents for web/GUI/mobile/computer automation**.

Its role in S4 is:

```text
GA: A Comprehensive Survey on LLM-based GUI Agent
→ GUI-agent survey
→ supporting P2 source for web/GUI/computer-use agent discussion
```

Use it after explaining what the paper does. Do not introduce it only as “P2”; introduce the method or idea first.

---

## Relation to thesis topic

Your thesis topic is:

```text
LLM-based agents for generalized web automation and data extraction
```

This paper matters because:

It can help broaden S4’s taxonomy, but should not be used as a main authoritative citation.

For generalized web automation, the connection is:

```text
web / GUI / mobile / computer-use interaction
→ agent observes a digital environment
→ agent chooses actions
→ agent extracts information or completes a workflow
```

Even when the paper is not directly about data extraction, it still helps explain the automation layer needed before extraction can be generalized.

---

## How to use this paper in the literature review

Recommended use:

- Use as **P2 support**, not as the central backbone.
- Use for one precise idea, architecture, benchmark, or limitation.
- If peer-reviewed, it can support stronger claims.
- If preprint/workshop/technical report, use it for recent trends and emerging directions.

Suggested sentence:

> GA: A Comprehensive Survey on LLM-based GUI Agent shows how GUI-agent survey contributes to the development of LLM-based agents for digital task automation, but its limitations indicate that generalized web automation still requires stronger grounding, verification, and recovery mechanisms.

---

## Reading decision

- **Keep in S4 P2:** Yes
- **Read fully?** No, selected sections are enough unless promoted later
- **Depth needed:** Low to medium
- **Main use:** Support S4 discussion of GUI-agent survey
- **Most important parts:**
  - Abstract
  - Introduction
  - Main architecture / method figure
  - Dataset or benchmark section
  - Results table
  - Limitations / discussion

---

## One-sentence summary

GA: A Comprehensive Survey on LLM-based GUI Agent is a P2 supporting paper for S4 because it explains **GUI-agent survey**, but it should be cited according to its venue/status and not overused beyond its evidence.

---

## BibTeX placeholder

```bibtex
@misc{gaacomprehensivesurveyonllmbasedgui2025,
  title = {GA: A Comprehensive Survey on LLM-based GUI Agent},
  year = {2025},
  note = {TechRxiv / submitted manuscript; TechRxiv survey / submitted preprint. Verify final bibliographic metadata before thesis submission.}
}
```


---

<!-- ========== FILE: S4_P2_paper_first_detailed_markdown_notes\S4_P2_26_Build_the_Web_for_Agents_Not_Agents_for_the_Web.md ========== -->

## Source: `S4_P2_paper_first_detailed_markdown_notes\S4_P2_26_Build_the_Web_for_Agents_Not_Agents_for_the_Web.md`

# S4 P2 Paper 26 — Build the Web for Agents, Not Agents for the Web

## Metadata

- **Title:** Build the Web for Agents, Not Agents for the Web
- **Year:** 2025
- **Venue / status:** arXiv position paper / under review
- **Peer-reviewed status:** No
- **Publication type:** Position paper / preprint
- **Thesis section:** S4 — agentic web interface design
- **Category:** agentic web interface / position paper
- **Priority:** P2
- **BibTeX key:** `buildthewebforagentsnotagentsforthe2025`

---

## Simple understanding

This position paper argues that instead of forcing agents to adapt to human-designed websites, we should build web interfaces designed for agents.

In simple terms:

```text
Problem → how can an AI agent interact with a web, GUI, mobile, desktop, or application environment?
Method → add perception, planning, action, memory, API/tool use, state tracking, or browser control.
Goal → complete real user tasks more flexibly than scripts or static chatbots.
```

This note explains the paper first, then connects it to S4 and your thesis.

---

## Core idea

Introduce the idea of Agentic Web Interfaces (AWIs): standardized, machine-oriented interfaces for web agents.

The paper is mainly about:

```text
agentic web interface / position paper
```

It contributes to the larger agent loop:

```text
observe → understand state → plan → act → receive feedback → verify / recover → complete task
```

---

## Key finding / main claim

The paper argues that screenshots, DOMs, and developer-oriented APIs are all imperfect for web agents, motivating a new agent-native interaction layer.

For S4, the important question is not only whether the method works on its benchmark, but **which part of web/GUI agency it improves**:

- perception and grounding,
- planning and reasoning,
- action execution,
- API/tool use,
- memory/state tracking,
- recovery and verification,
- or deployment/evaluation.

---

## Key evidence to extract from the paper

When reading the paper, extract these points:

- **Definition of web agents as sequential decision-making systems.**
- **Critique of screenshot, DOM, and API interaction methods.**
- **Six guiding principles for AWI design.**

These are the most useful parts for writing a literature-review paragraph.

---

## Limitations

- **Limitation 1:** Position paper, not an implemented system or benchmark.
- **Limitation 2:** No prototype is provided by design.
- **Limitation 3:** Claims are conceptual and should be framed as a research direction.

General thesis-level limitation:

```text
Improving one agent component is not enough for generalized web automation.
A robust web agent still needs grounding, planning, execution, verification, recovery, and safety.
```

---

## Relation to S4

This paper belongs in S4 because S4 discusses **LLM-based agents for web/GUI/mobile/computer automation**.

Its role in S4 is:

```text
Build the Web for Agents, Not Agents for the Web
→ agentic web interface / position paper
→ supporting P2 source for web/GUI/computer-use agent discussion
```

Use it after explaining what the paper does. Do not introduce it only as “P2”; introduce the method or idea first.

---

## Relation to thesis topic

Your thesis topic is:

```text
LLM-based agents for generalized web automation and data extraction
```

This paper matters because:

It gives a strong conceptual argument for your thesis: generalized web automation may require redesigning the web, not only improving agents.

For generalized web automation, the connection is:

```text
web / GUI / mobile / computer-use interaction
→ agent observes a digital environment
→ agent chooses actions
→ agent extracts information or completes a workflow
```

Even when the paper is not directly about data extraction, it still helps explain the automation layer needed before extraction can be generalized.

---

## How to use this paper in the literature review

Recommended use:

- Use as **P2 support**, not as the central backbone.
- Use for one precise idea, architecture, benchmark, or limitation.
- If peer-reviewed, it can support stronger claims.
- If preprint/workshop/technical report, use it for recent trends and emerging directions.

Suggested sentence:

> Build the Web for Agents, Not Agents for the Web shows how agentic web interface / position paper contributes to the development of LLM-based agents for digital task automation, but its limitations indicate that generalized web automation still requires stronger grounding, verification, and recovery mechanisms.

---

## Reading decision

- **Keep in S4 P2:** Yes
- **Read fully?** No, selected sections are enough unless promoted later
- **Depth needed:** Low to medium
- **Main use:** Support S4 discussion of agentic web interface / position paper
- **Most important parts:**
  - Abstract
  - Introduction
  - Main architecture / method figure
  - Dataset or benchmark section
  - Results table
  - Limitations / discussion

---

## One-sentence summary

Build the Web for Agents, Not Agents for the Web is a P2 supporting paper for S4 because it explains **agentic web interface / position paper**, but it should be cited according to its venue/status and not overused beyond its evidence.

---

## BibTeX placeholder

```bibtex
@misc{buildthewebforagentsnotagentsforthe2025,
  title = {Build the Web for Agents, Not Agents for the Web},
  year = {2025},
  note = {arXiv position paper / under review; Position paper / preprint. Verify final bibliographic metadata before thesis submission.}
}
```


---

<!-- ========== FILE: S4_P2_paper_first_detailed_markdown_notes\S4_P2_27_Embodied_Web_Agents_Bridging_Physical-Digital_Realms_for_Integrated_Agent_Intelligence.md ========== -->

## Source: `S4_P2_paper_first_detailed_markdown_notes\S4_P2_27_Embodied_Web_Agents_Bridging_Physical-Digital_Realms_for_Integrated_Agent_Intelligence.md`

# S4 P2 Paper 27 — Embodied Web Agents: Bridging Physical-Digital Realms for Integrated Agent Intelligence

## Metadata

- **Title:** Embodied Web Agents: Bridging Physical-Digital Realms for Integrated Agent Intelligence
- **Year:** 2025
- **Venue / status:** arXiv preprint / under review
- **Peer-reviewed status:** No
- **Publication type:** Preprint / benchmark paper
- **Thesis section:** S4 — emerging web-agent paradigms
- **Category:** embodied web agents / physical-digital integration
- **Priority:** P2
- **BibTeX key:** `embodiedwebagentsbridgingphysicaldi2025`

---

## Simple understanding

This paper introduces embodied web agents: agents that combine physical embodied interaction with web-scale reasoning and online information access.

In simple terms:

```text
Problem → how can an AI agent interact with a web, GUI, mobile, desktop, or application environment?
Method → add perception, planning, action, memory, API/tool use, state tracking, or browser control.
Goal → complete real user tasks more flexibly than scripts or static chatbots.
```

This note explains the paper first, then connects it to S4 and your thesis.

---

## Core idea

Create environments and a benchmark where agents must coordinate between 3D physical environments and web interfaces.

The paper is mainly about:

```text
embodied web agents / physical-digital integration
```

It contributes to the larger agent loop:

```text
observe → understand state → plan → act → receive feedback → verify / recover → complete task
```

---

## Key finding / main claim

Current agents struggle with cross-domain integration between physical perception/action and web reasoning.

For S4, the important question is not only whether the method works on its benchmark, but **which part of web/GUI agency it improves**:

- perception and grounding,
- planning and reasoning,
- action execution,
- API/tool use,
- memory/state tracking,
- recovery and verification,
- or deployment/evaluation.

---

## Key evidence to extract from the paper

When reading the paper, extract these points:

- **Figure 1 examples: traveling, cooking, and geolocation tasks crossing web and embodied environments.**
- **Unified simulation platform integrating AI2-THOR, Google Earth, and web interfaces.**
- **Benchmark with about 1.5k tasks across cooking, navigation, shopping, tourism, and geolocation.**

These are the most useful parts for writing a literature-review paragraph.

---

## Limitations

- **Limitation 1:** Preprint/under-review status.
- **Limitation 2:** The paradigm is broader than web automation and requires simulated physical environments.
- **Limitation 3:** Benchmark results may not directly transfer to browser-only data extraction.

General thesis-level limitation:

```text
Improving one agent component is not enough for generalized web automation.
A robust web agent still needs grounding, planning, execution, verification, recovery, and safety.
```

---

## Relation to S4

This paper belongs in S4 because S4 discusses **LLM-based agents for web/GUI/mobile/computer automation**.

Its role in S4 is:

```text
Embodied Web Agents: Bridging Physical-Digital Realms for Integrated Agent Intelligence
→ embodied web agents / physical-digital integration
→ supporting P2 source for web/GUI/computer-use agent discussion
```

Use it after explaining what the paper does. Do not introduce it only as “P2”; introduce the method or idea first.

---

## Relation to thesis topic

Your thesis topic is:

```text
LLM-based agents for generalized web automation and data extraction
```

This paper matters because:

It helps show that web agents may become part of broader physical-digital agent systems.

For generalized web automation, the connection is:

```text
web / GUI / mobile / computer-use interaction
→ agent observes a digital environment
→ agent chooses actions
→ agent extracts information or completes a workflow
```

Even when the paper is not directly about data extraction, it still helps explain the automation layer needed before extraction can be generalized.

---

## How to use this paper in the literature review

Recommended use:

- Use as **P2 support**, not as the central backbone.
- Use for one precise idea, architecture, benchmark, or limitation.
- If peer-reviewed, it can support stronger claims.
- If preprint/workshop/technical report, use it for recent trends and emerging directions.

Suggested sentence:

> Embodied Web Agents: Bridging Physical-Digital Realms for Integrated Agent Intelligence shows how embodied web agents / physical-digital integration contributes to the development of LLM-based agents for digital task automation, but its limitations indicate that generalized web automation still requires stronger grounding, verification, and recovery mechanisms.

---

## Reading decision

- **Keep in S4 P2:** Yes
- **Read fully?** No, selected sections are enough unless promoted later
- **Depth needed:** Low to medium
- **Main use:** Support S4 discussion of embodied web agents / physical-digital integration
- **Most important parts:**
  - Abstract
  - Introduction
  - Main architecture / method figure
  - Dataset or benchmark section
  - Results table
  - Limitations / discussion

---

## One-sentence summary

Embodied Web Agents: Bridging Physical-Digital Realms for Integrated Agent Intelligence is a P2 supporting paper for S4 because it explains **embodied web agents / physical-digital integration**, but it should be cited according to its venue/status and not overused beyond its evidence.

---

## BibTeX placeholder

```bibtex
@misc{embodiedwebagentsbridgingphysicaldi2025,
  title = {Embodied Web Agents: Bridging Physical-Digital Realms for Integrated Agent Intelligence},
  year = {2025},
  note = {arXiv preprint / under review; Preprint / benchmark paper. Verify final bibliographic metadata before thesis submission.}
}
```


---

<!-- ========== FILE: S4_P2_paper_first_detailed_markdown_notes\S4_P2_28_Agentic_Web_Weaving_the_Next_Web_with_AI_Agents.md ========== -->

## Source: `S4_P2_paper_first_detailed_markdown_notes\S4_P2_28_Agentic_Web_Weaving_the_Next_Web_with_AI_Agents.md`

# S4 P2 Paper 28 — Agentic Web: Weaving the Next Web with AI Agents

## Metadata

- **Title:** Agentic Web: Weaving the Next Web with AI Agents
- **Year:** 2025
- **Venue / status:** arXiv survey / vision paper
- **Peer-reviewed status:** No confirmed archival venue
- **Publication type:** Survey / vision preprint
- **Thesis section:** S4 — Agentic Web framing
- **Category:** agentic web / web architecture and governance
- **Priority:** P2
- **BibTeX key:** `agenticwebweavingthenextwebwithaiag2025`

---

## Simple understanding

This paper presents a broad vision of the Agentic Web, where AI agents act, communicate, coordinate, and execute tasks across web services on behalf of users.

In simple terms:

```text
Problem → how can an AI agent interact with a web, GUI, mobile, desktop, or application environment?
Method → add perception, planning, action, memory, API/tool use, state tracking, or browser control.
Goal → complete real user tasks more flexibly than scripts or static chatbots.
```

This note explains the paper first, then connects it to S4 and your thesis.

---

## Core idea

Frame the Agentic Web through intelligence, interaction, and economics, including protocols, orchestration, applications, risks, and governance.

The paper is mainly about:

```text
agentic web / web architecture and governance
```

It contributes to the larger agent loop:

```text
observe → understand state → plan → act → receive feedback → verify / recover → complete task
```

---

## Key finding / main claim

The web may shift from human-driven browsing to agent-mediated workflows involving discovery, planning, inter-agent collaboration, and execution.

For S4, the important question is not only whether the method works on its benchmark, but **which part of web/GUI agency it improves**:

- perception and grounding,
- planning and reasoning,
- action execution,
- API/tool use,
- memory/state tracking,
- recovery and verification,
- or deployment/evaluation.

---

## Key evidence to extract from the paper

When reading the paper, extract these points:

- **Definition of Agentic Web.**
- **Figure 1 process cycle: user request → plan → agent discovery → inter-agent discussion → action → report.**
- **Discussion of MCP, A2A, agent attention economy, risks, and governance.**

These are the most useful parts for writing a literature-review paragraph.

---

## Limitations

- **Limitation 1:** Vision/survey preprint, not a primary empirical paper.
- **Limitation 2:** Broad scope means less depth on individual web-agent algorithms.
- **Limitation 3:** Future-looking claims should be phrased cautiously.

General thesis-level limitation:

```text
Improving one agent component is not enough for generalized web automation.
A robust web agent still needs grounding, planning, execution, verification, recovery, and safety.
```

---

## Relation to S4

This paper belongs in S4 because S4 discusses **LLM-based agents for web/GUI/mobile/computer automation**.

Its role in S4 is:

```text
Agentic Web: Weaving the Next Web with AI Agents
→ agentic web / web architecture and governance
→ supporting P2 source for web/GUI/computer-use agent discussion
```

Use it after explaining what the paper does. Do not introduce it only as “P2”; introduce the method or idea first.

---

## Relation to thesis topic

Your thesis topic is:

```text
LLM-based agents for generalized web automation and data extraction
```

This paper matters because:

It provides useful high-level framing for the future of web automation and web-agent ecosystems.

For generalized web automation, the connection is:

```text
web / GUI / mobile / computer-use interaction
→ agent observes a digital environment
→ agent chooses actions
→ agent extracts information or completes a workflow
```

Even when the paper is not directly about data extraction, it still helps explain the automation layer needed before extraction can be generalized.

---

## How to use this paper in the literature review

Recommended use:

- Use as **P2 support**, not as the central backbone.
- Use for one precise idea, architecture, benchmark, or limitation.
- If peer-reviewed, it can support stronger claims.
- If preprint/workshop/technical report, use it for recent trends and emerging directions.

Suggested sentence:

> Agentic Web: Weaving the Next Web with AI Agents shows how agentic web / web architecture and governance contributes to the development of LLM-based agents for digital task automation, but its limitations indicate that generalized web automation still requires stronger grounding, verification, and recovery mechanisms.

---

## Reading decision

- **Keep in S4 P2:** Yes
- **Read fully?** No, selected sections are enough unless promoted later
- **Depth needed:** Low to medium
- **Main use:** Support S4 discussion of agentic web / web architecture and governance
- **Most important parts:**
  - Abstract
  - Introduction
  - Main architecture / method figure
  - Dataset or benchmark section
  - Results table
  - Limitations / discussion

---

## One-sentence summary

Agentic Web: Weaving the Next Web with AI Agents is a P2 supporting paper for S4 because it explains **agentic web / web architecture and governance**, but it should be cited according to its venue/status and not overused beyond its evidence.

---

## BibTeX placeholder

```bibtex
@misc{agenticwebweavingthenextwebwithaiag2025,
  title = {Agentic Web: Weaving the Next Web with AI Agents},
  year = {2025},
  note = {arXiv survey / vision paper; Survey / vision preprint. Verify final bibliographic metadata before thesis submission.}
}
```


---

<!-- ========== FILE: S4_P2_paper_first_detailed_markdown_notes\S4_P2_29_CoAct-1_Computer-using_Agents_with_Coding_as_Actions.md ========== -->

## Source: `S4_P2_paper_first_detailed_markdown_notes\S4_P2_29_CoAct-1_Computer-using_Agents_with_Coding_as_Actions.md`

# S4 P2 Paper 29 — CoAct-1: Computer-using Agents with Coding as Actions

## Metadata

- **Title:** CoAct-1: Computer-using Agents with Coding as Actions
- **Year:** 2025
- **Venue / status:** arXiv preprint
- **Peer-reviewed status:** No confirmed archival venue
- **Publication type:** Preprint
- **Thesis section:** S4 — hybrid computer-use agents
- **Category:** computer-use agents / coding as actions
- **Priority:** P2
- **BibTeX key:** `coact1computerusingagentswithcoding2025`

---

## Simple understanding

CoAct-1 argues that computer-use agents should not rely only on GUI actions. It adds coding as an action, allowing agents to use Python or Bash when more reliable.

In simple terms:

```text
Problem → how can an AI agent interact with a web, GUI, mobile, desktop, or application environment?
Method → add perception, planning, action, memory, API/tool use, state tracking, or browser control.
Goal → complete real user tasks more flexibly than scripts or static chatbots.
```

This note explains the paper first, then connects it to S4 and your thesis.

---

## Core idea

Use a multi-agent system with an Orchestrator, Programmer, and GUI Operator to dynamically choose between GUI control and programmatic execution.

The paper is mainly about:

```text
computer-use agents / coding as actions
```

It contributes to the larger agent loop:

```text
observe → understand state → plan → act → receive feedback → verify / recover → complete task
```

---

## Key finding / main claim

CoAct-1 reports stronger OSWorld performance and fewer steps by replacing fragile GUI sequences with code when appropriate.

For S4, the important question is not only whether the method works on its benchmark, but **which part of web/GUI agency it improves**:

- perception and grounding,
- planning and reasoning,
- action execution,
- API/tool use,
- memory/state tracking,
- recovery and verification,
- or deployment/evaluation.

---

## Key evidence to extract from the paper

When reading the paper, extract these points:

- **Architecture with Orchestrator, Programmer, and GUI Operator.**
- **Reported OSWorld success rate of 60.76%.**
- **Average step reduction to 10.15 compared with about 15 for leading GUI agents.**

These are the most useful parts for writing a literature-review paragraph.

---

## Limitations

- **Limitation 1:** Preprint status.
- **Limitation 2:** Coding actions require sandboxing and security controls.
- **Limitation 3:** Some GUI tasks cannot be replaced by code, especially when APIs/files are inaccessible.

General thesis-level limitation:

```text
Improving one agent component is not enough for generalized web automation.
A robust web agent still needs grounding, planning, execution, verification, recovery, and safety.
```

---

## Relation to S4

This paper belongs in S4 because S4 discusses **LLM-based agents for web/GUI/mobile/computer automation**.

Its role in S4 is:

```text
CoAct-1: Computer-using Agents with Coding as Actions
→ computer-use agents / coding as actions
→ supporting P2 source for web/GUI/computer-use agent discussion
```

Use it after explaining what the paper does. Do not introduce it only as “P2”; introduce the method or idea first.

---

## Relation to thesis topic

Your thesis topic is:

```text
LLM-based agents for generalized web automation and data extraction
```

This paper matters because:

It supports the hybrid-action argument: generalized automation should combine GUI actions with code/tool execution.

For generalized web automation, the connection is:

```text
web / GUI / mobile / computer-use interaction
→ agent observes a digital environment
→ agent chooses actions
→ agent extracts information or completes a workflow
```

Even when the paper is not directly about data extraction, it still helps explain the automation layer needed before extraction can be generalized.

---

## How to use this paper in the literature review

Recommended use:

- Use as **P2 support**, not as the central backbone.
- Use for one precise idea, architecture, benchmark, or limitation.
- If peer-reviewed, it can support stronger claims.
- If preprint/workshop/technical report, use it for recent trends and emerging directions.

Suggested sentence:

> CoAct-1: Computer-using Agents with Coding as Actions shows how computer-use agents / coding as actions contributes to the development of LLM-based agents for digital task automation, but its limitations indicate that generalized web automation still requires stronger grounding, verification, and recovery mechanisms.

---

## Reading decision

- **Keep in S4 P2:** Yes
- **Read fully?** No, selected sections are enough unless promoted later
- **Depth needed:** Low to medium
- **Main use:** Support S4 discussion of computer-use agents / coding as actions
- **Most important parts:**
  - Abstract
  - Introduction
  - Main architecture / method figure
  - Dataset or benchmark section
  - Results table
  - Limitations / discussion

---

## One-sentence summary

CoAct-1: Computer-using Agents with Coding as Actions is a P2 supporting paper for S4 because it explains **computer-use agents / coding as actions**, but it should be cited according to its venue/status and not overused beyond its evidence.

---

## BibTeX placeholder

```bibtex
@misc{coact1computerusingagentswithcoding2025,
  title = {CoAct-1: Computer-using Agents with Coding as Actions},
  year = {2025},
  note = {arXiv preprint; Preprint. Verify final bibliographic metadata before thesis submission.}
}
```


---

<!-- ========== FILE: S4_P2_paper_first_detailed_markdown_notes\S4_P2_30_OpenCUA_Open_Foundations_for_Computer-Use_Agents.md ========== -->

## Source: `S4_P2_paper_first_detailed_markdown_notes\S4_P2_30_OpenCUA_Open_Foundations_for_Computer-Use_Agents.md`

# S4 P2 Paper 30 — OpenCUA: Open Foundations for Computer-Use Agents

## Metadata

- **Title:** OpenCUA: Open Foundations for Computer-Use Agents
- **Year:** 2025
- **Venue / status:** NeurIPS 2025
- **Peer-reviewed status:** Yes
- **Publication type:** Peer-reviewed conference paper
- **Thesis section:** S4 — computer-use agent foundations
- **Category:** open computer-use agent foundation / dataset and model
- **Priority:** P2
- **BibTeX key:** `opencuaopenfoundationsforcomputerus2025`

---

## Simple understanding

OpenCUA provides an open-source framework, dataset, benchmark, and models for computer-use agents. It addresses the lack of open foundations for CUA research.

In simple terms:

```text
Problem → how can an AI agent interact with a web, GUI, mobile, desktop, or application environment?
Method → add perception, planning, action, memory, API/tool use, state tracking, or browser control.
Goal → complete real user tasks more flexibly than scripts or static chatbots.
```

This note explains the paper first, then connects it to S4 and your thesis.

---

## Core idea

Collect large-scale human computer-use demonstrations, convert them into state-action trajectories with reflective CoT, and train open CUA models.

The paper is mainly about:

```text
open computer-use agent foundation / dataset and model
```

It contributes to the larger agent loop:

```text
observe → understand state → plan → act → receive feedback → verify / recover → complete task
```

---

## Key finding / main claim

OpenCUA reports state-of-the-art open-source performance on OSWorld-Verified and strong cross-domain generalization.

For S4, the important question is not only whether the method works on its benchmark, but **which part of web/GUI agency it improves**:

- perception and grounding,
- planning and reasoning,
- action execution,
- API/tool use,
- memory/state tracking,
- recovery and verification,
- or deployment/evaluation.

---

## Key evidence to extract from the paper

When reading the paper, extract these points:

- **Figure 2 overview of OpenCUA framework and AgentNet pipeline.**
- **AGENTNET dataset: 22.6K trajectories across 100+ applications and 200 websites across Windows, macOS, and Ubuntu.**
- **OpenCUA-72B reported 45.0% success on OSWorld-Verified.**

These are the most useful parts for writing a literature-review paragraph.

---

## Limitations

- **Limitation 1:** Computer-use agents are broader than web agents and include desktop applications.
- **Limitation 2:** Performance still remains far below perfect reliability.
- **Limitation 3:** Large-scale data collection and privacy controls are complex.

General thesis-level limitation:

```text
Improving one agent component is not enough for generalized web automation.
A robust web agent still needs grounding, planning, execution, verification, recovery, and safety.
```

---

## Relation to S4

This paper belongs in S4 because S4 discusses **LLM-based agents for web/GUI/mobile/computer automation**.

Its role in S4 is:

```text
OpenCUA: Open Foundations for Computer-Use Agents
→ open computer-use agent foundation / dataset and model
→ supporting P2 source for web/GUI/computer-use agent discussion
```

Use it after explaining what the paper does. Do not introduce it only as “P2”; introduce the method or idea first.

---

## Relation to thesis topic

Your thesis topic is:

```text
LLM-based agents for generalized web automation and data extraction
```

This paper matters because:

It is one of the strongest recent sources for open computer-use agent data, models, and evaluation.

For generalized web automation, the connection is:

```text
web / GUI / mobile / computer-use interaction
→ agent observes a digital environment
→ agent chooses actions
→ agent extracts information or completes a workflow
```

Even when the paper is not directly about data extraction, it still helps explain the automation layer needed before extraction can be generalized.

---

## How to use this paper in the literature review

Recommended use:

- Use as **P2 support**, not as the central backbone.
- Use for one precise idea, architecture, benchmark, or limitation.
- If peer-reviewed, it can support stronger claims.
- If preprint/workshop/technical report, use it for recent trends and emerging directions.

Suggested sentence:

> OpenCUA: Open Foundations for Computer-Use Agents shows how open computer-use agent foundation / dataset and model contributes to the development of LLM-based agents for digital task automation, but its limitations indicate that generalized web automation still requires stronger grounding, verification, and recovery mechanisms.

---

## Reading decision

- **Keep in S4 P2:** Yes
- **Read fully?** Yes or selected sections carefully
- **Depth needed:** Medium to high
- **Main use:** Support S4 discussion of open computer-use agent foundation / dataset and model
- **Most important parts:**
  - Abstract
  - Introduction
  - Main architecture / method figure
  - Dataset or benchmark section
  - Results table
  - Limitations / discussion

---

## One-sentence summary

OpenCUA: Open Foundations for Computer-Use Agents is a P2 supporting paper for S4 because it explains **open computer-use agent foundation / dataset and model**, but it should be cited according to its venue/status and not overused beyond its evidence.

---

## BibTeX placeholder

```bibtex
@misc{opencuaopenfoundationsforcomputerus2025,
  title = {OpenCUA: Open Foundations for Computer-Use Agents},
  year = {2025},
  note = {NeurIPS 2025; Peer-reviewed conference paper. Verify final bibliographic metadata before thesis submission.}
}
```


---

<!-- ========== FILE: S4_P2_paper_first_detailed_markdown_notes\S4_P2_31_Are_LLM_Agents_the_New_RPA_A_Comparative_Study_with_RPA_Across_Enterprise_Workflows.md ========== -->

## Source: `S4_P2_paper_first_detailed_markdown_notes\S4_P2_31_Are_LLM_Agents_the_New_RPA_A_Comparative_Study_with_RPA_Across_Enterprise_Workflows.md`

# S4 P2 Paper 31 — Are LLM Agents the New RPA? A Comparative Study with RPA Across Enterprise Workflows

## Metadata

- **Title:** Are LLM Agents the New RPA? A Comparative Study with RPA Across Enterprise Workflows
- **Year:** 2025
- **Venue / status:** Uploaded copy does not show confirmed venue
- **Peer-reviewed status:** Unclear / likely preprint or proceedings draft
- **Publication type:** Comparative study / unclear venue
- **Thesis section:** S4 — enterprise automation and RPA comparison
- **Category:** LLM agents vs RPA / enterprise automation
- **Priority:** P2
- **BibTeX key:** `arellmagentsthenewrpaacomparativest2025`

---

## Simple understanding

This paper compares LLM agents with traditional RPA across enterprise workflows such as data entry, monitoring, and document extraction.

In simple terms:

```text
Problem → how can an AI agent interact with a web, GUI, mobile, desktop, or application environment?
Method → add perception, planning, action, memory, API/tool use, state tracking, or browser control.
Goal → complete real user tasks more flexibly than scripts or static chatbots.
```

This note explains the paper first, then connects it to S4 and your thesis.

---

## Core idea

Empirically compare RPA tools and agentic automation with computer use in terms of speed, reliability, and development effort.

The paper is mainly about:

```text
LLM agents vs RPA / enterprise automation
```

It contributes to the larger agent loop:

```text
observe → understand state → plan → act → receive feedback → verify / recover → complete task
```

---

## Key finding / main claim

RPA remains faster and more reliable in stable repetitive environments, while LLM agents reduce development time and adapt more flexibly to dynamic interfaces.

For S4, the important question is not only whether the method works on its benchmark, but **which part of web/GUI agency it improves**:

- perception and grounding,
- planning and reasoning,
- action execution,
- API/tool use,
- memory/state tracking,
- recovery and verification,
- or deployment/evaluation.

---

## Key evidence to extract from the paper

When reading the paper, extract these points:

- **Three hypotheses comparing speed, reliability, and development time.**
- **Tasks from rpachallenge.com.**
- **Conclusion that AACU is promising but not yet production-ready compared with RPA.**

These are the most useful parts for writing a literature-review paragraph.

---

## Limitations

- **Limitation 1:** Final venue/status is unclear from the uploaded copy.
- **Limitation 2:** Evaluation covers only a small number of RPA-style workflows.
- **Limitation 3:** Current AACU tools may change rapidly, so results can become outdated.

General thesis-level limitation:

```text
Improving one agent component is not enough for generalized web automation.
A robust web agent still needs grounding, planning, execution, verification, recovery, and safety.
```

---

## Relation to S4

This paper belongs in S4 because S4 discusses **LLM-based agents for web/GUI/mobile/computer automation**.

Its role in S4 is:

```text
Are LLM Agents the New RPA? A Comparative Study with RPA Across Enterprise Workflows
→ LLM agents vs RPA / enterprise automation
→ supporting P2 source for web/GUI/computer-use agent discussion
```

Use it after explaining what the paper does. Do not introduce it only as “P2”; introduce the method or idea first.

---

## Relation to thesis topic

Your thesis topic is:

```text
LLM-based agents for generalized web automation and data extraction
```

This paper matters because:

It is useful for your thesis because it directly compares LLM agent automation with classical RPA.

For generalized web automation, the connection is:

```text
web / GUI / mobile / computer-use interaction
→ agent observes a digital environment
→ agent chooses actions
→ agent extracts information or completes a workflow
```

Even when the paper is not directly about data extraction, it still helps explain the automation layer needed before extraction can be generalized.

---

## How to use this paper in the literature review

Recommended use:

- Use as **P2 support**, not as the central backbone.
- Use for one precise idea, architecture, benchmark, or limitation.
- If peer-reviewed, it can support stronger claims.
- If preprint/workshop/technical report, use it for recent trends and emerging directions.

Suggested sentence:

> Are LLM Agents the New RPA? A Comparative Study with RPA Across Enterprise Workflows shows how LLM agents vs RPA / enterprise automation contributes to the development of LLM-based agents for digital task automation, but its limitations indicate that generalized web automation still requires stronger grounding, verification, and recovery mechanisms.

---

## Reading decision

- **Keep in S4 P2:** Yes
- **Read fully?** No, selected sections are enough unless promoted later
- **Depth needed:** Low to medium
- **Main use:** Support S4 discussion of LLM agents vs RPA / enterprise automation
- **Most important parts:**
  - Abstract
  - Introduction
  - Main architecture / method figure
  - Dataset or benchmark section
  - Results table
  - Limitations / discussion

---

## One-sentence summary

Are LLM Agents the New RPA? A Comparative Study with RPA Across Enterprise Workflows is a P2 supporting paper for S4 because it explains **LLM agents vs RPA / enterprise automation**, but it should be cited according to its venue/status and not overused beyond its evidence.

---

## BibTeX placeholder

```bibtex
@misc{arellmagentsthenewrpaacomparativest2025,
  title = {Are LLM Agents the New RPA? A Comparative Study with RPA Across Enterprise Workflows},
  year = {2025},
  note = {Uploaded copy does not show confirmed venue; Comparative study / unclear venue. Verify final bibliographic metadata before thesis submission.}
}
```


---

<!-- ========== FILE: S4_P2_paper_first_detailed_markdown_notes\S4_P2_32_BrowserAgent_Building_Web_Agents_with_Human-Inspired_Web_Browsing_Actions.md ========== -->

## Source: `S4_P2_paper_first_detailed_markdown_notes\S4_P2_32_BrowserAgent_Building_Web_Agents_with_Human-Inspired_Web_Browsing_Actions.md`

# S4 P2 Paper 32 — BrowserAgent: Building Web Agents with Human-Inspired Web Browsing Actions

## Metadata

- **Title:** BrowserAgent: Building Web Agents with Human-Inspired Web Browsing Actions
- **Year:** 2025
- **Venue / status:** arXiv preprint / work in progress
- **Peer-reviewed status:** No
- **Publication type:** Work-in-progress preprint
- **Thesis section:** S4 — browser-native web agents
- **Category:** browser-native web agents
- **Priority:** P2
- **BibTeX key:** `browseragentbuildingwebagentswithhu2025`

---

## Simple understanding

BrowserAgent trains web agents to use human-inspired browser actions such as scrolling, clicking, typing, and tab management rather than relying on static text extraction.

In simple terms:

```text
Problem → how can an AI agent interact with a web, GUI, mobile, desktop, or application environment?
Method → add perception, planning, action, memory, API/tool use, state tracking, or browser control.
Goal → complete real user tasks more flexibly than scripts or static chatbots.
```

This note explains the paper first, then connects it to S4 and your thesis.

---

## Core idea

Build a browser-native agent framework that interacts with raw web pages through Playwright and trains with SFT followed by rejection fine-tuning.

The paper is mainly about:

```text
browser-native web agents
```

It contributes to the larger agent loop:

```text
observe → understand state → plan → act → receive feedback → verify / recover → complete task
```

---

## Key finding / main claim

BrowserAgent reports strong results on open QA and multi-hop QA tasks while using less training data than some search-agent baselines.

For S4, the important question is not only whether the method works on its benchmark, but **which part of web/GUI agency it improves**:

- perception and grounding,
- planning and reasoning,
- action execution,
- API/tool use,
- memory/state tracking,
- recovery and verification,
- or deployment/evaluation.

---

## Key evidence to extract from the paper

When reading the paper, extract these points:

- **Figure 2 comparing BrowserAgent with traditional deep research pipeline.**
- **Action set: click, type, scroll, hover, goto, and tab/browser operations.**
- **Reported around 20% improvement over Search-R1 on multi-hop QA tasks.**

These are the most useful parts for writing a literature-review paragraph.

---

## Limitations

- **Limitation 1:** Marked Work in Progress, so cite carefully.
- **Limitation 2:** QA-focused browser interaction differs from transactional web automation.
- **Limitation 3:** Results depend on browser orchestration infrastructure and training data quality.

General thesis-level limitation:

```text
Improving one agent component is not enough for generalized web automation.
A robust web agent still needs grounding, planning, execution, verification, recovery, and safety.
```

---

## Relation to S4

This paper belongs in S4 because S4 discusses **LLM-based agents for web/GUI/mobile/computer automation**.

Its role in S4 is:

```text
BrowserAgent: Building Web Agents with Human-Inspired Web Browsing Actions
→ browser-native web agents
→ supporting P2 source for web/GUI/computer-use agent discussion
```

Use it after explaining what the paper does. Do not introduce it only as “P2”; introduce the method or idea first.

---

## Relation to thesis topic

Your thesis topic is:

```text
LLM-based agents for generalized web automation and data extraction
```

This paper matters because:

It supports a recent trend: training agents to interact with the live browser instead of only processed HTML or search summaries.

For generalized web automation, the connection is:

```text
web / GUI / mobile / computer-use interaction
→ agent observes a digital environment
→ agent chooses actions
→ agent extracts information or completes a workflow
```

Even when the paper is not directly about data extraction, it still helps explain the automation layer needed before extraction can be generalized.

---

## How to use this paper in the literature review

Recommended use:

- Use as **P2 support**, not as the central backbone.
- Use for one precise idea, architecture, benchmark, or limitation.
- If peer-reviewed, it can support stronger claims.
- If preprint/workshop/technical report, use it for recent trends and emerging directions.

Suggested sentence:

> BrowserAgent: Building Web Agents with Human-Inspired Web Browsing Actions shows how browser-native web agents contributes to the development of LLM-based agents for digital task automation, but its limitations indicate that generalized web automation still requires stronger grounding, verification, and recovery mechanisms.

---

## Reading decision

- **Keep in S4 P2:** Yes
- **Read fully?** No, selected sections are enough unless promoted later
- **Depth needed:** Low to medium
- **Main use:** Support S4 discussion of browser-native web agents
- **Most important parts:**
  - Abstract
  - Introduction
  - Main architecture / method figure
  - Dataset or benchmark section
  - Results table
  - Limitations / discussion

---

## One-sentence summary

BrowserAgent: Building Web Agents with Human-Inspired Web Browsing Actions is a P2 supporting paper for S4 because it explains **browser-native web agents**, but it should be cited according to its venue/status and not overused beyond its evidence.

---

## BibTeX placeholder

```bibtex
@misc{browseragentbuildingwebagentswithhu2025,
  title = {BrowserAgent: Building Web Agents with Human-Inspired Web Browsing Actions},
  year = {2025},
  note = {arXiv preprint / work in progress; Work-in-progress preprint. Verify final bibliographic metadata before thesis submission.}
}
```


---

<!-- ========== FILE: S4_P2_paper_first_detailed_markdown_notes\S4_P2_33_UltraCUA_A_Foundation_Model_for_Computer_Use_Agents_with_Hybrid_Action.md ========== -->

## Source: `S4_P2_paper_first_detailed_markdown_notes\S4_P2_33_UltraCUA_A_Foundation_Model_for_Computer_Use_Agents_with_Hybrid_Action.md`

# S4 P2 Paper 33 — UltraCUA: A Foundation Model for Computer Use Agents with Hybrid Action

## Metadata

- **Title:** UltraCUA: A Foundation Model for Computer Use Agents with Hybrid Action
- **Year:** 2025
- **Venue / status:** arXiv preprint
- **Peer-reviewed status:** No confirmed archival venue
- **Publication type:** Preprint
- **Thesis section:** S4 — hybrid computer-use agents
- **Category:** hybrid-action computer-use foundation model
- **Priority:** P2
- **BibTeX key:** `ultracuaafoundationmodelforcomputer2025`

---

## Simple understanding

UltraCUA proposes a foundation model for computer-use agents that can use both low-level GUI actions and high-level programmatic tool calls.

In simple terms:

```text
Problem → how can an AI agent interact with a web, GUI, mobile, desktop, or application environment?
Method → add perception, planning, action, memory, API/tool use, state tracking, or browser control.
Goal → complete real user tasks more flexibly than scripts or static chatbots.
```

This note explains the paper first, then connects it to S4 and your thesis.

---

## Core idea

Train CUA models with hybrid action trajectories so they learn when to click/type/scroll and when to call tools.

The paper is mainly about:

```text
hybrid-action computer-use foundation model
```

It contributes to the larger agent loop:

```text
observe → understand state → plan → act → receive feedback → verify / recover → complete task
```

---

## Key finding / main claim

UltraCUA reports improved OSWorld and WindowsAgentArena performance, arguing that hybrid action reduces cascading GUI errors.

For S4, the important question is not only whether the method works on its benchmark, but **which part of web/GUI agency it improves**:

- perception and grounding,
- planning and reasoning,
- action execution,
- API/tool use,
- memory/state tracking,
- recovery and verification,
- or deployment/evaluation.

---

## Key evidence to extract from the paper

When reading the paper, extract these points:

- **Figure 1 comparing GUI-only cascade errors with hybrid tool calls.**
- **Figure 2 showing tool collection, task synthesis, trajectory collection, and SFT/RL training.**
- **Reported OSWorld and WindowsAgentArena gains.**

These are the most useful parts for writing a literature-review paragraph.

---

## Limitations

- **Limitation 1:** Preprint status.
- **Limitation 2:** Tool extraction and hybrid trajectory generation may be difficult to reproduce.
- **Limitation 3:** Hybrid action requires safe tool execution and reliable tool availability.

General thesis-level limitation:

```text
Improving one agent component is not enough for generalized web automation.
A robust web agent still needs grounding, planning, execution, verification, recovery, and safety.
```

---

## Relation to S4

This paper belongs in S4 because S4 discusses **LLM-based agents for web/GUI/mobile/computer automation**.

Its role in S4 is:

```text
UltraCUA: A Foundation Model for Computer Use Agents with Hybrid Action
→ hybrid-action computer-use foundation model
→ supporting P2 source for web/GUI/computer-use agent discussion
```

Use it after explaining what the paper does. Do not introduce it only as “P2”; introduce the method or idea first.

---

## Relation to thesis topic

Your thesis topic is:

```text
LLM-based agents for generalized web automation and data extraction
```

This paper matters because:

It reinforces the argument that future agents should combine GUI universality with API/tool precision.

For generalized web automation, the connection is:

```text
web / GUI / mobile / computer-use interaction
→ agent observes a digital environment
→ agent chooses actions
→ agent extracts information or completes a workflow
```

Even when the paper is not directly about data extraction, it still helps explain the automation layer needed before extraction can be generalized.

---

## How to use this paper in the literature review

Recommended use:

- Use as **P2 support**, not as the central backbone.
- Use for one precise idea, architecture, benchmark, or limitation.
- If peer-reviewed, it can support stronger claims.
- If preprint/workshop/technical report, use it for recent trends and emerging directions.

Suggested sentence:

> UltraCUA: A Foundation Model for Computer Use Agents with Hybrid Action shows how hybrid-action computer-use foundation model contributes to the development of LLM-based agents for digital task automation, but its limitations indicate that generalized web automation still requires stronger grounding, verification, and recovery mechanisms.

---

## Reading decision

- **Keep in S4 P2:** Yes
- **Read fully?** No, selected sections are enough unless promoted later
- **Depth needed:** Low to medium
- **Main use:** Support S4 discussion of hybrid-action computer-use foundation model
- **Most important parts:**
  - Abstract
  - Introduction
  - Main architecture / method figure
  - Dataset or benchmark section
  - Results table
  - Limitations / discussion

---

## One-sentence summary

UltraCUA: A Foundation Model for Computer Use Agents with Hybrid Action is a P2 supporting paper for S4 because it explains **hybrid-action computer-use foundation model**, but it should be cited according to its venue/status and not overused beyond its evidence.

---

## BibTeX placeholder

```bibtex
@misc{ultracuaafoundationmodelforcomputer2025,
  title = {UltraCUA: A Foundation Model for Computer Use Agents with Hybrid Action},
  year = {2025},
  note = {arXiv preprint; Preprint. Verify final bibliographic metadata before thesis submission.}
}
```


---

<!-- ========== FILE: S4_P2_paper_first_detailed_markdown_notes\S4_P2_34_Agent-SAMA_State-Aware_Mobile_Assistant.md ========== -->

## Source: `S4_P2_paper_first_detailed_markdown_notes\S4_P2_34_Agent-SAMA_State-Aware_Mobile_Assistant.md`

# S4 P2 Paper 34 — Agent-SAMA: State-Aware Mobile Assistant

## Metadata

- **Title:** Agent-SAMA: State-Aware Mobile Assistant
- **Year:** 2025
- **Venue / status:** arXiv preprint
- **Peer-reviewed status:** No confirmed archival venue
- **Publication type:** Preprint
- **Thesis section:** S4 — state-aware GUI/mobile agents
- **Category:** state-aware mobile agents / FSM memory
- **Priority:** P2
- **BibTeX key:** `agentsamastateawaremobileassistant2025`

---

## Simple understanding

Agent-SAMA is a state-aware mobile assistant that models mobile app execution as a finite state machine. It uses app states and transitions for planning, verification, and recovery.

In simple terms:

```text
Problem → how can an AI agent interact with a web, GUI, mobile, desktop, or application environment?
Method → add perception, planning, action, memory, API/tool use, state tracking, or browser control.
Goal → complete real user tasks more flexibly than scripts or static chatbots.
```

This note explains the paper first, then connects it to S4 and your thesis.

---

## Core idea

Use four agents to build and exploit FSMs in real time: planning, screen parsing/state modeling, acting, reflection/recovery, and memory retention.

The paper is mainly about:

```text
state-aware mobile agents / FSM memory
```

It contributes to the larger agent loop:

```text
observe → understand state → plan → act → receive feedback → verify / recover → complete task
```

---

## Key finding / main claim

Agent-SAMA reports higher success and recovery rates on Mobile-Eval-E, SPA-Bench, and AndroidWorld by using structured state modeling.

For S4, the important question is not only whether the method works on its benchmark, but **which part of web/GUI agency it improves**:

- perception and grounding,
- planning and reasoning,
- action execution,
- API/tool use,
- memory/state tracking,
- recovery and verification,
- or deployment/evaluation.

---

## Key evidence to extract from the paper

When reading the paper, extract these points:

- **FSM formulation: UI screens as states and actions as transitions.**
- **Reported 84.0% success and 71.9% recovery on Mobile-Eval-E.**
- **Four phases: planning, execution, error recovery/verification, and knowledge retention.**

These are the most useful parts for writing a literature-review paragraph.

---

## Limitations

- **Limitation 1:** Preprint status.
- **Limitation 2:** FSM construction may be imperfect when screens are visually similar or highly dynamic.
- **Limitation 3:** Mobile app state modeling may not directly transfer to web pages with complex DOM states.

General thesis-level limitation:

```text
Improving one agent component is not enough for generalized web automation.
A robust web agent still needs grounding, planning, execution, verification, recovery, and safety.
```

---

## Relation to S4

This paper belongs in S4 because S4 discusses **LLM-based agents for web/GUI/mobile/computer automation**.

Its role in S4 is:

```text
Agent-SAMA: State-Aware Mobile Assistant
→ state-aware mobile agents / FSM memory
→ supporting P2 source for web/GUI/computer-use agent discussion
```

Use it after explaining what the paper does. Do not introduce it only as “P2”; introduce the method or idea first.

---

## Relation to thesis topic

Your thesis topic is:

```text
LLM-based agents for generalized web automation and data extraction
```

This paper matters because:

It is useful for discussing memory/state tracking as a solution to reactive GUI-agent limitations.

For generalized web automation, the connection is:

```text
web / GUI / mobile / computer-use interaction
→ agent observes a digital environment
→ agent chooses actions
→ agent extracts information or completes a workflow
```

Even when the paper is not directly about data extraction, it still helps explain the automation layer needed before extraction can be generalized.

---

## How to use this paper in the literature review

Recommended use:

- Use as **P2 support**, not as the central backbone.
- Use for one precise idea, architecture, benchmark, or limitation.
- If peer-reviewed, it can support stronger claims.
- If preprint/workshop/technical report, use it for recent trends and emerging directions.

Suggested sentence:

> Agent-SAMA: State-Aware Mobile Assistant shows how state-aware mobile agents / FSM memory contributes to the development of LLM-based agents for digital task automation, but its limitations indicate that generalized web automation still requires stronger grounding, verification, and recovery mechanisms.

---

## Reading decision

- **Keep in S4 P2:** Yes
- **Read fully?** No, selected sections are enough unless promoted later
- **Depth needed:** Low to medium
- **Main use:** Support S4 discussion of state-aware mobile agents / FSM memory
- **Most important parts:**
  - Abstract
  - Introduction
  - Main architecture / method figure
  - Dataset or benchmark section
  - Results table
  - Limitations / discussion

---

## One-sentence summary

Agent-SAMA: State-Aware Mobile Assistant is a P2 supporting paper for S4 because it explains **state-aware mobile agents / FSM memory**, but it should be cited according to its venue/status and not overused beyond its evidence.

---

## BibTeX placeholder

```bibtex
@misc{agentsamastateawaremobileassistant2025,
  title = {Agent-SAMA: State-Aware Mobile Assistant},
  year = {2025},
  note = {arXiv preprint; Preprint. Verify final bibliographic metadata before thesis submission.}
}
```


---

<!-- ========== FILE: S4_P2_paper_first_detailed_markdown_notes\S4_P2_35_Building_the_Web_for_Agents_A_Declarative_Framework_for_AgentWeb_Interaction.md ========== -->

## Source: `S4_P2_paper_first_detailed_markdown_notes\S4_P2_35_Building_the_Web_for_Agents_A_Declarative_Framework_for_AgentWeb_Interaction.md`

# S4 P2 Paper 35 — Building the Web for Agents: A Declarative Framework for Agent–Web Interaction

## Metadata

- **Title:** Building the Web for Agents: A Declarative Framework for Agent–Web Interaction
- **Year:** 2025
- **Venue / status:** arXiv preprint
- **Peer-reviewed status:** No confirmed archival venue
- **Publication type:** Preprint
- **Thesis section:** S4 — agentic web interface design
- **Category:** declarative agent-web interface / VOIX
- **Priority:** P2
- **BibTeX key:** `buildingthewebforagentsadeclarative2025`

---

## Simple understanding

This paper proposes VOIX, a declarative framework that lets websites expose machine-readable tools and context to AI agents using HTML tags.

In simple terms:

```text
Problem → how can an AI agent interact with a web, GUI, mobile, desktop, or application environment?
Method → add perception, planning, action, memory, API/tool use, state tracking, or browser control.
Goal → complete real user tasks more flexibly than scripts or static chatbots.
```

This note explains the paper first, then connects it to S4 and your thesis.

---

## Core idea

Introduce <tool> and <context> tags so developers can explicitly define available actions and relevant state for agents.

The paper is mainly about:

```text
declarative agent-web interface / VOIX
```

It contributes to the larger agent loop:

```text
observe → understand state → plan → act → receive feedback → verify / recover → complete task
```

---

## Key finding / main claim

The paper argues that declarative agent-web contracts can improve reliability, auditability, privacy, and developer control compared with scraping DOM/screenshots.

For S4, the important question is not only whether the method works on its benchmark, but **which part of web/GUI agency it improves**:

- perception and grounding,
- planning and reasoning,
- action execution,
- API/tool use,
- memory/state tracking,
- recovery and verification,
- or deployment/evaluation.

---

## Key evidence to extract from the paper

When reading the paper, extract these points:

- **VOIX mechanism with <tool> and <context> tags.**
- **Three-day hackathon study with 16 developers.**
- **Argument that machine-native affordances reduce brittle inference from human UI.**

These are the most useful parts for writing a literature-review paragraph.

---

## Limitations

- **Limitation 1:** Preprint status.
- **Limitation 2:** Hackathon evaluation with 16 developers is useful but limited.
- **Limitation 3:** Standard adoption would require ecosystem-level agreement.

General thesis-level limitation:

```text
Improving one agent component is not enough for generalized web automation.
A robust web agent still needs grounding, planning, execution, verification, recovery, and safety.
```

---

## Relation to S4

This paper belongs in S4 because S4 discusses **LLM-based agents for web/GUI/mobile/computer automation**.

Its role in S4 is:

```text
Building the Web for Agents: A Declarative Framework for Agent–Web Interaction
→ declarative agent-web interface / VOIX
→ supporting P2 source for web/GUI/computer-use agent discussion
```

Use it after explaining what the paper does. Do not introduce it only as “P2”; introduce the method or idea first.

---

## Relation to thesis topic

Your thesis topic is:

```text
LLM-based agents for generalized web automation and data extraction
```

This paper matters because:

It operationalizes the Agentic Web idea with a concrete declarative framework, directly relevant to generalized web automation.

For generalized web automation, the connection is:

```text
web / GUI / mobile / computer-use interaction
→ agent observes a digital environment
→ agent chooses actions
→ agent extracts information or completes a workflow
```

Even when the paper is not directly about data extraction, it still helps explain the automation layer needed before extraction can be generalized.

---

## How to use this paper in the literature review

Recommended use:

- Use as **P2 support**, not as the central backbone.
- Use for one precise idea, architecture, benchmark, or limitation.
- If peer-reviewed, it can support stronger claims.
- If preprint/workshop/technical report, use it for recent trends and emerging directions.

Suggested sentence:

> Building the Web for Agents: A Declarative Framework for Agent–Web Interaction shows how declarative agent-web interface / VOIX contributes to the development of LLM-based agents for digital task automation, but its limitations indicate that generalized web automation still requires stronger grounding, verification, and recovery mechanisms.

---

## Reading decision

- **Keep in S4 P2:** Yes
- **Read fully?** No, selected sections are enough unless promoted later
- **Depth needed:** Low to medium
- **Main use:** Support S4 discussion of declarative agent-web interface / VOIX
- **Most important parts:**
  - Abstract
  - Introduction
  - Main architecture / method figure
  - Dataset or benchmark section
  - Results table
  - Limitations / discussion

---

## One-sentence summary

Building the Web for Agents: A Declarative Framework for Agent–Web Interaction is a P2 supporting paper for S4 because it explains **declarative agent-web interface / VOIX**, but it should be cited according to its venue/status and not overused beyond its evidence.

---

## BibTeX placeholder

```bibtex
@misc{buildingthewebforagentsadeclarative2025,
  title = {Building the Web for Agents: A Declarative Framework for Agent–Web Interaction},
  year = {2025},
  note = {arXiv preprint; Preprint. Verify final bibliographic metadata before thesis submission.}
}
```


---

<!-- ========== FILE: S4_P2_paper_first_detailed_markdown_notes\S4_P2_36_LegalWebAgent_Empowering_Access_to_Justice_via_LLM-Based_Web_Agents.md ========== -->

## Source: `S4_P2_paper_first_detailed_markdown_notes\S4_P2_36_LegalWebAgent_Empowering_Access_to_Justice_via_LLM-Based_Web_Agents.md`

# S4 P2 Paper 36 — LegalWebAgent: Empowering Access to Justice via LLM-Based Web Agents

## Metadata

- **Title:** LegalWebAgent: Empowering Access to Justice via LLM-Based Web Agents
- **Year:** 2025
- **Venue / status:** AI4A2J Workshop 2025, to appear
- **Peer-reviewed status:** Workshop / pending final proceedings
- **Publication type:** Workshop paper / domain case study
- **Thesis section:** S4 — domain-specific web agents
- **Category:** domain-specific legal web agent
- **Priority:** P2
- **BibTeX key:** `legalwebagentempoweringaccesstojust2025`

---

## Simple understanding

LegalWebAgent is a multimodal web-agent framework for legal access-to-justice tasks. It helps users search legal information, navigate websites, fill forms, and book appointments.

In simple terms:

```text
Problem → how can an AI agent interact with a web, GUI, mobile, desktop, or application environment?
Method → add perception, planning, action, memory, API/tool use, state tracking, or browser control.
Goal → complete real user tasks more flexibly than scripts or static chatbots.
```

This note explains the paper first, then connects it to S4 and your thesis.

---

## Core idea

Use Ask, Browse, and Act modules to understand user needs, navigate legal websites using HTML and screenshots, and perform concrete web actions.

The paper is mainly about:

```text
domain-specific legal web agent
```

It contributes to the larger agent loop:

```text
observe → understand state → plan → act → receive feedback → verify / recover → complete task
```

---

## Key finding / main claim

The paper reports high task success on a benchmark of Québec civil-law web tasks.

For S4, the important question is not only whether the method works on its benchmark, but **which part of web/GUI agency it improves**:

- perception and grounding,
- planning and reasoning,
- action execution,
- API/tool use,
- memory/state tracking,
- recovery and verification,
- or deployment/evaluation.

---

## Key evidence to extract from the paper

When reading the paper, extract these points:

- **Figure 1 workflow: Ask → Browse → Act modules with web browser environment.**
- **Benchmark of 15 Québec civil-law tasks.**
- **Reported peak success rate 86.7% and average 84.4% across tested models.**

These are the most useful parts for writing a literature-review paragraph.

---

## Limitations

- **Limitation 1:** Workshop/pending venue; cite carefully.
- **Limitation 2:** Legal tasks are high-stakes and require strong legal validation and human oversight.
- **Limitation 3:** The benchmark has only 15 real-world tasks, so generalization is limited.

General thesis-level limitation:

```text
Improving one agent component is not enough for generalized web automation.
A robust web agent still needs grounding, planning, execution, verification, recovery, and safety.
```

---

## Relation to S4

This paper belongs in S4 because S4 discusses **LLM-based agents for web/GUI/mobile/computer automation**.

Its role in S4 is:

```text
LegalWebAgent: Empowering Access to Justice via LLM-Based Web Agents
→ domain-specific legal web agent
→ supporting P2 source for web/GUI/computer-use agent discussion
```

Use it after explaining what the paper does. Do not introduce it only as “P2”; introduce the method or idea first.

---

## Relation to thesis topic

Your thesis topic is:

```text
LLM-based agents for generalized web automation and data extraction
```

This paper matters because:

It is useful as an applied example showing web agents for access-to-justice and form/navigation assistance.

For generalized web automation, the connection is:

```text
web / GUI / mobile / computer-use interaction
→ agent observes a digital environment
→ agent chooses actions
→ agent extracts information or completes a workflow
```

Even when the paper is not directly about data extraction, it still helps explain the automation layer needed before extraction can be generalized.

---

## How to use this paper in the literature review

Recommended use:

- Use as **P2 support**, not as the central backbone.
- Use for one precise idea, architecture, benchmark, or limitation.
- If peer-reviewed, it can support stronger claims.
- If preprint/workshop/technical report, use it for recent trends and emerging directions.

Suggested sentence:

> LegalWebAgent: Empowering Access to Justice via LLM-Based Web Agents shows how domain-specific legal web agent contributes to the development of LLM-based agents for digital task automation, but its limitations indicate that generalized web automation still requires stronger grounding, verification, and recovery mechanisms.

---

## Reading decision

- **Keep in S4 P2:** Yes
- **Read fully?** No, selected sections are enough unless promoted later
- **Depth needed:** Low to medium
- **Main use:** Support S4 discussion of domain-specific legal web agent
- **Most important parts:**
  - Abstract
  - Introduction
  - Main architecture / method figure
  - Dataset or benchmark section
  - Results table
  - Limitations / discussion

---

## One-sentence summary

LegalWebAgent: Empowering Access to Justice via LLM-Based Web Agents is a P2 supporting paper for S4 because it explains **domain-specific legal web agent**, but it should be cited according to its venue/status and not overused beyond its evidence.

---

## BibTeX placeholder

```bibtex
@misc{legalwebagentempoweringaccesstojust2025,
  title = {LegalWebAgent: Empowering Access to Justice via LLM-Based Web Agents},
  year = {2025},
  note = {AI4A2J Workshop 2025, to appear; Workshop paper / domain case study. Verify final bibliographic metadata before thesis submission.}
}
```


---

<!-- ========== FILE: S4_P2_paper_first_detailed_markdown_notes\S4_P2_37_NetGent_Agent-Based_Automation_of_Network_Application_Workflows.md ========== -->

## Source: `S4_P2_paper_first_detailed_markdown_notes\S4_P2_37_NetGent_Agent-Based_Automation_of_Network_Application_Workflows.md`

# S4 P2 Paper 37 — NetGent: Agent-Based Automation of Network Application Workflows

## Metadata

- **Title:** NetGent: Agent-Based Automation of Network Application Workflows
- **Year:** 2025
- **Venue / status:** arXiv preprint
- **Peer-reviewed status:** No confirmed archival venue
- **Publication type:** Preprint
- **Thesis section:** S4 — workflow automation and scalable web interaction
- **Category:** workflow automation / network application data generation
- **Priority:** P2
- **BibTeX key:** `netgentagentbasedautomationofnetwor2025`

---

## Simple understanding

NetGent automates web/network application workflows to generate realistic network traffic datasets. It combines natural-language workflow specification with compiled deterministic execution.

In simple terms:

```text
Problem → how can an AI agent interact with a web, GUI, mobile, desktop, or application environment?
Method → add perception, planning, action, memory, API/tool use, state tracking, or browser control.
Goal → complete real user tasks more flexibly than scripts or static chatbots.
```

This note explains the paper first, then connects it to S4 and your thesis.

---

## Core idea

Compile natural-language state-dependent rules into nondeterministic finite automata and reusable executable code for robust replay.

The paper is mainly about:

```text
workflow automation / network application data generation
```

It contributes to the larger agent loop:

```text
observe → understand state → plan → act → receive feedback → verify / recover → complete task
```

---

## Key finding / main claim

NetGent automates 50+ workflows across streaming, conferencing, social media, and web scraping while improving repeatability, robustness, and efficiency.

For S4, the important question is not only whether the method works on its benchmark, but **which part of web/GUI agency it improves**:

- perception and grounding,
- planning and reasoning,
- action execution,
- API/tool use,
- memory/state tracking,
- recovery and verification,
- or deployment/evaluation.

---

## Key evidence to extract from the paper

When reading the paper, extract these points:

- **Abstract NFA → concrete NFA → cache/replay design.**
- **Evaluation across 50+ workflows.**
- **Claims about reducing redundant LLM calls through state caching and deterministic replay.**

These are the most useful parts for writing a literature-review paragraph.

---

## Limitations

- **Limitation 1:** Preprint status.
- **Limitation 2:** Its target is networking dataset generation, not user-facing web automation generally.
- **Limitation 3:** Workflow compilation still requires robust state detectors and handling UI drift.

General thesis-level limitation:

```text
Improving one agent component is not enough for generalized web automation.
A robust web agent still needs grounding, planning, execution, verification, recovery, and safety.
```

---

## Relation to S4

This paper belongs in S4 because S4 discusses **LLM-based agents for web/GUI/mobile/computer automation**.

Its role in S4 is:

```text
NetGent: Agent-Based Automation of Network Application Workflows
→ workflow automation / network application data generation
→ supporting P2 source for web/GUI/computer-use agent discussion
```

Use it after explaining what the paper does. Do not introduce it only as “P2”; introduce the method or idea first.

---

## Relation to thesis topic

Your thesis topic is:

```text
LLM-based agents for generalized web automation and data extraction
```

This paper matters because:

It gives a useful hybrid design pattern: language-based flexibility plus compiled execution reliability.

For generalized web automation, the connection is:

```text
web / GUI / mobile / computer-use interaction
→ agent observes a digital environment
→ agent chooses actions
→ agent extracts information or completes a workflow
```

Even when the paper is not directly about data extraction, it still helps explain the automation layer needed before extraction can be generalized.

---

## How to use this paper in the literature review

Recommended use:

- Use as **P2 support**, not as the central backbone.
- Use for one precise idea, architecture, benchmark, or limitation.
- If peer-reviewed, it can support stronger claims.
- If preprint/workshop/technical report, use it for recent trends and emerging directions.

Suggested sentence:

> NetGent: Agent-Based Automation of Network Application Workflows shows how workflow automation / network application data generation contributes to the development of LLM-based agents for digital task automation, but its limitations indicate that generalized web automation still requires stronger grounding, verification, and recovery mechanisms.

---

## Reading decision

- **Keep in S4 P2:** Yes
- **Read fully?** No, selected sections are enough unless promoted later
- **Depth needed:** Low to medium
- **Main use:** Support S4 discussion of workflow automation / network application data generation
- **Most important parts:**
  - Abstract
  - Introduction
  - Main architecture / method figure
  - Dataset or benchmark section
  - Results table
  - Limitations / discussion

---

## One-sentence summary

NetGent: Agent-Based Automation of Network Application Workflows is a P2 supporting paper for S4 because it explains **workflow automation / network application data generation**, but it should be cited according to its venue/status and not overused beyond its evidence.

---

## BibTeX placeholder

```bibtex
@misc{netgentagentbasedautomationofnetwor2025,
  title = {NetGent: Agent-Based Automation of Network Application Workflows},
  year = {2025},
  note = {arXiv preprint; Preprint. Verify final bibliographic metadata before thesis submission.}
}
```


---

<!-- ========== FILE: S4_P2_paper_first_detailed_markdown_notes\S4_P2_GLOBAL_SYNTHESIS.md ========== -->

## Source: `S4_P2_paper_first_detailed_markdown_notes\S4_P2_GLOBAL_SYNTHESIS.md`

# S4 P2 — Global Synthesis

## What S4 P2 papers cover

This S4 P2 batch covers:

1. early instruction-to-UI and web-support grounding,
2. mobile GUI agents,
3. web agents and browser-native agents,
4. computer-use agents,
5. API-first and hybrid-action agents,
6. agentic web interface proposals,
7. domain-specific web agents,
8. surveys and position papers on future web/GUI agents.

## How to use them

Use S4 P2 papers as supporting evidence:

```text
P0/P1 = central structure and core claims
P2 = breadth, recent examples, system variants, limitations, and trends
```

## Stronger papers

The stronger S4 P2 sources are the peer-reviewed or archival papers:

- ACL 2020 mobile UI action sequence paper
- NAACL 2021 web support task grounding
- KDD 2023 WebGLM
- ACL demo 2024 OpenWebAgent
- NAACL 2025 ReachAgent
- TMLR 2025 phone GUI agents survey
- NeurIPS 2025 WebThinker
- NeurIPS 2025 OpenCUA

## Main trend

The S4 P2 set shows a clear shift:

```text
scripted automation
→ instruction-grounded UI actions
→ LLM/VLM web and mobile agents
→ computer-use agents
→ API-first and hybrid-action agents
→ agent-native web interfaces
```

## Main caution

Many 2025 papers are arXiv preprints, under-review papers, TechRxiv reports, or work-in-progress papers. They are valuable for recent trends, but central claims should rely more on peer-reviewed papers.


---

<!-- ========== FILE: S4_P2_paper_first_detailed_markdown_notes\S4_P2_INDEX.md ========== -->

## Source: `S4_P2_paper_first_detailed_markdown_notes\S4_P2_INDEX.md`

# S4 P2 — Paper-First Detailed Notes Index

Each file follows the paper-first structure: understand the paper first, then connect it to S4/P2/thesis.

## Files

- [01. Mapping Natural Language Instructions to Mobile UI Action Sequences](./S4_P2_01_Mapping_Natural_Language_Instructions_to_Mobile_UI_Action_Sequences.md)
- [02. Grounding Open-Domain Instructions to Automate Web Support Tasks](./S4_P2_02_Grounding_Open-Domain_Instructions_to_Automate_Web_Support_Tasks.md)
- [03. SYNAPSE: Leveraging Few-Shot Exemplars for Human-Level Computer Control](./S4_P2_03_SYNAPSE_Leveraging_Few-Shot_Exemplars_for_Human-Level_Computer_Control.md)
- [04. WebGLM: Towards an Efficient Web-Enhanced Question Answering System with Human Preferences](./S4_P2_04_WebGLM_Towards_an_Efficient_Web-Enhanced_Question_Answering_System_with_Human_Preferences.md)
- [05. A Zero-Shot Language Agent for Computer Control with Structured Reflection](./S4_P2_05_A_Zero-Shot_Language_Agent_for_Computer_Control_with_Structured_Reflection.md)
- [06. GPT-4V in Wonderland: Large Multimodal Models for Zero-Shot Smartphone GUI Navigation](./S4_P2_06_GPT-4V_in_Wonderland_Large_Multimodal_Models_for_Zero-Shot_Smartphone_GUI_Navigation.md)
- [07. AppAgent: Multimodal Agents as Smartphone Users](./S4_P2_07_AppAgent_Multimodal_Agents_as_Smartphone_Users.md)
- [08. Mobile-Agent: Autonomous Multi-Modal Mobile Device Agent with Visual Perception](./S4_P2_08_Mobile-Agent_Autonomous_Multi-Modal_Mobile_Device_Agent_with_Visual_Perception.md)
- [09. CRADLE: Empowering Foundation Agents Towards General Computer Control](./S4_P2_09_CRADLE_Empowering_Foundation_Agents_Towards_General_Computer_Control.md)
- [10. ChatShop: Interactive Information Seeking with Language Agents](./S4_P2_10_ChatShop_Interactive_Information_Seeking_with_Language_Agents.md)
- [11. Grounded Language Agent for Product Search via Intelligent Web Interactions](./S4_P2_11_Grounded_Language_Agent_for_Product_Search_via_Intelligent_Web_Interactions.md)
- [12. Automating the Enterprise with Foundation Models](./S4_P2_12_Automating_the_Enterprise_with_Foundation_Models.md)
- [13. OpenWebAgent: An Open Toolkit to Enable Web Agents on Large Language Models](./S4_P2_13_OpenWebAgent_An_Open_Toolkit_to_Enable_Web_Agents_on_Large_Language_Models.md)
- [14. Steward: Natural Language Web Automation](./S4_P2_14_Steward_Natural_Language_Web_Automation.md)
- [15. AXIS: Efficient Human-Agent-Computer Interaction with API-First LLM-Based Agents](./S4_P2_15_AXIS_Efficient_Human-Agent-Computer_Interaction_with_API-First_LLM-Based_Agents.md)
- [16. Foundations and Recent Trends in Multimodal Mobile Agents: A Survey](./S4_P2_16_Foundations_and_Recent_Trends_in_Multimodal_Mobile_Agents_A_Survey.md)
- [17. The Dawn of GUI Agent: A Preliminary Case Study with Claude 3.5 Computer Use](./S4_P2_17_The_Dawn_of_GUI_Agent_A_Preliminary_Case_Study_with_Claude_3.5_Computer_Use.md)
- [18. A Comprehensive Survey of Agents for Computer Use: Foundations, Challenges, and Future Directions](./S4_P2_18_A_Comprehensive_Survey_of_Agents_for_Computer_Use_Foundations_Challenges_and_Future_Directions.md)
- [19. Mobile-Agent-E: Self-Evolving Mobile Assistant for Complex Tasks](./S4_P2_19_Mobile-Agent-E_Self-Evolving_Mobile_Assistant_for_Complex_Tasks.md)
- [20. ReachAgent: Enhancing Mobile Agent via Page Reaching and Page Operation](./S4_P2_20_ReachAgent_Enhancing_Mobile_Agent_via_Page_Reaching_and_Page_Operation.md)
- [21. LiteWebAgent: The Open-Source Suite for VLM-Based Web-Agent Applications](./S4_P2_21_LiteWebAgent_The_Open-Source_Suite_for_VLM-Based_Web-Agent_Applications.md)
- [22. LLM-Powered GUI Agents in Phone Automation: Surveying Progress and Prospects](./S4_P2_22_LLM-Powered_GUI_Agents_in_Phone_Automation_Surveying_Progress_and_Prospects.md)
- [23. WebThinker: Empowering Large Reasoning Models with Deep Research Capability](./S4_P2_23_WebThinker_Empowering_Large_Reasoning_Models_with_Deep_Research_Capability.md)
- [24. Beyond Browsing: API-Based Web Agents](./S4_P2_24_Beyond_Browsing_API-Based_Web_Agents.md)
- [25. GA: A Comprehensive Survey on LLM-based GUI Agent](./S4_P2_25_GA_A_Comprehensive_Survey_on_LLM-based_GUI_Agent.md)
- [26. Build the Web for Agents, Not Agents for the Web](./S4_P2_26_Build_the_Web_for_Agents_Not_Agents_for_the_Web.md)
- [27. Embodied Web Agents: Bridging Physical-Digital Realms for Integrated Agent Intelligence](./S4_P2_27_Embodied_Web_Agents_Bridging_Physical-Digital_Realms_for_Integrated_Agent_Intelligence.md)
- [28. Agentic Web: Weaving the Next Web with AI Agents](./S4_P2_28_Agentic_Web_Weaving_the_Next_Web_with_AI_Agents.md)
- [29. CoAct-1: Computer-using Agents with Coding as Actions](./S4_P2_29_CoAct-1_Computer-using_Agents_with_Coding_as_Actions.md)
- [30. OpenCUA: Open Foundations for Computer-Use Agents](./S4_P2_30_OpenCUA_Open_Foundations_for_Computer-Use_Agents.md)
- [31. Are LLM Agents the New RPA? A Comparative Study with RPA Across Enterprise Workflows](./S4_P2_31_Are_LLM_Agents_the_New_RPA_A_Comparative_Study_with_RPA_Across_Enterprise_Workflows.md)
- [32. BrowserAgent: Building Web Agents with Human-Inspired Web Browsing Actions](./S4_P2_32_BrowserAgent_Building_Web_Agents_with_Human-Inspired_Web_Browsing_Actions.md)
- [33. UltraCUA: A Foundation Model for Computer Use Agents with Hybrid Action](./S4_P2_33_UltraCUA_A_Foundation_Model_for_Computer_Use_Agents_with_Hybrid_Action.md)
- [34. Agent-SAMA: State-Aware Mobile Assistant](./S4_P2_34_Agent-SAMA_State-Aware_Mobile_Assistant.md)
- [35. Building the Web for Agents: A Declarative Framework for Agent–Web Interaction](./S4_P2_35_Building_the_Web_for_Agents_A_Declarative_Framework_for_AgentWeb_Interaction.md)
- [36. LegalWebAgent: Empowering Access to Justice via LLM-Based Web Agents](./S4_P2_36_LegalWebAgent_Empowering_Access_to_Justice_via_LLM-Based_Web_Agents.md)
- [37. NetGent: Agent-Based Automation of Network Application Workflows](./S4_P2_37_NetGent_Agent-Based_Automation_of_Network_Application_Workflows.md)


---

<!-- ========== FILE: S4_P2_venue_status_verification_report.md ========== -->

## Source: `S4_P2_venue_status_verification_report.md`

# S4 P2 — Venue / Status Verification Report

## Scope

This report covers the current **S4 P2 batch: 37 papers** on web agents, GUI agents, mobile agents, computer-use agents, enterprise automation, API-first agents, and agentic web systems.

## Status legend

- **Confirmed peer-reviewed / archival**: venue is visible in the paper or confirmed by an official venue index.
- **Workshop / demo / system track**: accepted, useful, but usually weaker than a main conference/journal paper.
- **Preprint / technical report / under review**: useful for recent systems and trends, but cite carefully.
- **Position / survey preprint**: useful for framing and taxonomy, but not primary empirical evidence.

## Summary

| Status group | Count | Use in thesis |
|---|---:|---|
| Strong confirmed archival / journal / main conference | 8–9 | Good for stronger claims |
| Workshop / demo / system papers | 3–4 | Good for systems/toolkits, but not central evidence |
| Preprint / technical report / under review / work in progress | ~24–26 | Good for recency, trends, gaps, and examples |

**Main conclusion:** S4 P2 is valuable for breadth and recency, but the venue quality is mixed. Use ACL/NAACL/KDD/TMLR/NeurIPS papers for stronger claims. Use arXiv/TechRxiv/work-in-progress papers as supporting recent evidence only.

---

## Detailed verification table

| # | Paper | Year | Venue / status | Peer-reviewed? | Use strength | Decision |
|---:|---|---:|---|---|---|---|
| 1 | Mapping Natural Language Instructions to Mobile UI Action Sequences | 2020 | ACL 2020 main conference | Yes | Strong | Keep as strong S4 support |
| 2 | Grounding Open-Domain Instructions to Automate Web Support Tasks | 2021 | NAACL-HLT 2021 main conference | Yes | Strong | Keep as strong S4 support |
| 3 | SYNAPSE: Leveraging Few-Shot Exemplars for Human-Level Computer Control | 2023 | arXiv preprint | No confirmed archival venue found | Medium-low | Keep P2 only |
| 4 | WebGLM: Towards an Efficient Web-Enhanced QA System with Human Preferences | 2023 | KDD 2023 | Yes | Strong | Keep as strong S4 support |
| 5 | A Zero-Shot Language Agent for Computer Control with Structured Reflection | 2023 | arXiv preprint | No confirmed archival venue found | Medium-low | Keep P2 only |
| 6 | GPT-4V in Wonderland: Large Multimodal Models for Zero-Shot Smartphone GUI Navigation | 2023 | arXiv preprint | No confirmed archival venue found | Medium-low | Keep P2 only |
| 7 | AppAgent: Multimodal Agents as Smartphone Users | 2023 | arXiv preprint | No confirmed archival venue found | Medium-low | Keep P2 only |
| 8 | Mobile-Agent: Autonomous Multi-Modal Mobile Device Agent with Visual Perception | 2024 | arXiv preprint / technical report | No confirmed archival venue found | Medium-low | Keep P2 only |
| 9 | CRADLE: Empowering Foundation Agents Towards General Computer Control | 2024 | arXiv preprint; marked under review | No | Medium-low | Keep P2 only |
| 10 | ChatShop: Interactive Information Seeking with Language Agents | 2024 | arXiv preprint | No confirmed archival venue found | Medium-low | Keep P2 only |
| 11 | Grounded Language Agent for Product Search via Intelligent Web Interactions | 2024 | ACL Workshop CustomNLP4U 2024 | Workshop | Medium | Use as supporting web-shopping/web-interaction source |
| 12 | Automating the Enterprise with Foundation Models | 2024 | arXiv preprint | No confirmed archival venue found | Medium-low | Keep P2 only |
| 13 | OpenWebAgent: An Open Toolkit to Enable Web Agents on LLMs | 2024 | ACL 2024 System Demonstrations | Yes, system demo | Medium-strong | Good toolkit/system source |
| 14 | Steward: Natural Language Web Automation | 2024 | arXiv preprint | No confirmed archival venue found | Medium-low | Keep P2 only |
| 15 | AXIS: Efficient Human-Agent-Computer Interaction with API-First LLM-Based Agents | 2024/2025 | arXiv preprint | No confirmed archival venue found | Medium-low | Keep P2 only |
| 16 | Foundations and Recent Trends in Multimodal Mobile Agents: A Survey | 2024/2025 | arXiv survey | No confirmed archival venue found | Medium-low | Use for taxonomy only |
| 17 | The Dawn of GUI Agent: A Preliminary Case Study with Claude 3.5 Computer Use | 2024 | arXiv preprint / case study | No | Low-medium | Use only as case-study evidence |
| 18 | A Comprehensive Survey of Agents for Computer Use | 2025 | arXiv survey | No confirmed archival venue found | Medium-low | Use for taxonomy/gaps only |
| 19 | Mobile-Agent-E: Self-Evolving Mobile Assistant for Complex Tasks | 2025 | arXiv; SEA @ NeurIPS 2025 workshop oral | Workshop | Medium | Good recent system, not main archival |
| 20 | ReachAgent: Enhancing Mobile Agent via Page Reaching and Page Operation | 2025 | NAACL 2025 long paper | Yes | Strong | Keep as strong S4 support |
| 21 | LiteWebAgent: The Open-Source Suite for VLM-Based Web-Agent Applications | 2025 | NAACL 2025 System Demonstrations | Yes, demo | Medium-strong | Good toolkit/system source |
| 22 | LLM-Powered GUI Agents in Phone Automation: Surveying Progress and Prospects | 2025 | TMLR 2025 | Yes | Strong | Strong survey source |
| 23 | WebThinker: Empowering Large Reasoning Models with Deep Research Capability | 2025 | NeurIPS 2025 | Yes | Strong | Strong deep-research/web-agent source |
| 24 | Beyond Browsing: API-Based Web Agents | 2025 | arXiv preprint | No confirmed archival venue found | Medium-low | Important but cite as preprint |
| 25 | GA: A Comprehensive Survey on LLM-based GUI Agent | 2025 | TechRxiv / submitted manuscript | Not peer-reviewed in uploaded version | Low-medium | Supplementary only |
| 26 | Build the Web for Agents, Not Agents for the Web | 2025 | arXiv position paper / under review | No | Medium-low | Good for Agentic Web Interface argument |
| 27 | Embodied Web Agents: Bridging Physical-Digital Realms | 2025 | arXiv preprint / under review | No | Medium-low | Good emerging benchmark/paradigm source |
| 28 | Agentic Web: Weaving the Next Web with AI Agents | 2025 | arXiv survey/vision paper | No confirmed archival venue found | Medium-low | Use for conceptual framing |
| 29 | CoAct-1: Computer-using Agents with Coding as Actions | 2025 | arXiv preprint | No confirmed archival venue found | Medium-low | Useful for coding-as-action trend |
| 30 | OpenCUA: Open Foundations for Computer-Use Agents | 2025 | NeurIPS 2025 | Yes | Strong | Strong CUA dataset/model source |
| 31 | Are LLM Agents the New RPA? A Comparative Study with RPA Across Enterprise Workflows | 2025 | Uploaded copy does not show confirmed venue | Unclear | Low-medium | Verify final proceedings before citation |
| 32 | BrowserAgent: Building Web Agents with Human-Inspired Web Browsing Actions | 2025 | arXiv; marked Work in Progress | No | Low-medium | Use carefully as WIP |
| 33 | UltraCUA: A Foundation Model for Computer Use Agents with Hybrid Action | 2025 | arXiv preprint | No confirmed archival venue found | Medium-low | Useful recent hybrid-action CUA paper |
| 34 | Agent-SAMA: State-Aware Mobile Assistant | 2025 | arXiv preprint | No confirmed archival venue found | Medium-low | Useful FSM/state-aware mobile-agent trend |
| 35 | Building the Web for Agents: A Declarative Framework for Agent-Web Interaction | 2025 | arXiv preprint | No confirmed archival venue found | Medium-low | Useful for declarative agent-web interface |
| 36 | LegalWebAgent: Empowering Access to Justice via LLM-Based Web Agents | 2025 | AI4A2J Workshop 2025, to appear | Workshop / pending final proceedings | Medium-low | Domain-specific web-agent example |
| 37 | NetGent: Agent-Based Automation of Network Application Workflows | 2025 | arXiv preprint | No confirmed archival venue found | Medium-low | Useful workflow automation/data-generation example |

---

## Strongest S4 P2 papers to cite

1. **Mapping Natural Language Instructions to Mobile UI Action Sequences** — ACL 2020.
2. **Grounding Open-Domain Instructions to Automate Web Support Tasks** — NAACL-HLT 2021.
3. **WebGLM** — KDD 2023.
4. **Grounded Language Agent for Product Search** — ACL workshop 2024.
5. **OpenWebAgent** — ACL System Demonstrations 2024.
6. **ReachAgent** — NAACL 2025 long paper.
7. **LLM-Powered GUI Agents in Phone Automation** — TMLR 2025.
8. **WebThinker** — NeurIPS 2025.
9. **OpenCUA** — NeurIPS 2025.

## Papers to cite carefully

These are mostly **arXiv / TechRxiv / work-in-progress / under-review** versions:

- SYNAPSE
- Zero-Shot Language Agent with Structured Reflection
- GPT-4V in Wonderland
- AppAgent
- Mobile-Agent
- CRADLE
- ChatShop
- Automating the Enterprise with Foundation Models
- Steward
- AXIS
- Computer Use survey
- Build the Web for Agents
- Embodied Web Agents
- Agentic Web
- CoAct-1
- UltraCUA
- Agent-SAMA
- BrowserAgent
- NetGent

## Recommended S4 writing strategy

Use the confirmed papers to build the backbone:

```text
2020–2021: instruction grounding to UI/web actions
→ 2023: web-enhanced QA and early GUI/web-agent systems
→ 2024: open web-agent toolkits and product-search/web automation
→ 2025: mobile/computer-use agents, deep research agents, API-first/hybrid-action agents
```

Use P2 papers mainly for:

- examples of systems,
- recent trends,
- benchmarks,
- architectural variants,
- limitations and open problems,
- emerging Agentic Web arguments.

Avoid claiming that recent preprint trends are settled facts. Prefer wording such as:

> Recent preprint and system papers suggest an emerging trend toward API-first, hybrid-action, and agent-native web interfaces, but robust peer-reviewed validation remains limited.

## Final decision

S4 P2 is **highly useful** for breadth and recency, but mixed in venue quality.

- **Promote for stronger citation use:** ACL / NAACL / KDD / TMLR / NeurIPS / ACL-demo papers.
- **Keep as P2 support:** arXiv systems, technical reports, surveys, and position papers.
- **Use with caution:** 2025 future-looking papers, work-in-progress papers, and TechRxiv/submitted manuscripts.


---

