#dictionary ornekleri

# sözlük comprehension kullanarak her kelimenin uzunluğunu içeren bir sözlük oluştur
my_list = ['elma', 'armut', 'çilek', 'muz']
fruit_len = {v: len(v) for v in my_list}
print(fruit_len)


# sözlük comprehension kullanarak her elemanın karesini içeren bir sözlük oluştur
my_list2 = [1, 2, 3, 4, 5]
nbr_sqr = {v: v**2 for v in my_list2}
print(nbr_sqr)


# sözlük comprehension kullanarak her elemanı büyük harflere dönüştürerek bir sözlük oluştur
def plaka(city):
    city_plaka = {"istanbul": 34,
                "ankara": 6,
                "izmir": 35,
                "bursa": 16}
    return city_plaka.get(city)

my_city = ['istanbul', 'ankara', 'izmir', 'bursa']
city_up = {c: c.upper() + "-" + str(plaka(c)) for c in my_city}
print(city_up)



# sadece çift sayıların olduğu bir sözlük oluştur
fruit_dict2 = {'apple': 3, 'banana': 5, 'cherry': 7, 'kiwi': 2}
fruit_dict3 = {k: v*2  for (k, v) in fruit_dict2.items() if v % 2 == 0}
print(fruit_dict3)
fruit_dict4 = {k: v*2 if v % 2 == 0 else v*3 for (k, v) in fruit_dict2.items()}
print(fruit_dict4)


# key ve value değerlerini yer değiştiren yeni bir sözlük oluştur
fruit_dict5 = {'apple': 1, 'banana': 2, 'cherry': 3}
fruit_dict6 = {k: v for (v, k) in fruit_dict5.items()}
print(fruit_dict6)




#######################
 # Bir Veri Setindeki Deisken Îsimlerini Degiętirmek
#######################


# before:
 # ['total', 'speeding', 'alcohol', 'not_distracted', 'no_previous' , 'ins_premium', 'ins_losses']
# after:
# ['TOTAL', 'SPEEDING', 'ALCOHOL', 'NOT_DISTRACTED*, 'NO_PREVIOUS', 'INS_PREMIUM', 'INS_LOSSES',]

import seaborn as sns
df = sns.load_dataset("car_crashes")
up = [k.upper() for k in df.columns] 
print(up)


#H#####################
 # Îsminde "INS" olan degißkenlerin bașina FLAG digerlerine NO_FLAG eklemek istiyoruz.
######################

def first_three(word):
    if (word[0:3] =="INS"):
        return 1
    else:
        return 0

ins_flag_list = ["FLAG_" + c  if first_three(c) == 1 else "NO_FLAG_" + c for c in up]
#ins_flag_list = ["FLAG_" + c  if "INS" in c else "NO_FLAG_" + c for c in up]
print(ins_flag_list)


# Amaç key'i string, value'su aa1daki gibi bir liste olan sözlük olusturmak.

# Output:
# {'total': ['mean', 'min', 'max', 'var'],
#'speeding' : ['mean', 'min', 'max', 'var'],
#'alcohol': ['mean', 'min', 'max', 'var'],
#'not_distracted': ['mean', 'min', 'max', 'var'],
#'no_previous': ['mean', 'min', 'max', 'var'],
#'ins_premium*: ['mean', 'min', 'max', 'var'],
#'ins_losses' : [ [ mean', 'min', 'max', 'var'}



num_cols = {k for k in df.columns if df[k].dtype != "O"}# "O" -> object
soz = {}
agg_list = ['mean', 'min', 'max', 'var']
car_creash_dict_res = {key: agg_list for key in  num_cols}
df[num_cols].head()

df[num_cols].agg(car_creash_dict_res)