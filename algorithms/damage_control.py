"""
Damage-control longevity simulator.

Implements a simplified two-pathway model inspired by control-theoretic
aging boundedness (Pathway A = regulatable repair; Pathway B = engineered
correction of information-limited lesions).

This is a research toy model for design exploration - not a biological oracle.

Age-phased repair_a (Ralph wake #49): optional schedule mirrors ITP finding
that most geroprotectors act in restricted life windows, not constant RA.

Sex clearance multipliers (Ralph wake #50): optional male/female and late-life
female toxicity window (cana-like). Defaults are identity (1.0) so legacy
policies are unchanged until a sealed calibration oracle exists.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import asdict, dataclass, field


@dataclass
class Params:
    years: int = 120
    a0: float = 0.05
    b0: float = 0.02
    prod_a: float = 0.035  # A production / year
    prod_b: float = 0.012  # B production / year
    repair_a: float = 0.028  # endogenous RA (used when schedule is empty)
    repair_b: float = 0.0  # engineered RB (0 = natural aging)
    morbidity: float = 1.0
    cancer_risk_gain: float = 0.15  # repair-without-derisk penalty on B growth
    derisk: bool = False
    # Optional (start_year, end_year_exclusive, repair_a) windows; empty = constant.
    repair_a_schedule: tuple[tuple[int, int, float], ...] = field(default_factory=tuple)
    # Sex split: "" = unspecified (multiplier 1.0). "male" / "female" use fields below.
    sex: str = ""
    sex_clearance_male: float = 1.0
    sex_clearance_female: float = 1.0
    # If set, female effective RA is scaled by female_late_clearance_mult from this year.
    # NOT ITP-cana calibrated: female plasma ~3.7x male yet lifespan benefit is male-only
    # (Miller JCI Insight 2020) — see design/gaps/age-matrix.md wake #65.
    female_late_toxicity_start: int | None = None
    female_late_clearance_mult: float = 1.0


@dataclass
class YearState:
    t: int
    a: float
    b: float
    d: float
    morbidity_hit: bool
    repair_a_used: float = 0.0


def repair_a_at(t: int, p: Params) -> float:
    """Return Pathway-A repair capacity at year t (before sex multiplier).

    With an empty schedule, returns constant p.repair_a.
    With a schedule, first matching [start, end) window wins; years outside
    all windows get 0.0 (no continuous overstatement).
    """
    if not p.repair_a_schedule:
        return p.repair_a
    for start, end, ra in p.repair_a_schedule:
        if start <= t < end:
            return ra
    return 0.0


def clearance_mult(t: int, p: Params) -> float:
    """Sex- and age-dependent multiplier on effective Pathway-A repair."""
    if p.sex not in ("male", "female"):
        return 1.0
    base = p.sex_clearance_male if p.sex == "male" else p.sex_clearance_female
    if (
        p.sex == "female"
        and p.female_late_toxicity_start is not None
        and t >= p.female_late_toxicity_start
    ):
        return p.female_late_clearance_mult
    return base


def effective_repair_a(t: int, p: Params) -> float:
    return repair_a_at(t, p) * clearance_mult(t, p)


def step(a: float, b: float, p: Params, t: int = 0) -> tuple[float, float]:
    # Saturable clearance -> non-zero asymptote when capacity > production
    km = 0.25
    ra = effective_repair_a(t, p)
    clear_a = ra * a / (a + km) if (a + km) > 0 else 0.0
    a_next = max(0.0, a + p.prod_a - clear_a)
    # Pathway B: engineered removal; clone expansion if repairing without derisk
    expand = p.cancer_risk_gain * max(0.0, ra - p.prod_a) if not p.derisk else 0.0
    clear_b = p.repair_b * b / (b + km) if (b + km) > 0 else 0.0
    b_next = max(0.0, b + p.prod_b * (1.0 + expand) - clear_b)
    return a_next, b_next


def simulate(p: Params) -> list[YearState]:
    a, b = p.a0, p.b0
    out: list[YearState] = []
    for t in range(p.years + 1):
        ra = effective_repair_a(t, p)
        d = a + b
        out.append(
            YearState(
                t=t,
                a=a,
                b=b,
                d=d,
                morbidity_hit=d >= p.morbidity,
                repair_a_used=ra,
            )
        )
        a, b = step(a, b, p, t=t)
    return out


def ascii_plot(states: list[YearState], width: int = 60) -> str:
    mx = max(s.d for s in states) or 1.0
    lines = ["year | D(t) damage burden", "-" * (width + 12)]
    for s in states:
        if s.t % 5 != 0 and s.t != states[-1].t:
            continue
        n = int((s.d / mx) * width)
        bar = "#" * n
        flag = " <-- morbidity" if s.morbidity_hit else ""
        lines.append(f"{s.t:4d} | {bar} {s.d:.3f}{flag}")
    return "\n".join(lines)


def compare_policies(years: int = 120) -> dict:
    policies = {
        "natural": Params(years=years, repair_a=0.04, repair_b=0.004, derisk=False),
        "repair_only_A": Params(years=years, repair_a=0.09, repair_b=0.004, derisk=False),
        "derisk_then_repair": Params(years=years, repair_a=0.09, repair_b=0.05, derisk=True),
        # Derisk-first with illustrative late female clearance collapse (wake #64)
        "derisk_then_repair_male": Params(
            years=years,
            repair_a=0.09,
            repair_b=0.05,
            derisk=True,
            sex="male",
            sex_clearance_male=1.0,
        ),
        "derisk_then_repair_female": Params(
            years=years,
            repair_a=0.09,
            repair_b=0.05,
            derisk=True,
            sex="female",
            sex_clearance_female=1.0,
            female_late_toxicity_start=60,
            female_late_clearance_mult=0.05,
        ),
        "immortality_stack": Params(years=years, repair_a=0.12, repair_b=0.08, derisk=True),
        # Immortality stack with illustrative late female clearance collapse
        "immortality_stack_male": Params(
            years=years,
            repair_a=0.12,
            repair_b=0.08,
            derisk=True,
            sex="male",
            sex_clearance_male=1.0,
        ),
        "immortality_stack_female": Params(
            years=years,
            repair_a=0.12,
            repair_b=0.08,
            derisk=True,
            sex="female",
            sex_clearance_female=1.0,
            female_late_toxicity_start=60,
            female_late_clearance_mult=0.05,
        ),
        # ITP-inspired midlife pulse (illustrative; not calibrated)
        "midlife_pulse_A": Params(
            years=years,
            repair_a=0.0,
            repair_b=0.004,
            derisk=False,
            repair_a_schedule=((40, 70, 0.09),),
        ),
        # Midlife pulse with illustrative late female clearance collapse (wake #68).
        # Three-window schedule keeps endogenous RA outside the pulse so morbidity
        # lands after female_late_toxicity_start (unlike midlife_pulse_A, which hits ~y21).
        "midlife_pulse_male": Params(
            years=years,
            repair_a=0.0,
            repair_b=0.004,
            derisk=False,
            repair_a_schedule=((0, 40, 0.05), (40, 70, 0.09), (70, 200, 0.05)),
            sex="male",
            sex_clearance_male=1.0,
        ),
        "midlife_pulse_female": Params(
            years=years,
            repair_a=0.0,
            repair_b=0.004,
            derisk=False,
            repair_a_schedule=((0, 40, 0.05), (40, 70, 0.09), (70, 200, 0.05)),
            sex="female",
            sex_clearance_female=1.0,
            female_late_toxicity_start=60,
            female_late_clearance_mult=0.05,
        ),
        # Cana-like sex split (illustrative): late-life female clearance collapse
        "cana_like_male": Params(
            years=years,
            repair_a=0.09,
            repair_b=0.004,
            derisk=True,
            sex="male",
            sex_clearance_male=1.0,
        ),
        "cana_like_female": Params(
            years=years,
            repair_a=0.09,
            repair_b=0.004,
            derisk=True,
            sex="female",
            sex_clearance_female=1.0,
            female_late_toxicity_start=60,
            female_late_clearance_mult=0.05,
        ),
        # Combined: midlife RA pulse + cana-like late female toxicity (illustrative)
        "midlife_pulse_cana_male": Params(
            years=years,
            repair_a=0.0,
            repair_b=0.004,
            derisk=True,
            repair_a_schedule=((40, 70, 0.09),),
            sex="male",
            sex_clearance_male=1.0,
        ),
        "midlife_pulse_cana_female": Params(
            years=years,
            repair_a=0.0,
            repair_b=0.004,
            derisk=True,
            repair_a_schedule=((40, 70, 0.09),),
            sex="female",
            sex_clearance_female=1.0,
            female_late_toxicity_start=60,
            female_late_clearance_mult=0.05,
        ),
    }
    report = {}
    for name, p in policies.items():
        states = simulate(p)
        hit = next((s.t for s in states if s.morbidity_hit), None)
        report[name] = {
            "params": asdict(p),
            "final_D": states[-1].d,
            "final_A": states[-1].a,
            "final_B": states[-1].b,
            "morbidity_year": hit,
            "bounded": hit is None and states[-1].d < p.morbidity,
        }
    return report


def main() -> None:
    ap = argparse.ArgumentParser(description="Two-pathway aging damage simulator")
    ap.add_argument("--years", type=int, default=120)
    ap.add_argument(
        "--policy",
        choices=[
            "natural",
            "repair_only_A",
            "derisk_then_repair",
            "derisk_then_repair_male",
            "derisk_then_repair_female",
            "immortality_stack",
            "immortality_stack_male",
            "immortality_stack_female",
            "midlife_pulse_A",
            "midlife_pulse_male",
            "midlife_pulse_female",
            "cana_like_male",
            "cana_like_female",
            "midlife_pulse_cana_male",
            "midlife_pulse_cana_female",
            "all",
        ],
        default="all",
    )
    ap.add_argument("--plot-ascii", action="store_true")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()

    if args.policy == "all":
        report = compare_policies(args.years)
        if args.json:
            print(json.dumps(report, indent=2))
        else:
            print("Policy comparison (morbidity threshold D>=1.0)\n")
            for name, r in report.items():
                my = r["morbidity_year"]
                print(
                    f"  {name:20s} final_D={r['final_D']:.3f}  "
                    f"morbidity_year={my}  bounded={r['bounded']}"
                )
            if args.plot_ascii:
                print("\n--- immortality_stack trajectory ---")
                print(
                    ascii_plot(
                        simulate(
                            Params(
                                years=args.years,
                                repair_a=0.12,
                                repair_b=0.08,
                                derisk=True,
                            )
                        )
                    )
                )
        return

    presets = {
        "natural": Params(years=args.years, repair_a=0.04, repair_b=0.004, derisk=False),
        "repair_only_A": Params(years=args.years, repair_a=0.09, repair_b=0.004, derisk=False),
        "derisk_then_repair": Params(years=args.years, repair_a=0.09, repair_b=0.05, derisk=True),
        "derisk_then_repair_male": Params(
            years=args.years,
            repair_a=0.09,
            repair_b=0.05,
            derisk=True,
            sex="male",
            sex_clearance_male=1.0,
        ),
        "derisk_then_repair_female": Params(
            years=args.years,
            repair_a=0.09,
            repair_b=0.05,
            derisk=True,
            sex="female",
            sex_clearance_female=1.0,
            female_late_toxicity_start=60,
            female_late_clearance_mult=0.05,
        ),
        "immortality_stack": Params(years=args.years, repair_a=0.12, repair_b=0.08, derisk=True),
        "immortality_stack_male": Params(
            years=args.years,
            repair_a=0.12,
            repair_b=0.08,
            derisk=True,
            sex="male",
            sex_clearance_male=1.0,
        ),
        "immortality_stack_female": Params(
            years=args.years,
            repair_a=0.12,
            repair_b=0.08,
            derisk=True,
            sex="female",
            sex_clearance_female=1.0,
            female_late_toxicity_start=60,
            female_late_clearance_mult=0.05,
        ),
        "midlife_pulse_A": Params(
            years=args.years,
            repair_a=0.0,
            repair_b=0.004,
            derisk=False,
            repair_a_schedule=((40, 70, 0.09),),
        ),
        "midlife_pulse_male": Params(
            years=args.years,
            repair_a=0.0,
            repair_b=0.004,
            derisk=False,
            repair_a_schedule=((0, 40, 0.05), (40, 70, 0.09), (70, 200, 0.05)),
            sex="male",
            sex_clearance_male=1.0,
        ),
        "midlife_pulse_female": Params(
            years=args.years,
            repair_a=0.0,
            repair_b=0.004,
            derisk=False,
            repair_a_schedule=((0, 40, 0.05), (40, 70, 0.09), (70, 200, 0.05)),
            sex="female",
            sex_clearance_female=1.0,
            female_late_toxicity_start=60,
            female_late_clearance_mult=0.05,
        ),
        "cana_like_male": Params(
            years=args.years,
            repair_a=0.09,
            repair_b=0.004,
            derisk=True,
            sex="male",
            sex_clearance_male=1.0,
        ),
        "cana_like_female": Params(
            years=args.years,
            repair_a=0.09,
            repair_b=0.004,
            derisk=True,
            sex="female",
            sex_clearance_female=1.0,
            female_late_toxicity_start=60,
            female_late_clearance_mult=0.05,
        ),
        "midlife_pulse_cana_male": Params(
            years=args.years,
            repair_a=0.0,
            repair_b=0.004,
            derisk=True,
            repair_a_schedule=((40, 70, 0.09),),
            sex="male",
            sex_clearance_male=1.0,
        ),
        "midlife_pulse_cana_female": Params(
            years=args.years,
            repair_a=0.0,
            repair_b=0.004,
            derisk=True,
            repair_a_schedule=((40, 70, 0.09),),
            sex="female",
            sex_clearance_female=1.0,
            female_late_toxicity_start=60,
            female_late_clearance_mult=0.05,
        ),
    }
    states = simulate(presets[args.policy])
    if args.json:
        print(json.dumps([asdict(s) for s in states], indent=2))
    elif args.plot_ascii:
        print(ascii_plot(states))
    else:
        print(f"final D={states[-1].d:.3f} A={states[-1].a:.3f} B={states[-1].b:.3f}")


if __name__ == "__main__":
    main()
