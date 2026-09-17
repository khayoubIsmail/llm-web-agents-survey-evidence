$ErrorActionPreference = 'Stop'
Set-Location $PSScriptRoot
$PythonExe = Join-Path $PSScriptRoot '.venv\Scripts\python.exe'
if (-not (Test-Path $PythonExe)) { throw 'Run setup.ps1 first.' }
& $PythonExe experiment.py doctor
if ($LASTEXITCODE -ne 0) { throw 'Preflight failed; no experiment runs started.' }
& $PythonExe experiment.py smoke
if ($LASTEXITCODE -ne 0) { throw 'Smoke run failed. Inspect smoke_runs before running again.' }
& $PythonExe experiment.py run-all
$RunExit = $LASTEXITCODE
& $PythonExe experiment.py evaluate
if ($LASTEXITCODE -ne 0) { throw 'Evaluation incomplete; inspect errors and resume run-all.' }
if ($RunExit -ne 0) { Write-Warning 'Some formal runs failed. They remain failures in evaluation; see metadata.' }
Write-Host 'Finished. Open results\REPORT.md or results\summary_table.csv'
