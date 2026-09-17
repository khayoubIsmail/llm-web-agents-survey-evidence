#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
.venv/bin/python experiment.py doctor
.venv/bin/python experiment.py smoke
run_status=0
.venv/bin/python experiment.py run-all || run_status=$?
.venv/bin/python experiment.py evaluate
if [ "$run_status" -ne 0 ]; then printf '%s\n' 'Some formal runs failed; retained as failures in evaluation.'; fi
printf '%s\n' 'Finished. Open results/REPORT.md'
