# Contributing — live-forever

## Rules

1. Literature/systems only — no DIY biotech or personal dosing.
2. Never invent clinical milligrams / NCT IDs / Finals doses.
3. TDD for code changes: failing test → implement → green.
4. Run `python scripts/validate_corpus.py` after corpus edits.
5. Prefer branch `enterprise/*` or `ralph/*` for non-trivial work; merge to `master` when CI green.

## Local loop

```powershell
pip install -r requirements-dev.txt
pre-commit install   # optional
ruff check algorithms scripts tests
pytest -q --cache-clear
python scripts\status.py
python scripts\validate_corpus.py
```

## Ralph wakes

Follow `docs/reference/JR_ANALYST_RUNBOOK.md` and skill `live-forever-ralph-hillclimb`.
