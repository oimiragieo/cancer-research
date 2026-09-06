# Enterprise hardening + honest backlog close-out — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use `superpowers:subagent-driven-development` (recommended) or `superpowers:executing-plans` to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Make `live-forever` a world-class **research-engine product** (CI, schema gates, TDD, jr-analyst runbook, secret hygiene) while **honestly refusing** to “close” sentinel clinical pins by inventing milligrams.

**Architecture:** Hybrid agentic harness (arxiv EligMeta / Samyama pattern): LLMs for Ralph research wakes; **deterministic** validators for corpus/schema/CI. Safety boundary unchanged — literature/systems only.

**Tech Stack:** Python 3.11+, pytest, PyYAML, jsonschema, ruff, GitHub Actions, pre-commit.

**Branch:** `enterprise/hardening-wave-1` from `master`.

---

## Honesty gate (load-bearing — thinktank must enforce)

| Bucket | Count | Closable by code? |
|--------|-------|-------------------|
| A Deferred dossiers | 5 | **NO** — need clinical data |
| C dysbiosis hallmark | 1 | **NO** — needs evidence, not invent |
| D1–D5 research pins | 35 | **NO** — sentinel Ralph only |
| E Ops harness | 9 | **Partial** — software/docs yes; Ralph loop runtime is ops |
| F Closed | — | Already closed |

**FORBIDDEN:** Filling VITAL-H/RESTOR/SHAPE/Finals mg, fabricating NCT IDs, marking D-pins DONE without CT.gov/preprint receipts.

**SUCCESS for this wave:** Closable software/docs/CI shipped + BACKLOG rewritten so a jr analyst sees **SENTINEL vs DONE** clearly + all tests green + dogfood `status.py`/`pytest`.

---

## File map

| File | Responsibility |
|------|----------------|
| `pyproject.toml` | Package metadata, ruff/pytest config, optional deps |
| `requirements.txt` | Runtime pins (pyyaml, jsonschema) |
| `requirements-dev.txt` | pytest, ruff, pre-commit, jsonschema |
| `.github/workflows/ci.yml` | pytest + ruff on push/PR |
| `.pre-commit-config.yaml` | ruff + trailing whitespace |
| `scripts/validate_corpus.py` | Deterministic corpus schema + unique-id gate |
| `tests/test_validate_corpus.py` | TDD for validator (bidirectional) |
| `docs/reference/JR_ANALYST_RUNBOOK.md` | Jr analyst how-to |
| `docs/reference/BACKLOG.md` | Rewrite: DONE software / OPEN sentinel |
| `docs/reference/SENTINEL_BOARD.md` | Machine-readable D1 status board (no invented mg) |
| `README.md` | Point to eve CEO + runbook + CI badge |
| `CONTRIBUTING.md` | Dev loop + safety |
| `algorithms/` / `scripts/` | Minor packaging imports if needed |

---

## Research grounding (Exa / arXiv — verified 2026-08-22)

1. **EligMeta** (arXiv 2604.02678) — hybrid LLM reasoning + **deterministic** numeric/logic execution for clinical evidence. We mirror: Ralph=LLM hunt; validators/CI=deterministic.
2. **Samyama / Clinical Trials KG** (arXiv 2603.15080) — schema-driven agent tools beat freeform Cypher. We add **typed corpus schema**, not a 7M-node KG in this wave (YAGNI).
3. **CTG-DB** (arXiv 2603.15936) — CT.gov as analytics needs normalization; we do **not** scrape CT.gov into doses — we keep adjacency≠invention.

---

### Task 1: Branch + failing corpus-validator test

**Files:**
- Create: `tests/test_validate_corpus.py`
- Create: `scripts/validate_corpus.py` (stub)

- [ ] `git checkout -b enterprise/hardening-wave-1`
- [ ] Write failing test: empty sources list → fail; duplicate `id` → fail; missing required fields → fail; real `corpus/sources.yaml` → pass (or skip if too heavy — sample fixture)
- [ ] Run `pytest tests/test_validate_corpus.py -q` — expect FAIL
- [ ] Implement minimal `validate_corpus.py` until PASS
- [ ] Wire `status.py` or CI to call validator (optional import)

### Task 2: Packaging + ruff + pytest config

**Files:**
- Create: `pyproject.toml`
- Create: `requirements-dev.txt`
- Modify: `requirements.txt`

- [ ] Add `pyproject.toml` with `[tool.pytest.ini_options]`, `[tool.ruff]`
- [ ] Add `jsonschema` to requirements; ruff/pytest/pre-commit to requirements-dev
- [ ] `pip install -r requirements-dev.txt`
- [ ] `ruff check algorithms scripts tests` — fix only introduced issues
- [ ] `pytest -q --cache-clear` green

### Task 3: GitHub Actions CI + secret hygiene

**Files:**
- Create: `.github/workflows/ci.yml`

- [ ] Workflow: checkout, setup-python 3.12, install deps, `ruff check`, `pytest -q --cache-clear`, `python scripts/validate_corpus.py`
- [ ] Add secret scan step: `gitleaks detect --source . --no-git` OR `detect-secrets scan` with baseline (fail on high-entropy / key patterns). No false green on `.env` accidental commit.
- [ ] Confirm YAML valid

**Thinktank self-chair note (2026-08-22):** External `tt_quick` seats could not inspect the plan (codex policy + agy read_file deny + WSL `agent` auth-down). Chairman (this session) **APPROVE_WAVE1** with these must-fixes applied: secret scan in CI; validator TDD uses small fixtures (full corpus validate in CI/script only, not every unit test); document cursor-agent login as ops finding E45.

### Task 4: pre-commit

**Files:**
- Create: `.pre-commit-config.yaml`

- [ ] ruff + end-of-file-fixer + check-yaml (exclude giant corpus if needed — validate via script instead)
- [ ] Document install in CONTRIBUTING

### Task 5: Jr analyst runbook + CONTRIBUTING

**Files:**
- Create: `docs/reference/JR_ANALYST_RUNBOOK.md`
- Create: `CONTRIBUTING.md`
- Modify: `README.md`

- [ ] Runbook: safety, Ralph wake steps, how to bank a negative, how to run CI locally, what NOT to invent
- [ ] README: link eve CEO update, runbook, sentinel board
- [ ] CONTRIBUTING: branch policy, TDD, never invent mg

### Task 6: SENTINEL_BOARD + BACKLOG rewrite

**Files:**
- Create: `docs/reference/SENTINEL_BOARD.md`
- Modify: `docs/reference/BACKLOG.md`

- [ ] SENTINEL_BOARD: D1–D5 table with status OPEN / as-of date / last wake — **no mg invention**
- [ ] BACKLOG: section **G. Software wave DONE** vs **D still OPEN sentinel**
- [ ] Document cursor-agent auth blocker as ops finding

### Task 7: Land eve CEO docs on branch

**Files:**
- `docs/reference/ceo-update-2026-08-22-eve.md`
- `docs/reference/lessons-learned-2026-08-22-eve.md`
- `AGENTS.md` (already modified)

- [ ] Include in branch commit(s)

### Task 8: Dogfood + merge gate

- [ ] `python scripts/status.py` → GOAL_MET
- [ ] `python scripts/validate_corpus.py` → exit 0
- [ ] `pytest -q --cache-clear` → 42+ new tests green
- [ ] `ruff check` → clean (scoped)
- [ ] Codex/cursor-agent code review vs this plan (or Task code-reviewer if agent auth down)
- [ ] Fix issues until clean
- [ ] Merge to `master` (fast-forward or PR)
- [ ] Update BACKLOG with any new findings from dogfood

---

## Out of scope (explicit)

- Closing any D1–D5 pin without external disclosure
- Building a full Clinical Trials KG / MCP fleet (future wave)
- Auto-merge Ralph commits of invented doses
- DIY biotech / personal dosing

## Verification commands

```powershell
cd C:\dev\projects\live-forever
python scripts\status.py
python scripts\validate_corpus.py
pytest -q --cache-clear
ruff check algorithms scripts tests
```

## Thinktank ask

Approve only if: (1) honesty gate preserved, (2) scope is software-closable only, (3) TDD+CI present, (4) sentinel pins stay OPEN, (5) YAGNI on 7M-node KG this wave.
