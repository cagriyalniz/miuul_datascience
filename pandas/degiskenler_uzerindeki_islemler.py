import pandas as pd
import seaborn as sns

df = sns.load_dataset("titanic")

"age" in df
df.age.head()

df["age"].head()
type(df["age"].head())#tip degisti series oldu

type(df[["age"]].head())#tip dataframe kaldi

df[["age", "alive"]]

col_name = ["age", "adult_male", "alive"]
df[col_name]

#data frame e degisken ekleme
df["age2"] = df["age"]**2

df.drop(col_name, axis=1).head()

#veri setinde belirli bir string ifadelerini silme
df.loc[:, ~df.columns.str.contains("age")].head()
