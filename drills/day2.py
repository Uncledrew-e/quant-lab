import numpy as np
import pandas as pd

rng = np.random.default_rng(42)
dates = pd.bdate_range("2022-01-03", periods=750)
rets = rng.normal(0.0004, 0.012, len(dates))
close = pd.Series(100 * np.exp(rets.cumsum()), index=dates, name="close")
df = close.to_frame()

table = pd.DataFrame({
    "ret": rets,
    "cumsum": rets.cumsum(),
    "close": 100 * np.exp(rets.cumsum()),
}, index=dates)

pd.set_option("display.precision", 6)
print(table.head(5))


df["ret"] = df["close"].pct_change()
print(df.head())