#!/usr/bin/env python3
"""计算财务指标"""

import json
import sys
from dataclasses import dataclass
from typing import Optional

@dataclass
class FinancialData:
    """财务数据结构"""
    revenue: float = 0              # 营业收入
    cost_of_revenue: float = 0      # 营业成本
    gross_profit: float = 0         # 毛利润
    operating_profit: float = 0     # 营业利润
    net_income: float = 0           # 净利润
    total_assets: float = 0         # 总资产
    total_liabilities: float = 0    # 总负债
    equity: float = 0               # 股东权益
    current_assets: float = 0       # 流动资产
    current_liabilities: float = 0  # 流动负债
    inventory: float = 0            # 存货
    accounts_receivable: float = 0  # 应收账款
    accounts_payable: float = 0     # 应付账款
    operating_cash_flow: float = 0  # 经营活动现金流
    capex: float = 0                # 资本支出
    interest_expense: float = 0     # 利息费用
    interest_bearing_debt: float = 0 # 有息负债
    cash: float = 0                 # 现金及等价物
    ebit: float = 0                 # EBIT
    depreciation: float = 0         # 折旧摊销
    tax_rate: float = 0.25          # 税率

def calculate_profitability(data: FinancialData) -> dict:
    """计算盈利能力指标"""
    metrics = {}

    # 毛利率
    if data.revenue > 0:
        if data.gross_profit > 0:
            metrics['gross_margin'] = data.gross_profit / data.revenue
        elif data.cost_of_revenue > 0:
            metrics['gross_margin'] = (data.revenue - data.cost_of_revenue) / data.revenue

    # 净利率
    if data.revenue > 0 and data.net_income != 0:
        metrics['net_margin'] = data.net_income / data.revenue

    # ROE
    if data.equity > 0 and data.net_income != 0:
        metrics['roe'] = data.net_income / data.equity

    # ROA
    if data.total_assets > 0 and data.net_income != 0:
        metrics['roa'] = data.net_income / data.total_assets

    # ROIC
    invested_capital = data.equity + data.interest_bearing_debt - data.cash
    if invested_capital > 0 and data.operating_profit != 0:
        nopat = data.operating_profit * (1 - data.tax_rate)
        metrics['roic'] = nopat / invested_capital

    return metrics

def calculate_growth(current: FinancialData, previous: FinancialData) -> dict:
    """计算成长性指标"""
    metrics = {}

    # 营收同比
    if previous.revenue > 0:
        metrics['revenue_yoy'] = (current.revenue - previous.revenue) / previous.revenue

    # 净利润同比
    if previous.net_income != 0:
        metrics['net_income_yoy'] = (current.net_income - previous.net_income) / abs(previous.net_income)

    return metrics

def calculate_cagr(start_value: float, end_value: float, years: int) -> Optional[float]:
    """计算复合年增长率"""
    if start_value <= 0 or end_value <= 0 or years <= 0:
        return None
    return (end_value / start_value) ** (1 / years) - 1

def calculate_solvency(data: FinancialData) -> dict:
    """计算偿债能力指标"""
    metrics = {}

    # 资产负债率
    if data.total_assets > 0:
        metrics['debt_to_assets'] = data.total_liabilities / data.total_assets

    # 流动比率
    if data.current_liabilities > 0:
        metrics['current_ratio'] = data.current_assets / data.current_liabilities

    # 速动比率
    if data.current_liabilities > 0:
        metrics['quick_ratio'] = (data.current_assets - data.inventory) / data.current_liabilities

    # 利息保障倍数
    if data.interest_expense > 0 and data.ebit != 0:
        metrics['interest_coverage'] = data.ebit / data.interest_expense

    # 净负债率
    if data.equity > 0:
        net_debt = data.interest_bearing_debt - data.cash
        metrics['net_debt_to_equity'] = net_debt / data.equity

    return metrics

def calculate_efficiency(data: FinancialData, prev_data: Optional[FinancialData] = None) -> dict:
    """计算运营效率指标"""
    metrics = {}

    # 使用平均值（如有上期数据）
    avg_ar = data.accounts_receivable
    avg_inv = data.inventory
    avg_ap = data.accounts_payable

    if prev_data:
        avg_ar = (data.accounts_receivable + prev_data.accounts_receivable) / 2
        avg_inv = (data.inventory + prev_data.inventory) / 2
        avg_ap = (data.accounts_payable + prev_data.accounts_payable) / 2

    # 应收周转天数
    if data.revenue > 0 and avg_ar > 0:
        metrics['dso'] = 365 / (data.revenue / avg_ar)

    # 存货周转天数
    if data.cost_of_revenue > 0 and avg_inv > 0:
        metrics['dio'] = 365 / (data.cost_of_revenue / avg_inv)

    # 应付周转天数
    if data.cost_of_revenue > 0 and avg_ap > 0:
        metrics['dpo'] = 365 / (data.cost_of_revenue / avg_ap)

    # 现金周期
    if 'dso' in metrics and 'dio' in metrics and 'dpo' in metrics:
        metrics['ccc'] = metrics['dso'] + metrics['dio'] - metrics['dpo']

    # 总资产周转率
    if data.total_assets > 0:
        metrics['asset_turnover'] = data.revenue / data.total_assets

    return metrics

def calculate_cash_flow(data: FinancialData) -> dict:
    """计算现金流指标"""
    metrics = {}

    # 经营现金流/净利润
    if data.net_income != 0:
        metrics['ocf_to_net_income'] = data.operating_cash_flow / data.net_income

    # 自由现金流
    metrics['fcf'] = data.operating_cash_flow - data.capex

    # 自由现金流/营收
    if data.revenue > 0:
        metrics['fcf_margin'] = metrics['fcf'] / data.revenue

    return metrics

def format_metrics(metrics: dict) -> dict:
    """格式化指标输出"""
    formatted = {}
    for key, value in metrics.items():
        if isinstance(value, float):
            if 'margin' in key or 'roe' in key or 'roa' in key or 'roic' in key or 'yoy' in key or 'ratio' in key.lower():
                formatted[key] = f"{value:.2%}"
            elif 'dso' in key or 'dio' in key or 'dpo' in key or 'ccc' in key:
                formatted[key] = f"{value:.1f} 天"
            else:
                formatted[key] = f"{value:,.2f}"
        else:
            formatted[key] = value
    return formatted

def calculate_all_metrics(data: FinancialData, prev_data: Optional[FinancialData] = None) -> dict:
    """计算所有财务指标"""
    all_metrics = {
        '盈利能力': calculate_profitability(data),
        '偿债能力': calculate_solvency(data),
        '运营效率': calculate_efficiency(data, prev_data),
        '现金流': calculate_cash_flow(data),
    }

    if prev_data:
        all_metrics['成长性'] = calculate_growth(data, prev_data)

    # 格式化输出
    formatted = {}
    for category, metrics in all_metrics.items():
        formatted[category] = format_metrics(metrics)

    return formatted

def main():
    # 示例用法
    example_data = FinancialData(
        revenue=100_000_000,
        cost_of_revenue=60_000_000,
        gross_profit=40_000_000,
        operating_profit=25_000_000,
        net_income=20_000_000,
        total_assets=200_000_000,
        total_liabilities=80_000_000,
        equity=120_000_000,
        current_assets=50_000_000,
        current_liabilities=30_000_000,
        inventory=15_000_000,
        accounts_receivable=20_000_000,
        accounts_payable=10_000_000,
        operating_cash_flow=25_000_000,
        capex=5_000_000,
        interest_expense=2_000_000,
        interest_bearing_debt=50_000_000,
        cash=30_000_000,
        ebit=27_000_000,
    )

    metrics = calculate_all_metrics(example_data)
    print(json.dumps(metrics, ensure_ascii=False, indent=2))

if __name__ == "__main__":
    main()
