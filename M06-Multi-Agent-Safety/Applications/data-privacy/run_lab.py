#!/usr/bin/env python3
"""Synthetic Data Privacy teaching lab. Not a production data release service."""
import argparse
import json
import math
import random
import secrets
from pathlib import Path

HERE = Path(__file__).resolve().parent
FIXTURE = HERE / "data/synthetic-class.json"


def load_fixture(path=FIXTURE):
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    if set(data) != {"synthetic", "scenario", "records"} or data["synthetic"] is not True:
        raise ValueError("仅接受显式标记的合成教学数据")
    rows = data["records"]
    if not isinstance(rows, list) or len(rows) < 3:
        raise ValueError("合成记录不足")
    ids = []
    for row in rows:
        if set(row) != {"id", "cohort", "risk_flag"}:
            raise ValueError("记录字段不符合合成案例契约")
        if not isinstance(row["id"], str) or not row["id"].startswith("SYN-"):
            raise ValueError("只能使用合成编号")
        if row["cohort"] not in {"A", "B"} or type(row["risk_flag"]) is not int or row["risk_flag"] not in (0, 1):
            raise ValueError("分组或二元教学变量不合法")
        ids.append(row["id"])
    if len(ids) != len(set(ids)):
        raise ValueError("合成编号重复")
    return rows


def leakage_demo(rows):
    a = [r for r in rows if r["cohort"] == "A"]
    if len(a) != 3 or not any(r["id"] == "SYN-03" for r in a):
        raise ValueError("重叠查询演示需要固定的虚构三人小组")
    all_a = sum(r["risk_flag"] for r in a)
    without_one = sum(r["risk_flag"] for r in a if r["id"] != "SYN-03")
    return {"all_three": all_a, "other_two": without_one,
            "inferred_SYN_03": all_a - without_one,
            "interpretation": "两个精确且重叠的统计结果可推断一名虚构成员的标志；这是统计发布的隐私泄露示例。"}


def breach_demo(role, raw_export_enabled):
    if role not in {"teacher", "external"} or type(raw_export_enabled) is not bool:
        raise ValueError("角色或配置不合法")
    return {"role": role, "raw_export_enabled": raw_export_enabled,
            "would_expose_raw_records": role == "external" and raw_export_enabled,
            "interpretation": "这是权限配置的风险判断，不执行或生成任何原始记录导出。"}


def positive_number(value, name):
    if not isinstance(value, (int, float)) or isinstance(value, bool) or not math.isfinite(value) or value <= 0:
        raise ValueError(f"{name} 必须是有限正数")
    return float(value)


def privacy_cost(epsilon, queries, total_budget):
    epsilon = positive_number(epsilon, "epsilon")
    total_budget = positive_number(total_budget, "total_budget")
    if not isinstance(queries, int) or isinstance(queries, bool) or queries < 1 or queries > 100:
        raise ValueError("queries 必须为 1–100 的整数")
    spent = epsilon * queries
    if not math.isfinite(spent) or spent > total_budget + 1e-12:
        raise ValueError("重复发布将超出设定的教学预算")
    return round(spent, 12)


def laplace_noise(epsilon, rng):
    # Difference of independent exponential variables has Laplace scale 1/epsilon.
    return rng.expovariate(epsilon) - rng.expovariate(epsilon)


def release(rows, epsilon, queries, total_budget):
    """Return only randomized outputs; exact synthetic count is kept out of this result."""
    spent = privacy_cost(epsilon, queries, total_budget)
    true_count = sum(r["risk_flag"] for r in rows if r["cohort"] == "A")
    rng = secrets.SystemRandom()
    noisy = [true_count + laplace_noise(epsilon, rng) for _ in range(queries)]
    if not all(math.isfinite(value) for value in noisy):
        raise ValueError("数值结果非有限；停止输出")
    return {"scenario": "synthetic_fixed_cohort_A", "privacy_unit": "one synthetic row",
            "epsilon_per_query": float(epsilon), "queries": queries,
            "epsilon_spent_upper_bound": spent,
            "epsilon_budget_remaining": round(float(total_budget) - spent, 12),
            "noisy_counts": [round(value, 6) for value in noisy],
            "note": "仅为教学实现；不跨命令保存预算；没有经过真实数据部署所需的隐私、安全与浮点实现审查。"}


def compare(rows, epsilons=(0.25, 0.5, 1.0), trials=400, seed=2026):
    """Seeded utility simulation; intentionally NOT a differentially private release."""
    if not isinstance(trials, int) or trials < 10 or trials > 10000:
        raise ValueError("trials 超出教学范围")
    rng = random.Random(seed)
    count = sum(r["risk_flag"] for r in rows if r["cohort"] == "A")
    series = []
    for eps in epsilons:
        eps = positive_number(eps, "epsilon")
        errors = [abs(laplace_noise(eps, rng)) for _ in range(trials)]
        series.append({"epsilon": eps, "mean_absolute_error": round(sum(errors) / trials, 4)})
    return {"mode": "seeded_synthetic_utility_simulation_not_a_private_release",
            "exact_synthetic_count": count, "trials": trials, "series": series}


def write_new(path, value):
    path = Path(path)
    if path.is_symlink() or path.exists():
        raise ValueError("输出文件已存在；不覆盖")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def main():
    p = argparse.ArgumentParser(description=__doc__)
    sub = p.add_subparsers(dest="mode", required=True)
    sub.add_parser("risk")
    sub.add_parser("compare")
    q = sub.add_parser("release")
    q.add_argument("--epsilon", type=float, required=True)
    q.add_argument("--queries", type=int, default=1)
    q.add_argument("--budget", type=float, required=True)
    q.add_argument("--out", type=Path, required=True)
    a = p.parse_args()
    try:
        rows = load_fixture()
        if a.mode == "risk":
            result = {"mode": "synthetic_risk_demonstration", "leakage": leakage_demo(rows),
                      "safe_export": breach_demo("external", False),
                      "misconfigured_export": breach_demo("external", True)}
        elif a.mode == "compare":
            result = compare(rows)
        else:
            result = release(rows, a.epsilon, a.queries, a.budget)
            write_new(a.out, result)
        print(json.dumps(result, ensure_ascii=False, indent=2))
    except (OSError, ValueError, TypeError) as error:
        p.exit(2, f"停止：{error}\n")


if __name__ == "__main__":
    main()
