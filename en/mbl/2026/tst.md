# Test

```python
import util as u
import pandas as pd
pd.set_option('display.max_columns', None)
```

```python
window=3
df = u.get_pd().read_csv("schiller.csv", index_col='Date', parse_dates=['Date']).sort_index()
df = df.resample('YE').last()
df['PE'] = df['S&P Comp P'] / df['Earnings E']
df['Div Yield %'] = (df['Dividends D'] / df['S&P Comp P']) * 100
df['E Growth'] = df['Earnings E'].pct_change().rolling(window).mean() * 100
denom = df['E Growth'] + df['Div Yield %']
df['PEGY'] = df['PE'] / denom

cols = ['S&P Comp P','Div Yield %','E Growth','PE','PEGY']
df[df.index > '1980-01-01']['PEGY'].plot(ylim=(0,5))
plt.axvspan('1990-09-01', '1991-07-01', color='y', alpha=0.5, lw=0)
plt.axvspan('2001-03-01', '2002-01-01', color='y', alpha=0.5, lw=0)
plt.axvspan('2007-12-22', '2009-05-09', color='y', alpha=0.5, lw=0)
plt.axvspan('2020-02-01', '2020-07-01', color='y', alpha=0.5, lw=0)

df[cols].tail(4)
```

```text
Out[1]: 
             S&P Comp P  Div Yield %   E Growth         PE      PEGY
Date                                                                
2023-12-31  4685.051500     1.500596  36.302089  24.346783  0.644049
2024-12-31  6010.908571     1.244941   2.638639  28.600222  7.364396
2025-12-31  6853.025455     1.160363  11.702018  28.479041  2.214134
2026-12-31  7450.032857     1.096682  15.489323  25.221168  1.520629
```

































