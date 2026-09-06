"""Geroscience Clinical Trial Transparency and Evidence Maturity Engine.

Formalizes the core epistemic lessons of geroscience translation:
1. "COMPLETED != Results": Tracks the evidence publication latency (months between
   trial completion and public peer-reviewed / registry results disclosure).
2. Evidence Maturity Ladder:
   - Tier 1: Preclinical (in vitro / murine lifespan signals)
   - Tier 2: Disease-Bridge Phase I/II (e.g., Barth syndrome, oncology RP2D)
   - Tier 3: Healthy-Aging Intermediate Biomarker / IC Domain Phase II (e.g., XPRIZE, PROSPR)
   - Tier 4: Healthspan / Hard Endpoint Multi-Center Phase III RCT (e.g., TAME, VITAL-H)
3. Negative Result & Publication Bottleneck Auditor: Identifies unregistered, delayed,
   or undisclosed trial outcomes to avoid publication bias in meta-analyses.
"""

from __future__ import annotations

import argparse
import datetime
import json
from dataclasses import asdict, dataclass
from enum import Enum


class EvidenceTier(Enum):
    TIER_1_PRECLINICAL = "Tier 1 (Preclinical)"
    TIER_2_DISEASE_BRIDGE = "Tier 2 (Disease Phase I/II)"
    TIER_3_BIOMARKER_IC_DOMAIN = "Tier 3 (Healthy-Aging Biomarker / IC Phase II)"
    TIER_4_HEALTHSPAN_HARD_ENDPOINT = "Tier 4 (Hard Endpoint Phase III RCT)"


@dataclass
class TrialRecord:
    id: str  # Identifier (e.g., NCT05835999, UMIN000059942, or project name)
    name: str
    target_intervention: str
    registry_status: str  # COMPLETED, RECRUITING, ACTIVE_NOT_RECRUITING, UNREGISTERED
    results_posted: bool
    peer_reviewed_results: bool
    completion_date: str | None  # YYYY-MM-DD or YYYY-MM
    evidence_tier: EvidenceTier
    sample_size: int | None
    endpoint_type: (
        str  # "Disease Intermediate", "IC Domains", "Multi-Omic Biomarker", "Lifespan/MACE"
    )
    notes: str = ""


# Curated benchmark clinical registry dataset from the live-forever corpus
BENCHMARK_TRIALS: list[TrialRecord] = [
    TrialRecord(
        id="NCT05835999",
        name="EVERLAST (Everolimus Metabolic Healthspan)",
        target_intervention="Everolimus 0.5mg/d or 5mg/wk",
        registry_status="COMPLETED",
        results_posted=False,
        peer_reviewed_results=False,
        completion_date="2026-07-22",
        evidence_tier=EvidenceTier.TIER_3_BIOMARKER_IC_DOMAIN,
        sample_size=84,
        endpoint_type="Insulin resistance & frailty biomarkers",
        notes="Completed Jul 2026; results tables still absent.",
    ),
    TrialRecord(
        id="VITAL-H",
        name="VITAL-H (ARPA-H Healthy Aging Oral Triad)",
        target_intervention="Rapamycin + Dapagliflozin + Semaglutide",
        registry_status="UNREGISTERED",
        results_posted=False,
        peer_reviewed_results=False,
        completion_date=None,
        evidence_tier=EvidenceTier.TIER_4_HEALTHSPAN_HARD_ENDPOINT,
        sample_size=726,
        endpoint_type="ARPA-H Intrinsic Capacity (IC) 5-Domain Composite",
        notes="Funded Feb 2026; recruitment pending ~2027; no NCT yet.",
    ),
    TrialRecord(
        id="NCT07275424",
        name="SHAPE (Elamipretide Healthy Older Muscle)",
        target_intervention="Elamipretide daily SC (vial 80mg/mL)",
        registry_status="RECRUITING",
        results_posted=False,
        peer_reviewed_results=False,
        completion_date="2026-03-31",
        evidence_tier=EvidenceTier.TIER_3_BIOMARKER_IC_DOMAIN,
        sample_size=30,
        endpoint_type="6MWT, knee extensor power, cognitive battery",
        notes="Past estimated primary completion; daily mg still undisclosed.",
    ),
    TrialRecord(
        id="NCT06658093",
        name="RESTOR (Adaptive mTORC1 Inhibition in Older Adults)",
        target_intervention="Sirolimus or Everolimus adaptive PK/PD",
        registry_status="RECRUITING",
        results_posted=False,
        peer_reviewed_results=False,
        completion_date="2027-12-31",
        evidence_tier=EvidenceTier.TIER_3_BIOMARKER_IC_DOMAIN,
        sample_size=194,
        endpoint_type="Immune & metabolic biomarker restoration",
        notes="Started Mar 2026; adaptive OD mg unpublished.",
    ),
    TrialRecord(
        id="UMIN000059942",
        name="TIME TRAVELER (Plant-Derived EV Healthspan)",
        target_intervention="Plant-derived extracellular vesicles (Factor-K)",
        registry_status="COMPLETED",
        results_posted=False,
        peer_reviewed_results=False,
        completion_date="2025-12-31",
        evidence_tier=EvidenceTier.TIER_3_BIOMARKER_IC_DOMAIN,
        sample_size=40,
        endpoint_type="Grip strength, TUG, NK cell activity, Cognitrax",
        notes="Completed in Japan registry; numerical results unpublished.",
    ),
    TrialRecord(
        id="NCT04886622",
        name="DT2216 (Platelet-Sparing Bcl-xL PROTAC)",
        target_intervention="DT2216 IV 0.4 mg/kg BIW",
        registry_status="COMPLETED",
        results_posted=True,
        peer_reviewed_results=True,
        completion_date="2024-06-30",
        evidence_tier=EvidenceTier.TIER_2_DISEASE_BRIDGE,
        sample_size=36,
        endpoint_type="Safety, RP2D, platelet-sparing pharmacodynamics",
        notes="FIH oncology completed; demonstrated platelet-sparing senolytic mechanism.",
    ),
    TrialRecord(
        id="NCT07290244",
        name="ER-100 (Inducible AAV-OSK Partial Reprogramming)",
        target_intervention="AAV-OSK intravitreal + doxycycline switch",
        registry_status="RECRUITING",
        results_posted=False,
        peer_reviewed_results=False,
        completion_date="2027-06-30",
        evidence_tier=EvidenceTier.TIER_2_DISEASE_BRIDGE,
        sample_size=18,
        endpoint_type="Visual acuity & optic nerve regeneration (NAION/Glaucoma)",
        notes="First-in-human OSK trial; ocular-only safety sentinel.",
    ),
    TrialRecord(
        id="NCT04375657",
        name="TRIIM-X (Thymus Regeneration & Epigenetic Aging)",
        target_intervention="rhGH + DHEA + Metformin + Zinc/Vitamin D",
        registry_status="RECRUITING",
        results_posted=False,
        peer_reviewed_results=False,
        completion_date="2025-12-31",
        evidence_tier=EvidenceTier.TIER_3_BIOMARKER_IC_DOMAIN,
        sample_size=100,
        endpoint_type="Thymic MRI density, GrimAge/Horvath epigenetic clocks",
        notes="Recruiting past est. completion; full peer-reviewed package pending.",
    ),
]


@dataclass
class TransparencyAuditReport:
    total_trials: int
    completed_trials: int
    completed_without_results: int
    unregistered_trials: int
    transparency_rate: float  # (Trials with posted or published results) / (Completed trials)
    average_delay_months_for_completed: float
    tier_distribution: dict[str, int]
    undisclosed_completed_list: list[str]


def parse_date(date_str: str | None) -> datetime.date | None:
    if not date_str:
        return None
    parts = [int(p) for p in date_str.split("-")]
    if len(parts) == 3:
        return datetime.date(parts[0], parts[1], parts[2])
    elif len(parts) == 2:
        return datetime.date(parts[0], parts[1], 1)
    return None


def calculate_evidence_delay_months(
    completion_date_str: str | None, as_of_date: datetime.date | None = None
) -> float:
    """Calculate months elapsed since completion date."""
    comp_date = parse_date(completion_date_str)
    if not comp_date:
        return 0.0
    ref_date = as_of_date or datetime.date(2026, 8, 23)
    days = (ref_date - comp_date).days
    return round(max(0.0, days / 30.4375), 1)


def audit_transparency(trials: list[TrialRecord] | None = None) -> TransparencyAuditReport:
    """Audit evidence disclosure and calculate the trial transparency index."""
    records = trials if trials is not None else BENCHMARK_TRIALS
    total = len(records)

    completed = [t for t in records if t.registry_status == "COMPLETED"]
    completed_no_res = [
        t for t in completed if not t.results_posted and not t.peer_reviewed_results
    ]
    unreg = [t for t in records if t.registry_status == "UNREGISTERED"]

    # Calculate transparency rate over completed trials
    if completed:
        trans_rate = round(((len(completed) - len(completed_no_res)) / len(completed)) * 100, 1)
    else:
        trans_rate = 100.0

    # Calculate mean delay for completed trials lacking results
    delays = [
        calculate_evidence_delay_months(t.completion_date)
        for t in completed_no_res
        if t.completion_date
    ]
    avg_delay = round(sum(delays) / len(delays), 1) if delays else 0.0

    tier_dist = {tier.value: 0 for tier in EvidenceTier}
    for t in records:
        tier_dist[t.evidence_tier.value] += 1

    return TransparencyAuditReport(
        total_trials=total,
        completed_trials=len(completed),
        completed_without_results=len(completed_no_res),
        unregistered_trials=len(unreg),
        transparency_rate=trans_rate,
        average_delay_months_for_completed=avg_delay,
        tier_distribution=tier_dist,
        undisclosed_completed_list=[f"{t.id} ({t.name})" for t in completed_no_res],
    )


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Geroscience Clinical Trial Transparency & Evidence Auditor"
    )
    parser.add_argument("--audit", action="store_true", help="Run full transparency audit")
    parser.add_argument(
        "--list-trials", action="store_true", help="List benchmark trials and evidence tiers"
    )
    parser.add_argument("--json", action="store_true", help="Output JSON results")
    args = parser.parse_args()

    if args.list_trials:
        if args.json:
            data = [
                {
                    **asdict(t),
                    "evidence_tier": t.evidence_tier.value,
                    "delay_months": calculate_evidence_delay_months(t.completion_date),
                }
                for t in BENCHMARK_TRIALS
            ]
            print(json.dumps(data, indent=2))
        else:
            print("=== Benchmarked Longevity Clinical Trials & Evidence Tiers ===\n")
            print(f"{'ID':14s} | {'Status':12s} | {'Tier':26s} | {'Results?':9s} | {'Trial Name'}")
            print("-" * 90)
            for t in BENCHMARK_TRIALS:
                res_str = "YES" if (t.results_posted or t.peer_reviewed_results) else "NO"
                tier = t.evidence_tier.value[:26]
                print(
                    f"{t.id:14s} | {t.registry_status:12s} | {tier:26s} | {res_str:9s} | {t.name}"
                )
        return

    # Default audit
    audit_res = audit_transparency()
    if args.json:
        print(json.dumps(asdict(audit_res), indent=2))
    else:
        print("=== Geroscience Trial Transparency & Negatives Audit ===\n")
        print(f"Total Tracked Trials:            {audit_res.total_trials}")
        print(f"Completed Trials:               {audit_res.completed_trials}")
        print(f"Completed WITHOUT Results (Gap):{audit_res.completed_without_results}")
        print(f"Registry Transparency Rate:     {audit_res.transparency_rate}%")
        print(
            f"Average Evidence Delay (Months):{audit_res.average_delay_months_for_completed} months"
        )
        print("\nEvidence Tier Breakdown:")
        for tier, count in audit_res.tier_distribution.items():
            print(f"  - {tier:45s}: {count}")
        if audit_res.undisclosed_completed_list:
            print("\nUndisclosed Completed Trials (Active 'COMPLETED != Results' Pins):")
            for item in audit_res.undisclosed_completed_list:
                print(f"  * {item}")


if __name__ == "__main__":
    main()
