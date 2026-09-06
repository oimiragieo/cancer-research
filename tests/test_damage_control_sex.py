"""Bidirectional tests for sex-specific clearance in damage_control."""

from __future__ import annotations

import unittest

from algorithms.damage_control import Params, clearance_mult, effective_repair_a, simulate


class TestSexClearance(unittest.TestCase):
    def test_unspecified_sex_is_identity(self) -> None:
        p = Params(years=40, repair_a=0.06, sex="")
        for t in (0, 20, 40):
            self.assertEqual(clearance_mult(t, p), 1.0)
            self.assertEqual(effective_repair_a(t, p), 0.06)

    def test_default_sex_mults_match_unspecified_trajectory(self) -> None:
        """Control: male/female with identity mults must match sex=''."""
        years = 60
        base = Params(years=years, repair_a=0.05, repair_b=0.0, derisk=True, sex="")
        male = Params(
            years=years,
            repair_a=0.05,
            repair_b=0.0,
            derisk=True,
            sex="male",
            sex_clearance_male=1.0,
        )
        female = Params(
            years=years,
            repair_a=0.05,
            repair_b=0.0,
            derisk=True,
            sex="female",
            sex_clearance_female=1.0,
        )
        d0 = simulate(base)[-1].d
        self.assertAlmostEqual(simulate(male)[-1].d, d0, places=9)
        self.assertAlmostEqual(simulate(female)[-1].d, d0, places=9)

    def test_female_late_toxicity_worsens_final_d(self) -> None:
        """Treatment: late female clearance collapse must raise final D vs male."""
        years = 100
        male = Params(
            years=years,
            repair_a=0.09,
            repair_b=0.0,
            derisk=True,
            sex="male",
            sex_clearance_male=1.0,
        )
        female = Params(
            years=years,
            repair_a=0.09,
            repair_b=0.0,
            derisk=True,
            sex="female",
            sex_clearance_female=1.0,
            female_late_toxicity_start=60,
            female_late_clearance_mult=0.05,
        )
        self.assertEqual(clearance_mult(59, female), 1.0)
        self.assertEqual(clearance_mult(60, female), 0.05)
        self.assertGreater(simulate(female)[-1].d, simulate(male)[-1].d)

    def test_removing_late_toxicity_removes_sex_gap(self) -> None:
        """Bidirectional: same params without late window must not diverge."""
        years = 100
        male = Params(
            years=years,
            repair_a=0.09,
            repair_b=0.0,
            derisk=True,
            sex="male",
            sex_clearance_male=1.0,
        )
        female_no_tox = Params(
            years=years,
            repair_a=0.09,
            repair_b=0.0,
            derisk=True,
            sex="female",
            sex_clearance_female=1.0,
            female_late_toxicity_start=None,
            female_late_clearance_mult=0.05,
        )
        self.assertAlmostEqual(
            simulate(male)[-1].d, simulate(female_no_tox)[-1].d, places=9
        )

    def test_midlife_pulse_plus_cana_sex_diverges(self) -> None:
        """Combined schedule+sex: female late tox must worsen vs male twin."""
        years = 100
        male = Params(
            years=years,
            repair_a=0.0,
            repair_b=0.0,
            derisk=True,
            repair_a_schedule=((40, 70, 0.09),),
            sex="male",
            sex_clearance_male=1.0,
        )
        female = Params(
            years=years,
            repair_a=0.0,
            repair_b=0.0,
            derisk=True,
            repair_a_schedule=((40, 70, 0.09),),
            sex="female",
            sex_clearance_female=1.0,
            female_late_toxicity_start=60,
            female_late_clearance_mult=0.05,
        )
        self.assertGreater(simulate(female)[-1].d, simulate(male)[-1].d)

    def test_immortality_stack_sex_split_still_diverges(self) -> None:
        """Even high RA+RB stack: late female tox must raise final D vs male twin."""
        years = 120
        male = Params(
            years=years,
            repair_a=0.12,
            repair_b=0.08,
            derisk=True,
            sex="male",
            sex_clearance_male=1.0,
        )
        female = Params(
            years=years,
            repair_a=0.12,
            repair_b=0.08,
            derisk=True,
            sex="female",
            sex_clearance_female=1.0,
            female_late_toxicity_start=60,
            female_late_clearance_mult=0.05,
        )
        d_m = simulate(male)[-1].d
        d_f = simulate(female)[-1].d
        self.assertGreater(d_f, d_m)
        # Control: identity female (no late tox) must match male
        female_id = Params(
            years=years,
            repair_a=0.12,
            repair_b=0.08,
            derisk=True,
            sex="female",
            sex_clearance_female=1.0,
        )
        self.assertAlmostEqual(simulate(female_id)[-1].d, d_m, places=9)

    def test_derisk_then_repair_sex_split(self) -> None:
        """Wake #64: derisk-first policy must still diverge under late female tox."""
        years = 120
        male = Params(
            years=years,
            repair_a=0.09,
            repair_b=0.05,
            derisk=True,
            sex="male",
            sex_clearance_male=1.0,
        )
        female = Params(
            years=years,
            repair_a=0.09,
            repair_b=0.05,
            derisk=True,
            sex="female",
            sex_clearance_female=1.0,
            female_late_toxicity_start=60,
            female_late_clearance_mult=0.05,
        )
        d_m = simulate(male)[-1].d
        d_f = simulate(female)[-1].d
        self.assertGreater(d_f, d_m)
        # Control: identity female matches male; derisk must keep B expand off
        female_id = Params(
            years=years,
            repair_a=0.09,
            repair_b=0.05,
            derisk=True,
            sex="female",
            sex_clearance_female=1.0,
        )
        self.assertAlmostEqual(simulate(female_id)[-1].d, d_m, places=9)
        # Positive: without derisk, final B rises vs derisk twin (same RA/RB)
        no_derisk = Params(
            years=years,
            repair_a=0.09,
            repair_b=0.05,
            derisk=False,
            sex="male",
            sex_clearance_male=1.0,
        )
        self.assertGreater(simulate(no_derisk)[-1].b, simulate(male)[-1].b)

    def test_midlife_pulse_sex_split_morbidity_years(self) -> None:
        """Wake #68: midlife RA pulse + late female tox -> earlier morbidity than male twin."""
        years = 120
        sched = ((0, 40, 0.05), (40, 70, 0.09), (70, 200, 0.05))
        male = Params(
            years=years,
            repair_a=0.0,
            repair_b=0.004,
            derisk=False,
            repair_a_schedule=sched,
            sex="male",
            sex_clearance_male=1.0,
        )
        female = Params(
            years=years,
            repair_a=0.0,
            repair_b=0.004,
            derisk=False,
            repair_a_schedule=sched,
            sex="female",
            sex_clearance_female=1.0,
            female_late_toxicity_start=60,
            female_late_clearance_mult=0.05,
        )
        hit_m = next((s.t for s in simulate(male) if s.morbidity_hit), None)
        hit_f = next((s.t for s in simulate(female) if s.morbidity_hit), None)
        self.assertIsNotNone(hit_m)
        self.assertIsNotNone(hit_f)
        assert hit_m is not None and hit_f is not None
        self.assertGreater(hit_m, 60)  # past late-tox start so sex can matter
        self.assertLess(hit_f, hit_m)
        # Control: identity female matches male morbidity year
        female_id = Params(
            years=years,
            repair_a=0.0,
            repair_b=0.004,
            derisk=False,
            repair_a_schedule=sched,
            sex="female",
            sex_clearance_female=1.0,
        )
        hit_id = next((s.t for s in simulate(female_id) if s.morbidity_hit), None)
        self.assertEqual(hit_id, hit_m)


if __name__ == "__main__":
    unittest.main()
