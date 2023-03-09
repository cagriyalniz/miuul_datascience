import pandas as pd
import seaborn as sns

#Integer Base Selection
#Label Base Selection

df = sns.load_dataset("titanic")
df.head()

df.iloc[0:3]
df.iloc[0, 0]

df.loc[0: 3]


df.iloc[0:3, 0:2]
df.loc[0:3, "age"]

col_names = ["age", "alive"]
df.loc[0:3,col_names]