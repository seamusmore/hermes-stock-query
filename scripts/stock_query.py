#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
股票查询脚本 - 使用 tushare 获取 A 股实时行情
用法：python3 stock_query.py
"""

import tushare as ts
import json
from datetime import datetime

# 股票列表
STOCKS = {
    '002544': '普天科技',
    '600036': '招商银行',
    '603899': '晨光股份',
    '600879': '航天电子',
    '000002': '万科 A',
    '510300': '沪深 300ETF 华夏',
    '510330': '沪深 300ETF 华泰柏瑞'
}

def query_stocks():
    """查询所有股票实时行情"""
    df = ts.get_realtime_quotes(list(STOCKS.keys()))
    
    results = []
    for _, row in df.iterrows():
        code = row['code']
        name = STOCKS.get(code, row['name'])
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
    results = query_stocks()
    report = format_report(results)
    print(report)
    
    # 同时输出 JSON 格式供程序使用
    print("\n--- JSON DATA ---")
    print(json.dumps({
        'timestamp': datetime.now().isoformat(),
        'stocks': results
    }, ensure_ascii=False, indent=2))
