from openbb import obb
from openbb_equity.fundamental.fundamental_router import metrics

obb.user.preferences.output_type = "dataframe"

data = obb.equity.price.historical(symbol="SPY", provide="yfinance")
funda_data = obb.equity.fundamental.metrics(symbol="AMZN,GOOG", provide="yfinance")
print(data)
print(funda_data)

screener = obb.equity.compare.groups(
    group="industry",
    metric="valuation",
    provide="finviz"
)
print(screener)

screener = obb.equity.compare.groups(
    group="technology",
    metric="performance",
    provide="finviz"
)
print(screener)

screener = obb.equity.compare.groups(
    group="sector",
    metric="overview",
    provide="finviz"
)
print(screener)