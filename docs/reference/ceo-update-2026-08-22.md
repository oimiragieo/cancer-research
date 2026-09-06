# CEO update — live-forever (2026-08-22)

**Plain English:** We built a machine that reads longevity science and tracks what trials *haven't* published yet (doses, registries, results). The build goal is green. The machine keeps running anyway — that's the point.

**Since last update:** [`ceo-update-2026-08-21.md`](ceo-update-2026-08-21.md) (wake **#159**, corpus **853**).  
**Now:** Ralph wake **#218** / hillclimb tick **#221**. Corpus **1177**. `GOAL_MET`. Tests **42** green.

---

## What worked

1. **Still green.** Corpus way above floor (1177 vs 50). All scaffold gates pass. Zero open scientific gaps. Five deferred dossiers still on disk with evidence.
2. **Ralph didn't stop at "done."** ~59 wakes since last CEO update (#160–#218). Each added 3–5 sourced pins. Corpus grew **853 → 1177** (+324).
3. **Negative hunts are real work.** We re-checked the same hot pins every few wakes and *banked* "still absent" so nobody treats them as never searched. Examples held across the period:
   - **EVERLAST** — trial finished Jul 2026, **no Results table**
   - **VITAL-H** — big ARPA-H trial announced, **no ClinicalTrials.gov ID, no per-drug mg**
   - **RESTOR / SHAPE** — recruiting, **adaptive / daily mg still secret**
   - **ER-100** — first eye patient dosed Jun 9, **no public DSMB "second patient cleared"**
4. **Fence rules held.** We did *not* invent doses from neighbor trials (OASIS obesity sema 25/50 mg ≠ VITAL-H aging arm). We did *not* confuse Sapience **ST101** (cancer peptide) with Stellate **STL-101** (queuine). We did *not* treat patents as INDs (Deciduous).
5. **Ops stayed stable.** Windows YAML appends, quoted summaries, `pytest --cache-clear` after corpus edits — no scaffold regressions.

---

## Scoreboard (now)

| What | Number / status |
|------|-----------------|
| Corpus sources | **1177** (floor 50) |
| Open scientific gaps | **0** |
| Deferred dossiers (need real clinical data) | **5** |
| Hallmark still thin | **dysbiosis** (weak evidence stack) |
| Ralph wakes since last CEO update | **59** (#160–#218) |
| Best near-term readout hunt | **EVERLAST Results** (COMPLETED, tables still missing) |

---

## Backlog — ALL of it (plain English)

`open_gaps == 0` does **not** mean "nothing left to do." Full machine-readable list: [`BACKLOG.md`](BACKLOG.md).

### A. Five big science questions we're waiting on (deferred dossiers)

| # | Topic | Plain English "why still backlog" |
|---|--------|-----------------------------------|
| A1 | **Systemic OSK safety** | ER-100 is **eye-only** first-in-human. Full-body OSK rejuvenation still not cleared. |
| A2 | **NAD → healthspan** | We can measure NAD in people; **hard proof it extends healthy life** still missing. |
| A3 | **Senolytic CAR-T in humans** | Works in mice; **no published human aging CAR-T trial**. |
| A4 | **A/B longevity trial design** | Blueprints exist (CHIP/CHRS); **no approved longevity drug + full RCT** yet. |
| A5 | **ECM / glucosepane drugs** | ALT-711 class proved concept; **real glucosepane-scale longevity Rx** still R&D. |

### B. Ultra-design — same five, clinical not literature

1. Multi-organ human OSK beyond ER-100 eye trial  
2. NAD causal healthspan RCTs with hard endpoints  
3. Human senolytic CAR-T for aging  
4. Approved clonal-hematopoiesis-directed drugs  
5. Glucosepane-scale ECM longevity treatment  

### C. Hallmark gap

| Item | Status |
|------|--------|
| **dysbiosis** | Still the weakest hallmark in our graph — needs more evidence before we pretend the stack is complete |

### D. Unpublished trial / Finals pins (still hunting — do NOT invent numbers)

#### D1 — Top priority (current Ralph rotation)

| # | Pin | Status (Aug 22) |
|---|-----|-----------------|
| D1-1 | **EVERLAST NCT05835999 Results** | **COMPLETED** Jul 2026, n=106; **No Results Posted**; no Konopka preprint; lab site still has stale recruitment copy |
| D1-2 | **VITAL-H ClinicalTrials.gov NCT** | n≈726, four oral arms (rapa/dapa/sema); ARPA-H award Feb 2026; **no CT.gov registration**; recruitment not begun |
| D1-3 | **VITAL-H arm milligrams** | Oral route confirmed; OASIS/Wegovy pill **25 mg obesity** adjacency banked — **protocol mg per arm still unpublished** |
| D1-4 | **RESTOR NCT06658093 dose mg** | Started Mar 2026; adaptive PK/PD recruiting — **starting/open-label mg still unpublished** |
| D1-5 | **SHAPE NCT07275424 daily SC mg** | Still RECRUITING past Apr 2026 est.; vial **80 mg/mL** only — **mg/day unpublished**; No Results |

#### D2 — XPRIZE M2 / Finals dose & registry gaps

| # | Pin |
|---|-----|
| D2-6 | Goda / NanoTitan / Relife **Finals EV particle counts** (jRCT high/low unpublished; recruitment suspended) |
| D2-7 | AgelessRx **Finals agent-mg + Finals NCT** (NCT07092605 microdose ≠ Finals) |
| D2-8 | Longeveron **Finals cell dose** (Ph2b 25–200M ≠ ELPIS II ≠ Finals) |
| D2-9 | Minicircle **Finals plasmid µg** / 1y schedule |
| D2-10 | NYC-Vita **Finals n** (Ph1b n≈22 << floors) |
| D2-11 | RETRO-EPIGERNA **KYN / queuine capsule human mg + registry** |
| D2-12 | Suninflam **SIF001 Finals MCI dose** |
| D2-13 | Progerinin **Finals ordinary-aging dose** (HGPS/Werner disease doses ≠ healthspan) |
| D2-14 | TIME TRAVELER **UMIN000059942 Results** (COMPLETED; numbers unpublished) |
| D2-15 | Mighty **Finals n/dose** beyond SHAPE IIT |

#### D3 — Non-M2 Finalists / adjacency

| # | Pin |
|---|-----|
| D3-16 | **GIANTS-1 Results** + named cognitive partner |
| D3-17 | **Lono LON301** human oral NCT / mg (patent-only) |
| D3-18 | **Abe Yoando** Finals drink mg + Finals NCT |
| D3-19 | **Morinaga** Finals Passienol+niacin **NCT/mg** |
| D3-20 | **ASU** operating Finals **ATA / %O2** |
| D3-21 | **GOQii Sanjeevini** Finals NCT / CogState / supplement IDs |
| D3-22 | **ANI Biome** Finals NCT (ELITE unregistered; GlycanAge ≠ iAge) |
| D3-23 | **Boston Healthspan** ALG-801 Finals mg |

#### D4 — PROSPR / disease-bridge / other clinical

| # | Pin |
|---|-----|
| D4-24 | LNS8801 **PROSPR healthy-older NCT/dose** |
| D4-25 | TPN-101 **aging / HEALEY RSA NCT** |
| D4-26 | Cyclarity **UDP-003 Ph2 NCT** + ACS **CCTA interim** |
| D4-27 | TRIIM-X **peer-reviewed package** (RECRUITING past est. completion) |
| D4-28 | XPRIZE **3rd immune response-to-challenge** assay vendor / SOP |
| D4-29 | Deciduous **iNKT IND** (still absent; fobi Jul 2026 preclinical ~$6.5M) |
| D4-30 | ER-100 **second-patient / DSMB** public update (first dose Jun 9 only) |

#### D5 — Mechanism / assay tensions

| # | Pin |
|---|-----|
| D5-31 | Queuine / **STL-101** plasma age-decline **reconciliation** (**UNSETTLED**: PLOS flat vs bioRxiv drop) |
| D5-32 | Human **queuine longevity NCT/mg** (bioRxiv Mar 2026 mouse +15.3% ≠ human trial) |
| D5-33 | Nitazoxanide **human aging / FOXN1** NCT (Genah 2026 mouse only) |
| D5-34 | Oral sema **25/50** vs VITAL-H (OASIS COMPLETED; **≠ VITAL-H aging mg**) |
| D5-35 | Selective **B2M / CCL11** aging depletion IND (2025 review: CCL11 trials vacant; CAT-213 inflammatory only) |

### E. Ops / harness (keep the machine running)

| # | Item |
|---|------|
| E36 | Ralph tick loop healthy (~600s; sentinel `AGENT_LOOP_TICK_liveforever`) |
| E37 | Refresh `NEXT_QUERIES` every wake toward highest-value absent pin |
| E38 | Append ≥3–5 corpus sources per wake; update hillclimb + ab-trial-design |
| E39 | Run `status.py` + `pytest -q --cache-clear` after corpus edits |
| E40 | Never commit unless CEO asks |
| E41 | Safety: literature/systems only — no DIY biotech or personal dosing |

### F. Explicitly NOT backlog (closed — don't reopen)

- Repo scaffold, two-pathway sim, ITP/parabiosis ingest, pro-aging catalog v1  
- `thymic-restoration` as separate gap (mapped to L3)  
- Inventing mg from adjacency ladders (**forbidden**)

**Backlog count:** 5 deferred + 1 hallmark seed + 35 research pins + 6 ops ≈ **47 enumerated rows** (ultra-design overlaps deferred).

---

## Needs research (priority order)

1. **EVERLAST Results** / Konopka preprint or abstract — trial done, tables empty  
2. **RESTOR adaptive OD mg** — study started, dose still secret  
3. **SHAPE daily SC mg + Results** — recruiting, vial concentration ≠ protocol dose  
4. **VITAL-H NCT + arm mg** — biggest funded healthy-aging oral trial; registry vacuum  
5. **ER-100 DSMB second-patient** — sentinel design; public outcome may lag 28+ days  
6. **Queuine plasma reconciliation** — harmonized cohort+assay before trusting "decline"  
7. **STL-101 human NCT** — mouse lifespan preprint is not a trial  
8. **Deciduous IND** — patent ≠ clinic  
9. **B2M/CCL11 aging depletion IND** — mechanism hot, human longevity trial absent  

Active Exa seeds: `scripts/ralph_tick.py` → `NEXT_QUERIES` (currently RESTOR → SHAPE → EVERLAST top 3).

---

## New lessons since last CEO update (≥8)

Full write-up: [`lessons-learned-2026-08-22.md`](lessons-learned-2026-08-22.md). Prior L1–L10 unchanged in [`lessons-learned-2026-08-21.md`](lessons-learned-2026-08-21.md).

| # | Lesson (one line) |
|---|-------------------|
| **L11** | Stale lab/recruitment web pages ≠ Results — Konopka EVERLAST still shows recruitment while CT.gov COMPLETED |
| **L12** | Patent / IP grant ≠ IND filed — Deciduous US20250381206 still preclinical on fobi Jul 2026 |
| **L13** | OASIS obesity sema 25/50 mg COMPLETED ≠ VITAL-H healthy-older arm mg |
| **L14** | Queuine "flat vs drop" is **assay/cohort mismatch** — unsettled until harmonized measurement |
| **L15** | Mouse lifespan preprint (bioRxiv +15.3%) ≠ human supplementation NCT |
| **L16** | Intravitreal ER-100 OSK ≠ systemic OSK dossier clearance |
| **L17** | CCL11 human trials **vacant** per 2025 review; CAT-213 = inflammatory path only |
| **L18** | Run `status.py` + pytest **after every wake** before claiming done — oracle is the scoreboard |

Retention: `AGENTS.md`, `.cursor/rules/live-forever-ralph.mdc`, skill `live-forever-ralph-hillclimb`, Claude memory `feedback_ceo_update_lessons_2026_08_22.md`.

---

## Ask of CEO

Nothing blocking. Keep Ralph running. Do **not** treat green scaffold as "stop researching." Safety boundary unchanged: **literature + systems only** — no DIY dosing or gene editing.
