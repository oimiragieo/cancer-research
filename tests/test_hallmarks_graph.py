"""Bidirectional tests for hallmarks_graph.driver_targets and coverage_matrix."""

from __future__ import annotations

import unittest

from algorithms.hallmarks_graph import (
    DRIVER_EDGES,
    HALLMARKS,
    INTERVENTION_EDGES,
    coverage_matrix,
    driver_targets,
    intervention_targets,
    uncovered,
)


class TestDriverTargets(unittest.TestCase):
    def test_known_driver_returns_nonempty_hallmarks(self) -> None:
        """Positive control: every DRIVER_EDGES key must resolve to known hallmarks."""
        hallmark_ids = {h.id for h in HALLMARKS}
        self.assertGreater(len(DRIVER_EDGES), 0)
        for driver, expected in DRIVER_EDGES.items():
            got = driver_targets(driver)
            self.assertEqual(got, list(expected))
            self.assertTrue(got, f"{driver} must have >=1 target")
            for hid in got:
                self.assertIn(hid, hallmark_ids)

    def test_unknown_driver_returns_empty(self) -> None:
        """Negative control: miss must be distinguishable from hit (empty list)."""
        self.assertEqual(driver_targets("not_a_real_driver_xyz"), [])
        self.assertEqual(driver_targets(""), [])

    def test_galectin3_covers_inflammation_and_intercellular(self) -> None:
        """Wake #74: Gal-3 driver must hit inflammation + intercellular (Suninflam L3 map)."""
        targets = driver_targets("galectin3")
        self.assertIn("inflammation", targets)
        self.assertIn("intercellular", targets)
        self.assertIn("loss_of_proteostasis", targets)
        # Coverage: each target hallmark must list an L3-capable stack layer
        by_id = {h.id: h for h in HALLMARKS}
        for hid in targets:
            layers = by_id[hid].stack_layers
            self.assertTrue(
                any(L in layers for L in ("L1", "L3")),
                f"{hid} from galectin3 lacks L1/L3 stack coverage: {layers}",
            )
        # Negative: unknown galectin key must miss
        self.assertEqual(driver_targets("galectin9_fake"), [])

    def test_mutating_returned_list_does_not_mutate_edges(self) -> None:
        """Bidirectional isolation: callers get a copy, not the tuple/list store."""
        before = list(DRIVER_EDGES["galectin3"])
        got = driver_targets("galectin3")
        got.append("should_not_persist")
        self.assertEqual(list(DRIVER_EDGES["galectin3"]), before)
        self.assertEqual(driver_targets("galectin3"), before)


class TestCoverageMatrix(unittest.TestCase):
    def test_every_hallmark_appears_under_its_stack_layers(self) -> None:
        """Positive: coverage_matrix is the inverse of Hallmark.stack_layers."""
        m = coverage_matrix()
        self.assertTrue(m)
        for h in HALLMARKS:
            for layer in h.stack_layers:
                self.assertIn(layer, m)
                self.assertIn(h.id, m[layer])

    def test_unknown_layer_absent(self) -> None:
        """Negative: fake layer must not appear (empty miss vs hit)."""
        self.assertNotIn("L99", coverage_matrix())

    def test_mutating_matrix_lists_does_not_corrupt_rerun(self) -> None:
        """Bidirectional: mutating returned lists must not poison next call."""
        m1 = coverage_matrix()
        layer = next(iter(m1))
        before = list(m1[layer])
        m1[layer].append("should_not_persist")
        m2 = coverage_matrix()
        self.assertEqual(m2[layer], before)

    def test_uncovered_seeds_subset_of_hallmarks(self) -> None:
        ids = {h.id for h in HALLMARKS}
        for u in uncovered():
            self.assertIn(u, ids)

    def test_uncovered_matches_predicate_exactly(self) -> None:
        """Bidirectional: uncovered() must equal the documented filter, no more/less."""
        seed_ids = {"dysbiosis", "telomere_attrition"}
        expected = [
            h.id
            for h in HALLMARKS
            if len(h.stack_layers) < 2 and h.id in seed_ids
        ]
        self.assertEqual(uncovered(), expected)

    def test_uncovered_includes_dysbiosis_excludes_multilayer_telomere(self) -> None:
        """Positive + negative: dysbiosis is weak; telomere has 3 layers so not a seed."""
        u = uncovered()
        self.assertIn("dysbiosis", u)
        self.assertNotIn("telomere_attrition", u)
        self.assertNotIn("genomic_instability", u)
        # Control: single-layer nutrient sensing is intentionally not in seed set
        self.assertNotIn("deregulated_nutrient", u)


class TestInterventionEdges(unittest.TestCase):
    def test_l1_dysbiosis_interventions_resolve(self) -> None:
        """Positive: fiber/polyphenol/abx-avoid map to dysbiosis without fake L2 coverage."""
        hallmark_ids = {h.id for h in HALLMARKS}
        self.assertGreater(len(INTERVENTION_EDGES), 0)
        for name, expected in INTERVENTION_EDGES.items():
            got = intervention_targets(name)
            self.assertEqual(got, list(expected))
            for hid in got:
                self.assertIn(hid, hallmark_ids)
        self.assertIn("dysbiosis", intervention_targets("fiber_prebiotic"))
        self.assertIn("dysbiosis", intervention_targets("polyphenol_diet"))
        self.assertEqual(intervention_targets("avoid_chronic_abx"), ["dysbiosis"])

    def test_unknown_intervention_empty(self) -> None:
        """Negative: miss must be empty, not a default hallmark."""
        self.assertEqual(intervention_targets("not_a_real_intervention_xyz"), [])

    def test_intervention_edges_do_not_clear_uncovered_dysbiosis(self) -> None:
        """Control: naming L1 levers must not pretend dysbiosis has multi-layer stack."""
        self.assertIn("dysbiosis", uncovered())
        dys = next(h for h in HALLMARKS if h.id == "dysbiosis")
        self.assertEqual(dys.stack_layers, ("L1",))

    def test_l3_clinical_modalities_map_without_clearing_dysbiosis(self) -> None:
        """Wake #77/#78: L3 clinical edges hit hallmarks; dysbiosis stays uncovered."""
        msc = intervention_targets("laromestrocel_msc")
        self.assertEqual(msc, ["stem_cell", "inflammation", "intercellular"])
        udp = intervention_targets("udp003_7kc_clearance")
        self.assertEqual(udp, ["mitochondrial", "inflammation", "intercellular"])
        sif = intervention_targets("sif001_gal3_mab")
        self.assertEqual(sif, ["inflammation", "intercellular", "loss_of_proteostasis"])
        # Align with DRIVER_EDGES galectin3 (same hallmark set)
        self.assertEqual(set(sif), set(driver_targets("galectin3")))
        ela = intervention_targets("elamipretide_mito")
        self.assertEqual(ela, ["mitochondrial", "stem_cell", "inflammation"])
        vital = intervention_targets("vital_h_triad")
        self.assertEqual(vital, ["deregulated_nutrient", "inflammation", "mitochondrial"])
        goda = intervention_targets("goda_super_exosome")
        self.assertEqual(goda, ["cellular_senescence", "stem_cell", "inflammation"])
        mini = intervention_targets("minicircle_fst_klotho")
        self.assertEqual(mini, ["stem_cell", "intercellular", "inflammation"])
        nyc = intervention_targets("nyc_vita_combo")
        self.assertEqual(nyc, ["deregulated_nutrient", "inflammation", "mitochondrial"])
        gi = intervention_targets("gi102_gib7")
        self.assertEqual(gi, ["inflammation", "dysbiosis", "stem_cell"])
        prog = intervention_targets("progerinin")
        self.assertEqual(prog, ["epigenetic_alterations", "genomic_instability", "stem_cell"])
        self.assertEqual(set(prog), set(driver_targets("nuclear_envelope")))
        lns = intervention_targets("lns8801_gper")
        self.assertEqual(lns, ["inflammation", "mitochondrial", "deregulated_nutrient"])
        # Naming a dysbiosis lever must not clear uncovered() (same rule as L1 fiber)
        self.assertIn("dysbiosis", uncovered())
        self.assertEqual(intervention_targets("laromestrocel_fake"), [])


if __name__ == "__main__":
    unittest.main()
