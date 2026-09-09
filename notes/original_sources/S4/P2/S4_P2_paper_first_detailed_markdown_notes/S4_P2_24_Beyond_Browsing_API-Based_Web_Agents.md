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
