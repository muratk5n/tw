# Test

```python
import util as u
import pandas as pd
pd.set_option('display.max_columns', None)
```

```python
import json
corr = json.loads(open("corridors2.json").read())
colors = {"BRI1": "red", "BRI2": "red", "Zenzagur": "red", "imec": "blue", "imec2": "blue",
          "imec3": "blue", "IDR": "purple", "INTSC": "orange", "Traditional Route": "black"}
u.map_coords([25,46], {}, lines=corr, zoom=3, colors=colors, outfile="map18.html")
```






```python
u.random_ufo_sighting()
```







