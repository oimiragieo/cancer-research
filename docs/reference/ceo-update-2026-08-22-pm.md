# CEO update — live-forever (2026-08-22, afternoon)

**Plain English:** The longevity research machine is still green and still climbing. Since this morning's CEO note it ran another **~28 wakes**, banked more "still missing" pins, and did **not** invent any trial doses. Build goal = done. Research goal = never done.

**Since last update:** [`ceo-update-2026-08-22.md`](ceo-update-2026-08-22.md) (wake **#218**, corpus **1177**).  
**Now:** Ralph wake **#246** / hillclimb tick **#250**. Corpus **1318**. `GOAL_MET`. Tests **42** green.

---

## What worked (dumb version)

1. **Still green.** Corpus 1318 (floor is 50). Zero open science gaps. Five "waiting on clinic" dossiers still parked with evidence.
2. **Ralph kept hunting.** Wakes **#219–#246** (~28). Corpus **1177 → 1318** (+141). Same hot pins, fresh negatives, no fake numbers.
3. **"Still missing" is progress.** We re-checked EVERLAST / VITAL-H / RESTOR / SHAPE / ER-100 / Deciduous / STL-101 / queuine / NTZ / B2M-CCL11 / OASIS fence and **wrote down** that nothing new published.
4. **Fence rules held.** Did not fill VITAL-H mg from OASIS obesity 25/50. Did not treat Forzinity Barth **40 mg** as SHAPE dose. Did not treat Deciduous patents as IND. Did not treat Sapience ST101 cancer peptide as Stellate STL-101 queuine.
5. **Ops held.** YAML appends, query rotation, `status.py` + pytest after wakes. Fixed a few mid-file dossier mis-inserts same turn.

---

## Scoreboard (now)

| What | Number / status |
|------|-----------------|
| Corpus sources | **1318** (floor 50) |
| Open scientific gaps | **0** |
| Deferred dossiers (need real clinical data) | **5** |
| Hallmark still thin | **dysbiosis** |
| Ralph wakes since morning CEO update | **28** (#219–#246) |
| Best near-term readout hunt | **EVERLAST Results** (trial done; tables empty) |

---

## Backlog — ALL of it (plain English)

Full machine list: [`BACKLOG.md`](BACKLOG.md). `open_gaps == 0` ≠ empty backlog.

### A. Five big science questions we're waiting on (deferred dossiers)

| # | Topic | Why still backlog |
|---|--------|-------------------|
| A1 | **Systemic OSK safety** | ER-100 is **eye-only**. Full-body OSK still not cleared. |
| A2 | **NAD → healthspan** | We can measure NAD; **hard proof it extends healthy life** missing. |
| A3 | **Senolytic CAR-T in humans** | Works in mice; **no published human aging CAR-T trial**. |
| A4 | **A/B longevity trial design** | Blueprints exist; **no approved longevity drug + full RCT** yet. |
| A5 | **ECM / glucosepane drugs** | ALT-711 class PoC; **real glucosepane-scale longevity Rx** still R&D. |

### B. Ultra-design — same five, clinical not literature

1. Multi-organ human OSK beyond ER-100 eye trial  
2. NAD causal healthspan RCTs with hard endpoints  
3. Human senolytic CAR-T for aging  
4. Approved clonal-hematopoiesis-directed drugs  
5. Glucosepane-scale ECM longevity treatment  

### C. Hallmark gap

| Item | Status |
|------|--------|
| **dysbiosis** | Weakest hallmark in our graph — needs more evidence |

### D. Unpublished trial / Finals pins (do NOT invent numbers)

#### D1 — Top priority (current Ralph rotation)

| # | Pin | Status (Aug 22 PM) |
|---|-----|---------------------|
| D1-1 | **EVERLAST NCT05835999 Results** | **COMPLETED** Jul 2026, n=106; **No Results Posted**; no Konopka preprint; lab site still stale recruitment copy |
| D1-2 | **VITAL-H ClinicalTrials.gov NCT** | n≈726, four oral arms; ARPA-H Feb 2026; press says start later 2026/early 2027; **no CT.gov ID**; recruitment not begun |
| D1-3 | **VITAL-H arm milligrams** | Oral route known; OASIS/Wegovy **25/50 obesity** ≠ VITAL-H aging arm mg (**still unpublished**) |
| D1-4 | **RESTOR NCT06658093 dose mg** | Started Mar 4 2026; adaptive PK/PD recruiting — **OD mg still unpublished** |
| D1-5 | **SHAPE NCT07275424 daily SC mg** | Still RECRUITING (CT.gov Jun 15); vial **80 mg/mL** only — **mg/day unpublished**; No Results; Forzinity Barth **40 mg ≠ invent SHAPE** |

#### D2 — XPRIZE M2 / Finals dose & registry gaps

| # | Pin |
|---|-----|
| D2-6 | Goda / NanoTitan / Relife **Finals EV particle counts** |
| D2-7 | AgelessRx **Finals agent-mg + Finals NCT** (NCT07092605 microdose ≠ Finals) |
| D2-8 | Longeveron **Finals cell dose** |
| D2-9 | Minicircle **Finals plasmid µg** / 1y schedule |
| D2-10 | NYC-Vita **Finals n** |
| D2-11 | RETRO-EPIGERNA **KYN / queuine capsule human mg + registry** |
| D2-12 | Suninflam **SIF001 Finals MCI dose** |
| D2-13 | Progerinin **Finals ordinary-aging dose** |
| D2-14 | TIME TRAVELER **UMIN000059942 Results** |
| D2-15 | Mighty **Finals n/dose** beyond SHAPE IIT |

#### D3 — Non-M2 Finalists / adjacency

| # | Pin |
|---|-----|
| D3-16 | **GIANTS-1 Results** + named cognitive partner |
| D3-17 | **Lono LON301** human oral NCT / mg |
| D3-18 | **Abe Yoando** Finals drink mg + Finals NCT |
| D3-19 | **Morinaga** Finals Passienol+niacin **NCT/mg** |
| D3-20 | **ASU** operating Finals **ATA / %O2** |
| D3-21 | **GOQii Sanjeevini** Finals NCT / CogState / supplement IDs |
| D3-22 | **ANI Biome** Finals NCT |
| D3-23 | **Boston Healthspan** ALG-801 Finals mg |

#### D4 — PROSPR / disease-bridge / other clinical

| # | Pin |
|---|-----|
| D4-24 | LNS8801 **PROSPR healthy-older NCT/dose** |
| D4-25 | TPN-101 **aging / HEALEY RSA NCT** |
| D4-26 | Cyclarity **UDP-003 Ph2 NCT** + ACS **CCTA interim** |
| D4-27 | TRIIM-X **peer-reviewed package** |
| D4-28 | XPRIZE **3rd immune response-to-challenge** assay vendor / SOP |
| D4-29 | Deciduous **iNKT IND** (still preclinical; patents ≠ IND) |
| D4-30 | ER-100 **second-patient / DSMB** (first dose Jun 9 only) |

#### D5 — Mechanism / assay tensions

| # | Pin |
|---|-----|
| D5-31 | Queuine / **STL-101** plasma age-decline **reconciliation** (UNSETTLED: PLOS flat vs bioRxiv drop) |
| D5-32 | Human **queuine longevity NCT/mg** (mouse +15.3% ≠ human trial) |
| D5-33 | Nitazoxanide **human aging / FOXN1** NCT (Genah 2026 mouse only) |
| D5-34 | Oral sema **25/50** vs VITAL-H (OASIS COMPLETED; ≠ VITAL-H aging mg) |
| D5-35 | Selective **B2M / CCL11** aging depletion IND (CCL11 trials vacant; CAT-213 inflammatory only) |

### E. Ops / harness (keep the machine running)

| # | Item |
|---|------|
| E36 | Ralph tick loop healthy (~600s; sentinel `AGENT_LOOP_TICK_liveforever`) |
| E37 | Refresh `NEXT_QUERIES` every wake toward highest-value absent pin |
| E38 | Append ≥3–5 corpus sources per wake; update hillclimb + ab-trial-design |
| E39 | Run `status.py` + `pytest -q --cache-clear` after corpus edits |
| E40 | Never commit unless CEO asks |
| E41 | Safety: literature/systems only — no DIY biotech or personal dosing |
| E42 | **Dossier append hygiene** — never StrReplace on non-unique "negatives held" lines; append after unique `## Update (Ralph wake #N)` or file end; dedupe duplicates same turn |

### F. Explicitly NOT backlog (closed — don't reopen)

- Repo scaffold, two-pathway sim, ITP/parabiosis ingest, pro-aging catalog v1  
- `thymic-restoration` as separate gap (mapped to L3)  
- Inventing mg from adjacency ladders (**forbidden**)

**Backlog count:** 5 deferred + 1 hallmark seed + 35 research pins + **7** ops ≈ **48 enumerated rows** (ultra-design overlaps deferred).

---

## Needs research (priority order)

1. **EVERLAST Results** / Konopka preprint — trial done, tables empty  
2. **RESTOR adaptive OD mg** — study started, dose still secret  
3. **SHAPE daily SC mg + Results** — recruiting; vial conc ≠ protocol dose; Barth label ≠ invent  
4. **VITAL-H NCT + arm mg** — biggest funded healthy-aging oral trial; registry vacuum  
5. **ER-100 DSMB second-patient** — sentinel design; public outcome may lag 28+ days  
6. **Queuine plasma reconciliation** — harmonized cohort+assay before trusting "decline"  
7. **STL-101 human NCT** — mouse lifespan preprint is not a trial  
8. **Deciduous IND** — patent ≠ clinic  
9. **B2M/CCL11 aging depletion IND** — mechanism hot, human longevity trial absent  
10. **NTZ FOXN1 human aging NCT** — post-IR mouse + review ≠ healthy-aging trial  

Active Exa seeds: `scripts/ralph_tick.py` → `NEXT_QUERIES` (currently **ER-100 → Deciduous → STL-101** top 3).

---

## New lessons since morning CEO update (≥7)

Full write-up: [`lessons-learned-2026-08-22-pm.md`](lessons-learned-2026-08-22-pm.md). Prior **L1–L18** still in force.

| # | Lesson (one line) |
|---|-------------------|
| **L19** | **Disease-label dose ≠ healthy-aging pilot dose** — Forzinity Barth **40 mg/day ≠ invent SHAPE** protocol mg |
| **L20** | **Press timeline ≠ CT.gov NCT** — "start later 2026 / early 2027" (San Antonio Report) does not create a registry ID |
| **L21** | **Non-unique StrReplace inserts mid-file** — dossier edits must target unique `## Update (Ralph wake #N)` or append at EOF |
| **L22** | **Duplicate wake sections = same-turn cleanup** — found duplicates are defects; delete them before leaving |
| **L23** | **Estimated primary completion past ≠ Results** — SHAPE est Mar 15 2026 + still RECRUITING Jun 15 = still No Results |
| **L24** | **Protocol Version / aggregator metadata ≠ Results tables** — Syfrah "Protocol Version 6/5/2026" on EVERLAST ≠ posted outcomes |
| **L25** | **Review saying "not demonstrated" corroborates absence** — Immun Ageing Jul 2026 ≠ invent NTZ human aging NCT |

Retention: `AGENTS.md`, `.cursor/rules/live-forever-ralph.mdc`, skill `live-forever-ralph-hillclimb` (project + `~/.claude/skills/`), Claude memory `feedback_ceo_update_lessons_2026_08_22_pm.md`.

---

## Ask of CEO

Nothing blocking. Keep Ralph running. Do **not** treat green scaffold as "stop researching." Safety boundary unchanged: **literature + systems only**.
