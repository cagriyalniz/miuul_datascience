import numpy as np

a = np.array([1, 2, 3])
b = np.array([3, 2, 1])
print(a*b)

np.zeros(10, dtype=str)
np.random.randint(-4, 100, size = 4)
np.random.normal(10, 3, (4, 3))

#numpy array ozellikleri

# ndim: boyut sayis1
# shape: boyut bilgisi
# size: toplam eleman sayis1
# dtype: array veri tipi

a = np.random.randint(10, size=5)
a.ndim
a.shape
a.size
a.dtype

#reshaping

b = np.random.randint(1, 10, size=9)
b.reshape(3, 3)#3*3 = 9

#index islemleri

#index slice
c = np.random.randint(10, size=10)
print(c)
print(c[0])
print(c[0:3])
c[3] = 5555.5
print(c)

d = np.random.randint(0, 88, size=(3,3))
print(d)
print(d[1:, :1])

#fancy index
e = np.arange(0, 30, 3)
print(e)

catch = [1, 2, 3]
e[catch]


#kosullu eleman secme

f = np.arange(-1, 99, 7)
print(f)
print(f[f < 19])

#matematiksel islemler

g = np.arange(-10, 10, 5)
print(g)
print(g / 5)

np.subtract(g, 1)#cikarma
np.add(g, 1)
np.mean(g)
np.sum(g)
np.min(g)
np.max(g)
np.var(g)#varyans


#iki bilinmeyenli denklem cozumu

#5*X0 + X1 = 12
#X0 + 3*X1 = 10

a = np.array([[5, 1], [1, 3]])
b = np.array([12, 10])

print(np.linalg.solve(a, b))