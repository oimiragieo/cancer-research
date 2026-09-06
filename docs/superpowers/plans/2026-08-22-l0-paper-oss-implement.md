# L0 Paper + OSS Moat + Public Publish Implementation Plan

> **For agentic workers:** Execute task-by-task. Checkboxes track progress.

**Goal:** Bank paper brief + open-tools map + epistemics dossier, wire pointers, cite sources, publish public GitHub research repo.

**Architecture:** Docs-first research moat (Approach B). No clock/database forks. Honesty guards baked into every public claim.

**Tech Stack:** Markdown research corpus, YAML sources, Python status/pytest, GitHub (`gh`).

---

### Task 1: Thinktank gate (tt_quick)

- [ ] Dispatch codex+agy on design spec hash + recommended path
- [ ] Record RECOMMENDED line into plan appendix

### Task 2: Paper ideation doc

- [ ] Create `docs/ideation/paper-l0-control-instrumentation.md`
- [ ] Include thesis, honesty guards, §1–5 outline, corpus citations

### Task 3: Related open tools

- [ ] Create `docs/reference/related-open-tools.md` with cited URLs
- [ ] Correct pyaging attribution (lucascamillomd / Bioinformatics 2024 DOI) — not anfederico

### Task 4: Epistemics dossier

- [ ] Create `design/gaps/geroscience-epistemics.md`
- [ ] Seed COMPLETED-without-Results ledger pointing at BACKLOG + wake receipts

### Task 5: Wire + corpus

- [ ] Update README, ultra-design, BACKLOG, AGENTS
- [ ] Append ≥5 cited `corpus/sources.yaml` entries
- [ ] Hillclimb tick for this banking wave
- [ ] `status.py` + `pytest -q --cache-clear`

### Task 6: Public GitHub

- [ ] Add `.gitignore` (pytest cache, `__pycache__`, `.env`, secrets)
- [ ] Add `LICENSE` (MIT)
- [ ] `git init`, initial commit, `gh repo create --public --source=. --push`
- [ ] Return repo URL

## Appendix — Thinktank receipt (2026-08-22)

- `tt_smoke` (codex+agy): ALL SEATS GREEN
- `tt_quick` WSL: codex=OK → **RECOMMENDED: APPROVE_B_WITH_EDITS**; agy=PROVIDER_FAILURE (`tg` permission denied)
- Edits applied in paper brief + ultra-design wording + epistemics search-method language
- Public publish: after status+pytest + MIT + .gitignore secrets gate
