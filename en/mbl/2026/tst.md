# Test

```python
import util as u
import pandas as pd
pd.set_option('display.max_columns', None)
```

```python
u.get_fred(1980, "APU000072610").plot(title='Average Price: Electricity per Kilowatt-Hour in U.S. City Average',grid=True)
plt.savefig('out1.jpg')
```




















