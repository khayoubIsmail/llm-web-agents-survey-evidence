# S3 P3 Deep Notes — LLM Agent Architectures

Scope: S3 P3 papers and technical reports uploaded for the agent-architecture section.  
Purpose: personal deep archive + later selective use in the thesis chapter and ACM Computing Surveys-style survey.

Important status convention:
- **Peer-reviewed / accepted**: confirmed by official venue/proceedings/OpenReview where available.
- **Workshop**: accepted to workshop, not main conference/journal.
- **Preprint / arXiv only**: no confirmed peer-reviewed venue found in the available venue checks.
- **Tool/framework / grey literature**: useful for ecosystem discussion but weaker evidential status.

## Section-level synthesis

The S3 P3 batch reinforces that LLM-agent architecture is moving from simple ReAct-style loops toward **compound, adaptive, and memory-heavy systems**. The most important architectural axes are:

1. **Control policy**: single-agent loop → planner-executor → orchestrator → learned organization policy.
2. **Agent composition**: fixed roles → sub-agents-as-tools → dynamic on-demand sub-agent creation.
3. **Memory architecture**: flat text history → RAG memory → structured event memory → visual/optical memory → latent role-aware memory.
4. **Tool ecosystem**: static APIs → MCP tools → automated tool discovery, tool selection, and tool learning.
5. **Self-improvement**: reflection → playbook/context evolution → tool generation → memory-policy learning.
6. **Deployment constraints**: cost, latency, observability, sandboxing, and trust become architectural requirements, not only engineering afterthoughts.

## Best S3 P3 papers to keep strongly in the final S3 narrative

| Priority | Paper | Why it matters |
|---|---|---|
| Keep | ACE | Strong accepted paper for evolving context/playbook memory. |
| Keep | AORCHESTRA | Clean model of dynamic sub-agent creation. |
| Keep | AgentScope 1.0 | Good framework/tooling ecosystem example. |
| Keep | MCP-Flow | Strong MCP/tool ecosystem paper; very useful for tool-use subsection. |
| Keep | Context-Folding | Strong long-horizon context-management mechanism. |
| Keep | AtomMem | Clean memory-as-action-space framing. |
| Keep | StructMem / xMemory / OCR-Memory | Strong memory architecture cluster. |
| Keep selectively | InfoSeek / Caesar | Useful for deep-research and web-exploration architecture. |
| Use cautiously | ALITA-G / AlphaApollo / LatentMem | Interesting self-evolving/tool/memory ideas, but mostly preprint/workshop. |
| Probably brief only | Agentic AI survey / Agentic RAG survey / Data Agents tutorial | Good positioning, not central technical evidence. |
| Likely exclude or footnote | PRefLexOR | Too peripheral/speculative for main S3 unless space remains. |

## Recommended S3 paragraph to add

Modern LLM-agent architectures increasingly treat agency as a **compound systems problem** rather than a single prompting pattern. Beyond ReAct-style reasoning-action loops, recent work decomposes agents into planner, executor, memory, tool, and orchestration modules; dynamically creates sub-agents with task-specific context and tool permissions; and learns how to manage context, memory, and tool use over long horizons. This trend is directly relevant to generalized web extraction: an extraction agent must coordinate navigation, page understanding, field grounding, validation, provenance tracking, and security checks while controlling cost and avoiding unbounded context growth.

---

## 1. Analyzing Information Sharing and Coordination in Multi-Agent Planning

### Venue / status
- Year: 2025
- Authors: Tianyue Ou, Saujas Vaduguru, Daniel Fried
- Status: arXiv preprint / CoRR only found; arXiv:2508.12981, v1 18 Aug 2025. No confirmed peer-reviewed venue found in available checks.
- Citation caution: Use as supporting P3 evidence for multi-agent coordination; do not cite as peer-reviewed.

### Core idea
Studies how structured information sharing and explicit orchestration affect LLM-based multi-agent systems on long-horizon, multi-constraint planning.

### Key contribution
Introduces a MAS for TravelPlanner with expert agents, a shared notebook for grounded information sharing, an orchestrator for turn selection, and plan compiler/critic components. The paper isolates two architectural levers: persistent shared evidence and dynamic coordination.

### Method / approach
Agents specialize by information source or planning role. Experts gather facts and write them to a notebook; an orchestrator decides which agent should act next; a compiler and critic synthesize and refine the final plan. The evaluation compares single-agent, MAS without notebook/orchestrator, and variants with the proposed mechanisms.

### Key findings
The notebook reduces hallucinated details; orchestration reduces errors in focused sub-areas; combining notebook plus orchestrator improves final pass rate over a single-agent baseline on TravelPlanner. The key lesson is not simply that 'more agents help', but that communication substrate and control policy determine whether multi-agent decomposition helps or adds overhead.

### Limitations
The domain is travel planning, not web extraction. Delivery rate can drop because coordination overhead consumes steps and agents may become more conservative. The evaluation does not test adversarial web pages, schema-constrained extraction, provenance accuracy, or live browser operations.

### Relevance to my thesis / S3
Useful for S3 because it gives concrete evidence for the architectural claim that multi-agent agents need explicit shared state and coordination. It supports the thesis distinction between naive multi-agent role assignment and structured orchestration.

### How to use it in the literature review
Use in S3 under multi-agent coordination and shared memory. Mention later in S5/S6 only as an architectural analogy for extraction agents that must coordinate discovery, navigation, extraction, validation, and verification sub-agents.

### Connects to
S3 agent architectures; S5.3 planning; S6 extraction pipeline decomposition; S8 open challenges on long-horizon coordination.

### Sentence to add later
> Recent MAS work shows that long-horizon planning benefits less from merely adding agents than from providing structured shared evidence and an orchestrator that controls which specialist acts next; this distinction is directly relevant to web-extraction agents that must coordinate navigation, field grounding, validation, and provenance tracking.

---

## 2. Open Data Synthesis for Deep Research / InfoSeek

### Venue / status
- Year: 2025
- Authors: Ziyi Xia, Kun Luo, Hongjin Qian, Zheng Liu
- Status: arXiv technical report / preprint; arXiv:2509.00375, 30 Aug 2025. No confirmed peer-reviewed venue found in available checks.
- Citation caution: Good P3 support for data synthesis and deep-research training; cite cautiously as preprint.

### Core idea
Frames deep-research tasks as Hierarchical Constraint Satisfaction Problems (HCSPs) and proposes InfoSeek, a data synthesis framework for generating structurally complex, verifiable deep-research questions.

### Key contribution
Moves beyond single-hop, multi-hop, and flat CSP QA by explicitly modeling hierarchical dependency trees. Generates more than 50K training examples and 16.5K trajectories, preserving intermediate nodes and retrieval labels for later SFT/RL optimization.

### Method / approach
Mines entities and relations from large-scale webpages, builds recursive research trees, blurs intermediate nodes into valid sub-problems, converts trees into natural language questions, and filters for uniqueness/verifiability. InfoSeeker uses parallel multi-query search and a refiner agent.

### Key findings
Models optimized with InfoSeek outperform strong baselines on BrowseComp-Plus; the dataset’s difficulty scales with tree complexity, with high failure rates for strong CoT baselines. The paper argues that deep-research ability requires training data with hierarchical structure rather than ordinary multi-hop QA.

### Limitations
Synthetic data may encode shortcuts or distribution artifacts despite filtering. It targets verifiable answer finding, not full web automation or schema-based extraction. It does not evaluate provenance completeness at field level or extraction over dynamic pages.

### Relevance to my thesis / S3
Important for S3 because it shows a data-centric route to agentic reasoning: architectures improve when paired with training data that matches the control structure of the task.

### How to use it in the literature review
Use under S3 agent learning/data synthesis, and cross-link to S5.7 deep research and S5.4 training strategies. It helps justify why web-extraction agents need task-specific training/evaluation data rather than generic QA corpora.

### Connects to
S3 learning agents; S5.4 training; S5.7 deep research; S8 benchmark gaps.

### Sentence to add later
> InfoSeek illustrates a broader shift in agent research from prompting-only architectures toward data-centric agent training, where the structure of the synthesized tasks mirrors the decomposition and evidence-integration structure required at inference time.

---

## 3. Orchestrator: Active Inference for Multi-Agent Systems in Long-Horizon Tasks

### Venue / status
- Year: 2025
- Authors: Lukas Beckenbauer, Johannes-Lucas Loewe, Ge Zheng, Alexandra Brintrup
- Status: arXiv preprint / CoRR; arXiv:2509.05651, 6 Sep 2025. No confirmed conference/journal venue found in available checks.
- Citation caution: Use as conceptual/architectural support; synthetic maze benchmark limits external validity.

### Core idea
Proposes a dynamic MAS orchestration framework grounded in active inference and reflective benchmarking for long-horizon tasks under partial observability.

### Key contribution
Introduces a cell-structured graph architecture with planning, execution, and orchestration nodes; uses free-energy-inspired metrics to monitor agent-environment and agent-agent dynamics; adjusts behavior when agents encounter local minima.

### Method / approach
Models MAS as a graph with planner, executors, and orchestrator. Execution nodes are monitored using uncertainty/information-gain style metrics, while the orchestrator acts as communication hub and global memory. Evaluated on maze-solving tasks of increasing difficulty.

### Key findings
Reported improvements over baseline agent ensembles, especially in medium and hard mazes, suggest that dynamic feedback-driven orchestration can improve reliability and scalability compared with static agent ensembles.

### Limitations
Evaluation is limited to synthetic maze tasks and small teams. It is not clear how free-energy metrics transfer to web browsing, extraction, or heterogeneous tool environments. No evidence for schema adherence, provenance, or adversarial robustness.

### Relevance to my thesis / S3
Useful for S3 as an example of moving from fixed workflows to adaptive orchestration. It supports the taxonomy dimension of control policy: static pipeline, central planner, reflective orchestrator, learned/dynamic organizer.

### How to use it in the literature review
Use in S3 to enrich multi-agent orchestration discussion. Do not present as evidence for web extraction performance.

### Connects to
S3 multi-agent orchestration; S5.3 planning; S8 challenge of adaptive coordination under uncertainty.

### Sentence to add later
> Active-inference-inspired orchestration represents a more ambitious direction than fixed role-based MAS: the system continuously monitors coordination quality and adapts agent behavior based on uncertainty and progress signals.

---

## 4. Agentic AI: A Comprehensive Survey of Architectures, Applications, and Future Directions

### Venue / status
- Year: 2025
- Authors: Mohamad Abou Ali, Fadi Dornaika
- Status: arXiv preprint / survey; arXiv:2510.25445, 29 Oct 2025. No confirmed journal venue found in available checks.
- Citation caution: Use mainly as related-survey positioning; verify methodology claims independently.

### Core idea
A broad survey arguing that contemporary agentic AI should not be retrofitted into classical symbolic-agent vocabulary; proposes a dual-lineage taxonomy: symbolic/classical vs neural/generative.

### Key contribution
Provides a PRISMA-style review of 90 studies, compares symbolic and neural agentic paradigms, discusses domain-specific implementations, and emphasizes governance differences between paradigms.

### Method / approach
Organizes agentic AI literature by architectural paradigm, degree of agency/coordination, application domain, and governance issues. Includes related-survey comparison and taxonomy tables.

### Key findings
The main useful finding for your review is conceptual: 'agent' is overloaded. Classical BDI/POMDP vocabulary and LLM-based prompt/tool orchestration share surface similarities but differ operationally. Hybrid neuro-symbolic systems are positioned as a future direction.

### Limitations
Very broad and not web-agent/extraction-specific. Its taxonomy may be too high-level for technical web automation details. Some domain examples are more illustrative than experimentally grounded.

### Relevance to my thesis / S3
Useful for the beginning of S3 to clarify terminology: single-agent system vs agentic AI vs MAS; symbolic planning vs neural/prompt-driven orchestration.

### How to use it in the literature review
Use as a related survey in the S3 introduction and in the related-surveys comparison table, not as a central technical source.

### Connects to
S3 taxonomy; S1/S2 conceptual framing; S7 governance/safety.

### Sentence to add later
> Recent surveys warn against conceptual retrofitting: modern LLM agents often implement agency through stochastic generation, prompt-controlled tool use, and runtime orchestration rather than the explicit symbolic state machines assumed by classical agent frameworks.

---

## 5. Agentic Context Engineering: Evolving Contexts for Self-Improving Language Models (ACE)

### Venue / status
- Year: 2025/2026
- Authors: Qizheng Zhang et al.
- Status: Accepted at ICLR 2026 according to the paper front matter and OpenReview page; also available as arXiv:2510.04618.
- Citation caution: Safe to cite as peer-reviewed ICLR 2026 if final proceedings page is available; otherwise cite OpenReview/arXiv with acceptance note.

### Core idea
Proposes context adaptation as an agentic process: contexts should be evolving playbooks that accumulate, refine, and organize task strategies instead of being repeatedly compressed into brief summaries.

### Key contribution
Identifies brevity bias and context collapse in prompt/context optimization. Introduces ACE with Generator, Reflector, and Curator roles; uses incremental delta updates and grow-and-refine mechanisms to avoid destructive rewriting.

### Method / approach
The Generator produces trajectories; the Reflector extracts lessons from success/failure traces; the Curator integrates lessons into structured context entries. Updates are itemized rather than monolithic, enabling scalable context evolution across offline prompt optimization and online agent memory.

### Key findings
Reports strong gains on AppWorld and domain benchmarks, lower adaptation latency, fewer rollouts, and better cost efficiency than baselines. The case of context collapse shows how a large useful context can be rewritten into a tiny uninformative one, reducing accuracy below no-adaptation baseline.

### Limitations
Relies on the assumption that long, detailed contexts remain usable by the base model. Does not solve grounding/provenance for web extraction. Playbook growth may require governance, pruning, and security controls to avoid accumulating poisoned or obsolete instructions.

### Relevance to my thesis / S3
Highly relevant to S3 because it reframes memory/prompting as an adaptive architectural component. For web extraction agents, it suggests preserving site-specific strategies, failure modes, and schema-handling lessons as structured playbooks rather than lossy summaries.

### How to use it in the literature review
Use in S3 under memory/context engineering and self-improving agents. Cross-link to S5.5 failure modes and S7 memory poisoning.

### Connects to
S3 memory/context; S5.4 training/self-improvement; S5.5 failure; S7 security.

### Sentence to add later
> ACE suggests that self-improving agents should treat context not as a short prompt to be optimized for brevity, but as a structured playbook that preserves accumulated strategies, tool-use heuristics, and failure lessons across episodes.

---

## 6. Agentic Reasoning and Refinement through Semantic Interaction (VIS-ReAct)

### Venue / status
- Year: 2025
- Authors: Xuxin Tang, Rehema Abulikemu, Eric Krokos, Kirsten Whitley, Xuan Wang, Chris North
- Status: Author version states published in IEEE Visualization conference / TVCG final version placeholder. arXiv:2510.02157. Needs final DOI/TVCG record verification before strong citation.
- Citation caution: Use as IEEE VIS/TVCG author-version with caution until DOI/official proceedings record is confirmed.

### Core idea
Introduces VIS-ReAct, a two-agent framework that uses semantic interactions in visual workspaces to guide targeted refinement of LLM-generated sensemaking reports.

### Key contribution
Bridges visual analytics, human semantic interaction, and ReAct-style reasoning. The method interprets user actions such as highlights, notes, and cluster changes, infers intent, and then uses that intent to refine only relevant report parts.

### Method / approach
Converts visual workspace state into structured text, extracts semantic interactions by comparing previous/current workspaces, uses an LLM analysis agent to infer user intent and generate refinement plans, and then uses an LLM refinement agent to update the report.

### Key findings
Case studies indicate improved targeted refinement, semantic fidelity, and transparency compared with direct regeneration or action-only refinement. The paper highlights that human interaction traces can serve as planning signals for LLM agents.

### Limitations
Small case-study evaluation; not web automation or autonomous extraction. It assumes a structured visual workspace and explicit user interaction traces. No large benchmark or automated reproducibility evidence.

### Relevance to my thesis / S3
Useful in S3 as evidence for human-in-the-loop agent architectures and semantic-interaction-driven refinement. Also relevant for survey discussion of interactive agents where users guide refinement through actions rather than only text prompts.

### How to use it in the literature review
Use as P3 example in S3 or later HCI discussion. It can support the idea that future extraction systems may accept user corrections as structured feedback to update extraction rules/provenance.

### Connects to
S3 human-agent collaboration; S6 interactive extraction validation; S8 human-in-the-loop evaluation.

### Sentence to add later
> VIS-ReAct shows that user interactions can become first-class reasoning signals: instead of regenerating a whole output from scratch, an agent can infer intent from semantic actions and perform targeted refinement.

---

## 7. ALITA-G: Self-Evolving Generative Agent for Agent Generation

### Venue / status
- Year: 2025
- Authors: Jiahao Qiu et al.
- Status: arXiv preprint; arXiv:2510.23601. OpenReview ICLR 2026 submission page found, but acceptance not confirmed in available checks.
- Citation caution: Use as preprint/submission unless official acceptance is later confirmed.

### Core idea
Proposes a self-evolution framework that converts a general-purpose agent into domain-specialized agents by generating, abstracting, and curating MCP tools from successful trajectories.

### Key contribution
Extends self-evolution beyond prompt rewriting. Introduces MCP generation, abstraction into parameterized primitives, MCP Box construction, and retrieval-augmented MCP selection at inference.

### Method / approach
A master/generalist agent executes target-domain tasks; successful trajectories are mined to synthesize candidate MCPs; tools are abstracted and standardized; a specialized agent retrieves relevant MCPs and executes through an MCP executor.

### Key findings
Reports strong performance on GAIA, PathVQA, and Humanity's Last Exam, including high pass@1/pass@3 on GAIA and reduced token cost relative to a baseline. The important result is the architectural trend: agents can generate reusable tool affordances from experience.

### Limitations
Preprint; claims of SOTA should be treated carefully. Tool generation can introduce security, correctness, and maintainability risks. Generated MCPs require validation, provenance, sandboxing, and lifecycle management.

### Relevance to my thesis / S3
Very relevant to S3 because it connects tool use, agent generation, and self-evolution. For web extraction, it suggests agents might learn reusable extraction tools or site adapters from successful trajectories.

### How to use it in the literature review
Use in S3 under self-evolving agents and tool-making. Cross-link to S7 for MCP/tool security and to S6 for reusable extraction primitives.

### Connects to
S3 self-evolving agents; S6 extraction-tool generation; S7 MCP security; S8 adaptive systems.

### Sentence to add later
> ALITA-G pushes self-evolution from prompt repair toward tool-level evolution, where successful task trajectories are distilled into reusable MCP primitives that can be retrieved and executed by later specialist agents.

---

## 8. AlphaApollo: Orchestrating Foundation Models and Professional Tools into a Self-Evolving System for Deep Agentic Reasoning

### Venue / status
- Year: 2025/2026
- Authors: Zhanke Zhou et al.
- Status: arXiv preprint; arXiv:2510.06261. OpenReview result indicates Lifelong Agent Workshop @ ICLR 2026, not main conference.
- Citation caution: Cite as workshop/preprint, not main ICLR paper.

### Core idea
Presents a tool-augmented, multi-model reasoning system that combines computation tools, retrieval tools, shared evolving state, and iterative refinement.

### Key contribution
Emphasizes verifiable tool-augmented reasoning: exact computation through Python/scientific libraries and task-relevant retrieval, plus a shared state map for candidate solutions, executable checks, and feedback.

### Method / approach
Models propose candidate solutions, call tools, execute checks, record candidate states in an evolving map, and iteratively refine. The current release focuses mainly on tool-augmented reasoning, with future extensions planned for multi-round/multi-model scaling.

### Key findings
Reports consistent gains on AIME 2024/2025 across multiple model families, with tool-call success above 80% in many settings and improvements over non-tool baselines.

### Limitations
Math/scientific reasoning focus, not web extraction. Preprint/workshop; current release does not fully implement all planned self-evolving features. Heavy reliance on tool correctness and executable verification.

### Relevance to my thesis / S3
Useful in S3 to show the 'compound agentic system' pattern: LLMs are embedded in a tool-and-state architecture where external verification improves reliability.

### How to use it in the literature review
Use as P3 support for tool-augmented reasoning and shared-state iterative refinement. For extraction, map 'executable checks' to schema validation and provenance checks.

### Connects to
S3 tool use; S5.3 planning; S6 validation; S8 cost/reproducibility.

### Sentence to add later
> AlphaApollo exemplifies a compound-agent design in which reasoning quality is improved by placing LLMs inside an architecture of professional tools, shared state, and executable feedback rather than relying on self-reflection alone.

---

## 9. Scaling Long-Horizon LLM Agent via Context-Folding

### Venue / status
- Year: 2025
- Authors: Weiwei Sun, Miao Lu, Zhan Ling, Kang Liu, Xuesong Yao, Yiming Yang, Jiecao Chen
- Status: arXiv preprint / CoRR; arXiv:2510.11967. OpenReview record lists venue as CoRR in available search.
- Citation caution: Use as preprint unless later venue confirmed.

### Core idea
Introduces context folding, an active context-management mechanism where agents branch into sub-trajectories for local subtasks and then fold the branch back into a concise outcome.

### Key contribution
Defines branch and return actions; trains the behavior end-to-end with FoldGRPO and process rewards for decomposition, focus, and information preservation.

### Method / approach
The agent maintains a main planning thread. It branches for token-heavy subtasks such as web search or code exploration, then returns/folds the branch by retaining only the key result. FoldGRPO optimizes folded trajectories and encourages efficient branching.

### Key findings
On BrowseComp-Plus and SWE-Bench Verified, the folding agent reportedly matches or outperforms ReAct baselines while using a much smaller active context, and improves strongly over summarization-based context management.

### Limitations
Preprint. Folding summaries may lose evidence needed for provenance or extraction validation. It evaluates deep research/coding, not structured field extraction.

### Relevance to my thesis / S3
Highly relevant to S3 memory/planning architecture and to web agents. For generalized extraction, context folding could manage long multi-page crawls while keeping the main context focused.

### How to use it in the literature review
Use in S3 and S5.3 as a mechanism for long-horizon planning and active context management. Cross-link to S6 to warn that extraction evidence should not be folded away unless provenance is preserved.

### Connects to
S3 context management; S5.3 planning; S5.7 deep research; S6 provenance.

### Sentence to add later
> Context folding reframes context compression as an action the agent learns to perform: it can open a temporary sub-trajectory for token-heavy work and fold only task-relevant results back into the main reasoning thread.

---

## 10. The Era of Agentic Organization: Learning to Organize with Language Models / AsyncThink

### Venue / status
- Year: 2025
- Authors: Zewen Chi, Li Dong, Qingxiu Dong, Yaru Hao, Xun Wu, Shaohan Huang, Furu Wei
- Status: arXiv preprint / CoRR; arXiv:2510.26658. No confirmed peer-reviewed venue found in available checks.
- Citation caution: Use as preprint/conceptual support.

### Core idea
Introduces agentic organization and AsyncThink, a learned organizer-worker reasoning protocol that structures internal thinking into concurrent, collaborative processes.

### Key contribution
Formalizes learning-to-organize as an optimization problem. Defines organizer, worker, agent pool, and organization policy. Uses Fork/Join textual actions and RL to train concurrent reasoning structures.

### Method / approach
An organizer LLM can Think, Fork subqueries to worker instances, Join returned results, and Answer. Training uses cold-start format fine-tuning followed by RL rewards for correctness, format compliance, and concurrency.

### Key findings
Reports improved accuracy-latency trade-offs over sequential and parallel thinking baselines on countdown, math reasoning, and Sudoku; demonstrates zero-shot generalization of learned asynchronous thinking to unseen tasks.

### Limitations
Reasoning benchmarks rather than embodied/web tasks. No browser/tool environment, provenance, safety, or extraction evaluation. Coordination overhead and correctness of worker decomposition remain open.

### Relevance to my thesis / S3
Useful for S3 as a new architecture category: learned organization policy rather than hand-coded workflow or naive parallel voting.

### How to use it in the literature review
Use in S3 under multi-agent/parallel reasoning and learned orchestration. Mention that web extraction could benefit from learned organization across search, navigation, extraction, and validation, but this is untested.

### Connects to
S3 orchestration; S5.3 planning; S8 scalable agent organizations.

### Sentence to add later
> AsyncThink suggests that agent organization can itself become a learned policy: an organizer dynamically forks sub-questions to workers and joins their outputs instead of relying on fixed sequential or parallel reasoning templates.

---

## 11. AgentOCR: Reimagining Agent History via Optical Self-Compression

### Venue / status
- Year: 2026
- Authors: Lang Feng et al.
- Status: arXiv preprint; arXiv:2601.04786, 8 Jan 2026. No confirmed peer-reviewed venue found in available checks.
- Citation caution: Use as preprint. Distinguish from OCR-Memory; AgentOCR is about self-compressing ongoing histories for RL/rollouts.

### Core idea
Represents accumulated observation-action histories as compact rendered images, exploiting visual token density to reduce token burden in long-horizon agents.

### Key contribution
Introduces segment optical caching to avoid repeated rendering and agentic self-compression, where the agent selects compression rates under a compression-aware reward.

### Method / approach
The textual trajectory is rendered into images and tokenized as visual patches. Hashable segments support caching. RL trains the agent to balance task success and compression. Evaluated on ALFWorld and search-based QA.

### Key findings
Reports preserving more than 95% of text-agent performance while reducing token consumption by more than 50%, with 20x rendering speedup from caching.

### Limitations
Rendering histories as images may lose fine-grained textual fidelity and adds visual-model dependency. It does not address field-level extraction, provenance, or web-page grounding. Storage/rendering trade-offs require deployment analysis.

### Relevance to my thesis / S3
Important for S3 memory architecture because it introduces multimodal memory compression. For web agents, it suggests an alternative to text-only history accumulation.

### How to use it in the literature review
Use as P3 under memory/context compression. Cross-link to S5.2 multimodal representation and S8 cost/efficiency.

### Connects to
S3 memory; S5.2 multimodal perception; S5.5 context failure; S8 efficiency.

### Sentence to add later
> AgentOCR shows a new memory-compression direction: instead of summarizing long trajectories into text, the agent can render them into compact visual histories and learn how much fidelity to preserve.

---

## 12. Aligning Agentic World Models via Knowledgeable Experience Learning / WorldMind

### Venue / status
- Year: 2026
- Authors: Baochang Ren et al.
- Status: arXiv preprint; arXiv:2601.13247, 19 Jan 2026. No confirmed peer-reviewed venue found in available checks.
- Citation caution: Use as preprint; embodied-agent domain, not web.

### Core idea
Treats LLM agents as implicit world models that need experiential alignment to avoid physically invalid plans.

### Key contribution
Introduces WorldMind, which builds a symbolic World Knowledge Repository from Process Experience (prediction errors) and Goal Experience (successful trajectories).

### Method / approach
The agent predicts next states, acts, compares prediction with real environment, reflects on mismatches, and stores causal/procedural rules. These rules are retrieved later to constrain rollout planning.

### Key findings
Reports superior performance on EB-ALFRED and EB-Habitat and cross-model/cross-environment transferability of learned world knowledge.

### Limitations
Embodied physical environments differ from web environments. Physical hallucination is not the same as DOM/action hallucination. Requires reliable environment feedback and verification.

### Relevance to my thesis / S3
Useful for S3 because it shows a general architecture for experience-based alignment: errors become persistent knowledge rather than discarded failures.

### How to use it in the literature review
Use as analogy for web agents: prediction errors from failed clicks, incorrect DOM assumptions, or invalid extraction paths could populate a web-world knowledge repository.

### Connects to
S3 memory/self-improvement; S5.3 world models; S5.5 failure modes; S8 adaptive web agents.

### Sentence to add later
> WorldMind reframes execution failures as training-free alignment signals: prediction errors are converted into explicit process knowledge that constrains future planning.

---

## 13. AtomMem: Learnable Dynamic Agentic Memory with Atomic Memory Operation

### Venue / status
- Year: 2026
- Authors: Yupeng Huo, Yaxi Lu, Zhong Zhang, Haotian Chen, Yankai Lin
- Status: arXiv preprint; arXiv:2601.08323, 13 Jan 2026. No confirmed peer-reviewed venue found in available checks.
- Citation caution: Use as preprint; results are long-context QA, not live web automation.

### Core idea
Reframes agent memory management as a learnable decision process over atomic CRUD operations: Create, Read, Update, Delete.

### Key contribution
Critiques static memory workflows and 'update every step' designs. Exposes memory operations as agent actions and trains the agent through SFT plus RL to orchestrate memory use depending on task needs.

### Method / approach
The agent interacts with long documents/web-like environments while maintaining a vector database and scratchpad. Memory actions are emitted as structured tokens; SFT teaches schema adherence and RL optimizes task-aligned memory policy.

### Key findings
AtomMem-RL outperforms static and partially dynamic baselines on HotpotQA, 2WikiMultihopQA, and Musique long-context variants; learned policies increasingly use Create/Update/Delete and stabilize Read usage.

### Limitations
Memory operations are evaluated mostly in QA settings with chunked documents. Real web tasks require memory security, provenance, stale-memory revision, and conflict resolution.

### Relevance to my thesis / S3
Very useful for S3: it gives a clean architectural vocabulary for agent memory as controllable action space rather than passive retrieval.

### How to use it in the literature review
Use in S3 memory section. For your thesis, map CRUD to web-extraction memory: Create site facts, Read prior selectors, Update schema mappings, Delete stale/poisoned memories.

### Connects to
S3 memory; S5.5 failure/staleness; S7 memory poisoning; S6 provenance.

### Sentence to add later
> AtomMem turns memory from a fixed retrieval module into an agent-controlled action space, allowing the agent to learn when to store, retrieve, revise, or delete information based on task demands.

---

## 14. AORCHESTRA: Automating Sub-Agent Creation for Agentic Orchestration

### Venue / status
- Year: 2026
- Authors: Jianhao Ruan et al.
- Status: arXiv preprint; arXiv:2602.03786, Feb 2026. No confirmed peer-reviewed venue found in available checks.
- Citation caution: Use as preprint; strong results but pending peer review.

### Core idea
Introduces an orchestration-centric framework that creates task-tailored sub-agents on demand using a unified four-tuple abstraction.

### Key contribution
Defines an agent as Instruction, Context, Tools, Model. The orchestrator dynamically specifies this tuple for sub-agents, separating working memory from capabilities and supporting cost-performance trade-offs.

### Method / approach
The central orchestrator decomposes the goal, curates task-relevant context, selects tools and model, creates a sub-agent, and invokes it as a tool. The orchestration policy can be improved via supervised fine-tuning and in-context cost-aware routing.

### Key findings
Reports strong gains on GAIA, Terminal-Bench, and SWE-Bench-Verified; AORCHESTRA outperforms popular baselines and supports plug-and-play sub-agent backends.

### Limitations
Preprint. Depends heavily on frontier models and benchmark selection. Dynamic sub-agent creation increases attack surface and makes reproducibility/debugging harder unless trace and policy logging are strong.

### Relevance to my thesis / S3
Highly relevant to S3 multi-agent architectures. It is one of the clearest papers for the 'sub-agent-as-tools' paradigm and dynamic role creation.

### How to use it in the literature review
Use in S3 under orchestration and agent-as-tool. For web extraction, propose sub-agents for search, navigation, DOM grounding, extraction, schema validation, provenance, and security auditing.

### Connects to
S3 MAS; S5.3 planning; S6 extraction stack; S7 tool/security; S8 cost-aware orchestration.

### Sentence to add later
> AORCHESTRA formalizes sub-agents as dynamically creatable executors specified by instruction, context, tools, and model, shifting multi-agent design from fixed roles to on-demand specialization.

---

## 15. Beyond RAG for Agent Memory: Retrieval by Decoupling and Aggregation / xMemory

### Venue / status
- Year: 2026
- Authors: Zhanghao Hu, Qinglin Zhu, Hanqi Yan, Yulan He, Lin Gui
- Status: arXiv preprint; arXiv:2602.02007, 2 Feb 2026. No confirmed peer-reviewed venue found in available checks.
- Citation caution: Use as preprint; personal-memory focus, not web automation.

### Core idea
Argues that standard top-k RAG retrieval is mismatched to agent memory because memories are coherent, correlated streams rather than diverse documents.

### Key contribution
Introduces xMemory, which organizes memory into a hierarchy of themes, semantic units, episodes, and raw messages, using a sparsity-semantics objective and top-down retrieval.

### Method / approach
Memory construction decouples dialogue history into semantic components, groups them into themes, and maintains intact episode/message units. Retrieval first selects diverse themes/semantics, then expands to finer evidence only when it reduces uncertainty.

### Key findings
Reports better answer quality and token efficiency on LoCoMo and PerLTQA across multiple LLM backbones. xMemory reduces redundant context while preserving temporally linked evidence.

### Limitations
Designed for conversational/personal memory. Web extraction involves structured data, DOM evidence, and source provenance; these are not directly evaluated.

### Relevance to my thesis / S3
Useful in S3 memory/RAG discussion: agent memory is not ordinary RAG. This supports a critique of naively using vector search over trajectory chunks.

### How to use it in the literature review
Use to explain why extraction agents need structure-aware memory for site histories, selector decisions, and evidence chains rather than fixed top-k retrieval.

### Connects to
S3 memory; S6 provenance/evidence chains; S5.5 lost-in-the-middle; S8 scalable memory.

### Sentence to add later
> xMemory highlights a key architectural mismatch: agent memory is a temporally entangled stream, so retrieval must control redundancy without fragmenting evidence chains.

---

## 16. Caesar: Deep Agentic Web Exploration for Creative Answer Synthesis

### Venue / status
- Year: 2026
- Authors: Jason Liang, Elliot Meyerson, Risto Miikkulainen
- Status: arXiv preprint; arXiv:2604.20855, v1 Feb 2026, v2 May 2026. No confirmed peer-reviewed venue found in available checks.
- Citation caution: Use as web/deep-research preprint. Creativity framing is less directly relevant to extraction.

### Core idea
Proposes an agentic web exploration architecture that builds a knowledge graph during traversal and uses adversarial synthesis to generate novel, coherent answers.

### Key contribution
Combines domain-specific role adaptation, graph-augmented insight generation, knowledge-guided exploration, and adversarial artifact synthesis. Treats navigation history and insight graph as active control signals, not passive memory.

### Method / approach
Phase 1 performs deep web exploration with Perceive-Think-Act, a navigational stack, and a graph/KB. Phase 2 performs recursive synthesis, critique, adversarial query refinement, draft merging, and post-processing.

### Key findings
Claims stronger novelty and structural coherence than state-of-the-art research agents on creative synthesis tasks. Cost analysis shows exploration is expensive due to heavy page ingestion and link processing.

### Limitations
Targets creative synthesis, not reliable extraction. Evaluation of novelty is inherently subjective. It may trade convergent accuracy for exploratory diversity. High cost and dependence on web retrieval stack are concerns.

### Relevance to my thesis / S3
Useful for S3/S5.7 as an example of graph-based web exploration and active information foraging. For extraction, its graph/stack memory can inspire navigation-state tracking.

### How to use it in the literature review
Use as P3 support in S3 for web-exploration architectures, and in S5.7 for deep research. Avoid using it as evidence for extraction performance.

### Connects to
S3 web agent architecture; S5.7 deep research; S6 source discovery; S8 cost-aware exploration.

### Sentence to add later
> Caesar shows how web exploration can move beyond linear ReAct history by maintaining a graph of visited concepts and using that graph as an active signal for backtracking, branching, and synthesis.

---

## 17. Data Agents: Levels, State of the Art, and Open Problems

### Venue / status
- Year: 2026
- Authors: Yuyu Luo, Guoliang Li, Ju Fan, Nan Tang
- Status: SIGMOD 2026 Tutorial; arXiv:2602.04261; official SIGMOD 2026 accepted tutorial page found.
- Citation caution: Cite as tutorial/roadmap, not as a full research paper.

### Core idea
Proposes an L0-L5 autonomy taxonomy for data agents across data management, preparation, and analysis.

### Key contribution
Clarifies the overloaded term 'data agent' and links autonomy level to responsibility, governance, and data lifecycle scope. Distinguishes assistants/copilots from conditional, high, and full autonomy data agents.

### Method / approach
Tutorial-style synthesis of systems and research directions; categorizes systems by lifecycle stage and autonomy level, highlighting Proto-L3 orchestration systems and future L4/L5 challenges.

### Key findings
The key insight is that data agents should be evaluated not only by task success but by autonomy, governance, robustness, adaptability, and lifecycle coverage.

### Limitations
Tutorial, not empirical benchmark. Focuses on data systems broadly, not web extraction specifically. Higher autonomy levels remain aspirational.

### Relevance to my thesis / S3
Highly relevant to thesis positioning because web data extraction sits at the boundary between web agents and data agents. This taxonomy helps frame generalized extraction as a data-lifecycle agent problem, not only browser control.

### How to use it in the literature review
Use in S3 or S6 as a bridge to data management literature. It can support an autonomy-level table for web extraction agents.

### Connects to
S3 agent taxonomy; S6 data extraction; S8 open challenges and evaluation.

### Sentence to add later
> The data-agent literature emphasizes that autonomy must be tied to accountability: as agents move from assistants to workflow orchestrators, evaluation must include governance, robustness, and data-quality guarantees, not only task completion.

---

## 18. AgentScope 1.0: A Developer-Centric Framework for Building Agentic Applications

### Venue / status
- Year: 2025
- Authors: Dawei Gao et al.
- Status: arXiv preprint; arXiv:2508.16279, 22 Aug 2025. No confirmed peer-reviewed venue found in available checks.
- Citation caution: Framework/technical report; good for tool/ecosystem examples, not core scientific evidence.

### Core idea
Presents AgentScope 1.0, a modular framework for building agentic applications with ReAct grounding, message/model/memory/tool abstractions, MCP integration, evaluation, tracing, sandboxing, and built-in agents.

### Key contribution
Defines foundational modules; supports asynchronous execution, parallel tool calls, memory modules, MCP tool registration, browser-use agent, deep research agent, and meta-planner agent.

### Method / approach
Provides developer-facing abstractions and interfaces. Browser-use agent combines visual/web textual information, subtask decomposition, multi-tab browsing, and long-page chunking. Meta Planner uses roadmap tools and worker management for complex workflows.

### Key findings
Not primarily an experimental paper; its value is architectural and practical. It shows how current frameworks operationalize agent components for real-world deployment.

### Limitations
Framework paper; evaluation may not prove scientific performance. Framework capabilities can change rapidly. Not extraction-specific and does not guarantee safety or correctness.

### Relevance to my thesis / S3
Useful for S3 tools/framework examples and grey-literature ecosystem table. Also useful for showing how research abstractions become developer APIs.

### How to use it in the literature review
Include in S3 framework subsection and grey literature/tooling table. Mention MCP support as important for tool interoperability.

### Connects to
S3 framework ecosystem; S5.3 browser agents; S7 sandbox/security; S8 deployment.

### Sentence to add later
> AgentScope illustrates the engineering convergence around modular agent runtimes: messages, models, memory, and tools are exposed as separable components, while MCP integration, tracing, sandboxing, and built-in browser/deep-research agents support deployment-oriented workflows.

---

## 19. AgentSquare: Automatic LLM Agent Search in Modular Design Space

### Venue / status
- Year: 2024
- Authors: Not fully extracted in current snippets
- Status: Preprint; title file indicates 2024-10. No confirmed peer-reviewed venue found in available checks.
- Citation caution: Use as preprint. Verify authors and arXiv/OpenReview before final bibliography.

### Core idea
Proposes automatic search over modular LLM-agent design space.

### Key contribution
Abstracts an agent as a combination of Planning, Reasoning, Tool-use, and Memory modules, then searches over combinations to optimize performance on tasks.

### Method / approach
Builds a modular design space from existing agents and recombines modules. The framework evaluates candidate agents on task benchmarks and updates module/experience pools.

### Key findings
The important lesson is architectural modularity: agent performance depends on interactions between planning, reasoning, memory, and tool-use modules rather than a single prompting recipe.

### Limitations
Preprint and broad task evaluation. Search may be expensive and benchmark-specific. It does not provide extraction-specific modules or provenance evaluation.

### Relevance to my thesis / S3
Useful for S3 taxonomy because it gives a clean decomposition into agent modules and supports the idea that agent design can be optimized.

### How to use it in the literature review
Use in S3 as an example of modular architecture search. Could support a table showing agent design dimensions.

### Connects to
S3 architecture taxonomy; S5.4 optimization/training; S8 automatic agent design.

### Sentence to add later
> AgentSquare treats agent design itself as a search problem over planning, reasoning, tool-use, and memory modules, reinforcing the view that LLM agents are modular systems rather than monolithic prompts.

---

## 20. Orchestrating Agents and Data for Enterprise: A Blueprint Architecture for Compound AI

### Venue / status
- Year: 2025
- Authors: Not fully extracted in current snippets
- Status: arXiv preprint; arXiv:2504.08148, 10 Apr 2025.
- Citation caution: Use as architectural/enterprise systems perspective, not web-agent benchmark evidence.

### Core idea
Proposes a blueprint architecture for compound AI in enterprise settings, emphasizing data/control orchestration, registries, planners, dedicated components, streaming databases, observability, and QoS optimization.

### Key contribution
Argues against LLMs handling everything end-to-end; instead places LLMs inside a larger architecture with dedicated retrieval, planning, verification, moderation, model/service registries, and orchestration layers.

### Method / approach
Conceptual enterprise architecture. Highlights data/service discovery, declarative plans, streaming control/data flows, optimization objectives, containers, restarts, observability, and QoS constraints.

### Key findings
The key lesson is system-level: practical agents need integration, control, observability, optimization, and data governance, especially in enterprise environments with many data sources and services.

### Limitations
Blueprint/position style; lacks a standardized benchmark and may be high-level. Not web extraction-specific.

### Relevance to my thesis / S3
Very useful for S3 when shifting from agent algorithms to deployable agent systems. Supports later deployment and cost/observability sections.

### How to use it in the literature review
Use as P3 support in S3 framework/ecosystem discussion and S8 deployment constraints.

### Connects to
S3 compound AI; S7 governance; S8 deployment, cost, observability.

### Sentence to add later
> Enterprise compound-AI architectures argue that reliable agents should be embedded in controlled systems with explicit data/service registries, orchestration layers, observability, and QoS objectives, rather than treated as autonomous LLM prompts operating alone.

---

## 21. Towards Agentic RAG with Deep Reasoning: A Survey of RAG-Reasoning Systems in LLMs

### Venue / status
- Year: 2025
- Authors: Not fully extracted in current snippets
- Status: Survey preprint/technical paper; uploaded file dated 2025-06. Final venue not confirmed in available checks.
- Citation caution: Use as related survey/background; verify final venue before bibliography.

### Core idea
Surveys RAG-reasoning systems and distinguishes predefined reasoning workflows from agentic reasoning workflows.

### Key contribution
Frames predefined RAG as System-1-like: structured, modular, efficient, but constrained. Frames agentic RAG as System-2-like: autonomous, adaptive, tool-using, and better for complex multi-step tasks.

### Method / approach
Categorizes RAG workflows into route-based, loop-based, tree-based, hybrid-modular, prompt-based agentic, and training-based agentic approaches.

### Key findings
The most useful conceptual distinction is between fixed pipeline retrieval and agentic retrieval, where the LLM identifies knowledge gaps, formulates queries, selects tools, and iteratively refines.

### Limitations
Survey is broad and not focused on browser automation or extraction. It may overlap heavily with other RAG surveys. Needs venue verification.

### Relevance to my thesis / S3
Useful for S3 and S6 to explain why extraction agents need agentic retrieval/planning rather than one-shot RAG over pages.

### How to use it in the literature review
Use as related survey and terminology support, not as primary evidence.

### Connects to
S3 tool/retrieval agents; S6 extraction; S5.7 deep research.

### Sentence to add later
> Agentic RAG reframes retrieval as an active decision-making loop: the model decides when to search, what to search for, which tool or retriever to use, and how to revise its plan after new evidence arrives.

---

## 22. PRefLexOR: Preference-based Recursive Language Modeling for Exploratory Optimization of Reasoning and Agentic Thinking

### Venue / status
- Year: 2024
- Authors: Not fully extracted in current snippets
- Status: Preprint from uploaded file; final venue not confirmed in available checks.
- Citation caution: Use only as peripheral conceptual P3; verify bibliographic metadata before citation.

### Core idea
Explores recursive reasoning, preference-based refinement, symbolic representation, interdisciplinary synthesis, collaborative refinement, and evolutionary memory updates.

### Key contribution
Combines critic/refiner style loops with multi-agent collaborative refinement and symbolic abstraction concepts. Proposes richer recursive reasoning workflows.

### Method / approach
Iterative process involving initial response generation, symbolic representation, interdisciplinary synthesis, contemplative reflection, collaborative agents, integration, and evolutionary memory update.

### Key findings
The main value is conceptual: agentic reasoning can be organized as recursive synthesis and refinement rather than single-pass reasoning.

### Limitations
Likely speculative/theoretical and broad; unclear empirical validation from snippets. Not web-agent/extraction-specific.

### Relevance to my thesis / S3
Weak P3 for S3. Use only if you want an example of recursive/self-reflective agentic thinking, not as core evidence.

### How to use it in the literature review
Maybe exclude from final survey or keep as background note. If included, cite carefully and briefly.

### Connects to
S3 reflection; S5.3 reasoning; S8 self-improving agents.

### Sentence to add later
> Recursive agentic-thinking frameworks such as PRefLexOR represent a more speculative strand of work in which reasoning is iteratively abstracted, synthesized, critiqued, and stored as evolving memory.

---

## 23. MCP-Flow: Facilitating LLM Agents to Master Real-World, Diverse and Scaling MCP Tools

### Venue / status
- Year: 2026
- Authors: Wenhao Wang et al.
- Status: arXiv preprint; arXiv:2510.24284v3, 16 Apr 2026. No confirmed peer-reviewed venue found in available checks.
- Citation caution: Use as preprint/dataset; very relevant to MCP/tool ecosystem but not peer-reviewed yet.

### Core idea
Presents an automated web-agent-driven pipeline for discovering MCP servers, synthesizing tool-use data, and training models to use real-world MCP tools.

### Key contribution
Collects 1,166 servers and 11,536 tools, generates 68,733 instruction-function-call pairs and 6,439 trajectories, and supports training, retrieval augmentation, and server/tool evaluation.

### Method / approach
Uses web agents over MCP marketplaces, local deployment, tool extraction, few-shot generation, slot-fill revision, WizardLM-style evolution, function-call generation, tool-response collection, and filtering through similarity, tool-invocation checks, and quality scoring.

### Key findings
Fine-tuned small models outperform much larger models on MCP tool selection/function formatting. Retrieval-augmented examples improve closed models. Initial function-call generation improves GAIA performance and can reduce costs.

### Limitations
Synthetic tasks differ from messy real users; many servers may fail, degrade, or require API keys; single-turn function invocation dominates; real MCP ecosystem has security/adversarial risks.

### Relevance to my thesis / S3
Very relevant to S3 tool-use architecture and S7 security. For generalized web extraction, MCP-Flow is evidence that the tool ecosystem is becoming too large for manual curation, requiring automated tool discovery/evaluation.

### How to use it in the literature review
Use in S3 tool-use/MCP subsection and tools/framework table. Cross-link to S7 for adversarial MCP servers and S8 for tool evaluation.

### Connects to
S3 tools/MCP; S5.4 training; S7 tool security; S8 scaling/evaluation.

### Sentence to add later
> MCP-Flow shows that tool use is becoming an ecosystem-scale problem: agents must not only call tools, but discover, select, format, evaluate, and learn from thousands of heterogeneous MCP tools.

---

## 24. OCR-Memory: Optical Context Retrieval for Long-Horizon Agent Memory

### Venue / status
- Year: 2026
- Authors: Jinze Li et al.
- Status: arXiv preprint; arXiv:2604.26622, 29 Apr 2026. A LinkedIn claim indicates ACL 2026 Main acceptance, but official ACL Anthology/proceedings verification was not found in available checks.
- Citation caution: Until official ACL page exists, cite as arXiv preprint; optionally note claimed ACL 2026 acceptance only after official confirmation.

### Core idea
Stores complete agent trajectories as images and retrieves relevant evidence via locate-and-transcribe: visual anchors are selected, then exact original text is deterministically fetched.

### Key contribution
Introduces visual memory bank, Set-of-Mark anchors, index-only retrieval, deterministic text fetching, adaptive multi-resolution storage, and active-recall upsampling.

### Method / approach
Historical trajectories are rendered into marked images. The optical retriever predicts relevant segment IDs instead of generating free text; selected IDs map to exact stored text. Training repurposes HotpotQA supporting-fact labels and fine-tunes DeepSeek-OCR-style architecture.

### Key findings
Reports gains over text retrieval/memory baselines on Mind2Web and AppWorld, 100% evidence-fetch faithfulness after segment selection, and strong token savings. Shows trade-off: fewer reasoning-context tokens but more storage and retrieval latency.

### Limitations
Requires fine-tuned optical retriever and rendering pipeline. More disk and latency than text RAG. Exact fetching is faithful only after correct segment selection; relevance errors can still occur.

### Relevance to my thesis / S3
Highly relevant to S3 memory and S5.2 multimodal grounding. For web extraction, it suggests preserving full interaction evidence without injecting all text into context.

### How to use it in the literature review
Use under S3 long-horizon memory and S5.2 multimodal representation. Cross-link to S6 provenance because exact text fetching is close to source-grounded evidence retrieval.

### Connects to
S3 memory; S5.2 visual grounding; S6 provenance; S8 cost/token trade-offs.

### Sentence to add later
> OCR-Memory separates evidence selection from evidence generation: the model selects visual segment IDs, while exact text is fetched deterministically, reducing hallucinated memory recall.

---

## 25. StructMem: Structured Memory for Long-Horizon Behavior in LLMs

### Venue / status
- Year: 2026
- Authors: Buqiang Xu et al.
- Status: arXiv preprint; arXiv:2604.21748, 23 Apr 2026. No confirmed peer-reviewed venue found in available checks.
- Citation caution: Use as preprint; promising but not peer-reviewed.

### Core idea
Proposes event-centric hierarchical memory that preserves factual and relational event bindings and periodically consolidates cross-event relations.

### Key contribution
Offers a middle ground between flat vector memory and graph memory: event-level dual-perspective extraction plus cross-event consolidation without full graph construction.

### Method / approach
Extracts factual entries and relational entries from each utterance; anchors them temporally; periodically retrieves semantically related historical events and synthesizes cross-event memory. Evaluated on LoCoMo.

### Key findings
Reports state-of-the-art or strong performance on LoCoMo with much lower construction cost than graph-memory methods. Fidelity studies report low hallucination in event extraction and show grounding constraints reduce spurious cross-event links.

### Limitations
Prompt-dependent extraction quality. No explicit conflict resolution or memory updating; stale facts may persist. Dialogue memory differs from web extraction memory.

### Relevance to my thesis / S3
Very useful for S3 memory architecture. It supports a key thesis point: extraction agents need structured, temporally anchored memory, but full graph memory can be expensive and fragile.

### How to use it in the literature review
Use in S3 under structured memory and in S6 as inspiration for event/source-bound extraction provenance.

### Connects to
S3 memory; S6 provenance; S5.5 temporal/stale memory; S8 scalable memory.

### Sentence to add later
> StructMem suggests that effective long-horizon memory may require event-level bindings and cross-event consolidation, not merely isolated facts or expensive full knowledge graphs.

---

## 26. LatentMem: Customizing Latent Memory for Multi-Agent Systems

### Venue / status
- Year: 2026
- Authors: Muxin Fu et al.
- Status: arXiv preprint; arXiv:2602.03036, 3 Feb 2026. No confirmed peer-reviewed venue found in available checks.
- Citation caution: Use as preprint; latent-memory claims need peer review and reproducibility checks.

### Core idea
Introduces role-aware, token-efficient latent memories for multi-agent systems.

### Key contribution
Targets two MAS memory problems: memory homogenization, where all agents receive similar memories, and information overload from verbose memory entries. Uses a memory composer and Latent Memory Policy Optimization.

### Method / approach
Retrieves raw MAS trajectories from an experience bank, combines them with agent role profiles, composes fixed-length latent memory tokens, injects them into each agent, and optimizes the composer with LMPO while keeping backbones frozen.

### Key findings
Reports performance gains across six benchmarks and four MAS frameworks, with lower token/time cost than many memory baselines. Case study shows role-aware latent memory reduces step repetition and blind trajectory following.

### Limitations
Latent memories are less interpretable than textual memories; harder to audit, edit, or secure. Not evaluated on web extraction or source-verifiable tasks.

### Relevance to my thesis / S3
Useful for S3 multi-agent memory. It contrasts with textual memory frameworks and highlights the role-specific memory problem in MAS.

### How to use it in the literature review
Use in S3 under multi-agent memory customization. For thesis, note that extraction agents may need role-specific memory but source-verifiability favors transparent text/evidence memory over opaque latent memory.

### Connects to
S3 MAS memory; S7 auditability/security; S8 efficiency vs interpretability.

### Sentence to add later
> LatentMem shows that multi-agent memory should be role-aware: a planner, extractor, validator, and security auditor should not all receive the same memory representation.

---

# Tools, frameworks, and ecosystem examples for S3

| Category | Examples from S3 P3 batch | How to use |
|---|---|---|
| Agent framework/runtime | AgentScope 1.0, AORCHESTRA, AgentSquare | Shows modularization of agent components and developer-facing abstractions. |
| Multi-agent orchestration | AORCHESTRA, Orchestrator, AsyncThink, Information Sharing MAS | Supports the transition from static role assignment to dynamic/learned coordination. |
| Memory systems | ACE, AtomMem, xMemory, StructMem, OCR-Memory, AgentOCR, LatentMem | Use as the main P3 cluster for S3 memory architecture. |
| Tool-use and MCP ecosystem | MCP-Flow, ALITA-G, AlphaApollo, AgentScope MCP support | Shows tool discovery, tool selection, tool generation, and MCP integration. |
| Deep research / web exploration | InfoSeek, Caesar, AgentScope Deep Research Agent, Context-Folding | Useful bridge to S5.7 and S6 source discovery. |
| Enterprise/production systems | Enterprise Compound AI blueprint, AgentScope sandbox/tracing/evaluation | Supports deployment, observability, cost, and governance discussion. |
| Related surveys | Agentic AI survey, Agentic RAG survey, Data Agents tutorial | Use for positioning, definitions, and related-survey comparison tables. |

# Section-level critique for S3 after adding P3

## What P3 strengthens
P3 papers make S3 more current and more architectural. They show that modern agents are no longer only “LLM + prompt + tools”; they are **orchestrated systems** with state, tool registries, dynamic sub-agents, memory controllers, context managers, and deployment infrastructure.

## Risk
Do not let P3 turn S3 into a list of every 2025/2026 preprint. Many papers are arXiv-only and evaluate on different domains. Use them to show trends, not as hard evidence.

## Best final S3 structure after adding P3
1. ReAct and tool-using agents.
2. Planner-executor and hierarchical agents.
3. Memory and context engineering.
4. Multi-agent systems and orchestration.
5. Self-improving/self-evolving agents.
6. Frameworks, MCP, and deployment ecosystem.
7. Gap: current agent architectures still lack extraction-specific grounding, provenance, schema validation, and safe long-horizon execution.

# Direct thesis gap from S3 P3

The current S3 literature shows rapid progress in **agent architecture**, but most systems optimize task success on QA, coding, planning, math, or generic tool-use benchmarks. Very few directly address the full architecture needed for generalized web data extraction: source discovery, browser interaction, field-level extraction, schema-constrained validation, provenance preservation, adversarial-content handling, and cost-aware deployment. This gap justifies moving from generic LLM-agent architectures to extraction-specific web-agent architectures in later sections.

