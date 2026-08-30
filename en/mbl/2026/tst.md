# Test

```python
import util as u
import pandas as pd
pd.set_option('display.max_columns', None)
```

```python
df = u.get_fred(2000,['DGS2','FEDFUNDS']).interpolate()
```

```python
df['diff'] = df.DGS2 - df.FEDFUNDS
print (df['diff'])
df['diff'].plot()
plt.axvspan('2001-01-01','2001-01-01',color='y')
plt.axvspan('2009-01-01','2009-01-01',color='y')
plt.axvspan('2017-01-01','2017-01-01',color='y')
plt.axvspan('2021-01-01','2021-01-01',color='y')
plt.savefig('/tmp/out.jpg')
```

```text
2000-01-01         NaN
2000-01-03    0.917273
2000-01-04    0.824545
2000-01-05    0.891818
2000-01-06    0.849091
                ...   
2026-08-21    0.610000
2026-08-24    0.610000
2026-08-25    0.540000
2026-08-26    0.560000
2026-08-27    0.570000
Name: diff, Length: 7046, dtype: float64
```














