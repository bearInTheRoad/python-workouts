import numpy as np
from math import pi

a = np.array(range(15)).reshape(3, 5)
print(a.shape)
print(a.ndim)
print(a.size)
print(a.dtype)
print(a.itemsize)
print(a.data)

print(np.array([2, 3, 4]))
print(np.array([1.2, 3.4, 5.6]).dtype)


b = np.ones((2, 3, 4))
print(b.ndim)
print(b)

c = np.empty((2, 3))
print(c)


d = np.arange(1, 3, 1)
print(d)

e = np.linspace(3, 5, 3)
print(e)

print("-------------")
rg = np.random.default_rng(1)
a = np.ones((2, 3), dtype=np.int_)
b = rg.random((2, 3))
a *= 3
b += a
print(a)
print(b)

print("-------------")
a = np.ones(3, dtype=np.int32)
b = np.linspace(0, pi, 3)
print(b.dtype)
c = a + b
print(c.dtype)

print("--------------")
a = rg.random((2, 3))
print(a)
print(a.sum())
print(a.sum(axis=0))
print(a.sum(axis=1))
print(a.cumsum())


print("-------------")
a = np.arange(3)
print(a)
print(np.exp(a))
print(np.sqrt(a))


print("------------")
a = np.arange(10) ** 3

for i in a:
    print(i ** (1 / 3))

print("-------------")


def f(x, y):
    return x + y


b = np.fromfunction(f, (5, 3), dtype=np.int_)
print(b)
print(b[1, 2], 3)
print(b[:5, 0])

# the following is the same as [1, :]
print(b[1])
print("--------------")
for row in b:
    print(row)

for element in b.flat:
    print(element)
