#!/usr/bin/env python3
"""OpenDP comparison on a fixed, public-size synthetic cohort only."""
import argparse
import json
from importlib.metadata import version
import math
from pathlib import Path
from run_lab import load_fixture, write_new


def run(epsilon, queries):
    if not math.isfinite(epsilon) or epsilon <= 0:
        raise ValueError("epsilon 必须为有限正数")
    if not isinstance(queries, int) or queries < 1 or queries > 10:
        raise ValueError("queries 必须为 1–10 的整数")
    try:
        import opendp.prelude as dp
    except ImportError as error:
        raise ValueError("请在独立环境安装 opendp；基础 L1/L2 无需此库") from error
    # Context composition currently requires OpenDP contrib; use only for teaching.
    dp.enable_features("contrib")
    rows = load_fixture()
    values = [float(r["risk_flag"]) for r in rows if r["cohort"] == "A"]
    if len(values) != 3:
        raise ValueError("本教学演示需要公开固定的三人合成小组")
    context = dp.Context.compositor(
        data=values,
        privacy_unit=dp.unit_of(contributions=1),
        privacy_loss=dp.loss_of(epsilon=epsilon),
        split_evenly_over=queries,
    )
    noisy = [float(context.query().impute_constant(0.0).clamp((0.0, 1.0)).sum().laplace().release())
             for _ in range(queries)]
    return {"mode": "opendp_synthetic_fixed_roster",
            "opendp_version": version("opendp"),
            "privacy_unit": "one synthetic row",
            "assumptions": "fixed public cohort size and one bounded 0–1 value per fictional person",
            "epsilon_total": epsilon,
            "epsilon_per_query": epsilon / queries,
            "queries": queries,
            "noisy_sums": noisy,
            "note": "Budget state is per process only; no raw records or exact aggregate are exported. Real data needs independent design and review."}


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--epsilon", type=float, required=True)
    p.add_argument("--queries", type=int, default=2)
    p.add_argument("--out", type=Path, required=True)
    a = p.parse_args()
    try:
        result = run(a.epsilon, a.queries)
        write_new(a.out, result)
    except (OSError, ValueError, TypeError) as error:
        p.exit(2, f"停止：{error}\n")
    print("OpenDP 合成数据结果已保存；真实数据使用需独立审查。")


if __name__ == "__main__":
    main()
