# R1 headphone extraction results

Scored 108/108 runs. Complete scheduled experiment.

**Design:** 3 distinct agent architectures × 3 LLM backends = 9 architecture-model configurations.

| Agent config | Architecture | Model | Runs | Field F1 (macro) | Field F1 (micro) | Task success | Verified provenance precision |
|---|---|---|---:|---:|---:|---:|---:|
| A1__gemma | A1 | gemma4-131k:latest | 12 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |
| A1__qwen | A1 | qwen2.5vl:7b | 12 | 0.0581 | 0.0541 | 0.0000 | 0.1250 |
| A1__kimi | A1 | kimi-k2.6 | 12 | 0.9440 | 0.9492 | 0.8333 | 0.8822 |
| A2__gemma | A2 | gemma4-131k:latest | 12 | 0.2199 | 0.2543 | 0.0000 | 0.5139 |
| A2__qwen | A2 | qwen2.5vl:7b | 12 | 0.2576 | 0.3762 | 0.0833 | 0.2152 |
| A2__kimi | A2 | kimi-k2.6 | 12 | 0.8524 | 0.8649 | 0.7500 | 0.7899 |
| A3__gemma | A3 | gemma4-131k:latest | 12 | 0.0455 | 0.0510 | 0.0000 | 0.1875 |
| A3__qwen | A3 | qwen2.5vl:7b | 12 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |
| A3__kimi | A3 | kimi-k2.6 | 12 | 0.7872 | 0.8033 | 0.1667 | 0.8021 |

A1 is a direct frozen-DOM snapshot agent; A2 is a two-stage schema-state ground-and-verify agent; A3 is an iterative Playwright-MCP ReAct agent. All three architectures are evaluated with the same Gemma, Qwen, and Kimi model set. See docs/PROTOCOL.md.