import pandas as pd
import numpy as np

m = np.random.randint(1, 30, size=(5,3))

df1 = pd.DataFrame(m, columns=["vari", "“var2", "var3"])
df2 = df1 + 99

pd.concat([df1, df2], ignore_index=True)

#merge

df3 = pd.DataFrame({'employees': ['john', 'dennis', 'mark', 'maria'],
'group': ['accounting', 'engineering', 'engineering', 'hr']})

df4 = pd.DataFrame({'employees': ['mark', 'john', 'dennis', 'maria'],
'start_date': [2010, 2009, 2014, 2019]})

df5 = pd.merge(df3, df4, on="employees")

df6 = pd.DataFrame({'group': ['accounting', 'engineering', 'hr'],
'manager': ['Caner', 'Mustafa', 'Berkcan']})

pd.merge(df5, df6)
