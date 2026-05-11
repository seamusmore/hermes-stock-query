# stock-query

A 股股票实时行情查询技能，使用 tushare 数据源（新浪财经）。

## Features

- A 股实时行情查询
- 支持 watchlist 配置文件
- 支持命令行直接传入个股代码
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
    {"code": "000001", "name": "平安银行"},
    {"code": "600519", "name": "贵州茅台"}
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

**方式一：无参数（读取 watchlist）**

```bash
python3 scripts/stock_query.py
```

**方式二：传入个股代码（直接查询）**

```bash
python3 scripts/stock_query.py 000001 600519 002594
```

- 支持后跟多个股票代码，自动去重
- 如果代码在 watchlist 中有名称，优先显示 watchlist 名称
- 不在 watchlist 中的代码会用 tushare 返回的名称兜底

### Hermes Skill

Skill name: `stock-query`

Triggers:
- "查一下股票"
- "股票行情"
- "stock"
- "行情"

## License

MIT
