"""Bidirectional tests for portfolio optimizer and cocktail synergy evaluator."""

from __future__ import annotations

import unittest

from algorithms.portfolio_optimizer import (
    driver_impact_analysis,
    evaluate_cocktail,
    get_all_hallmark_ids,
    optimize_minimal_cocktail,
)


class TestPortfolioOptimizer(unittest.TestCase):
    def test_single_intervention_evaluation(self) -> None:
        """Positive: evaluating vital_h_triad yields proper coverage metrics."""
        eval_res = evaluate_cocktail(["vital_h_triad"])
        self.assertEqual(eval_res.interventions, ["vital_h_triad"])
        self.assertIn("deregulated_nutrient", eval_res.covered_hallmarks)
        self.assertIn("inflammation", eval_res.covered_hallmarks)
        self.assertIn("mitochondrial", eval_res.covered_hallmarks)
        self.assertGreater(eval_res.coverage_percentage, 0.0)
        self.assertEqual(eval_res.redundancy_index, 0.0)  # Single intervention = 0 redundancy
        self.assertEqual(eval_res.synergy_score, 3.0)  # 3 distinct hallmarks

    def test_multi_agent_cocktail_synergy_and_redundancy(self) -> None:
        """Positive: multi-agent cocktail covers higher percentage of hallmarks."""
        cocktail = ["vital_h_triad", "laromestrocel_msc", "sif001_gal3_mab", "progerinin"]
        eval_res = evaluate_cocktail(cocktail)
        self.assertGreaterEqual(eval_res.coverage_percentage, 50.0)
        self.assertIn("L1", eval_res.stack_layers_active)
        self.assertIn("L3", eval_res.stack_layers_active)
        self.assertIn("L4", eval_res.stack_layers_active)
        self.assertIn("L5", eval_res.stack_layers_active)
        self.assertGreaterEqual(eval_res.tier_breakdown["primary"], 1)
        self.assertGreaterEqual(eval_res.tier_breakdown["antagonistic"], 1)
        self.assertGreaterEqual(eval_res.tier_breakdown["integrative"], 1)
        self.assertGreater(eval_res.redundancy_index, 0.0)

    def test_empty_cocktail_returns_zero_coverage(self) -> None:
        """Negative control: empty intervention list produces 0% coverage and all uncovered."""
        all_ids = get_all_hallmark_ids()
        eval_res = evaluate_cocktail([])
        self.assertEqual(eval_res.coverage_percentage, 0.0)
        self.assertEqual(eval_res.covered_hallmarks, [])
        self.assertEqual(eval_res.uncovered_hallmarks, sorted(all_ids))
        self.assertEqual(eval_res.redundancy_index, 0.0)
        self.assertEqual(eval_res.synergy_score, 0.0)

    def test_optimization_finds_pareto_cocktails(self) -> None:
        """Positive: optimize_minimal_cocktail returns ranked non-empty solutions."""
        opts = optimize_minimal_cocktail(max_cocktail_size=3)
        self.assertGreater(len(opts), 0)
        best = opts[0]
        self.assertGreaterEqual(best.coverage_percentage, 40.0)
        self.assertLessEqual(len(best.interventions), 3)

    def test_driver_impact_analysis_ranks_known_drivers(self) -> None:
        """Positive: driver impact analysis ranks LINE-1, Galectin-3, 7KC, mTORC1."""
        impact = driver_impact_analysis()
        self.assertGreater(len(impact), 0)
        driver_names = [d["driver"] for d in impact]
        self.assertIn("line1_rt", driver_names)
        self.assertIn("galectin3", driver_names)
        self.assertIn("7kc", driver_names)
        self.assertIn("mtorc1", driver_names)
        # Top driver has positive centrality score
        self.assertGreater(impact[0]["centrality_score"], 0.0)


if __name__ == "__main__":
    unittest.main()
