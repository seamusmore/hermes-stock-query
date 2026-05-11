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

Or copy from the example file:

```bash
cp stock-watchlist.json.example ~/.hermes/stock-watchlist.json
# Then edit to replace with your own stocks
```

### Dependencies

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
- "\u67e5\u4e00\u4e0b\u80a1\u7968"
- "\u80a1\u7968\u884c\u60c5"
- "stock"
- "\u884c\u60c5"

## Cron Schedule

- **Trading day 9:35** \u2014 Morning check
- **Trading day 13:35** \u2014 Afternoon check
- **Non-trading day** \u2014 Auto skip with holiday notice

## License

MIT
