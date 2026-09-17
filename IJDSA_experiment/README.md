# Wireless-headphones extraction experiment

This folder contains the controlled experiment used in the survey revision.

The design is simple: three agent architectures are paired with the same three model backends and tested on four frozen shopping sites with three repetitions. That gives 108 formal runs.

## What is here

- `agents/` — the three agent implementations.
- `snapshots/` — the four frozen HTML pages.
- `gold/` — gold records and field-level provenance.
- `prompts/` — prompts used by the agents.
- `schema/` — output schema.
- `r1/` — shared experiment code and evaluator.
- `runs/` — raw outputs for the nine architecture-model configurations.
- `results/` — scored outputs, per-run details, and summary tables.
- `docs/PROTOCOL.md` — exact evaluation protocol.
- `docs/RESULTS.md` — short result summary and integrity notes.
- `freeze_manifest.json` — hashes for the frozen experiment inputs and code.

Temporary probes, smoke tests, diagnostics, and development changelogs were removed from the cleaned repository because they are not needed to reproduce or inspect the reported results.

## Architectures

- **A1 — Direct DOM snapshot:** one-step extraction from a frozen product-card DOM snapshot and evidence catalog.
- **A2 — Ground and verify:** two stages; first choose values and source nodes, then verify/finalize with exact source details.
- **A3 — Playwright-MCP ReAct:** iterative browser agent using Playwright MCP on the local frozen page.

## Models

- Gemma: `gemma4-131k:latest`
- Qwen: `qwen2.5vl:7b`
- Kimi: `kimi-k2.6`

Gemma and Qwen run locally through Ollama. Kimi uses the Moonshot API.

## Run

Create the Python environment, install the requirements, and install the Node dependency used by Playwright MCP. Put API settings in a local `.env` based on `.env.example`.

Windows:

```powershell
./setup.ps1
./run_experiment.ps1
```

Linux/macOS:

```bash
./setup.sh
./run_experiment.sh
```

The main entry point is also available directly:

```bash
python experiment.py --help
```

## Final result

All 108 scheduled runs were completed and scored. The strongest observed configuration in this controlled study was A1 + Kimi with macro Field F1 0.9440. See `docs/RESULTS.md` and `results/summary_table.csv` for the full table.

The experiment is intentionally narrow: one product domain and four frozen sites. It is used to test the evaluation framework and expose different failure modes, not to claim a general model or architecture ranking.
