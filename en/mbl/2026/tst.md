# Test

```python
import util as u
import pandas as pd
pd.set_option('display.max_columns', None)
```

```python
df = u.get_pd().read_csv('../2024/prez.csv').set_index('year').sort_index()
df.net_approval.plot(title="Potus Net Approvals")
plt.savefig('/tmp/out.jpg')
```
