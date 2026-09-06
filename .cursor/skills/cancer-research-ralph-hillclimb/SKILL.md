---
name: cancer-research-ralph-hillclimb
description: >-
  Use when working in the cancer-research oncology cure repo, running a Ralph
  wake/tick, filling corpus sources.yaml, chasing NCT/Results pins (IMCODE003,
  CAR-PRISM, GIANT, MonumenTAL-6, LOTIS-5, satri-cel), updating cure-climb-board,
  or when the user asks for a CEO update / backlog / hillclimb / resume/pause the
  10-minute tick loop. Enforces cure-definition, COMPLETED≠Results, MRD≠cured,
  adjacency≠invention, four-file commit+push, and Windows pytest/YAML hygiene.
  Not for DIY biotech or personal dosing advice.
---

# cancer-research Ralph hill-climb

## Safety

Literature synthesis + systems architecture only. Refuse DIY CRISPR, drug synthesis, and personalized dosing.

## Per-wake loop (match live-forever)

1. `python scripts\ralph_tick.py` — read status + `NEXT_QUERIES`.
2. Research (Exa / CT.gov / Web) the highest-value **absent** pin first.
3. Write `$env:TEMP\cr_wakeN.py` → append ≥3–5 sourced entries to `corpus/sources.yaml` (unique `id`s).
4. Update `docs/hillclimb.md` (`## Tick N`) + `design/gaps/cure-climb-board.md` (`## Update (Ralph wake #N)` at EOF).
5. Rotate researched queries to bottom of `NEXT_QUERIES`.
6. `python scripts\validate_corpus.py` then `python scripts\status.py` then `python -m pytest tests -q --cache-clear`.
7. Commit+push **four files** with PowerShell `$msg=…` (no bash heredoc).
8. Keep `scripts\start_ralph_loop.ps1` running unless CEO said **pause**.

## Laws

| Law | Practice |
|-----|----------|
| GOAL_MET is a floor | Keep climbing solid-tumor / unpublished Results |
| COMPLETED ≠ Results | Hunt manuscripts after registry COMPLETED |
| MRD/CR/pCR ≠ cured | Store assay, sensitivity, timepoint, denominator |
| Adjacency ≠ invention | Never invent arm outcomes from sister indications |
| Press ≠ peer review | Bank medium until tables |
| Name collisions | Verify NCT/drug identity |
| Hema ≠ solid | CAR-T hema success ≠ invent solid protocol |
| Bank negatives | Still absent is progress |
| Windows hygiene | `$env:TEMP\cr_wakeN.py`; quote summaries with `:`; `--cache-clear` |
| Bidirectional oracles | Empty deferred must fail goal_met |
| Public git | Four-file commit+push each wake |
| Pause | Stop loop PID; do not run next wake |

## Cure definition

Existing disease-specific intervention with replicated durable treatment-free remission / survival plateau + NCT/Results provenance. Not inventing a molecule.

## Four wake files

`corpus/sources.yaml` · `docs/hillclimb.md` · `design/gaps/cure-climb-board.md` · `scripts/ralph_tick.py`
