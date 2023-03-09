import pandas as pd
import seaborn as sns

df = sns.load_dataset("titanic")

df.pivot_table("survived", "sex", "embarked")

df.pivot_table("survived", "sex", "embarked", aggfunc = "std")

df.pivot_table("survived", "sex", ["embarked", "class"])

df.pivot_table("survived", "sex", ["embarked", "class"])
#kategorik sınıflar degiskenlere cevrilirken tanımlanabiliyorsa orn: 0-18 yas cocuk..... cut kullanilir

df["new_age"]= pd.cut(df["age"], [0, 10, 18, 36, 99])

df.pivot_table("survived", "sex", ["new_age", "class"])

