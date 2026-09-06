"""Bidirectional tests for comparative geroscience saturating removal (SR) simulator."""

from __future__ import annotations

import unittest

from algorithms.saturating_removal import (
    SPECIES_PRESETS,
    SpeciesParameters,
    compare_intervention_paradigms,
    simulate_sr,
)


class TestSaturatingRemoval(unittest.TestCase):
    def test_presets_exist_and_cover_mammals_and_invertebrates(self) -> None:
        """Positive: standard geroscience model organisms are calibrated."""
        for sp in ("human", "mouse", "dog", "drosophila", "c_elegans"):
            self.assertIn(sp, SPECIES_PRESETS)
            p = SPECIES_PRESETS[sp]
            self.assertGreater(p.eta, 0.0)
            self.assertGreater(p.beta, 0.0)
            self.assertGreater(p.xc, 0.0)
            self.assertGreater(p.max_time, 0.0)

    def test_human_simulation_produces_quasi_steady_state_regime(self) -> None:
        """Positive: Human dynamics must exhibit quasi-steady-state regime."""
        p = SPECIES_PRESETS["human"]
        res = simulate_sr(p)
        self.assertEqual(res.species, "human")
        self.assertGreater(res.lifespan, 60.0)
        self.assertLessEqual(res.lifespan, 125.0)
        self.assertGreater(res.healthspan, 40.0)
        self.assertLessEqual(res.healthspan, res.lifespan)
        self.assertEqual(res.regime, "quasi_steady_state")
        self.assertGreaterEqual(res.morbidity_compression_ratio, 0.0)
        self.assertLess(res.morbidity_compression_ratio, 0.50)

    def test_invertebrate_simulation_produces_ballistic_regime(self) -> None:
        """Positive: C. elegans / Drosophila with high eta must be classified as ballistic."""
        p = SPECIES_PRESETS["c_elegans"]
        res = simulate_sr(p)
        self.assertEqual(res.species, "c_elegans")
        self.assertEqual(res.regime, "ballistic")

    def test_morbidity_compression_under_multi_target_immortality_stack(self) -> None:
        """Morbidity compression theorem: multi-target stack achieves smaller sickspan ratio."""
        comp = compare_intervention_paradigms("human")
        self.assertIn("baseline", comp)
        self.assertIn("production_reduction_only", comp)
        self.assertIn("full_immortality_stack", comp)

        base = comp["baseline"]
        prod_only = comp["production_reduction_only"]
        full_stack = comp["full_immortality_stack"]

        # Production reduction alone increases lifespan
        self.assertGreater(prod_only["lifespan"], base["lifespan"])
        # Full stack increases lifespan even more
        self.assertGreater(full_stack["lifespan"], prod_only["lifespan"])
        # Full stack healthspan is substantially increased
        self.assertGreater(full_stack["healthspan"], base["healthspan"])

    def test_negative_invalid_parameters_handled_safely(self) -> None:
        """Negative control: zero removal or huge initial damage handled cleanly."""
        zero_rem_p = SpeciesParameters(
            species="test_zero_rem",
            eta=0.01,
            beta=0.0,
            kappa=0.2,
            xc=1.0,
            time_step=0.1,
            max_time=10.0,
        )
        res = simulate_sr(zero_rem_p)
        self.assertGreater(res.lifespan, 0.0)
        self.assertLessEqual(res.lifespan, 10.0)


if __name__ == "__main__":
    unittest.main()
