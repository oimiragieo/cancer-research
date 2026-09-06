# AGENTS.md — cancer-research

Oncology cure research engine (Hybrid D). Literature + systems design only. **Not** medical advice. **Not** DIY biotech.

## Before non-trivial work

1. Read `docs/reference/BACKLOG.md` and `scripts/ralph_tick.py` `NEXT_QUERIES`.
2. Read latest CEO update under `docs/reference/ceo-update-*.md`.
3. Load skill **`cancer-research-ralph-hillclimb`** (repo `.cursor/skills/` or `~/.cursor/skills/`).
4. Jr handoff: `docs/reference/JR_ANALYST_RUNBOOK.md` + `SENTINEL_BOARD.md`.

## Ralph wake checklist

```powershell
cd C:\dev\projects\cancer-research
python scripts\ralph_tick.py
# Exa/Web research NEXT_QUERIES → write $env:TEMP\cr_wakeN.py → append ≥3–5 sources
# Update docs\hillclimb.md (unique ## Tick N) + design\gaps\cure-climb-board.md (EOF or unique wake header)
python scripts\validate_corpus.py
python scripts\status.py
# Refresh NEXT_QUERIES in scripts\ralph_tick.py (rotate researched queries to bottom)
python -m pytest tests -q --cache-clear
# Public repo: git add (4 files) → $msg="…"; git commit -m $msg → git push
# If ticks stacked while busy: multi-wake catch-up same turn
```

**Four wake files (commit every wake):**
1. `corpus/sources.yaml`
2. `docs/hillclimb.md`
3. `design/gaps/cure-climb-board.md`
4. `scripts/ralph_tick.py`

PowerShell commit (no bash heredoc):

```powershell
git add corpus/sources.yaml docs/hillclimb.md design/gaps/cure-climb-board.md scripts/ralph_tick.py
$msg = "ralph wake #N: bank <pins> (corpus M)"
git commit --trailer "Co-authored-by: Cursor <cursoragent@cursor.com>" -m $msg
git push
```

## Hard rules

1. **GOAL_MET is a floor** — keep climbing solid-tumor / unpublished Results.
2. **COMPLETED ≠ Results** — hunt manuscripts after registry COMPLETED.
3. **Adjacency ≠ invention** — CRC vaccine fail ≠ invent PDAC outcome; hema dose ≠ solid protocol.
4. **MRD/CR/pCR ≠ cured** — store assay, sensitivity, timepoint, denominator.
5. **Press ≠ peer review** — bank medium until KM tables.
6. **Name-collision filter** before banking any NCT/drug pin.
7. **Bank negatives** (“still absent”) every wake; rotate queries.
8. **Windows YAML/pytest hygiene** (ASCII appends via `$env:TEMP\cr_wakeN.py`; quote summaries with `:`; `--cache-clear`).
9. **Bidirectional oracles** — empty deferred must fail goal_met.
10. **Safety** — no DIY gene editing, synthesis, or personal dosing.
11. **Public git → commit+push** each wake (unless CEO says pause/stop).
12. **Dossier append** — only after unique `## Update (Ralph wake #N)` or at EOF. Never StrReplace bare "negatives held".
13. **Stacked ticks → multi-wake catch-up** same turn when notifications pile.
14. **Absence = searched sources as of DATE** — not universal nonexistence.

## Do not

- Claim a novel molecular cure invented in this repo.
- Equate hema CAR-T doses with solid-tumor protocols.
- Treat IMCODE003 recruiting status as efficacy / Results.
- Skip assay/timepoint when banking MRD.
- Skip commit+push on a completed wake while `origin/master` tracks (unless CEO says pause).
- Claim clinical backlog closed because CI is green.

## Pointers

| Artifact | Path |
|----------|------|
| Backlog | `docs/reference/BACKLOG.md` |
| Sentinel board | `docs/reference/SENTINEL_BOARD.md` |
| Jr runbook | `docs/reference/JR_ANALYST_RUNBOOK.md` |
| Gap register | `docs/gap_register.json` |
| Climb board (wake dossier) | `design/gaps/cure-climb-board.md` |
| Cursor rule | `.cursor/rules/cancer-research-ralph.mdc` |
| Tick loop | `scripts/start_ralph_loop.ps1` |
