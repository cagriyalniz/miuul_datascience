import random

# Görev 2: Verilen string ifadenin tüm harflerini büyük harfe çeviriniz.
# Virgül ve nokta yerine space koyunuz,
# kelime kelime ayırınız

def capital(string):
    new_str = ""


    new_str = string.upper()
    new_str = new_str.replace(","," ")
    new_str = new_str.replace(".", " ")
    new_str = new_str.split()
    return new_str

print(capital("türkiye seninle gurur duyuyor,türkiye senden umutlu."))

#----------------------------------------------------------------------

# Görev 3: Verilen listeye aşağıdaki adımları uygulayınız.
# Adım 1: Verilen listenin eleman sayısına bakınız.
# Adım 2: Sıfırıncı ve üçüncü indeksteki elemanları çağırınız.
# Adım 3: Verilen liste üzerinden ["D", "A", "T", "A"] listesi oluşturunuz.
# Adım 4: İkinci indeksteki elemanı siliniz.
# Adım 5: Yeni bir eleman ekleyiniz.
# Adım 6: İkinci indekse "N" elemanını tekrar ekleyiniz.

def lst_edit(lst):
    len(lst)
    print(lst[2])
    new_list = lst[:3]
    print(new_list)
    lst.remove(lst[1])
    print((lst))
    lst.append("bilgisayar")
    print(lst)
    lst.insert(1,"topu")
    print(lst)



lst = ["ali","topu","attı"]
lst_edit(lst)


#----------------------------------------------------------------------

# Görev 4: Verilen sözlük yapısına aşağıdaki adımları uygulayınız.
# Adım 1: Key değerlerine erişiniz.
# Adım 2: Value'lara erişiniz.
# Adım 3: Daisy key'ine ait 12 değerini 13 olarak güncelleyiniz.
# Adım 4: Key değeri Ahmet value değeri [Turkey,24] olan yeni bir değer ekleyiniz.
# Adım 5: Antonio'yu dictionary'den siliniz.

def dictionary(dict):
    dict.keys()
    dict.values()
    dict['cagri'][1] = 26

    dict.get('cagri')

    dict['ahmet'] = ['ankara',18]

    dict.pop("cagri")
    print((dict))



dict = {  'yasir' : ["trabzon",21],
          'cagri' : ["artvin",27]
          }

dictionary(dict)


#----------------------------------------------------------------------
# Görev 5: Argüman olarak bir liste alan, listenin içerisindeki tek ve çift sayıları
# ayrı listelere atayan ve bu listeleri
# return eden fonksiyon yazınız.

def even_odd(data):
    even_list = [ ]
    odd_list = [ ]
    for i in data:
        if i % 2 == 0:
            even_list.append(i)
        else:
            odd_list.append(i)

    return even_list,odd_list



data = [ ]
import random

for i in range(100):
    data.append(random.randint(-1000,1000))
lst1,lst2 = even_odd(data)

print(lst1)
print(lst2)


#----------------------------------------------------------------------
# Görev 6: Aşağıda verilen listede mühendislik ve tıp fakülterinde
# dereceye giren öğrencilerin isimleri
# bulunmaktadır. Sırasıyla ilk üç öğrenci mühendislik fakültesinin başarı sırasını
# temsil ederken son üç öğrenci de
# tıp fakültesi öğrenci sırasına aittir. Enumarate kullanarak öğrenci derecelerini fakülte
# özelinde yazdırınız.

def uni(data):
    for i,stu in enumerate(data):
        if i < 3:
            print("MF",i+1,". öğrenci : ",stu)
        else:
            print("tıp", (i %3)+1, ". öğrenci : ", stu)



data = ['ali','ayşe','kazım','veli', 'zeynep', 'mustafa']
uni(data)




#----------------------------------------------------------------------
# Görev 7: Aşağıda 3 adet liste verilmiştir.
# Listelerde sırası ile bir dersin kodu, kredisi ve kontenjan bilgileri yer
# almaktadır. Zip kullanarak ders bilgilerini bastırınız.

ders_kod = ["123","234"]
ders_kredi = [3,4]
ders_kontejan = [25,14]
sonuc = list(zip(ders_kredi,ders_kod,ders_kontejan))

for i, k ,j in sonuc:
    print("Kredisi {} olan dersin kodu {} ve kontenjanı {} dır".format(i,k,j))


def subset(set1,set2):
    if set2.issubset(set1):
        print(set2)
    else:
        print(set2.difference(set1))

#----------------------------------------------------------------------
# Görev 8: Aşağıda 2 adet set verilmiştir.
# Sizden istenilen eğer 1. küme 2. kümeyi kapsiyor ise ortak elemanlarını
# eğer kapsamıyor ise 2. kümenin 1. kümeden farkını yazdıracak fonksiyonu tanımlamanız beklenmektedir.


set1 = set([10,20,30])
set2 = set([10,20])
set3 = set([45,78])


subset(set1,set2)
subset(set1,set3)