"""
Ralph loop tick helper: report status, list next research gaps, suggest Exa queries.
Cancer / oncology cure hill-climb (Hybrid D architecture).
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from status import exit_criteria  # noqa: E402

NEXT_QUERIES = [
    "IMCODE003 NCT05968326 interim DFS OR enrollment completed flip 2026",
    "CAR-PRISM NCT05767359 mature 24-month MRD plateau update beyond median 15.3mo FU 2026",
    "Satri-cel earlier-line CLDN18.2 CAR-T gastric ClinicalTrials.gov 2026",
    "GIANT NCT06816927 safety lead-in go no-go relatlimab GBM 2026",
    "NCT07066995 mesothelin Claudin18.2 dual CAR-T PDAC first patient OR DLT 2026",
    "TNBC personalized neoantigen vaccine randomized OS NCT Results 2026",
    "RedirecTT-1 Haematologica extended follow-up EMD talquetamab teclistamab 2026",
    "BNT122-01 NCT04486378 CRC autogene cevumeran full DSMB OS tables when published",
    "Zolbetuximab CLDN18.2 mAb vs satri-cel sequencing gastric cure-fraction 2026",
    "MonumenTAL-6 NCT06208150 ASH ASCO EHA congress full KM medians safety 2026",
    "LOTIS-5 NCT04384484 peer-reviewed manuscript loncastuximab rituximab Blood Lancet 2026",
]


def main() -> None:
    c = exit_criteria()
    gaps = json.loads((ROOT / "docs" / "gap_register.json").read_text(encoding="utf-8"))
    print("=== CANCER-RESEARCH RALPH TICK ===")
    print(json.dumps(c, indent=2))
    print("\nOpen gaps:")
    for g in gaps.get("open", []) or ["(none)"]:
        if isinstance(g, dict):
            print(f"  - [{g['priority']}] {g['id']}: {g['title']}")
        else:
            print(f"  - {g}")
    print("\nDeferred with evidence:")
    for g in gaps.get("deferred_with_evidence", []):
        print(f"  - {g['id']} -> {g.get('dossier')}")
    print("\nSuggested Exa queries:")
    for q in NEXT_QUERIES:
        print(f"  - {q}")
    print("\nGOAL_MET" if c["goal_met"] else "GOAL_OPEN — continue research")


if __name__ == "__main__":
    main()
