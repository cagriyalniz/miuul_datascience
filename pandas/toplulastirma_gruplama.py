import pandas as pd
import seaborn as sns

df = sns.load_dataset("titanic")

df["age"].mean()



df.groupby("sex").agg({"age" : "mean"})
df.groupby("sex").agg({"age" : ["mean", "sum"]})

df.groupby("sex").agg({"age" : ["mean", "sum"],
                        "survived": "mean"})



df.groupby(["sex", "embark_town"]).agg({"age" : ["mean"],
                        "survived": "mean"})



df.groupby(["sex", "embark_town", "class"]).agg({"age" : ["mean"],
                        "survived": "mean"})




df.groupby(["sex", "embark_town", "class"]).agg({
    "age" : ["mean"],
    "survived": "mean",
    "sex":"count"})