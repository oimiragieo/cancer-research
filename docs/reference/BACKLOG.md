# BACKLOG — cancer-research

## Ralph ops

| # | Item |
|---|------|
| 1 | Keep Ralph tick loop healthy (~600s; sentinel `AGENT_LOOP_TICK_cancerresearch`) |
| 2 | **Public repo:** commit+push four wake files each wake (`sources.yaml`, `hillclimb.md`, `cure-climb-board.md`, `ralph_tick.py`) |
| 3 | Prefer `$env:TEMP\cr_wakeN.py` appends; rotate `NEXT_QUERIES` |
| 4 | Honor CEO pause — stop loop PID; do not run next wake |

## Clinical climb (sentinels)

See `SENTINEL_BOARD.md` S1–S8. Highest-value absences currently: MonumenTAL-6 KM, LOTIS-5 manuscript, IMCODE003 DFS, CAR-PRISM 24mo, GIANT lead-in.

## Software

| # | Item |
|---|------|
| 10 | Retarget `portfolio_optimizer` / `hallmarks_graph` topic tags to oncology modalities |
| 11 | Optional cure-evidence scorer (RCT + FU years + endpoint class) — no invented numbers |
| 12 | Trim leftover longevity-only algorithm tests when they confuse jr analysts |
