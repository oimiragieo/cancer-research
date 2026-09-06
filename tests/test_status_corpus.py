"""Bidirectional tests for status.corpus_count / corpus_ok gate (cancer-research)."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path
from unittest import mock

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from status import (  # noqa: E402
    CORPUS_FLOOR,
    CURE_EVIDENCE_MIN_FOLLOWUP_YEARS,
    SENTINEL_HARD_CANCERS,
    corpus_count,
    exit_criteria,
    load_sources,
)


class TestCorpusCountOracle(unittest.TestCase):
    def test_live_corpus_count_matches_yaml_len(self) -> None:
        sources = load_sources()
        self.assertGreaterEqual(len(sources), CORPUS_FLOOR)
        self.assertEqual(corpus_count(sources), len(sources))
        self.assertEqual(exit_criteria()["corpus_count"], len(sources))
        self.assertTrue(exit_criteria()["corpus_ok"])

    def test_empty_list_is_not_ok(self) -> None:
        self.assertEqual(corpus_count([]), 0)
        self.assertFalse(corpus_count([]) >= CORPUS_FLOOR)

    def test_under_threshold_fails_ok_gate(self) -> None:
        stub = [{"id": f"x{i}"} for i in range(CORPUS_FLOOR - 1)]
        self.assertEqual(corpus_count(stub), CORPUS_FLOOR - 1)
        self.assertFalse(corpus_count(stub) >= CORPUS_FLOOR)
        stub.append({"id": "x_floor"})
        self.assertTrue(corpus_count(stub) >= CORPUS_FLOOR)

    def test_corpus_floor_constant_is_fifty(self) -> None:
        self.assertEqual(CORPUS_FLOOR, 50)

    def test_cure_followup_floor_is_three_years(self) -> None:
        self.assertEqual(CURE_EVIDENCE_MIN_FOLLOWUP_YEARS, 3)
        self.assertIn("PDAC", SENTINEL_HARD_CANCERS)
        self.assertIn("GBM", SENTINEL_HARD_CANCERS)
        self.assertIn("mTNBC", SENTINEL_HARD_CANCERS)

    def test_exit_criteria_corpus_ok_false_when_sources_empty(self) -> None:
        import status as status_mod

        with mock.patch.object(status_mod, "load_sources", return_value=[]):
            c = status_mod.exit_criteria()
        self.assertEqual(c["corpus_count"], 0)
        self.assertFalse(c["corpus_ok"])
        self.assertFalse(c["goal_met"])

    def test_goal_met_false_when_deferred_empty(self) -> None:
        import status as status_mod

        live = status_mod.exit_criteria()
        self.assertGreaterEqual(live["deferred_gaps"], 1)
        self.assertTrue(live["goal_met"])

        empty_register = {
            "open": [],
            "deferred_with_evidence": [],
            "closed": [],
        }

        real_read = status_mod.Path.read_text

        def fake_read(self, *args, **kwargs):
            if self.name == "gap_register.json":
                return status_mod.json.dumps(empty_register)
            return real_read(self, *args, **kwargs)

        with mock.patch.object(status_mod.Path, "read_text", fake_read):
            c = status_mod.exit_criteria()
        self.assertEqual(c["deferred_gaps"], 0)
        self.assertFalse(c["goal_met"])

    def test_oncology_artifacts_required(self) -> None:
        c = exit_criteria()
        self.assertTrue(c["ultra_design"])
        self.assertTrue(c["medicine_pipeline"])
        self.assertTrue(c["algorithms"])
        self.assertTrue(c["oncogenic_driver_catalog"])


if __name__ == "__main__":
    unittest.main()
