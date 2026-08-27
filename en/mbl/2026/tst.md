# Test

```python
import util as u
import pandas as pd
pd.set_option('display.max_columns', None)
```

```python
dfp = u.get_fred(2000,['POPTHM'])
dff = pd.read_csv('foreignb.csv',parse_dates=True,index_col='DATE')
df = dff.join(dfp, how='left').interpolate(method='bfill')
df['perc'] = (df.Count/10) / df.POPTHM 
df.perc.plot(grid='on',title='Percentage of Foreign-Born in US')
plt.axvline('2017-01-01', color='y')
plt.axvline('2021-01-01', color='y')
plt.savefig('/tmp/out.jpg')
```

