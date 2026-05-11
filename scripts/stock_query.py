#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
股票查询脚本 - 使用 tushare 获取 A 股实时行情
用法：python3 stock_query.py
"""

import tushare as ts
import json
import os
import sys
from datetime import datetime

# 从配置文件加载关注股票列表，优先 ~/.hermes/stock-watchlist.json，fallback 到本地配置
STOCKS = {}

def load_watchlist():
    """加载关注股票列表"""
    global STOCKS
    
    # 优先读取 ~/.hermes/stock-watchlist.json
    hermes_watchlist = os.path.expanduser("~/.hermes/stock-watchlist.json")
    local_watchlist = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../stock-watchlist.json")
    
    for path in [hermes_watchlist, local_watchlist]:
        if os.path.exists(path):
            try:
                with open(path, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    STOCKS = {item["code"]: item["name"] for item in data.get("stocks", [])}
                    return
            except Exception as e:
                print(f"Warning: Failed to load watchlist from {path}: {e}")
    
    # 如果都没找到，使用默认示例（仅用于演示）
    STOCKS = {
        '000001': '平安银行',  # 示例，请在配置文件中替换为自己的关注列表
    }

load_watchlist()

def query_stocks(codes=None):
    """查询股票实时行情
    Args:
        codes: 传入的个股代码列表，为 None 时读取 watchlist
    """
    if codes is None:
        codes = list(STOCKS.keys())
    
    # 去重并保持顺序
    seen = set()
    codes = [c for c in codes if not (c in seen or seen.add(c))]
    
    if not codes:
        print("没有需要查询的股票代码")
        return []
    
    df = ts.get_realtime_quotes(codes)
    
    results = []
    for _, row in df.iterrows():
        code = row['code']
        # 优先从 watchlist 取名称，其次从 tushare 返回，最后兜底
        name = STOCKS.get(code, row['name'] if row['name'] != '--' else code)
        price = float(row['price']) if row['price'] != '--' else 0
        pre_close = float(row['pre_close']) if row['pre_close'] != '--' else 0
        change = price - pre_close if pre_close > 0 else 0
        change_pct = (change / pre_close * 100) if pre_close > 0 else 0
        
        results.append({
            'code': code,
            'name': name,
            'price': price,
            'change': round(change, 2),
            'change_pct': round(change_pct, 2),
            'volume': int(row['volume']),
            'amount': int(float(row['amount'])) if row['amount'] != '--' else 0,
            'bid': float(row['bid']) if row['bid'] != '--' else 0,
            'ask': float(row['ask']) if row['ask'] != '--' else 0,
            'time': row['time'],
            'date': row['date']
        })
    
    return results

def format_report(results):
    """格式化报告"""
    lines = []
    lines.append("📈 **股票行情报告**")
    lines.append(f"**查询时间**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    lines.append("")
    lines.append("| 代码 | 名称 | 现价 | 涨跌 | 涨跌幅 | 成交量 |")
    lines.append("|------|------|------|------|--------|--------|")
    
    for stock in results:
        change_str = f"+{stock['change']:.2f}" if stock['change'] >= 0 else f"{stock['change']:.2f}"
        change_pct_str = f"+{stock['change_pct']:.2f}%" if stock['change_pct'] >= 0 else f"{stock['change_pct']:.2f}%"
        volume_str = f"{stock['volume']:,}"
        
        lines.append(f"| {stock['code']} | {stock['name']} | {stock['price']:.2f} | {change_str} | {change_pct_str} | {volume_str} |")
    
    lines.append("")
    
    # 投资建议
    lines.append("**📊 简要分析**:")
    
    # 计算整体涨跌情况
    up_count = sum(1 for s in results if s['change'] > 0)
    down_count = sum(1 for s in results if s['change'] < 0)
    
    lines.append(f"- 今日涨跌比：{up_count} 涨 {down_count} 跌")
    
    # 找出表现最好和最差的股票
    best = max(results, key=lambda x: x['change_pct'])
    worst = min(results, key=lambda x: x['change_pct'])
    
    lines.append(f"- 表现最佳：{best['name']} ({best['change_pct']:+.2f}%)")
    lines.append(f"- 表现最差：{worst['name']} ({worst['change_pct']:+.2f}%)")
    
    lines.append("")
    lines.append("*数据来源：tushare (新浪财经)*")
    
    return "\n".join(lines)

if __name__ == "__main__":
    # 支持命令行传入个股代码，比如：python3 stock_query.py 000001 600519
    # 无参数时读取 watchlist
    if len(sys.argv) > 1:
        codes_from_args = sys.argv[1:]
        results = query_stocks(codes=codes_from_args)
    else:
        results = query_stocks()
    
    if not results:
        sys.exit(1)
    
    report = format_report(results)
    print(report)
    
    # 同时输出 JSON 格式供程序使用
    print("\n--- JSON DATA ---")
    print(json.dumps({
        'timestamp': datetime.now().isoformat(),
        'stocks': results
    }, ensure_ascii=False, indent=2))
