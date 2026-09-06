"""
Tumor-burden / resistance control simulator.

Oncology analog of live-forever damage_control: models tumor burden T(t) under
clearance (therapy) vs resistance growth. Toy model for design exploration —
not a clinical oracle and not dosing advice.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import asdict, dataclass, field


@dataclass
class Params:
    months: int = 60
    t0: float = 1.0  # initial tumor burden (arbitrary units)
    growth: float = 0.08  # resistant clone growth / month
    clearance: float = 0.12  # therapy clearance / month
    resistance_gain: float = 0.04  # resistance accrual when clearance without dual-target
    dual_target: bool = False  # dual-antigen / dual-pathway derisk
    dual_target_mult: float = 0.45  # reduces resistance_gain when dual_target
    # Optional (start, end_exclusive, clearance) windows; empty = constant.
    clearance_schedule: tuple[tuple[int, int, float], ...] = field(default_factory=tuple)


@dataclass
class MonthState:
    t: int
    burden: float
    resistant_frac: float
    clearance_used: float
    progressed: bool


def clearance_at(month: int, p: Params) -> float:
    if not p.clearance_schedule:
        return p.clearance
    for start, end, c in p.clearance_schedule:
        if start <= month < end:
            return c
    return 0.0


def step(burden: float, resistant: float, month: int, p: Params) -> MonthState:
    c = clearance_at(month, p)
    r_gain = p.resistance_gain * (p.dual_target_mult if p.dual_target else 1.0)
    resistant = min(1.0, resistant + r_gain * (c / max(p.clearance, 1e-9)))
    # Sensitive compartment cleared; resistant grows
    sensitive = burden * (1.0 - resistant)
    resistant_mass = burden * resistant
    sensitive = max(0.0, sensitive * (1.0 - c))
    resistant_mass = resistant_mass * (1.0 + p.growth) * (1.0 - 0.15 * c)
    new_burden = sensitive + resistant_mass
    new_resistant = 0.0 if new_burden <= 1e-12 else resistant_mass / new_burden
    progressed = new_burden > burden * 1.05 and month > 3
    return MonthState(
        t=month,
        burden=new_burden,
        resistant_frac=new_resistant,
        clearance_used=c,
        progressed=progressed,
    )


def simulate(p: Params) -> list[MonthState]:
    burden = p.t0
    resistant = 0.05
    out: list[MonthState] = []
    for m in range(p.months):
        st = step(burden, resistant, m, p)
        out.append(st)
        burden = st.burden
        resistant = st.resistant_frac
    return out


def summary(states: list[MonthState]) -> dict:
    final = states[-1]
    nadir = min(s.burden for s in states)
    return {
        "months": len(states),
        "final_burden": round(final.burden, 4),
        "nadir_burden": round(nadir, 4),
        "final_resistant_frac": round(final.resistant_frac, 4),
        "any_progression_flag": any(s.progressed for s in states),
        "bounded": final.burden < 0.2,
    }


POLICIES = {
    "untreated": Params(clearance=0.0, resistance_gain=0.0),
    "mono_target": Params(clearance=0.14, dual_target=False),
    "dual_target": Params(clearance=0.14, dual_target=True),
    "finite_induction": Params(
        clearance=0.0,
        dual_target=True,
        clearance_schedule=((0, 6, 0.22), (6, 60, 0.02)),
    ),
}


def main() -> None:
    ap = argparse.ArgumentParser(description="Tumor burden control toy simulator")
    ap.add_argument("--months", type=int, default=60)
    ap.add_argument("--policy", choices=list(POLICIES) + ["all"], default="all")
    ap.add_argument("--plot-ascii", action="store_true")
    args = ap.parse_args()
    policies = list(POLICIES) if args.policy == "all" else [args.policy]
    report = {}
    for name in policies:
        p = POLICIES[name]
        p.months = args.months
        states = simulate(p)
        report[name] = summary(states)
        if args.plot_ascii:
            print(f"\n=== {name} ===")
            for s in states[:: max(1, args.months // 20)]:
                bar = "#" * int(min(40, s.burden * 10))
                print(f"m{s.t:02d} {s.burden:6.3f} r={s.resistant_frac:.2f} {bar}")
    print(json.dumps(report, indent=2))
    # Design claim: mono_target fails boundedness; dual_target improves it
    if "mono_target" in report and "dual_target" in report:
        mono = report["mono_target"]["final_burden"]
        dual = report["dual_target"]["final_burden"]
        print(
            "DESIGN_CHECK:",
            "dual_beats_mono" if dual < mono else "UNEXPECTED_mono_better",
        )


if __name__ == "__main__":
    main()
