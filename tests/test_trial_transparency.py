"""Bidirectional tests for geroscience trial transparency and evidence maturity auditor."""

from __future__ import annotations

import datetime
import unittest

from algorithms.trial_transparency import (
    BENCHMARK_TRIALS,
    EvidenceTier,
    audit_transparency,
    calculate_evidence_delay_months,
)


class TestTrialTransparency(unittest.TestCase):
    def test_benchmark_trials_populated_and_valid(self) -> None:
        """Positive: benchmark trial list contains key geroscience translational studies."""
        self.assertGreater(len(BENCHMARK_TRIALS), 5)
        ids = [t.id for t in BENCHMARK_TRIALS]
        self.assertIn("NCT05835999", ids)  # EVERLAST
        self.assertIn("VITAL-H", ids)  # VITAL-H
        self.assertIn("NCT07275424", ids)  # SHAPE
        self.assertIn("NCT07290244", ids)  # ER-100

    def test_evidence_delay_calculation(self) -> None:
        """Positive: calculates correct elapsed months since completion date."""
        as_of = datetime.date(2026, 8, 23)
        # Completed Jul 22, 2026 -> ~1 month
        delay_1mo = calculate_evidence_delay_months("2026-07-22", as_of_date=as_of)
        self.assertGreaterEqual(delay_1mo, 0.9)
        self.assertLessEqual(delay_1mo, 1.2)

        # Completed Dec 31, 2025 -> ~7.7 months
        delay_8mo = calculate_evidence_delay_months("2025-12-31", as_of_date=as_of)
        self.assertGreaterEqual(delay_8mo, 7.0)
        self.assertLessEqual(delay_8mo, 8.5)

        # None / invalid date returns 0.0
        self.assertEqual(calculate_evidence_delay_months(None), 0.0)
        self.assertEqual(calculate_evidence_delay_months(""), 0.0)

    def test_transparency_audit_detects_completed_without_results(self) -> None:
        """Positive: audit identifies EVERLAST and TIME TRAVELER as completed without results."""
        report = audit_transparency()
        self.assertGreater(report.total_trials, 0)
        self.assertGreater(report.completed_trials, 0)
        self.assertGreater(report.completed_without_results, 0)
        self.assertLess(
            report.transparency_rate, 100.0
        )  # Cannot be 100% while EVERLAST has no results
        self.assertGreater(report.average_delay_months_for_completed, 0.0)

        # Undisclosed list must include EVERLAST
        undisclosed_text = " ".join(report.undisclosed_completed_list)
        self.assertIn("NCT05835999", undisclosed_text)

    def test_tier_distribution_counts_all_four_tiers(self) -> None:
        """Positive: tier distribution accounts for all trial records."""
        report = audit_transparency()
        total_in_dist = sum(report.tier_distribution.values())
        self.assertEqual(total_in_dist, report.total_trials)
        self.assertIn(EvidenceTier.TIER_3_BIOMARKER_IC_DOMAIN.value, report.tier_distribution)


if __name__ == "__main__":
    unittest.main()
