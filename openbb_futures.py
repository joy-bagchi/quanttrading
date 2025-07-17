import pandas as pd
from openbb import obb
from matplotlib import pyplot as plt

obb.user.preferences.output_type = "dataframe"
vix = obb.derivatives.futures.curve(symbol="VIX", provide="yfinance")
print(vix)
vix.index = pd.to_datetime(vix.expiration)
vix.plot()
plt.show()