import pandas as pd
import seaborn as sns

df = sns.load_dataset("titanic")

df["age2"] = df["age"]*2
df["age5"] = df["age"]*5

(df["age2"]/10).head()
(df["age5"]/10).head()

for col in df.columns:
    if "age" in col:
        print(((df[col]/10).head()))

df[["age", "age2"]].apply(lambda x: x/10).head()

df.loc[:, df.columns.str.contains("age")].apply(lambda x: x/10).head()

df.loc[:, df.columns.str.contains("age")].apply(lambda x: (x - x.mean())).head()

def standart_scaler(col):
    return (col - col.mean()) / col.std()

df.loc[:, df.columns.str.contains("age")].apply(standart_scaler).head()

df.loc[:, df.columns.str.contains("age")] = df.loc[:, df.columns.str.contains("age")].apply(standart_scaler).head()
df.head()