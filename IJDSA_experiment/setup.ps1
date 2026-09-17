$ErrorActionPreference = 'Stop'
Set-Location $PSScriptRoot
function Check-Exit { if ($LASTEXITCODE -ne 0) { throw "Command failed (exit $LASTEXITCODE)" } }
if (-not (Get-Command python -ErrorAction SilentlyContinue)) { throw 'Install Python 3.11+ and add it to PATH.' }
if (-not (Get-Command node -ErrorAction SilentlyContinue)) { throw 'Install Node.js 20+ and add it to PATH.' }
if (-not (Get-Command ollama -ErrorAction SilentlyContinue)) { Write-Warning 'Ollama not found yet. Install it before doctor/run-all.' }
python -m venv .venv
Check-Exit
& .\.venv\Scripts\python.exe -m pip install -r requirements.txt
Check-Exit
npm.cmd ci
Check-Exit
& .\.venv\Scripts\python.exe -m playwright install chromium
Check-Exit
if (-not (Test-Path '.env')) { Copy-Item .env.example .env }
& .\.venv\Scripts\python.exe experiment.py verify --browser
Check-Exit
Write-Host 'Setup complete.'
Write-Host 'Next: ollama pull gemma4:e4b'
Write-Host '      ollama pull qwen3-vl:8b'
Write-Host 'Set MOONSHOT_API_KEY in .env, keep Ollama running, then execute .\run_experiment.ps1'
