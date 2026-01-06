from industry_data import INDUSTRY_DATA
from scoring_policy import SCORE_POLICY
from factor_mapping import FACTOR_POLICY_MAP

FACTOR_WEIGHT = 1 / 16  # 6.25%


def calculate_ir(industry_name: str) -> float:
    if industry_name not in INDUSTRY_DATA:
        raise ValueError(f"Industry '{industry_name}' not found")

    total_score = 0.0
    industry_factors = INDUSTRY_DATA[industry_name]

    for factor, qualitative_value in industry_factors.items():
        policy_key = FACTOR_POLICY_MAP[factor]
        score_table = SCORE_POLICY[policy_key]
        score = score_table.get(qualitative_value, 0)
        total_score += score * FACTOR_WEIGHT

    return round(total_score, 3)
