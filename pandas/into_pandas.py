import pandas as pd
import numpy as np
a = np.random.randint(0, 11, size= 100)

s = pd.Series(a)
type(s)
s.index
s.dtype
s.size
s.ndim
s.values
type(s.values)
s.head(9)
s.tail(9)

