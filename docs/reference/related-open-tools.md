# Related open tools (landscape) — what this repo is not

**As-of:** 2026-08-22  
**Purpose:** Cite existing open longevity tooling so this research codebase does **not** duplicate clocks/databases, and so the L0-control / negatives-bank moat is explicit.

> Characterizations below are from public project pages / papers retrieved 2026-08-22. Always re-verify URLs before citing in a manuscript.

## L0 — Clocks & biomarker toolkits

| Tool | Role | Source |
|------|------|--------|
| **pyaging** | GPU-optimized Python compendium of published aging clocks (DNAm, histone, ATAC, RNA, blood chemistry); one-line prediction API | GitHub: https://github.com/lucascamillomd/pyaging · Docs: https://pyaging.readthedocs.io/ · Paper: de Lima Camillo, *Bioinformatics* 2024, https://doi.org/10.1093/bioinformatics/btae200 |
| **methylclock** | R/Bioconductor DNAm age estimation pipeline | https://github.com/isglobal-brge/methylclock |
| **BioAge** | R package for composite biological age from clinical biomarkers (Klemera–Doubal, PhenoAge-style) | https://github.com/dayoonkwon/BioAge |

**Note:** Some secondary summaries cite an alternate pyaging fork path; the maintained package + DOI above are the citeable primary (lucascamillomd / Bioinformatics 2024).

## L1–L2 — Interventions & genetics databases

| Resource | Role | Source |
|----------|------|--------|
| **HAGR** (Human Ageing Genomic Resources) | Portal for GenAge, DrugAge, etc. (de Magalhães lab) | https://genomics.senescence.info/ |
| **DrugAge** | Compounds tested for lifespan effects in model organisms | via HAGR |
| **GenAge** | Genes associated with longevity / senescence | via HAGR |
| **SynergyAge** | Combinatorial / synergistic longevity interventions | via HAGR |
| **open-genes** | Community-curated human aging genes + intervention targets | https://github.com/open-genes/open-genes |
| **NIA ITP** | Interventions Testing Program — public lifespan / pathology datasets (rapamycin, acarbose, 17α-E2, canagliflozin, …) | https://www.nia.nih.gov/research/dab/interventions-testing-program |

## L3–L4 — Translational trackers / roadmaps

| Resource | Role | Source |
|----------|------|--------|
| **Lifespan.io Rejuvenation Roadmap** | Community tracker of rejuvenation therapies through clinical phases | https://www.lifespan.io/roadmaps/rejuvenation-roadmap/ |
| **Foresight Longevity Tech Tree** | Interactive technology roadmap across repair / clearance / rejuvenation | https://foresight.org/tech-tree-longevity/ |

## White space (not unified in those tools)

These gaps are where **this repo** aims to contribute research artifacts (not to replace the tools above):

1. **Control-theoretic framing** — operational \(D(t)=A(t)+B(t)\) + simulator with bidirectional tests (`design/ultra-design.md`, `algorithms/damage_control.py`). Proposed model, not a validated biological law.
2. **Driver / intervention adjacency graph** — `algorithms/hallmarks_graph.py` (`DRIVER_EDGES`, `INTERVENTION_EDGES`). Curated hypothesis edges — **not** a proven causal DAG.
3. **Geroscience negatives / epistemics bank** — dated audit of registry COMPLETED (or recruiting) entries lacking Results tables / dose pins (`design/gaps/geroscience-epistemics.md`, `docs/reference/BACKLOG.md`, Ralph wake updates in `design/gaps/ab-trial-design.md`).

## What we are not

- Not a clock calculator (use pyaging / methylclock / BioAge).
- Not a drug/gene encyclopedia (use HAGR / open-genes / ITP).
- Not a clinical-trial registry (use ClinicalTrials.gov and peers).
- Not medical advice or a DIY protocol library.
