import pandas as pd
import seaborn as sns

df = sns.load_dataset("titanic")
df.head()

df.index
df[0:13]

#silme
df.drop(0, axis=0).head()
delete_index = [1, 3, 5, 7]
df.drop(delete_index, axis=0).head()
#df.drop(delete_index, axis=0, inplace=True) inplace=True degisikligi kalici halde getirir

#degiskeni indexe cevirme

df["age"].head()
df.age.head()

df.index = df["age"]

df.drop("age", axis=1, inplace=True)

#indexi degiskene cevirme

df["age"] = df.index

df = df.reset_index()
df.head()