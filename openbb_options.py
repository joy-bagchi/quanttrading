from openbb import obb

obb.user.preferences.output_type = "dataframe"
spy_option_chain = obb.derivatives.options.chains(symbol="SPY")
print(spy_option_chain)
