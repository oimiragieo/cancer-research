# Cancer Research — Oncology Cure Ralph Engine

Fork of `live-forever` retargeted at **cancer / oncology cure research**. Continuous Ralph hill-climb over literature + ClinicalTrials.gov until cure-adjacent pins are banked — then **GOAL_MET is a floor** and climbing continues (especially solid-tumor sentinels).

> **Safety boundary:** Literature synthesis + systems/algorithms design. **Not** medical advice. **Not** DIY gene therapy, drug synthesis, or lab protocols.

## Architecture (Thinktank + Exa, 2026-09-05)

**Hybrid D:** hallmarks ultra-design + rotating sentinel hard cancers (PDAC, GBM, mTNBC) + emerging-modality clinical pins.

**Cure definition:** existing disease-specific intervention with replicated durable treatment-free remission / survival plateau + NCT/Results provenance — **not** inventing a molecule.

## Goal (Ralph exit floor)

1. **Corpus** ≥ 50 curated oncology sources
2. **Ultra-design** Hybrid D stack
3. **Algorithms** tumor-burden / resistance control
4. **Medicine map** translational stages
5. **Gap register** open=0 with deferred dossiers present

## Quick start

```powershell
cd C:\dev\projects\cancer-research
pip install -r requirements-dev.txt
python -m algorithms.tumor_burden --policy all --plot-ascii
python scripts\ralph_tick.py
python scripts\status.py
python scripts\validate_corpus.py
pytest -q --cache-clear
```

## Ralph loop

```powershell
cd C:\dev\projects\cancer-research
python scripts\ralph_tick.py
# … research → $env:TEMP\cr_wakeN.py → four-file commit+push …
powershell -File scripts\start_ralph_loop.ps1   # ~600s AGENT_LOOP_TICK_cancerresearch
```

Agent rules: `AGENTS.md` · skill `cancer-research-ralph-hillclimb` · climb board `design/gaps/cure-climb-board.md`.

