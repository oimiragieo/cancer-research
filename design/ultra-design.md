# Ultra-design — Cancer Cure Research Engine (Hybrid D)

> Literature synthesis + systems architecture. **Not** medical advice. **Not** DIY therapy.
> Thinktank (codex, 2026-09-05): **RECOMMENDED D** — hallmarks ultra-design + sentinel hard cancers + emerging-modality pins.
> **GOAL_MET is a floor** — keep climbing unpublished NCT/Results after green.

## Cure definition (load-bearing)

A **found cure** (for Ralph exit language) is an **existing, disease-specific** intervention with:

1. Replicated clinical evidence of **durable treatment-free remission** and/or a **survival plateau**
2. Adequate follow-up (design floor ≥3 years when claiming plateau)
3. Transparent **NCT / Results / manuscript** provenance

It is **not**: inventing a molecule, pan-cancer extrapolation, adjacency from a sister trial, or collapsing MRD/CR/pCR into “cured.”

## Layer stack (hallmarks → modalities → sentinels)

| Layer | Focus | Status |
|-------|--------|--------|
| L0 | Epistemics — COMPLETED≠Results; MRD assay honesty; cure-fraction stats | Mapped (`design/gaps/cure-evidence-epistemics.md`) |
| L1 | Hallmarks of cancer coverage map (Hanahan/Weinberg + 2022 dimensions) | Mapped |
| L2 | Modality portfolio — chemo curative (GCT/ALL), TKI/TFR (CML), CPI plateaus (melanoma), ADC, bispecifics, CAR-T, vaccines | Seeded in corpus |
| L3 | Hema cure-adjacent bank — blina E1910, CD19 CAR-T class, BCMA CAR-T / TCE | **Existence proofs banked** |
| L4 | Sentinel hard solids — PDAC, GBM, mTNBC (rotate) | Deferred dossiers; climb forever |
| L5 | Resistance engineering — dual-antigen, neoadjuvant timing, TME | Algorithms + gaps |
| L6 | Medicine pipeline — target → IND → GMP → randomized durable endpoints | `medicine-pipeline.md` |

## Climb order (Exa agent_run + thinktank)

1. Provenance-first evidence graph; hema modalities with mature cure-adjacent endpoints
2. Resected PDAC / high-risk TNBC (immune kinetics + recurrence); prioritize NCT05968326
3. GBM as high-risk mechanistic lane (neoadjuvant window) before efficacy claims
4. Each Ralph wake: one absent pin → Exa/CT.gov → ≥3–5 sources → update gaps → pytest

## Algorithms

- `algorithms/tumor_burden.py` — clearance vs resistance; dual-target derisks resistance accrual
- Retain `portfolio_optimizer`, `trial_transparency`, `hallmarks_graph` as modality/coverage tools (retarget tags over wakes)

## Safety boundary

No DIY CRISPR, synthesis recipes, personal dosing, or lab protocols. Translational path = standard discovery → trials → regulators.
