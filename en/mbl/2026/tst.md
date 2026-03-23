# Test

```python
import util as u
import pandas as pd
pd.set_option('display.max_columns', None)
```

```python
df = u.get_fred(2026,"GASREGW").plot(title="Gasoline Price - $/gallon")
```


