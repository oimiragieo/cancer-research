"""Project status / Ralph-loop exit criteria checker (cancer-research)."""

from __future__ import annotations

import json
from pathlib import Path

try:
    import yaml
except ImportError:
    yaml = None

ROOT = Path(__file__).resolve().parents[1]

# Bidirectional oracle floor: live corpus must be >= this for corpus_ok / goal_met.
CORPUS_FLOOR = 50

# Cure-evidence scoring floors (design parity — not automatic goal_met gates).
# Randomized durable OS/DFS with long FU scores higher than single-arm MRD.
CURE_EVIDENCE_MIN_FOLLOWUP_YEARS = 3
SENTINEL_HARD_CANCERS = (
    "PDAC",
    "GBM",
    "mTNBC",
    "ovarian",
    "metastatic melanoma brain",
)


def load_sources():
    path = ROOT / "corpus" / "sources.yaml"
    text = path.read_text(encoding="utf-8")
    if yaml:
        data = yaml.safe_load(text)
        return data.get("sources", [])
    return [
        {"id": line.split("id:")[1].strip()}
        for line in text.splitlines()
        if line.strip().startswith("- id:")
    ]


def corpus_count(sources: list | None = None) -> int:
    """Return number of corpus entries (bidirectional oracle target)."""
    if sources is None:
        sources = load_sources()
    return len(sources)


def exit_criteria() -> dict:
    sources = load_sources()
    n = corpus_count(sources)
    design = (ROOT / "design" / "ultra-design.md").exists()
    medicine = (ROOT / "design" / "medicine-pipeline.md").exists()
    algo = (ROOT / "algorithms" / "tumor_burden.py").exists()
    catalog = (ROOT / "design" / "oncogenic-driver-catalog.md").exists()
    gaps_path = ROOT / "docs" / "gap_register.json"
    gaps = (
        json.loads(gaps_path.read_text(encoding="utf-8"))
        if gaps_path.exists()
        else {"open": [], "deferred_with_evidence": []}
    )
    open_gaps = gaps.get("open", [])
    deferred = gaps.get("deferred_with_evidence", [])
    dossiers_ok = all(
        (ROOT / d["dossier"]).exists() for d in deferred if "dossier" in d
    )
    return {
        "corpus_count": n,
        "corpus_ok": n >= CORPUS_FLOOR,
        "ultra_design": design,
        "medicine_pipeline": medicine,
        "algorithms": algo,
        "oncogenic_driver_catalog": catalog,
        "open_gaps": len(open_gaps),
        "deferred_gaps": len(deferred),
        "dossiers_ok": dossiers_ok,
        "goal_met": (
            n >= CORPUS_FLOOR
            and design
            and medicine
            and algo
            and catalog
            and len(open_gaps) == 0
            and dossiers_ok
            and len(deferred) >= 1
        ),
    }


def main() -> None:
    c = exit_criteria()
    print(json.dumps(c, indent=2))
    print("GOAL_MET" if c["goal_met"] else "GOAL_OPEN")


if __name__ == "__main__":
    main()
