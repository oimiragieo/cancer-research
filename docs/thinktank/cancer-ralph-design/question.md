# Thinktank question — cancer-research Ralph engine design

**Do not dispatch other agents; respond inline. Answer from the brief; do not invent clinical milligrams or claim a novel molecule cure.**

## Context

CEO wants a fork of `C:\dev\projects\live-forever` retargeted at cancer/oncology cure research in `C:\dev\projects\cancer-research`.

Live-forever is a literature + systems research engine with:
- `corpus/sources.yaml` curated sources
- `design/ultra-design.md` multi-layer stack
- `algorithms/` simulators
- Ralph loop (`scripts/ralph_tick.py` + hillclimb log) that wakes, Exa/CT.gov researches missing pins, appends sources, updates gaps, pytest
- Laws: GOAL_MET is a floor; COMPLETED ≠ Results; adjacency ≠ invention; bank negatives; safety = no DIY biotech

CEO said scope = **everything** (pan-cancer + hard solid tumors + emerging modalities). When asked climb order A–D, redirected to Thinktank (do not ask CEO).

Exa 2026 signal samples (verify before banking):
- CAR-PRISM (NCT05767359): cilta-cel in HR-SMM → 100% MRD-neg 10^-6 at early follow-up (Nature Medicine 2026) — **curative-intent signal in precursor myeloma**, not pan-cancer cure
- ZUMA-14: axi-cel + rituximab dual CD19/CD20 — durable CRs in LBCL
- LOTIS-5: ZYNLONTA + rituximab Ph3 PFS win in r/r DLBCL (not cure claim)
- MonumenTAL-6: TECVAYLI + TALVEY dual BCMA/GPRC5D Ph3 HR 0.11 PFS
- Solid tumors (PDAC, GBM, mTNBC) remain the unmet-need frontier

## Decision required

Pick ONE architecture for the cancer-research repo fork:

**A)** Deadliest unmet-need first (PDAC, GBM, mTNBC, ovarian…)
**B)** Modality-first (IO → targeted → ADC → cell Rx → vaccines…)
**C)** Hallmarks-of-cancer ultra-design only, disease dossiers under each hallmark
**D)** Hybrid (recommended by orchestrator): hallmarks ultra-design + rotating sentinel hard cancers + emerging-modality clinical pins; GOAL_MET floor then forever climb

Also define **exit-criteria floor** (what turns GOAL_MET green) and **what "found a cure" means** without scientific fraud:
- Must NOT claim inventing a new molecular cure
- MUST bank evidence of existing/near-curative paths with NCT + Results honesty
- Analog to live-forever: floor = corpus N + ultra-design + algorithms + medicine map + open gaps closed/deferred; then keep climbing unpublished Results / solid-tumor curative pins

## Constraints

- Literature synthesis + systems design only (same safety boundary as live-forever)
- Copy/adapt live-forever structure; strip longevity-specific corpus; retarget algorithms (e.g. tumor burden / resistance / hallmark coverage instead of organismal damage D(t))
- Windows YAML/pytest hygiene applies
- Prefer unique `id`s in sources.yaml; bank negatives

## Required output format

End with exactly one line:

`RECOMMENDED: <A|B|C|D> | floor=<short exit criteria> | cure_def=<one sentence> | first_wake=<top 3 Exa queries>`

Then ≤15 lines of reasoning with any dissent risks.


---
COUNCIL INSTRUCTIONS: Answer inline. Do not dispatch other agents, use skills, or edit files. End your reply with a final line that starts with exactly: RECOMMENDED: <your one-line verdict>
