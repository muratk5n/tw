# Test

```python
import pandas as pd
pd.read_csv('debtgdp.csv',index_col='Year').plot()
plt.ylim(0,130)
plt.savefig('/tmp/out1.jpg')
```





