#LIST COMPHERESION

#Görev 1: List Comprehension yapısı kullanarak car_crashes verisindeki numeric değişkenlerin isimlerini büyük
#harfe çeviriniz ve başına NUM ekleyiniz.

#----------------------------------------------------------------
#research with ai:
#df.columns'un her bir değerinin tipini öğrenmek istiyorum. hangileri numeric nasıl bulabilirim?
import seaborn as sns
df = sns.load_dataset("car_crashes")
print(df.dtypes)

#bunu bir comprehensions içinde nasıl gösterebilirim?
#sadece numeric degiskenleri gosteren compheresion
numeric_columns = [column for column in df.columns if df[column].dtype != 'object']#chatgpt 'object yerine 'category' yazdiriyor. bu da yanlis bir sonuc almamıza neden oluyor
print(numeric_columns)

#numeric olanları büyük harf olmayanları küçük harf göstermek istersem ne yapmalıyım?
upper_for_numeric = [column.upper() if df[column].dtype != "object" else column.lower()for column in df.columns]
print(upper_for_numeric)
#----------------------------------------------------------------

#cevap:
new_df_columns = [c.upper() if df[c].dtype == 'object' else f"NUM_{c.upper()}" for c in df.columns]
print(new_df_columns)


#Görev 2: List Comprehension yapısı kullanarak car_crashes verisinde isminde "no" barındırmayan
#değişkenlerin isimlerinin sonuna "FLAG" yazınız.


flag_for_withtout_no = [c.upper() if "no" in c else f"{c.upper()}_FLAG" for c in df.columns]
flag_for_withtout_no2 = [f"{c.upper()}_FLAG" if "no" not in c else c.upper() for c in df.columns]
print(flag_for_withtout_no)
print(flag_for_withtout_no2)

#Görev 3: List Comprehension yapısı kullanarak aşağıda verilen değişken isimlerinden FARKLI olan
#değişkenlerin isimlerini seçiniz ve yeni bir dataframe oluşturunuz.

og_list = ["abbrev", "no_previous"]

without_og = df[[c  for c in df.columns if c not in og_list]]
print(without_og.head())

#------------------------------------------------------------------------------
#PANDAS

#Görev 1: Seaborn kütüphanesi içerisinden Titanic veri setini tanımlayınız.
import seaborn as sns
df = sns.load_dataset("titanic")
print(df)

#Görev 2: Titanic veri setindeki kadın ve erkek yolcuların sayısını bulunuz.
gender_count = df['sex'].value_counts()
print(gender_count)

women_count = gender_count["female"]
print(women_count)

men_count = gender_count["male"]
print(men_count)

female_count = sum(df['sex'] == 'female')
print(female_count)

male_count = sum(df['sex'] == 'male')
print(male_count)

#Görev 3: Her bir sutuna ait unique değerlerin sayısını bulunuz.

for col in df.columns:
    uniq_val = df[col].nunique()
    print(f"{col} {uniq_val}")

for col in df.columns:
    print(f"{col} -> {df[col].nunique()}")

#Görev 4: pclass değişkeninin unique değerlerinin sayısını bulunuz.

for col in df.columns:
    if col == "pclass":
        print(df[col].nunique())

#Görev 5: pclass ve parch değişkenlerinin unique değerlerinin sayısını bulunuz.

for col in df.columns:
    if col == "parch":
        print(df[col].nunique())

#Görev 6: embarked değişkeninin tipini kontrol ediniz. Tipini category olarak değiştiriniz ve tekrar kontrol ediniz.

print(df["embarked"].dtype)
df["embarked"] = df["embarked"].astype('category')
print(df["embarked"].dtype)

#Görev 7: embarked değeri C olanların tüm bilgelerini gösteriniz.

for index, col in df.iterrows():
    if col["embarked"] == "C":
        print(f"index: {index} \n{col}")

#Görev 8: embarked değeri S olmayanların tüm bilgelerini gösteriniz.

for index, col in df.iterrows():
    if col["embarked"] != "S":
        print(f"index: {index} \n{col}")


#Görev 9: Yaşı 30 dan küçük ve kadın olan yolcuların tüm bilgilerini gösteriniz.

for index, col in df.iterrows():
    if col["sex"] =="female" and col["age"] < 30:
        print(col)


#Görev 10: Fare'i 500'den büyük veya yaşı 70 den büyük yolcuların bilgilerini gösteriniz.

for index, col in df.iterrows():
    if col["fare"] > 500 and col["age"] > 70:
        print(col)


#
#