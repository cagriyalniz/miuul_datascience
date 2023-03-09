import pandas as pd
import seaborn as sns
import numpy as np

df = pd.read_csv("pandas/advertising.csv")
df.head()


df2 = sns.load_dataset("titanic")
df2.info()


arr = df2.head(20).to_numpy()
sum = 0
print(arr[0:,:1])
sum = np.sum(arr[:,0])
print(sum)

df2.columns
df2.index

df2.describe().T

#herhangi birinde null var mi
df2.isnull()
df2.isnull().values.any()
#hangi degiskende kac eksik var
df2.isnull().sum()
#kategorik degiskenlerin kac tipte oldugu/kadin-erkek
df2["sex"].head()
df2["sex"].value_counts()



