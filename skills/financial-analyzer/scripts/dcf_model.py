#!/usr/bin/env python3
"""DCF 估值模型"""

import json
from dataclasses import dataclass
from typing import List, Optional

@dataclass
class DCFInputs:
    """DCF 模型输入参数"""
    base_fcf: float                    # 基期自由现金流
    growth_rates: List[float]          # 各年增长率
    wacc: float                        # 加权平均资本成本
    terminal_growth_rate: float        # 永续增长率
    shares_outstanding: float          # 总股数
    net_debt: float = 0                # 净负债（有息负债-现金）
    minority_interest: float = 0       # 少数股东权益

@dataclass
class DCFOutput:
    """DCF 模型输出"""
    projected_fcf: List[float]         # 预测各年 FCF
    pv_fcf: List[float]                # 各年 FCF 现值
    sum_pv_fcf: float                  # FCF 现值合计
    terminal_value: float              # 终值
    pv_terminal_value: float           # 终值现值
    enterprise_value: float            # 企业价值
    equity_value: float                # 股权价值
    per_share_value: float             # 每股价值

def calculate_dcf(inputs: DCFInputs) -> DCFOutput:
    """执行 DCF 估值计算"""
    n_years = len(inputs.growth_rates)

    # 计算各年预测 FCF
    projected_fcf = []
    current_fcf = inputs.base_fcf
    for rate in inputs.growth_rates:
        current_fcf = current_fcf * (1 + rate)
        projected_fcf.append(current_fcf)

    # 计算各年 FCF 现值
    pv_fcf = []
    for i, fcf in enumerate(projected_fcf):
        pv = fcf / ((1 + inputs.wacc) ** (i + 1))
        pv_fcf.append(pv)

    sum_pv_fcf = sum(pv_fcf)

    # 计算终值（永续增长模型）
    terminal_fcf = projected_fcf[-1] * (1 + inputs.terminal_growth_rate)
    terminal_value = terminal_fcf / (inputs.wacc - inputs.terminal_growth_rate)

    # 终值现值
    pv_terminal_value = terminal_value / ((1 + inputs.wacc) ** n_years)

    # 企业价值
    enterprise_value = sum_pv_fcf + pv_terminal_value

    # 股权价值
    equity_value = enterprise_value - inputs.net_debt - inputs.minority_interest

    # 每股价值
    per_share_value = equity_value / inputs.shares_outstanding if inputs.shares_outstanding > 0 else 0

    return DCFOutput(
        projected_fcf=projected_fcf,
        pv_fcf=pv_fcf,
        sum_pv_fcf=sum_pv_fcf,
        terminal_value=terminal_value,
        pv_terminal_value=pv_terminal_value,
        enterprise_value=enterprise_value,
        equity_value=equity_value,
        per_share_value=per_share_value
    )

def sensitivity_analysis(inputs: DCFInputs,
                         wacc_range: List[float] = None,
                         growth_range: List[float] = None) -> dict:
    """敏感性分析"""
    if wacc_range is None:
        wacc_range = [inputs.wacc - 0.01, inputs.wacc, inputs.wacc + 0.01]
    if growth_range is None:
        growth_range = [inputs.terminal_growth_rate - 0.005,
                        inputs.terminal_growth_rate,
                        inputs.terminal_growth_rate + 0.005]

    matrix = {}
    for wacc in wacc_range:
        row_key = f"WACC {wacc:.1%}"
        matrix[row_key] = {}
        for g in growth_range:
            col_key = f"g={g:.1%}"
            test_inputs = DCFInputs(
                base_fcf=inputs.base_fcf,
                growth_rates=inputs.growth_rates,
                wacc=wacc,
                terminal_growth_rate=g,
                shares_outstanding=inputs.shares_outstanding,
                net_debt=inputs.net_debt,
                minority_interest=inputs.minority_interest
            )
            result = calculate_dcf(test_inputs)
            matrix[row_key][col_key] = round(result.per_share_value, 2)

    return matrix

def format_output(output: DCFOutput) -> dict:
    """格式化输出"""
    return {
        '预测期 FCF': [f"Year {i+1}: {fcf:,.0f}" for i, fcf in enumerate(output.projected_fcf)],
        '预测期 FCF 现值': [f"Year {i+1}: {pv:,.0f}" for i, pv in enumerate(output.pv_fcf)],
        '预测期现值合计': f"{output.sum_pv_fcf:,.0f}",
        '终值': f"{output.terminal_value:,.0f}",
        '终值现值': f"{output.pv_terminal_value:,.0f}",
        '企业价值': f"{output.enterprise_value:,.0f}",
        '股权价值': f"{output.equity_value:,.0f}",
        '每股价值': f"{output.per_share_value:.2f}",
    }

def main():
    # 示例: 5年期DCF估值
    inputs = DCFInputs(
        base_fcf=1_000_000_000,        # 基期FCF: 10亿
        growth_rates=[0.15, 0.12, 0.10, 0.08, 0.06],  # 5年增长率
        wacc=0.10,                      # WACC: 10%
        terminal_growth_rate=0.03,      # 永续增长率: 3%
        shares_outstanding=1_000_000_000,  # 10亿股
        net_debt=5_000_000_000,         # 净负债: 50亿
    )

    result = calculate_dcf(inputs)

    print("=" * 50)
    print("DCF 估值结果")
    print("=" * 50)

    formatted = format_output(result)
    print(json.dumps(formatted, ensure_ascii=False, indent=2))

    print("\n" + "=" * 50)
    print("敏感性分析")
    print("=" * 50)

    sensitivity = sensitivity_analysis(inputs)
    print(json.dumps(sensitivity, ensure_ascii=False, indent=2))

if __name__ == "__main__":
    main()
