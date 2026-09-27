# Test

```python
import util as u
import pandas as pd
pd.set_option('display.max_columns', None)
```

```python
u.get_fred(2020,['DGS10']).plot()
plt.savefig('/tmp/out1.jpg')
```































