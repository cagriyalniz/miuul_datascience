import pandas as pd
import seaborn as sns

df = sns.load_dataset("titanic")
df.head()

df[df["age"] > 50].head()
df[df["age"] > 50]["age"].count()

df.loc[df["age"] > 50, "class"].head()

df.loc[df["age"] > 50, ["age", "class"]].head()


df.loc[(df["age"] > 50) & (df["sex"] =="male"), ["age", "class"]].head()


df.loc[(df["age"] > 50) & (df["sex"] =="male") & ((df["class"] == "First")  | (df["class"] == "Second")), ["age", "class"]].head()


df_new = df.loc[(df["age"] > 50) & (df["sex"] =="male") & ((df["class"] == "First")  | (df["class"] == "Second")), ["age", "class"]].head()

df_new["class"].value_counts()
