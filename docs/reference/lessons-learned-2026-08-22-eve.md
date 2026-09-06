# Lessons learned — live-forever (2026-08-22 evening)

**Scope:** Lessons **since** PM [`lessons-learned-2026-08-22-pm.md`](lessons-learned-2026-08-22-pm.md) / [`ceo-update-2026-08-22-pm.md`](ceo-update-2026-08-22-pm.md) (wake **#246**). Drawn from Ralph wakes **#247–#275** (hillclimb ticks **#251–#281**). Corpus **1318 → 1469**. Includes L0 paper/OSS publish path + public GitHub.

Prior laws **L1–L25** remain in force — do not drop them. This file adds **L26–L32**.

Retain in: this file, `AGENTS.md`, `.cursor/rules/live-forever-ralph.mdc`, skill `live-forever-ralph-hillclimb` (project + `~/.claude/skills/`), agent `~/.claude/agents/live-forever-ralph-guardian.md`, Claude memory `feedback_ceo_update_lessons_2026_08_22_eve.md`.

---

## L26. PowerShell mangling of inline Python — use a TEMP script

Complex multi-line Python inside a PowerShell one-liner (here-strings, escaping, quoting) **silently corrupts** or fails mid-wake. **Write** `$env:TEMP\lf_wakeN.py`, **run** `python $env:TEMP\lf_wakeN.py`, **delete** the temp file. Receipt: wake #270+ pattern. Twin of ASCII YAML hygiene — the shell is part of the instrument.

## L27. Corpus settle before status / pytest

Append `corpus/sources.yaml` (and dossier/hillclimb) **first**, then run `status.py` + `pytest`. Counting/parsing against a half-written YAML yields false corpus_ok failures or stale counts. **Oracle last** (L18) assumes the corpus file is already closed.

## L28. Unique hillclimb tick headers every wake

Each wake needs a new `## Tick N - …` header. Reusing or omitting headers breaks Select-String history and confuses the next agent about which tick landed. Same family as unique `## Update (Ralph wake #N)` dossier anchors (L21).

## L29. Absence claims are search-scoped + dated — not universal nonexistence

For **VITAL-H** (and similar registry vacuums): say **“no matching NCT in searched sources as of DATE”** (name CT.gov + Barshop + ARPA-H press), **not** “does not exist anywhere.” Absolute nonexistence is unprovable from a finite search; scoped negatives are honest and re-checkable. Paper brief already pins this; wakes must use the same wording.

## L30. Public git tracking origin → wake ends with commit + push

Once `live-forever` is a public git repo on `origin/master`, a completed Ralph wake **commits and pushes** the four standard files (`sources.yaml`, `hillclimb.md`, `ab-trial-design.md`, `ralph_tick.py`) unless CEO says otherwise. PowerShell: `$msg = "…"; git commit -m $msg` — **no bash heredoc**. This **revises** older “never commit” ops copy for the public-repo era; still never invent secrets into commits.

## L31. MCP / tool-surface drift — rediscover before stalling

`CallMcpTool` may disappear mid-session; use `GetDynamicTools` + `CallDynamicTool` (or WebSearch) and continue the wake. A missing tool name is **not** a reason to skip Exa / CT.gov hunts.

## L32. Paper honesty: operational D(t); illustrative sex sim ≠ ITP; don’t re-litigate Barkman

L0 paper / OSS path banks: **operational** boundedness of \(D(t)\) (not metaphysical immortality); sex clearance \(D \approx 0.147\) is an **illustrative toy sim**, not ITP-calibrated biology; Barkman “theorem” already demoted to operational language in `ultra-design.md` — **do not re-litigate**. Adjacency ladders ≠ causal DAGs in the epistemics dossier.

---

## Rotation + publish receipt

Wakes **#247–#275** (~29) kept rotating EVERLAST / VITAL-H / RESTOR / SHAPE / ER-100 / Deciduous / STL-101 / queuine / NTZ / B2M / OASIS fence. Corpus **+151** without inventing milligrams. Tick **259** banked paper-l0 + related-open-tools + geroscience-epistemics; public GitHub `oimiragieo/live-forever` live.
