---
name: stock-query
description: A 股股票实时行情查询，使用 tushare 数据源。支持 7 只关注股票，自动判断交易日。
author: Luna
version: 1.0.0
triggers:
  - "股票查询"
  - "股价"
  - "stock"
  - "行情"
---

# 股票查询技能

查询 A 股实时行情，使用 tushare 数据源（新浪财经）。

## Installation

### 推荐（via Hermes CLI）

```bash
hermes skills install https://github.com/seamusmore/hermes-stock-query.git
```

Then restart the gateway for the skill to take effect.

### 手动

```bash
# Clone into Hermes skills directory
git clone https://github.com/seamusmore/hermes-stock-query.git \
  ~/.hermes/skills/stock-query
```

## Dependencies

```bash
pip3 install tushare --user
```

## 命令

```bash
python3 {baseDir}/scripts/stock_query.py
```

## 关注股票

| 代码 | 名称 |
|------|------|
| 002544 | 普天科技 |
| 600036 | 招商银行 |
| 603899 | 晨光股份 |
| 600879 | 航天电子 |
| 000002 | 万科 A |
| 510300 | 沪深300ETF 华夏 |
| 510330 | 沪深300ETF 华泰柏瑞 |

## 自动查询

- **交易日 9:35** — 早盘查询
- **交易日 13:35** — 午盘查询
- **非交易日** — 自动跳过，回复休市通知

## 输出格式

```markdown
📈 **股票行情报告**
**查询时间**: 2026-02-27 10:14:28

| 代码 | 名称 | 现价 | 涨跌 | 涨跌幅 | 成交量 |
|------|------|------|------|--------|--------|
| 002544 | 普天科技 | 31.86 | +0.02 | +0.06% | 4,281,900 |

**📊 简要分析**:
- 今日涨跌比：3 涨 2 跌
- 表现最佳：航天电子 (+0.73%)
- 表现最差：晨光股份 (-0.22%)
```

## 脚本位置

`{baseDir}/scripts/stock_query.py`
