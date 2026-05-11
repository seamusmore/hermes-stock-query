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

## Configuration

### Watchlist

Create `~/.hermes/stock-watchlist.json` with your own stocks:

```json
{
  "stocks": [
    {"code": "000001", "name": "平安银行"},
    {"code": "600519", "name": "贵州茅台"}
  ]
}
```

Or copy from `stock-watchlist.json.example` and edit.

## 命令

### 方式一：无参数（读取 watchlist）

```bash
python3 {baseDir}/scripts/stock_query.py
```

### 方式二：传入个股代码（直接查询）

```bash
python3 {baseDir}/scripts/stock_query.py 000001 600519 002594
```

- 支持后跟多个股票代码，自动去重
- 如果代码在 watchlist 中有名称，优先显示 watchlist 名称
- 不在 watchlist 中的代码会用 tushare 返回的名称兜底

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
