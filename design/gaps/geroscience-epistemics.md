# Gap dossier: Geroscience epistemics (L0 + negatives bank)

**Status:** active research climb (seed dossier 2026-08-22)  
**Related paper brief:** [`docs/ideation/paper-l0-control-instrumentation.md`](../../docs/ideation/paper-l0-control-instrumentation.md)  
**Related landscape:** [`docs/reference/related-open-tools.md`](../../docs/reference/related-open-tools.md)

## Problem statement

Closed-loop longevity control requires **sensors that can fail in both directions** (bidirectional oracles). Much of geroscience publishing and trial reporting is still **open-loop epistemically**: registries mark studies COMPLETED while Results tables / manuscripts remain absent; surrogate clocks move without coupled functional endpoints; competition and regulatory endpoint sets are still being invented (XPRIZE immune assay TBD; PROSPR Intrinsic Capacity construction).

This dossier tracks that **epistemic bottleneck** — not drug efficacy claims.

## Laws (load-bearing)

| Law | Meaning |
|-----|---------|
| COMPLETED ≠ Results | Registry completion is a hunt trigger, not evidence |
| Est. completion ≠ Results | Past primary-completion estimates do not invent tables |
| Protocol Version ≠ Results | Aggregator metadata churn ≠ outcomes |
| Press ≠ NCT | Journalism / award pages ≠ ClinicalTrials.gov registration |
| Clock ≠ healthspan | Molecular age shift alone is not a closed-loop success signal |
| Adjacency ≠ invention | Sister trials / disease labels do not fill unpublished arm mg |

## L0 instrumentation notes (cite ultra-design)

- Dual-track L0: FDA-facing IC domains (PROSPR / VITAL-H path) vs XPRIZE Finals triad (muscle + cognitive + immune).
- XPRIZE: immune cell response-to-challenge is a **named category**; specific assay still pending in public materials as of corpus wakes through 2026-08-22.
- Internal control layers (clocks, SASP, clone VAF) do not replace functional gates.

## Seed ledger — high-value epistemic pins

> Entries are **source-dated leads** with confidence. They are **not** established negative biological findings. Re-verify before manuscript use.

| Pin | Registry / source | Status signal (as of last wake) | Missing epistemic object | Confidence |
|-----|-------------------|----------------------------------|--------------------------|------------|
| EVERLAST | NCT05835999 | COMPLETED 2026-07-22 (n=106 ACTUAL on CT.gov materials) | Results tables / Konopka preprint | high |
| VITAL-H | ARPA-H award + Barshop listing | Recruitment not begun; **no matching NCT found in searched sources as of 2026-08-22** | NCT ID + per-arm mg | high (search-limited) |
| RESTOR | NCT06658093 | RECRUITING from 2026-03-04 | Adaptive OD milligrams | high |
| SHAPE | NCT07275424 | RECRUITING; vial 80 mg/mL disclosed | Daily SC protocol mg + Results | high |
| ER-100 | NCT07290244 | First dose press 2026-06-09 | Public DSMB second-patient clearance | high |
| TIME TRAVELER | UMIN000059942 | COMPLETED (per backlog) | Results numbers | medium |
| Queuine plasma | PLOS 2021 vs bioRxiv 2026 | Conflicting age associations | Assay/cohort reconciliation | high (UNSETTLED) |

Full enumerated climb: [`docs/reference/BACKLOG.md`](../../docs/reference/BACKLOG.md).  
Running narrative updates: [`design/gaps/ab-trial-design.md`](ab-trial-design.md).

## Search methods (for “no NCT found” claims)

When stating that VITAL-H lacks an NCT, document:

1. Query ClinicalTrials.gov for “VITAL-H”, “Volpi”, “Barshop”, “PROSPR”, “rapamycin dapagliflozin semaglutide” aging.
2. Check Barshop clinical-trials page and ARPA-H award page.
3. Record **as-of date** and hits (including false friends).
4. Prefer: “no matching NCT identifier found in the searched sources as of DATE” over absolute nonexistence.

## Open productization path (deferred)

A future OSS “negatives bank” could export structured JSONL:

- `nct_or_id`, `registry`, `status`, `completion_date`, `results_posted` (bool), `as_of`, `sources[]`, `fence_tags[]`, `confidence`

Not implemented this wave — seed dossier + BACKLOG only.

## Update (banking wave 2026-08-22)

- Created dossier from multi-model feedback + thinktank **APPROVE_B_WITH_EDITS**.
- Paper spine locked to L0 + sex sensitivity probe; Pathway B taxonomy supporting.
- Related-open-tools map published to prevent clock/database duplication.
