# Gap dossier: AGE / ECM clearance at organism scale
**Status:** DEFERRED WITH EVIDENCE (2026-08-20)  
**Verdict:** Concept validated (AGE crosslink breakers e.g. **alagebrium/ALT-711** improve stiffness in animals; limited human diastolic HF data). **Organism-scale, longevity-proven ECM rejuvenation does not exist.** Glucosepane-specific breakers remain an R&D frontier.

## Evidence
| Source | Finding |
|--------|---------|
| PubMed review crosslink breakers | ALT-711 breaks AGE crosslinks; CV/renal benefits in aged/diabetic/hypertensive models |
| Rejuvenation Res AGE breaker review | Clinical utility hypothesized; Little et al. alagebrium in elderly diastolic HF |
| Mechanistic AGE reviews | RAGE signaling drives inflammation/fibrosis; breakers ≠ full matrix reset |

## Design implications (ultra-design L5/L6)
1. Treat ECM/AGE as **information-limited structural B-type damage**.
2. Near-term: glycemic control + RAGE-axis research; mid-term: next-gen glucosepane breakers + matrix-targeted biologics.
3. Replacement (L6) may outrun chemistry for end-stage fibrotic organs.

## Remaining unknown
Safe chronic breaker dosing in non-diabetic aging; glucosepane-selective chemistry at clinical stage.


## Update (Ralph tick 5 / wake #3)
- Glucosepane remains the priority B-type ECM lesion (dominant crosslink abundance).
- 2025 FluMag-SELEX aptamers enable tissue labeling/monitoring — biomarker progress ahead of breaker drugs.
- MDPI 2025: still no FDA-approved AGE-disease-specific therapy; ALT-711 class remains clinical-historical.



## Update (Ralph wake #16)
- Glucosepane enzymatic breakers remain preclinical (Revel/Yale Spiegel lineage); ALT-711 was proof-of-concept for AGE breakers, not glucosepane-selective.



## Update (Ralph wake #17)
- **CMLase** (Nat Commun 2026, Revel): engineered enzymatic reversal of CML AGE in aged human tissue ex vivo — first clear AGE-repair PoC. Glucosepane-selective crosslink breakers remain the harder ECM elasticity target.



## Update (Ralph wake #46) — simulator calibration note
- Jiang 2025 temporal ITP analysis: most lifespan drugs act in restricted age windows; only ~8 reduce late-life mortality when aging burden peaks.
- Implication for lgorithms/damage_control.py: constant epair_a overstates continuous geroprotection; future params should allow age-phased RA and sex splits (cana/17aE2 male benefit / female harm).
- Do not retune numeric defaults until a bidirectional oracle (empty/wrong policy must fail) is defined.



## Update (Ralph wake #47)
- Cana_16 female harm tied to ~20x plasma levels in aged females vs young males (Miller 2024); pathology necropsy (2025) finds no single COD.
- Simulator note - sex-specific clearance multipliers needed before claiming SGLT2 RA equivalence.


## Update (Ralph wake #49) — age-phased RA prototype landed
- `algorithms/damage_control.py` now supports optional `repair_a_schedule` ((start, end), ra) windows; empty schedule = legacy constant `repair_a`.
- Bidirectional tests in `tests/test_damage_control_phased.py` (5/5): empty==constant; window bounds; midlife pulse > continuous final D; zeroed schedule worse than baseline; `repair_a_used` recorded.
- Default Params and immortality_stack numbers **unchanged** — illustrative `midlife_pulse_A` policy only. Sex-PK multipliers still deferred.


## Update (Ralph wake #50) — sex clearance prototype
- Added `sex`, `sex_clearance_male/female`, `female_late_toxicity_start`, `female_late_clearance_mult`; `effective_repair_a = repair_a_at * clearance_mult`.
- Tests `tests/test_damage_control_sex.py` (4/4): unspecified identity; default sex mults match baseline; late female tox worsens D; removing tox window closes sex gap.
- Illustrative `cana_like_male` / `cana_like_female` policies only — **do not** treat 0.05 late mult as calibrated to Miller 2024 20x plasma.
- PROSPR NCT hunt: TPN-101 aging + VITAL-H still unregistered on CT.gov (negative control banked).


## Update (Ralph wake #54) — combined midlife+sex demo
- Policies `midlife_pulse_cana_male` / `midlife_pulse_cana_female` compose schedule + sex tox; test asserts female final D > male twin. Still illustrative — not a sealed calibration.


## Update (Ralph wake #61) — immortality stack sex-split
- `immortality_stack_male` stays bounded (D≈0.147); `immortality_stack_female` with late tox unbounds (D≈1.98, morbidity y88). Shows sex-PK risk can break even a high RA/RB stack in the toy model — still not Miller-calibrated.


## Update (Ralph wake #64) — derisk_then_repair sex-split
- `derisk_then_repair_male` bounded (D≈0.238); `derisk_then_repair_female` late tox unbounds (D≈2.13, morbidity y84). Derisk still lowers B vs repair-without-derisk; female late clearance collapse remains the unbound driver. Not ITP-calibrated.


## Update (Ralph wake #65) — ITP cana calibration REFUSED
- Miller/ITP cana (JCI Insight 2020): female plasma ~13.2 vs male ~3.6 μg/mL (~3.7×) yet **lifespan benefit male-only**; both sexes get metabolic effects.
- **Do not** set `female_late_clearance_mult` from the plasma ratio. Higher exposure without female longevity is orthogonal to the toy "late clearance collapse" knobs.
- Keep `female_late_*` illustrative until a sealed bidirectional oracle (sex-split lifespan + PK + morbidity) exists. Default stack params unchanged.


## Update (Ralph wake #68) — midlife_pulse sex morbidity years
- `midlife_pulse_male` morbidity **y76**; `midlife_pulse_female` (late tox) **y65** under three-window RA schedule (0–40/40–70/70+). Plain `midlife_pulse_A` (RA=0 until 40) hits ~y21 for both — sex tox never fires. Illustrative only; not ITP-calibrated.


## Update (Ralph wake #75) — immortality_stack bounded oracle pin
- Default `immortality_stack` (120y): **bounded**, final_D ≈ **0.147**, morbidity_year None. Bidirectional: `natural` and `repair_only_A` unbounded. Pinned in `tests/test_damage_control_phased.py`.


## Update (Ralph wake #77) — UDP-003 dose ladder banked
- NCT06813339: SAD/MAD **1–25 mg/kg** IV bolus; Part 3 ACS cohort **25 mg/kg × 6** over ~16–35 days; 300 mg/mL vial; Ph2 plaque-regression still "later 2026" (no Ph2 NCT).


## Update (Ralph wake #93) — UDP-003 CTx-001 refresh
- CT.gov: acronym **CTx-001**; primary completion **2026-12-30** / study end **2027-12-30**; enrollment ~84; still RECRUITING.
- Part 3: **25 mg/kg × 6 over 6 weeks**; “up to 9 evaluable” (cohort also listed as 12) — prefer live CT.gov over older 16-day mirrors.
- CCTA plaque interim still absent; separate Ph2 NCT still absent.
- This is CV plaque / 7KC clearance PoC — **not** organism-scale ECM/glucosepane reset. L5 AGE gap remains deferred.
- Graph: `udp003_7kc_clearance` -> mitochondrial/inflammation/intercellular (does not clear dysbiosis uncovered seed).


## Update (Ralph wake #95) — UDP-003 PK press
- Press/secondary: plasma **t½ ~3 h**; dose-dependent urinary 7KC; no SAEs claimed in coverage — still not a peer-reviewed PK table.
- ACS CCTA cohort still enrolling; Ph2 later-2026 promise unchanged / no Ph2 NCT.


## Update (Ralph wake #96) — Cyclarity Series B framing
- BIO 2026 company card: Ph1 HNV completed (Adelaide / Victorian Heart / Nicholls); Ph1b plaque cohort ongoing; raising **$40M Series B** to fund Phase 2.
- Still **no** public CCTA plaque delta and **no** Ph2 NCT — financing intent ≠ registry readout.


## Update (Ralph wake #97) — Ph1b Q1 2027 catalyst
- BIO card: next inflection = Ph1b completion; catalyst update expected **Q1 2027**.
- Ph2 still contingent on Series B; do not treat Q1 2027 as a plaque-regression primary readout date.


## Update (Ralph wake #98) — Ph2 n~150 design + HNV n=72
- O'Connor interview: Ph1 HNV **n=72**; drug **not metabolized**, excreted in urine **<3 h**; max tested dose advances to Ph1b.
- Ph2 **designed** ~**150** patients (AU+US+UK/EU); wrap early **2029** if funded this year; traditional CAD approval ~2031–32.
- Still **no** Ph2 NCT and **no** CCTA plaque delta — design talk ≠ registry.


## Update (Ralph wake #99)
- XPRIZE Innovation Landscape climb elsewhere (TIME TRAVELER UMIN / AgelessRx Infinite / NYC-Vita Finals).
- Cyclarity: Ph2 NCT + CCTA interim still **absent**; NCT06813339 still RECRUITING.

## Update (Ralph wake #182)
- Cyclarity UDP-003: **7KC urinary PD** (AHA May 2026) **≠** **CCTA plaque** readout; Part 3 still enrolling; Ph2 NCT still absent; Series B funding gate unchanged.

