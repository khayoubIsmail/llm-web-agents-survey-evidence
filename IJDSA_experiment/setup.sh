#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
npm ci
.venv/bin/python -m playwright install chromium
if [ ! -f .env ]; then cp .env.example .env; fi
.venv/bin/python experiment.py verify --browser
printf '%s\n' 'Setup complete. Pull gemma4:e4b and qwen3-vl:8b in Ollama, set MOONSHOT_API_KEY in .env, then run bash run_experiment.sh'
