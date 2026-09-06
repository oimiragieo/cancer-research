# Start cancer-research Ralph 10-minute tick loop
# Emits AGENT_LOOP_TICK_cancerresearch for the Cursor agent harness to pick up.
# Stop with: Get-Content $env:TEMP\cr_ralph_loop.pid | ForEach-Object { Stop-Process -Id $_ -Force }

$ErrorActionPreference = "Continue"
$pidFile = Join-Path $env:TEMP "cr_ralph_loop.pid"
$Prompt = @'
Continue cancer-research Ralph loop: run python scripts/ralph_tick.py; Exa/CT.gov-search top NEXT_QUERIES; append 3+ sources via $env:TEMP\cr_wakeN.py to corpus/sources.yaml; update docs/hillclimb.md + design/gaps/cure-climb-board.md (EOF wake header); rotate NEXT_QUERIES; validate_corpus + status + pytest --cache-clear; git add the four wake files; commit+push with $msg="ralph wake #N: ..."; Safety: literature/systems only, no DIY biotech. Honor pause if CEO said pause.
'@

$payload = "AGENT_LOOP_TICK_cancerresearch " + (@{ prompt = $Prompt } | ConvertTo-Json -Compress)
$PID | Set-Content -Path $pidFile -Encoding ascii
Write-Output "Ralph tick loop started PID=$PID pidfile=$pidFile"
while ($true) {
    Start-Sleep -Seconds 600
    Write-Output $payload
}
