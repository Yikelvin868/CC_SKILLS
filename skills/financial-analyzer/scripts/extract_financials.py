#!/usr/bin/env python3
"""从 Excel/CSV 文件提取财务数据"""

import sys
import json
import pandas as pd
from pathlib import Path

def extract_from_excel(file_path: str, sheet_name: str = None) -> dict:
    """从 Excel 文件提取财务数据"""
    df = pd.read_excel(file_path, sheet_name=sheet_name)
    return df.to_dict(orient='records')

def extract_from_csv(file_path: str) -> dict:
    """从 CSV 文件提取财务数据"""
    df = pd.read_csv(file_path)
    return df.to_dict(orient='records')

def identify_financial_columns(df: pd.DataFrame) -> dict:
    """识别常见财务数据列"""
    mappings = {
        '营收': ['营业收入', '营收', 'revenue', 'sales', '总收入'],
        '净利润': ['净利润', 'net income', 'net profit', '归母净利润'],
        '毛利润': ['毛利润', '毛利', 'gross profit'],
        '总资产': ['总资产', 'total assets', '资产总计'],
        '总负债': ['总负债', 'total liabilities', '负债总计'],
        '股东权益': ['股东权益', 'equity', '所有者权益', '净资产'],
        '经营现金流': ['经营活动现金流', 'operating cash flow', 'CFO'],
        '资本支出': ['资本支出', 'capex', '购建固定资产'],
    }

    found = {}
    columns_lower = {col.lower(): col for col in df.columns}

    for key, patterns in mappings.items():
        for pattern in patterns:
            if pattern.lower() in columns_lower:
                found[key] = columns_lower[pattern.lower()]
                break

    return found

def main():
    if len(sys.argv) < 2:
        print("用法: python extract_financials.py <file_path> [sheet_name]")
        sys.exit(1)

    file_path = sys.argv[1]
    sheet_name = sys.argv[2] if len(sys.argv) > 2 else None

    path = Path(file_path)
    if not path.exists():
        print(f"错误: 文件不存在 {file_path}")
        sys.exit(1)

    if path.suffix.lower() in ['.xlsx', '.xls']:
        data = extract_from_excel(file_path, sheet_name)
    elif path.suffix.lower() == '.csv':
        data = extract_from_csv(file_path)
    else:
        print(f"错误: 不支持的文件格式 {path.suffix}")
        sys.exit(1)

    print(json.dumps(data, ensure_ascii=False, indent=2))

if __name__ == "__main__":
    main()
