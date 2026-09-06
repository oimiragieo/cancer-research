# Jr analyst runbook — cancer-research

Audience: someone picking up this repo cold. Read this before inventing anything.

## What this product is

An **oncology cure research engine**: curated literature corpus + Hybrid D ultra-design + Ralph hill-climb loop that banks honest "still missing" clinical pins (and disease-specific cure existence proofs).

It is **not** medical advice. It is **not** a place to invent trial outcomes or milligrams.

## Safety (non-negotiable)

- Literature + systems design only.
- No DIY gene editing, synthesis recipes, or personal dosing.
- Never fill unpublished NCT / Results from adjacency (CRC ≠ PDAC, hema ≠ solid, press ≠ KM).

## First 15 minutes

```powershell
cd C:\dev\projects\cancer-research
pip install -r requirements-dev.txt
python scripts\status.py
python scripts\validate_corpus.py
pytest -q --cache-clear
```

Expect: `GOAL_MET`, `CORPUS_OK`, tests green.

## How Ralph wakes work

1. Read `scripts/ralph_tick.py` → `NEXT_QUERIES` (top 3).
2. Search Exa / ClinicalTrials.gov.
3. Append ≥3–5 entries via `$env:TEMP\cr_wakeN.py` to `corpus/sources.yaml` (unique `id`, quote `summary:` if it contains `:`).
4. Append `## Tick N` to `docs/hillclimb.md` and `## Update (Ralph wake #N)` to `design/gaps/cure-climb-board.md` (**EOF only**).
5. Rotate top researched queries to the bottom of `NEXT_QUERIES`.
6. `validate_corpus.py` → `status.py` → `pytest`.
7. If public git: commit+push the **four** wake files (PowerShell `$msg=…`; no bash heredoc).
8. Keep `scripts/start_ralph_loop.ps1` running (~600s ticks) unless CEO says pause.

Skill: `cancer-research-ralph-hillclimb`. Rules: `AGENTS.md`.

## Banking a negative (this is progress)

If Results / NCT / durability still absent, write an explicit negative corpus entry and climb-board update. Do **not** invent numbers to "close" the pin.

## What software cannot close

See `docs/reference/SENTINEL_BOARD.md`. Those stay **OPEN** under Ralph sentinel until clinics publish.
