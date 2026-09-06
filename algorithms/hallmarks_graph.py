"""Hallmarks-of-aging intervention graph (static knowledge structure)."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Hallmark:
    id: str
    name: str
    layer: str  # primary | antagonistic | integrative
    stack_layers: tuple[str, ...]


HALLMARKS: list[Hallmark] = [
    Hallmark("genomic_instability", "Genomic instability", "primary", ("L2", "L5")),
    Hallmark("telomere_attrition", "Telomere attrition", "primary", ("L2", "L4", "L6")),
    Hallmark("epigenetic_alterations", "Epigenetic alterations", "primary", ("L4", "L5")),
    Hallmark("loss_of_proteostasis", "Loss of proteostasis", "primary", ("L1", "L2")),
    Hallmark("disabled_autophagy", "Disabled macroautophagy", "primary", ("L1", "L2")),
    Hallmark("deregulated_nutrient", "Deregulated nutrient sensing", "antagonistic", ("L1",)),
    Hallmark("mitochondrial", "Mitochondrial dysfunction", "antagonistic", ("L1", "L2")),
    Hallmark("cellular_senescence", "Cellular senescence", "antagonistic", ("L3",)),
    Hallmark("stem_cell", "Stem cell exhaustion", "integrative", ("L4", "L6")),
    Hallmark("intercellular", "Altered intercellular communication", "integrative", ("L3",)),
    Hallmark("inflammation", "Chronic inflammation", "integrative", ("L1", "L3")),
    Hallmark("dysbiosis", "Dysbiosis", "integrative", ("L1",)),
]


# Mechanistic drivers -> hallmarks they feed (Ralph wake #48).
# Edges inform L1/L3 target priority; not a full systems biology model.
DRIVER_EDGES: dict[str, tuple[str, ...]] = {
    "line1_rt": ("genomic_instability", "inflammation", "cellular_senescence"),
    "galectin3": ("inflammation", "intercellular", "loss_of_proteostasis"),
    "7kc": ("mitochondrial", "inflammation", "intercellular"),
    "bclxl_senescent": ("cellular_senescence",),
    "mtorc1": ("deregulated_nutrient", "disabled_autophagy", "stem_cell"),
    "nuclear_envelope": ("epigenetic_alterations", "genomic_instability", "stem_cell"),
    "ccl11": ("inflammation", "stem_cell", "intercellular"),
    "b2m": ("stem_cell", "intercellular"),
}

# Intervention levers -> hallmarks they primarily address (Ralph wake #66 L1;
# wake #77 adds L3 clinical modalities). These do NOT upgrade stack coverage;
# dysbiosis remains an uncovered() seed until a second stack layer is earned
# by evidence (not by renaming L1).
INTERVENTION_EDGES: dict[str, tuple[str, ...]] = {
    "fiber_prebiotic": ("dysbiosis", "inflammation"),
    "polyphenol_diet": ("dysbiosis", "inflammation"),
    "avoid_chronic_abx": ("dysbiosis",),
    "caloric_patterning": ("deregulated_nutrient", "dysbiosis"),
    # L3 clinical modalities (human dose-finding; not Finals protocol claims)
    "laromestrocel_msc": ("stem_cell", "inflammation", "intercellular"),
    "udp003_7kc_clearance": ("mitochondrial", "inflammation", "intercellular"),
    "sif001_gal3_mab": ("inflammation", "intercellular", "loss_of_proteostasis"),
    "elamipretide_mito": ("mitochondrial", "stem_cell", "inflammation"),
    "vital_h_triad": ("deregulated_nutrient", "inflammation", "mitochondrial"),
    "goda_super_exosome": ("cellular_senescence", "stem_cell", "inflammation"),
    "minicircle_fst_klotho": ("stem_cell", "intercellular", "inflammation"),
    "nyc_vita_combo": ("deregulated_nutrient", "inflammation", "mitochondrial"),
    # GI-102 0.02 mg/kg + GIB-7 ~5e8 CFU/day synbiotic
    "gi102_gib7": ("inflammation", "dysbiosis", "stem_cell"),
    # HGPS/progerin binder (PRG); aligns with nuclear_envelope DRIVER_EDGES targets
    "progerinin": ("epigenetic_alterations", "genomic_instability", "stem_cell"),
    # Oral selective GPER agonist (oncology RP2D 125 mg QD; PROSPR/ITP dose TBD)
    "lns8801_gper": ("inflammation", "mitochondrial", "deregulated_nutrient"),
}


def coverage_matrix() -> dict[str, list[str]]:
    m: dict[str, list[str]] = {}
    for h in HALLMARKS:
        for layer in h.stack_layers:
            m.setdefault(layer, []).append(h.id)
    return m


def driver_targets(driver: str) -> list[str]:
    return list(DRIVER_EDGES.get(driver, ()))


def intervention_targets(intervention: str) -> list[str]:
    return list(INTERVENTION_EDGES.get(intervention, ()))


def uncovered() -> list[str]:
    """Hallmarks with only weak stack coverage - research backlog seeds.

    Seed candidates are dysbiosis and telomere_attrition, but only those with
    fewer than 2 stack layers qualify. Today that means dysbiosis alone
    (telomere_attrition maps to L2/L4/L6).
    """
    seed_ids = {"dysbiosis", "telomere_attrition"}
    weak = []
    for h in HALLMARKS:
        if len(h.stack_layers) < 2 and h.id in seed_ids:
            weak.append(h.id)
    return weak


if __name__ == "__main__":
    print("Stack layer -> hallmarks")
    for layer, ids in sorted(coverage_matrix().items()):
        print(f"  {layer}: {', '.join(ids)}")
    print("Weak coverage seeds:", uncovered())
    print("Driver edges:")
    for driver, targets in sorted(DRIVER_EDGES.items()):
        print(f"  {driver} -> {', '.join(targets)}")
    print("L1 intervention edges:")
    for intervention, targets in sorted(INTERVENTION_EDGES.items()):
        print(f"  {intervention} -> {', '.join(targets)}")
