# stock-query

A 股股票实时行情查询技能，使用 tushare 数据源（新浪财经）。支持 7 只关注股票，自动判断交易日。

## Features

- A 股实时行情查询
- 自动判断交易日/非交易日
- 涨跌比、表现最佳/最差分析
- Markdown 格式化输出

## Installation

### Recommended (via Hermes CLI)

```bash
hermes skills install https://github.com/seamusmore/hermes-stock-query.git
```

Then restart the gateway for the skill to take effect.

### Manual (alternative)

```bash
# Clone into Hermes skills directory
git clone https://github.com/seamusmore/hermes-stock-query.git \
  ~/.hermes/skills/stock-query
```

## Dependencies

```bash
pip3 install tushare --user
```

## Usage

### Script

```bash
python3 scripts/stock_query.py
```

### Hermes Skill

Skill name: `stock-query`

Triggers:
- "查一下股票"
- "股票行情"
- "stock"
- "行情"

## Watchlist

| Code | Name |
|------|------|
| 002544 | 普天科技 |
| 600036 | 招商银行 |
| 603899 | 晨光股份 |
| 600879 | 航天电子 |
| 000002 | 万科 A |
| 510300 | 沪深300ETF 华夏 |
| 510330 | 沪深300ETF 华泰柏瑞 |

## Cron Schedule

- **Trading day 9:35** — Morning check
- **Trading day 13:35** — Afternoon check
- **Non-trading day** — Auto skip with holiday notice

## License

MIT
