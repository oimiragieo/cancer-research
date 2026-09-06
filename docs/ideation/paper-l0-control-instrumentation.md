# Paper brief: Longevity as L0 Control & Instrumentation

**Status:** ideation / pre-draft (2026-08-22)  
**Audience:** researchers using this repo as a citeable research codebase  
**Safety:** non-clinical; no dosing advice

## Thinktank receipt

- Gate: `tt_smoke` seats `codex`+`agy` GREEN (2026-08-22)
- `tt_quick`: **RECOMMENDED: APPROVE_B_WITH_EDITS** (codex OK; agy PROVIDER_FAILURE on unrelated `tg` permission)
- Must-edits applied below (operational model ≠ biological law; sim sex \(D\) illustrative; adjacency ≠ causal DAG; COMPLETED ≠ Results)

## Honesty-safe thesis

> We propose a reproducible **L0 instrumentation / closed-loop control framing** for decomposing modeled longevity interventions, and use **sex-stratified simulator divergence** as a **preregistered-style sensitivity / falsification probe** — without claiming causal validation, clinical efficacy, or a fitted biological law.

## Why this paper (not another molecule review)

1. Molecule/hallmarks reviews are saturated (rapa, metformin, senolytics, NAD).
2. Open tools (clocks, DrugAge, roadmaps) are mostly **observational lists** — see [`docs/reference/related-open-tools.md`](../reference/related-open-tools.md).
3. This repo’s distinctive assets: operational \(D(t)\), bidirectional simulator tests, endpoint dual-track (PROSPR-IC vs XPRIZE), and a **COMPLETED-without-Results** audit trail.

## Core claims (scoped)

| Claim | In-repo basis | Must not say |
|-------|---------------|--------------|
| Damage boundedness as operational goal | `design/ultra-design.md` | “Theorem proves immortality” |
| Open-loop Pathway A fails asymptotically **in this model** | `algorithms/damage_control.py` + tests | “Biology proved” |
| L0 sensors are under-specified for closed-loop trials | ultra-design L0 map; XPRIZE 3rd immune assay TBD; IC invention-in-progress | “All endpoints worthless” |
| Universal single stack is fragile under sex-PK-like clearance collapse **in the toy model** | `immortality_stack_male/female`; `design/gaps/age-matrix.md` | “Female \(D=1.98\) is measured biology” / “ITP-calibrated” |
| Registry COMPLETED ≠ published Results | Ralph wakes; `docs/reference/BACKLOG.md` | “Trial failed” or “efficacy absent” |

## Proposed structure

### §1 Operational boundedness model

- Define \(D(t)=A(t)+B(t)\) as a **proposed operational decomposition** (Pathway A repairable damage; Pathway B information-limited lesions).
- State necessary conditions **inside the model**: sustained \(R_A\) and engineered \(R_B\) — either alone fails asymptotically in simulation.
- Cite: `design/ultra-design.md`; `algorithms/damage_control.py`; `tests/test_damage_control_phased.py`.

### §2 L0 instrumentation crisis (empirical audit)

- Dual-track endpoints: PROSPR / Intrinsic Capacity vs XPRIZE Finals triad (muscle + cognitive + immune).
- Document: XPRIZE immune “response-to-challenge” named category with **assay still TBD**; clock move ≠ healthspan rule.
- Cite registry/aggregator receipts with **as-of dates** (EVERLAST COMPLETED without Results tables as of wake dates; VITAL-H: **no matching NCT found in searched sources as of 2026-08-22** — search: ClinicalTrials.gov + Barshop + ARPA-H press, not a universal proof of nonexistence).
- Cite: ultra-design L0 section; `design/gaps/ab-trial-design.md`; `design/gaps/geroscience-epistemics.md`.

### §3 Sex-stratified dynamics (sensitivity probe)

- Report simulator outputs only: e.g. `immortality_stack_male` bounded final \(D\approx0.147\); `immortality_stack_female` with illustrative late clearance collapse unbounds \(\approx1.98\) (morbidity year ~88) — **not Miller/ITP-calibrated** (`design/gaps/age-matrix.md`).
- Separately cite ITP public datasets as **empirical evidence of sex-asymmetric lifespan responses** (canagliflozin, 17α-estradiol, acarbose) — **directionally consistent with non-universality**, not a validation of the toy \(D\) numbers.
- Frame as: universal open-loop stacks are a hypothesis that fails this **preregistered-style sensitivity test** when late female clearance collapse is enabled.

### §4 Pathway B engineering taxonomy (supporting)

- Map information-limited targets (CHIP surveillance, mosaic clones, mtDNA heteroplasmy, AGEs) by detectability × correctability.
- Cite: `design/pro-aging-factor-catalog.md`; ultra-design L5.
- Keep shorter than §2–§3 — support, not co-lead thesis.

### §5 Closed-loop protocol architecture

- Six-layer blueprint already in ultra-design (L0→L5): sense → de-risk → repair/clear → epigenome reset → replace.
- Emphasize bidirectional oracles (empty/wrong must fail graders) as research-engineering practice already used in this repo’s tests.

## What this paper is not

- Not a clinical protocol.
- Not a claim that any compound extends human lifespan.
- Not a replacement for pyaging / HAGR / ITP databases.

## Next drafting steps

1. Pull a dated snapshot table of COMPLETED-without-Results pins from BACKLOG into §2 appendix.
2. Export ASCII/CSV of sex-split sim trajectories for reproducible figures.
3. Add ScholarEval pass before any preprint claim of novelty.
