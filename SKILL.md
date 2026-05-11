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
    {"code": "000001", "name": "\u5e73\u5b89\u94f6\u884c"},
    {"code": "600519", "name": "\u8d35\u5dde\u8305\u53f0"}
  ]
}
```

Or copy from `stock-watchlist.json.example` and edit.

## \u547d\u4ee4

```bash
python3 {baseDir}/scripts/stock_query.py
```

## \u81ea\u52a8\u67e5\u8be2

- **\u4ea4\u6613\u65e5 9:35** \u2014 \u65e9\u76d8\u67e5\u8be2
- **\u4ea4\u6613\u65e5 13:35** \u2014 \u5348\u76d8\u67e5\u8be2
- **\u975e\u4ea4\u6613\u65e5** \u2014 \u81ea\u52a8\u8df3\u8fc7\uff0c\u56de\u590d\u4f11\u5e02\u901a\u77e5

## \u8f93\u51fa\u683c\u5f0f

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
