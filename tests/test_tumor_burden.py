"""Tests for tumor_burden dual-target design claim."""

from __future__ import annotations

import unittest

from algorithms.tumor_burden import Params, POLICIES, simulate, summary


class TestTumorBurden(unittest.TestCase):
    def test_untreated_grows(self) -> None:
        s = summary(simulate(Params(months=24, clearance=0.0, growth=0.1)))
        self.assertGreater(s["final_burden"], 1.0)

    def test_dual_beats_mono_final_burden(self) -> None:
        mono = summary(simulate(POLICIES["mono_target"]))
        dual = summary(simulate(POLICIES["dual_target"]))
        self.assertLess(dual["final_burden"], mono["final_burden"])

    def test_dual_lower_resistant_frac(self) -> None:
        mono = summary(simulate(POLICIES["mono_target"]))
        dual = summary(simulate(POLICIES["dual_target"]))
        self.assertLessEqual(dual["final_resistant_frac"], mono["final_resistant_frac"])


if __name__ == "__main__":
    unittest.main()
