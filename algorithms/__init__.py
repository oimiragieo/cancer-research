"""Algorithms package for longevity research, damage modeling, and geroscience translation."""

from __future__ import annotations

from algorithms.damage_control import Params, compare_policies, simulate
from algorithms.hallmarks_graph import (
    DRIVER_EDGES,
    HALLMARKS,
    INTERVENTION_EDGES,
    Hallmark,
    coverage_matrix,
    driver_targets,
    intervention_targets,
    uncovered,
)
from algorithms.portfolio_optimizer import (
    CocktailEvaluation,
    driver_impact_analysis,
    evaluate_cocktail,
    optimize_minimal_cocktail,
)
from algorithms.saturating_removal import (
    SPECIES_PRESETS,
    SimulationResult,
    SpeciesParameters,
    classify_regime,
    compare_intervention_paradigms,
    simulate_sr,
)
from algorithms.trial_transparency import (
    BENCHMARK_TRIALS,
    EvidenceTier,
    TransparencyAuditReport,
    TrialRecord,
    audit_transparency,
    calculate_evidence_delay_months,
)

__all__ = [
    "Params",
    "simulate",
    "compare_policies",
    "Hallmark",
    "HALLMARKS",
    "DRIVER_EDGES",
    "INTERVENTION_EDGES",
    "coverage_matrix",
    "driver_targets",
    "intervention_targets",
    "uncovered",
    "SpeciesParameters",
    "SPECIES_PRESETS",
    "SimulationResult",
    "simulate_sr",
    "classify_regime",
    "compare_intervention_paradigms",
    "CocktailEvaluation",
    "evaluate_cocktail",
    "optimize_minimal_cocktail",
    "driver_impact_analysis",
    "EvidenceTier",
    "TrialRecord",
    "BENCHMARK_TRIALS",
    "TransparencyAuditReport",
    "calculate_evidence_delay_months",
    "audit_transparency",
]
