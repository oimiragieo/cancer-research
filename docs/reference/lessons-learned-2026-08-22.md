# Lessons learned — live-forever (2026-08-22)

**Scope:** Lessons **since** [`lessons-learned-2026-08-21.md`](lessons-learned-2026-08-21.md) / CEO update 2026-08-21. Drawn from Ralph wakes **#160–#218** (hillclimb ticks **#163–#221**). Corpus **853 → 1177**.

Prior laws **L1–L10** remain in force — do not drop them. This file adds **L11–L18**.

Retain in: this file, `AGENTS.md`, `.cursor/rules/live-forever-ralph.mdc`, skill `live-forever-ralph-hillclimb`, Claude memory `feedback_ceo_update_lessons_2026_08_22.md`.

---

## L11. Stale consumer/lab pages ≠ Results posted

**EVERLAST** (NCT05835999) shows **COMPLETED 2026-07-22** on CT.gov with **No Results Posted**, while the Konopka lab page can still list active recruitment/compensation. **Do not infer readout from lagging marketing copy.** Hunt Results tables, preprints, and registry updates — not lab brochure text.

## L12. Patent / IP publication ≠ IND filed ≠ trial live

**Deciduous** carries **US20250381206** (Dec 2025) and prior grants; **fobi Jul 2026** still rates **preclinical ~$6.5M seed**. A patent row is **IP**, not an IND, not CT.gov, not dose protocol. Same law as prior "commercial PR ≠ Finals protocol" — extend to **patent bibliographies**.

## L13. OASIS obesity oral sema ladder ≠ VITAL-H healthy-older arm mg

**OASIS 4** (NCT05564117) **25 mg** and **OASIS 1** (NCT05035095) **50 mg** obesity titration are **COMPLETED** with published weight-loss data. **Wegovy pill 25 mg** FDA/EC approval is obesity/MACE adjacency. **None** of this authorizes filling **VITAL-H** per-arm rapa/dapa/sema milligrams without protocol publication. **Indication + population + endpoint** fence still load-bearing.

## L14. Assay/cohort mismatch — "flat vs drop" can both be locally true

Queuine plasma tension: **PLOS ONE 2021** (n=160, ages 50–90) **no age decline**; **bioRxiv 713446** claims **>65% drop**; **PMC11493786** LOQ **0.3 nM** method (n=44 flat). Status = **UNSETTLED** until harmonized cohort + assay — not "pick the exciting preprint." Do not bank either side as settled biology.

## L15. Mouse lifespan preprint ≠ human supplementation NCT

**bioRxiv 713446 (Mar 2026)**: oral queuine **+15.3% mouse lifespan**, manQ/tRNA mechanism — **≠** human **STL-101** supplementation trial or protocol mg. Stellate **2021 "clinical next year"** timeline missed. **Preclinical efficacy ≠ NCT.**

## L16. Intravitreal ocular OSK ≠ systemic multi-organ OSK clearance

**ER-100** (NCT07290244): **intravitreal** AAV-OSK + doxycycline activation for **optic neuropathy**. First participant **2026-06-09** only; **DSMB sentinel** gating between dose levels. Progress on eye FIH **does not** close **`human-osk-safety`** systemic dossier — route and organ scope differ.

## L17. CCL11 "aging mechanism" ≠ human longevity depletion trial

**2025 review (PMC11868897)**: **"clinical trials for CCL11 are currently vacant."** **CAT-212/213** anti-CCL11 mAbs expected in **inflammatory disease**, not healthy longevity. **NCT07713680** = ESRD dialysis β2M **observational** (**≠** selective B2M/CCL11 depletion IND). Mechanism papers (Qifuyin Jul 2025 mouse) **≠** human aging IND.

## L18. Oracle last — never claim a wake complete without status + pytest

Handoff trap: corpus/hillclimb/dossier edits landed while **`status.py` + pytest** were skipped. **Corpus count and GOAL_MET come from the oracle**, not from counting YAML ids by hand. Every wake ends with:

```powershell
python scripts\status.py
python -m pytest tests -q --cache-clear
```

---

## Rotation discipline (receipt)

Negative rechecks on the same pin across **59 wakes** prevented false "never searched" drift. **`NEXT_QUERIES`** rotation (top 3 → bottom) spread coverage across RESTOR/SHAPE/EVERLAST/VITAL-H/ER-100/Deciduous/STL-101/queuine/B2M/OASIS fence without abandoning EVERLAST Results as highest-value readout hunt.
