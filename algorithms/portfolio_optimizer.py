"""Intervention portfolio optimizer and hallmark synergy analyzer.

Inspired by 2026 Network Medicine frameworks (Nature Aging 2026 SHARP) and the
6-layer longevity control architecture.

Provides:
1. Cocktail Hallmark Coverage: evaluates multi-hallmark targeting across primary,
   antagonistic, and integrative tiers.
2. Stack Layer Distribution: ensures balanced coverage across L1 (damage reduction),
   L2 (repair economy), L3 (clearance), L4 (reprogramming), L5 (information de-risking),
   and L6 (replacement).
3. Synergy & Redundancy Score: identifies synergistic orthogonal combinations versus
   redundant multi-agent stacking.
4. Minimal Optimal Cocktail Selector: solves the set-cover problem to find the smallest
   non-redundant intervention cocktail for maximum hallmark span.
5. Upstream Driver Impact Ranking: evaluates driver nodes (LINE-1, 7KC, Galectin-3, etc.)
   by downstream hallmark fan-out.
"""

from __future__ import annotations

import argparse
import itertools
import json
from dataclasses import asdict, dataclass

from algorithms.hallmarks_graph import (
    DRIVER_EDGES,
    HALLMARKS,
    INTERVENTION_EDGES,
    intervention_targets,
)


@dataclass
class CocktailEvaluation:
    interventions: list[str]
    covered_hallmarks: list[str]
    coverage_percentage: float  # Percentage of 12 canonical hallmarks covered
    tier_breakdown: dict[str, int]  # primary, antagonistic, integrative counts
    stack_layers_active: list[str]  # L1..L6 layers activated
    uncovered_hallmarks: list[str]
    redundancy_index: float  # 0.0 = completely orthogonal; 1.0 = completely overlapping
    synergy_score: float  # Distinct hallmarks per intervention unit
    has_uncovered_seed_risk: bool  # True if dysbiosis is untouched


def get_all_hallmark_ids() -> list[str]:
    return [h.id for h in HALLMARKS]


def get_hallmark_by_id(hid: str):
    for h in HALLMARKS:
        if h.id == hid:
            return h
    return None


def evaluate_cocktail(interventions: list[str]) -> CocktailEvaluation:
    """Evaluate a combinatorial intervention cocktail for hallmark coverage and synergy."""
    all_h = get_all_hallmark_ids()
    total_hallmarks = len(all_h)

    covered_set: set[str] = set()
    layer_set: set[str] = set()
    individual_targets: list[set[str]] = []

    for name in interventions:
        targets = set(intervention_targets(name))
        individual_targets.append(targets)
        covered_set.update(targets)

    # Calculate active stack layers from covered hallmarks
    for hid in covered_set:
        h_obj = get_hallmark_by_id(hid)
        if h_obj:
            layer_set.update(h_obj.stack_layers)

    tier_counts = {"primary": 0, "antagonistic": 0, "integrative": 0}
    for hid in covered_set:
        h_obj = get_hallmark_by_id(hid)
        if h_obj and h_obj.layer in tier_counts:
            tier_counts[h_obj.layer] += 1

    covered_list = sorted(covered_set)
    uncovered_list = sorted(set(all_h) - covered_set)
    coverage_pct = round((len(covered_list) / total_hallmarks) * 100, 1)

    # Redundancy calculation: average pairwise Jaccard overlap between interventions
    if len(interventions) > 1:
        pairwise_jaccard = []
        for t1, t2 in itertools.combinations(individual_targets, 2):
            union = t1.union(t2)
            inter = t1.intersection(t2)
            pairwise_jaccard.append(len(inter) / len(union) if union else 0.0)
        redundancy = round(sum(pairwise_jaccard) / len(pairwise_jaccard), 3)
    else:
        redundancy = 0.0

    # Synergy score: unique hallmarks covered per intervention count
    synergy = round(len(covered_list) / max(1, len(interventions)), 2)
    has_seed_risk = "dysbiosis" in uncovered_list

    return CocktailEvaluation(
        interventions=interventions,
        covered_hallmarks=covered_list,
        coverage_percentage=coverage_pct,
        tier_breakdown=tier_counts,
        stack_layers_active=sorted(layer_set),
        uncovered_hallmarks=uncovered_list,
        redundancy_index=redundancy,
        synergy_score=synergy,
        has_uncovered_seed_risk=has_seed_risk,
    )


def optimize_minimal_cocktail(
    max_cocktail_size: int = 4,
    preferred_interventions: list[str] | None = None,
) -> list[CocktailEvaluation]:
    """Find non-redundant minimal cocktails that maximize hallmark coverage."""
    available = list(INTERVENTION_EDGES.keys())
    if preferred_interventions:
        available = [i for i in available if i in preferred_interventions] or available

    candidates: list[CocktailEvaluation] = []

    for size in range(1, max_cocktail_size + 1):
        for combo in itertools.combinations(available, size):
            eval_res = evaluate_cocktail(list(combo))
            candidates.append(eval_res)

    # Rank: coverage desc, then redundancy asc, then smallest size
    candidates.sort(
        key=lambda c: (
            c.coverage_percentage,
            -c.redundancy_index,
            -len(c.interventions),
            c.synergy_score,
        ),
        reverse=True,
    )

    # Deduplicate by coverage signature to return the top diverse Pareto-optimal options
    seen_signatures: set[tuple[str, ...]] = set()
    pareto_top: list[CocktailEvaluation] = []

    for c in candidates:
        sig = tuple(sorted(c.covered_hallmarks))
        if sig not in seen_signatures:
            seen_signatures.add(sig)
            pareto_top.append(c)
        if len(pareto_top) >= 10:
            break

    return pareto_top


def driver_impact_analysis() -> list[dict]:
    """Rank upstream biological drivers by their downstream hallmark fan-out and tier impact."""
    impact = []
    for driver, targets in DRIVER_EDGES.items():
        tier_dist = {"primary": 0, "antagonistic": 0, "integrative": 0}
        for hid in targets:
            h_obj = get_hallmark_by_id(hid)
            if h_obj and h_obj.layer in tier_dist:
                tier_dist[h_obj.layer] += 1

        impact.append(
            {
                "driver": driver,
                "fan_out_count": len(targets),
                "targets": list(targets),
                "primary_count": tier_dist["primary"],
                "antagonistic_count": tier_dist["antagonistic"],
                "integrative_count": tier_dist["integrative"],
                "centrality_score": round(len(targets) + tier_dist["primary"] * 0.5, 2),
            }
        )

    impact.sort(key=lambda d: (d["centrality_score"], d["fan_out_count"]), reverse=True)
    return impact


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Intervention Portfolio Optimizer & Hallmark Synergy Analyzer"
    )
    parser.add_argument("--eval", nargs="+", help="Evaluate a specific list of interventions")
    parser.add_argument("--optimize", action="store_true", help="Compute minimal optimal cocktails")
    parser.add_argument(
        "--max-size", type=int, default=4, help="Maximum cocktail size for optimization"
    )
    parser.add_argument("--drivers", action="store_true", help="Rank upstream biological drivers")
    parser.add_argument("--json", action="store_true", help="Output JSON formatted results")
    args = parser.parse_args()

    if args.eval:
        res = evaluate_cocktail(args.eval)
        if args.json:
            print(json.dumps(asdict(res), indent=2))
        else:
            print("=== Cocktail Evaluation ===")
            print(f"Interventions:      {', '.join(res.interventions)}")
            print(
                f"Hallmark Coverage:  {res.coverage_percentage}% ({len(res.covered_hallmarks)}/12)"
            )
            print(f"Covered:            {', '.join(res.covered_hallmarks)}")
            print(f"Uncovered:          {', '.join(res.uncovered_hallmarks) or 'None'}")
            print(f"Active Stack Layers:{', '.join(res.stack_layers_active)}")
            tb = res.tier_breakdown
            print(
                "Tiers:              "
                f"Primary={tb['primary']}, "
                f"Antagonistic={tb['antagonistic']}, "
                f"Integrative={tb['integrative']}"
            )
            print(f"Redundancy Index:   {res.redundancy_index:.3f} (0=orthogonal, 1=redundant)")
            print(f"Synergy Score:      {res.synergy_score:.2f} hallmarks/intervention")
        return

    if args.drivers:
        drivers = driver_impact_analysis()
        if args.json:
            print(json.dumps(drivers, indent=2))
        else:
            print("=== Upstream Driver Impact Ranking (Network Centrality) ===\n")
            print(f"{'Driver':20s} | {'Fan-out':8s} | {'Primary':8s} | {'Score':6s} | {'Targets'}")
            print("-" * 75)
            for d in drivers:
                targets = ", ".join(d["targets"])
                print(
                    f"{d['driver']:20s} | {d['fan_out_count']:8d} | "
                    f"{d['primary_count']:8d} | {d['centrality_score']:6.2f} | {targets}"
                )
        return

    if args.optimize:
        opts = optimize_minimal_cocktail(max_cocktail_size=args.max_size)
        if args.json:
            print(json.dumps([asdict(o) for o in opts], indent=2))
        else:
            print(f"=== Optimal Minimal Cocktails (Max Size = {args.max_size}) ===\n")
            for rank, o in enumerate(opts, 1):
                covered = ", ".join(o.covered_hallmarks)
                layers = ", ".join(o.stack_layers_active)
                print(
                    f"#{rank} [{o.coverage_percentage}% Coverage] "
                    f"{', '.join(o.interventions)}\n"
                    f"    Covered ({len(o.covered_hallmarks)}): {covered}\n"
                    f"    Layers: {layers} | Redundancy: {o.redundancy_index:.3f} | "
                    f"Synergy: {o.synergy_score:.2f}\n"
                )
        return

    # Default overview
    print("Available interventions:")
    for k, v in sorted(INTERVENTION_EDGES.items()):
        print(f"  {k:25s} -> {', '.join(v)}")


if __name__ == "__main__":
    main()
