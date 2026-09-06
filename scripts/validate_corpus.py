"""Deterministic corpus validator — schema + unique ids (EligMeta-style hybrid gate)."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path
from typing import Any

try:
    import yaml
except ImportError:  # pragma: no cover
    yaml = None

ROOT = Path(__file__).resolve().parents[1]

REQUIRED = ("id", "title", "url", "year", "topics", "confidence", "summary")
CONFIDENCE = frozenset({"high", "medium", "med", "low"})


class ValidationError(ValueError):
    """Corpus failed a deterministic gate."""


def validate_sources(sources: list[Any]) -> int:
    if not sources:
        raise ValidationError("corpus sources list is empty")
    seen: set[str] = set()
    for i, row in enumerate(sources):
        if not isinstance(row, dict):
            raise ValidationError(f"entry {i}: not a mapping")
        for key in REQUIRED:
            if key not in row or row[key] in (None, "", []):
                raise ValidationError(f"entry {i}: missing required field '{key}'")
        sid = str(row["id"]).strip()
        if sid in seen:
            raise ValidationError(f"duplicate id: {sid}")
        seen.add(sid)
        if not isinstance(row["topics"], list) or not row["topics"]:
            raise ValidationError(f"entry {sid}: topics must be non-empty list")
        conf = str(row["confidence"]).strip().lower()
        if conf not in CONFIDENCE:
            raise ValidationError(
                f"entry {sid}: confidence must be one of {sorted(CONFIDENCE)}"
            )
        year = row["year"]
        if not isinstance(year, int) or year < 1900 or year > 2100:
            raise ValidationError(f"entry {sid}: year out of range")
        url = str(row["url"])
        if not (url.startswith("http://") or url.startswith("https://")):
            raise ValidationError(f"entry {sid}: url must be http(s)")
    return len(sources)


def load_and_validate(path: Path | None = None) -> int:
    if yaml is None:
        raise ValidationError("PyYAML required")
    path = path or (ROOT / "corpus" / "sources.yaml")
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict) or "sources" not in data:
        raise ValidationError("sources.yaml must have top-level 'sources' key")
    return validate_sources(data["sources"])


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description="Validate cancer-research corpus/sources.yaml")
    p.add_argument("--path", type=Path, default=None)
    args = p.parse_args(argv)
    try:
        n = load_and_validate(args.path)
    except ValidationError as e:
        print(f"CORPUS_INVALID: {e}", file=sys.stderr)
        return 1
    print(f"CORPUS_OK entries={n}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
