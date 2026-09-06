# Lessons learned — live-forever (2026-08-22 night)

**Scope:** Lessons **since** evening [`lessons-learned-2026-08-22-eve.md`](lessons-learned-2026-08-22-eve.md) / [`ceo-update-2026-08-22-eve.md`](ceo-update-2026-08-22-eve.md) (wake **#275**). Drawn from Ralph wakes **#276–#281** (hillclimb ticks **#282–#287**) + **Wave-1 enterprise hardening**. Corpus **1469 → 1499**.

Prior laws **L1–L32** remain in force — do not drop them. This file adds **L33–L39**.

Retain in: this file, `AGENTS.md`, `.cursor/rules/live-forever-ralph.mdc`, skill `live-forever-ralph-hillclimb` (`~/.claude/skills/`), agent `~/.claude/agents/live-forever-ralph-guardian.md`, Claude memory `feedback_ceo_update_lessons_2026_08_22_night.md`.

---

## L33. Software closes software; clinics close clinical pins

An enterprise close-out can ship validators, CI, runbooks, and Sentinel boards. It **cannot** close D1–D5 by inventing milligrams. Claiming “backlog complete” without CT.gov/preprint receipts is a **false green**. Partition: closable software vs sentinel research — keep both honest.

## L34. WSL free cursor-agent still needs auth

“Cursor-agent in WSL is free” ≠ “already logged in.” Headless `agent` / thinktank **cursor** seat dies without `agent login` or `CURSOR_API_KEY`. Bank as ops backlog (E45); don’t block Wave shipping on micro-agents that aren’t authenticated.

## L35. Thinktank / codex may deny file reads — self-chair, don’t stall

`tt_quick` / agy / codex can refuse plan inspection under policy. Fallback: **in-session adversarial review** with explicit security must-fixes, document E46, ship Wave with honesty about which seats were DOWN. A dead seat’s “REJECT” next to `CANNOT_READ` is not a real dissent.

## L36. Corpus dogfood before claiming CORPUS_OK

Wave-1 dogfood found: `year: null`, duplicate `id`s, legacy `confidence: med`. Fix before bragging. Validator must accept known aliases **and** enforce unique ids + required fields. Bidirectional: inject a bad row → red; revert → green.

## L37. Stacked Ralph ticks → multi-wake catch-up

When `AGENT_LOOP_TICK_liveforever` fires twice (or more) while the agent was busy, **catch up** with multiple wakes / ticks in one turn when Exa evidence is ready (receipt: ticks 151–152 → wakes #277+#278). Don’t leave a wake debt that silently grows.

## L38. Enterprise wave shape: branch → TDD → merge → dogfood → BACKLOG

Safe shipping pattern: feature branch → TDD first → `--no-ff` merge to `master` → local dogfood (`validate_corpus`, `status`, `pytest`, ruff) → bank findings in `BACKLOG.md` §G / E45–E48 → commit+push. Plan lives under `docs/superpowers/plans/`.

## L39. arXiv grounds patterns, not doses

Exa/arXiv papers (EligMeta hybrid LLM+gates, Samyama trials KG, CTG-DB analytics) **inspire** validators and future KG work. They do **not** authorize inventing RESTOR/SHAPE/VITAL-H milligrams. Research grounding ≠ clinical disclosure.

---

## Rotation + Wave-1 receipt

Wakes **#276–#281** kept rotating OASIS≠VITAL-H / ER-100 / Deciduous / STL-101 / queuine / RESTOR / SHAPE / EVERLAST / VITAL-H / NTZ / B2M. Corpus **+30** without inventing milligrams. Wave-1 merged: validator + CI + Jr runbook + Sentinel board; dogfood fixes banked.
