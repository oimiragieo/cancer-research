"""Bidirectional tests for age-phased repair_a in damage_control."""

from __future__ import annotations

import unittest

from algorithms.damage_control import Params, repair_a_at, simulate


class TestRepairAPhased(unittest.TestCase):
    def test_empty_schedule_matches_constant(self) -> None:
        """Control: empty schedule must equal constant repair_a at every year."""
        p = Params(years=50, repair_a=0.05, repair_a_schedule=())
        for t in (0, 25, 50):
            self.assertEqual(repair_a_at(t, p), 0.05)

    def test_schedule_windows_apply(self) -> None:
        p = Params(
            years=100,
            repair_a=0.99,  # must be ignored when schedule is set
            repair_a_schedule=((40, 70, 0.08),),
        )
        self.assertEqual(repair_a_at(39, p), 0.0)
        self.assertEqual(repair_a_at(40, p), 0.08)
        self.assertEqual(repair_a_at(69, p), 0.08)
        self.assertEqual(repair_a_at(70, p), 0.0)

    def test_midlife_pulse_differs_from_constant_high(self) -> None:
        """Treatment vs continuous high RA: final D must not be identical."""
        years = 100
        continuous = Params(years=years, repair_a=0.09, repair_b=0.0, derisk=True)
        pulsed = Params(
            years=years,
            repair_a=0.0,
            repair_b=0.0,
            derisk=True,
            repair_a_schedule=((40, 70, 0.09),),
        )
        d_cont = simulate(continuous)[-1].d
        d_pulse = simulate(pulsed)[-1].d
        self.assertNotAlmostEqual(d_cont, d_pulse, places=6)
        # Pulse misses early accumulation -> worse (higher) final D than continuous
        self.assertGreater(d_pulse, d_cont)

    def test_zero_repair_schedule_is_worse_than_baseline_ra(self) -> None:
        """Bidirectional: a schedule that zeros all RA must raise final D vs baseline."""
        years = 80
        baseline = Params(years=years, repair_a=0.04, repair_b=0.0, derisk=True)
        zeroed = Params(
            years=years,
            repair_a=0.04,
            repair_b=0.0,
            derisk=True,
            repair_a_schedule=((0, years + 1, 0.0),),
        )
        self.assertGreater(simulate(zeroed)[-1].d, simulate(baseline)[-1].d)

    def test_states_record_repair_a_used(self) -> None:
        p = Params(years=5, repair_a=0.0, repair_a_schedule=((2, 4, 0.07),))
        states = simulate(p)
        self.assertEqual(states[1].repair_a_used, 0.0)
        self.assertEqual(states[2].repair_a_used, 0.07)
        self.assertEqual(states[4].repair_a_used, 0.0)


class TestImmortalityStackOracle(unittest.TestCase):
    def test_immortality_stack_bounded_pin(self) -> None:
        """Wake #75: default immortality_stack must stay bounded with pinned final D."""
        from algorithms.damage_control import compare_policies

        report = compare_policies(120)
        stack = report["immortality_stack"]
        self.assertTrue(stack["bounded"])
        self.assertIsNone(stack["morbidity_year"])
        self.assertAlmostEqual(stack["final_D"], 0.147059, places=5)
        # Bidirectional: natural and repair_only_A must NOT be bounded
        self.assertFalse(report["natural"]["bounded"])
        self.assertFalse(report["repair_only_A"]["bounded"])
        self.assertIsNotNone(report["natural"]["morbidity_year"])


if __name__ == "__main__":
    unittest.main()
