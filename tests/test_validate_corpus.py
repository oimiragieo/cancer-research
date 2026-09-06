"""TDD: corpus schema + unique-id gate (deterministic; no clinical invention)."""

from __future__ import annotations

import textwrap
from pathlib import Path

import pytest
import yaml
from scripts.validate_corpus import ValidationError, validate_sources


def test_empty_sources_fails() -> None:
    with pytest.raises(ValidationError, match="empty"):
        validate_sources([])


def test_missing_required_field_fails() -> None:
    with pytest.raises(ValidationError, match="id"):
        validate_sources([{"title": "x", "url": "https://example.com", "year": 2026}])


def test_duplicate_id_fails() -> None:
    row = {
        "id": "dup-a",
        "title": "t",
        "url": "https://example.com/a",
        "year": 2026,
        "topics": ["clinical"],
        "confidence": "high",
        "summary": "ok",
    }
    with pytest.raises(ValidationError, match="duplicate"):
        validate_sources([row, {**row, "url": "https://example.com/b"}])


def test_valid_minimal_passes() -> None:
    n = validate_sources(
        [
            {
                "id": "ok-1",
                "title": "Valid entry",
                "url": "https://example.com",
                "year": 2026,
                "topics": ["clinical"],
                "confidence": "high",
                "summary": "A valid summary.",
            }
        ]
    )
    assert n == 1


def test_fixture_yaml_roundtrip(tmp_path: Path) -> None:
    fixture = tmp_path / "sources.yaml"
    fixture.write_text(
        textwrap.dedent(
            """\
            sources:
            - id: fixture-1
              title: Fixture
              url: https://example.com/f
              year: 2026
              topics:
              - preclinical
              confidence: medium
              summary: Fixture summary without colon issues.
            """
        ),
        encoding="utf-8",
    )
    data = yaml.safe_load(fixture.read_text(encoding="utf-8"))
    assert validate_sources(data["sources"]) == 1
