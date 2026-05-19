# Test

```python
import util as u
import pandas as pd
pd.set_option('display.max_columns', None)
```

```python
df = u.get_yahoo_tickers(2024, ["XAR"])
df.plot(title='State Street S&P Aerospace & Defense ETF')
print ((df/df.shift(252)-1).tail(3))
plt.savefig('/tmp/out.jpg')
```

```text
                 XAR
2026-05-12  0.519799
2026-05-13  0.505674
2026-05-14  0.488696
```



