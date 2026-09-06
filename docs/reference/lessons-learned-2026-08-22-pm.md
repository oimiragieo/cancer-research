# Lessons learned — live-forever (2026-08-22 PM)

**Scope:** Lessons **since** morning [`lessons-learned-2026-08-22.md`](lessons-learned-2026-08-22.md) / [`ceo-update-2026-08-22.md`](ceo-update-2026-08-22.md) (wake **#218**). Drawn from Ralph wakes **#219–#246** (hillclimb ticks **#222–#250**). Corpus **1177 → 1318**.

Prior laws **L1–L18** remain in force — do not drop them. This file adds **L19–L25**.

Retain in: this file, `AGENTS.md`, `.cursor/rules/live-forever-ralph.mdc`, skill `live-forever-ralph-hillclimb` (project + `~/.claude/skills/`), Claude memory `feedback_ceo_update_lessons_2026_08_22_pm.md`.

---

## L19. Disease-label dose ≠ healthy-aging pilot dose

**Forzinity** (elamipretide) FDA accelerated approval **Sep 19 2025** for **Barth syndrome** at **40 mg SC daily** (≥30 kg) is **disease-label adjacency**. **SHAPE** (NCT07275424) is an open-label **healthy-aging** pilot in adults 65–80 with unpublished daily protocol mg. **Do not invent SHAPE mg/day from the Barth label.** Same family as OASIS≠VITAL-H and HGPS≠Progerinin Finals.

## L20. Press timeline ≠ CT.gov NCT registration

**VITAL-H** Mar 2026 press + **San Antonio Report Mar 16 2026** ("expected start later 2026 or early 2027") restates arms, n, wearables — **still no CT.gov NCT**, recruitment not begun, per-arm mg unpublished. **Journalism timelines are not registry entries.** Bank as adjacency; keep hunting NCT + protocol mg.

## L21. Non-unique StrReplace inserts mid-file

`ab-trial-design.md` has dozens of near-identical "- **… negatives held.**" lines. Replacing on that string alone can insert a new wake **between older wakes** (receipts: wake #242/#246 mis-inserts). **Always** anchor on unique `## Update (Ralph wake #N)` blocks or **append at EOF**. Prefer unique wake-header context over bare "negatives held."

## L22. Duplicate wake sections = same-turn cleanup

When a wake block lands twice (or a mid-file insert creates out-of-order sections), **delete the wrong copy the same turn**. Leaving duplicates invites the next agent to edit the wrong section. Chronological order at file end is the contract.

## L23. Estimated primary completion past ≠ Results Posted

**SHAPE** primary completion **est Mar 15 2026**; CT.gov still **RECRUITING** with update **2026-06-15**; PeptideStat **Results not reported**. Passing an **estimated** date does not force Results tables. Twin of COMPLETED≠Results for the recruiting arm: **est. completion ≠ posted outcomes**.

## L24. Protocol Version / aggregator metadata ≠ Results tables

**EVERLAST** Syfrah/aggregators can show **Protocol Version 6/5/2026**, COMPLETED Jul 2026, arms restated — while CT.gov still has **No Results Posted** and Konopka lab shows stale recruitment. **Metadata churn ≠ readout.** Hunt Results tables / preprint / abstract.

## L25. Review saying "not demonstrated" corroborates absence — does not invent a trial

**Immun Ageing Jul 2026** thymic-restoration review notes domain-specific clinical benefits of adult thymus restoration **not yet demonstrated in controlled trials**. That **supports** the NTZ FOXN1 human-aging NCT vacuum; it is **not** a substitute NCT, dose, or IND. **Reviews ≠ registrations.**

---

## Rotation discipline (receipt)

Negative rechecks across wakes **#219–#246** kept EVERLAST Results as the highest-value readout hunt while rotating top-3 `NEXT_QUERIES` through RESTOR/SHAPE/VITAL-H/ER-100/Deciduous/STL-101/queuine/NTZ/B2M/OASIS fence. Corpus grew **+141** without inventing a single milligram.
