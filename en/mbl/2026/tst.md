# Test

```python
import util as u
import pandas as pd
pd.set_option('display.max_columns', None)
```

```python
df = u.get_pd().read_csv("/opt/Downloads/usd_oil_ir.csv", \
                          index_col="Date", parse_dates=True)

lookback = 100

df =  (df - df.rolling(window=lookback).mean()) / \
    df.rolling(window=lookback).std()
df['crash_ind'] = df.sum(axis=1).rolling(window=lookback*2).mean()

df['crash_ind'].plot()

u.plot_crises()

plt.savefig('/tmp/out.jpg')
```




