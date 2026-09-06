# Lessons learned — live-forever (2026-08-21)

**Scope:** First CEO update for this repo. Lessons drawn from scaffold closeout through Ralph wake **#159** (intensive Finals/dose-pin campaign wakes ~71–159).

Retain in: this file, `AGENTS.md`, `.cursor/rules/live-forever-ralph.mdc`, skill `live-forever-ralph-hillclimb`, Claude memory `feedback_ceo_update_lessons_2026_08_21.md`.

**Superseded for new lessons by:** [`lessons-learned-2026-08-22.md`](lessons-learned-2026-08-22.md) (L11–L18). L1–L10 below remain in force.

---

## L1. GOAL_MET is a floor, not a stop

`open_gaps == 0` means scientific unknowns are **deferred with evidence**, not that the hill is climbed. Ralph continues on unpublished NCT/mg/Results. Stopping at green freezes the design on yesterday’s adjacency.

## L2. COMPLETED ≠ Results posted

EVERLAST, UMIN TIME TRAVELER, and others can show **COMPLETED** on registries while **Results tables / manuscripts are absent**. Treat “COMPLETED” as a hunt trigger for Results — never as efficacy evidence.

## L3. Adjacency ≠ invention (the anti-hallucination law)

Label doses, sister trials, and bioequivalent ladders (Rybelsus R1/R2, Farxiga 5/10, FORZINITY 40 mg, UTSW 0.5/1/2 → trough) are **adjacency pins**. They do **not** authorize inventing VITAL-H / RESTOR / SHAPE / Finals arm milligrams. Prefer an explicit negative (“mg unpublished”) over a guessed number.

## L4. Concentration ≠ daily dose; route matters

SHAPE vial **80 mg/mL** (and FORZINITY **0.5 mL = 40 mg**) is formulation evidence, not daily SC mg. VITAL-H “**orally administered**” flips the sema assumption from injectable Ozempic to **Rybelsus-class** oral adjacency — route text is load-bearing.

## L5. Name collisions are a research class bug

Before banking a pin, filter collisions: Sapience **ST101** ≠ Stellate **STL-101**; Lono **LON301** ≠ Hanlim **HL301** ≠ Kiora **KIO-301** ≠ Lumen **LMN-301**; **Morinaga Milk** probiotic ≠ **Morinaga & Co** Passienol; **ASAGI Labs** track ≠ Morinaga Finals dose. A wrong NCT poisons the corpus for dozens of wakes.

## L6. Disease / commercial / patent path ≠ aging Finals protocol

HGPS, Barth, epilepsy, oncology RP2D, consumer SKUs, trademark ingredient lists, and mouse μg/kg ladders are bridges. They never auto-fill XPRIZE Finals or PROSPR healthy-aging milligrams. Same for cognition batteries: Creyos / Cognitrax / NIH Toolbox / MoCA **≠ CogState** (Rules supersede Guidelines where they conflict).

## L7. Negative rechecks are progress — bank them

A wake that finds “still absent” is not a failed wake. Record the negative in hillclimb + dossier so the next agent does not treat the pin as never-searched. Rotate `NEXT_QUERIES` toward the highest-value remaining absence.

## L8. Windows Ralph harness hygiene

- Prefer ASCII in PowerShell-appended YAML (Unicode arrows break / mis-encode).  
- Quote `summary:` values that contain colons.  
- Run `python -m pytest tests -q --cache-clear` after corpus edits (Ralph races + `__pycache__` flakes).  
- Verify `status.py` **after** YAML appends — do not claim a new corpus count until the oracle says so.

## L9. Bidirectional oracles beat prose claims

`goal_met` must fail when deferred is empty; dossiers must exist and be nontrivial; Finals floors (`≥40/arm`, `≥100 total`) live in code. A comment that says “key check” without an assert is not a check.

## L10. Safety boundary is non-negotiable

This repo is literature + systems architecture. Never ship DIY CRISPR, synthesis recipes, or personalized dosing for unapproved gerotherapeutics — even when the corpus has rich mg ladders.
