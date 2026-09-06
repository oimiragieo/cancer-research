# Design: L0 Paper Focus + Open-Science Moat + Public Publish

**Date:** 2026-08-22  
**Status:** approved-by-user-directive (plan → thinktank → implement → public GitHub)  
**Safety:** Literature synthesis + systems architecture only. No DIY dosing / gene therapy.

## Problem

External feedback converged on:

1. Paper should **not** be another molecule/hallmarks review.
2. Highest leverage thesis: **longevity as closed-loop control + L0 instrumentation bottleneck**, with **sex-bifurcated regimes** as the sharpest falsifier of universal open-loop stacks.
3. Open-science landscape (pyaging, HAGR, ITP, Lifespan.io, Foresight) is mostly clocks/lists/roadmaps — white space is **control theory + driver graph + completed-without-Results audit**.
4. This repo already holds pieces of that white space; they are under-foregrounded for external researchers and not yet published as a public GitHub research codebase.

## Goals

1. **Bank the paper brief** with honesty guards (toy model ≠ formal theorem; sex \(D\) illustrative ≠ ITP-calibrated).
2. **Bank related-open-tools + white-space map** with cited URLs (do not fork clocks/databases).
3. **Bank a geroscience epistemics / negatives-bank seed dossier** pointing at live corpus receipts.
4. **Wire** README / ultra-design / BACKLOG / AGENTS so newcomers find the research path.
5. **Cite** new sources in `corpus/sources.yaml`.
6. **Publish** as a **public** GitHub repo under the authenticated `oimiragieo` account (user-authorized).

## Non-goals

- Rebuilding pyaging / DrugAge / GenAge.
- Claiming a formal “Boundedness Theorem.”
- Claiming `hallmarks_graph` is a proven causal DAG.
- Auto-publishing secrets, `.env`, API keys, or private agent state.

## Approaches considered

| Approach | Pros | Cons |
|----------|------|------|
| A. Docs-only paper brief | Fast | Weak OSS positioning |
| B. Docs + epistemics dossier + related-tools + README moat + public repo | Matches feedback; citeable | Larger diff |
| C. Full negatives-bank product (multi-registry scraper) | Highest OSS uniqueness | Too large for this turn; defer |

**Chosen: B**, with C deferred to BACKLOG.

## Honesty guards (mandatory in all new docs)

- \(D(t)=A(t)+B(t)\) is an **operational model** + simulator, not a published theorem.
- `immortality_stack` male \(D\approx0.147\) / female late-tox \(D\approx1.98\) is **illustrative** (`design/gaps/age-matrix.md`); directionally consistent with ITP sex-asymmetric lifespan, **not** a fitted ITP damage ratio.
- `DRIVER_EDGES` = **mechanistic adjacency**, not proven causality.
- Queuine plasma age-decline remains **UNSETTLED** (PLOS flat vs bioRxiv decline).
- COMPLETED ≠ Results; press ≠ NCT; adjacency ≠ invention (existing laws).

## Deliverables

| Path | Role |
|------|------|
| `docs/ideation/paper-l0-control-instrumentation.md` | Paper thesis + § outline + corpus citations |
| `docs/reference/related-open-tools.md` | Cited landscape + “what we are not” |
| `design/gaps/geroscience-epistemics.md` | Negatives-bank / L0 epistemic bottleneck dossier |
| `docs/superpowers/plans/2026-08-22-l0-paper-oss-implement.md` | Implementation plan |
| README / ultra-design / BACKLOG / AGENTS | Pointers |
| `corpus/sources.yaml` | +sourced entries for open tools + paper brief |
| Public GitHub repo | `git init` + MIT or Apache-2.0 + push |

## Success criteria

- `python scripts/status.py` → `GOAL_MET`
- `pytest -q --cache-clear` → 42 passed (or current suite green)
- Public repo URL returned to user
- No secrets in tree
