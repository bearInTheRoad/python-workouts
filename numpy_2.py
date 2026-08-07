import numpy as np

rg = np.random.default_rng()
a = np.floor(10 * rg.random((2, 3)))
print(a)
print(a.shape)
b = a.T
print(b)
print(a)

print(b.ravel())
print("-------------")
# resize will change the shape of the array in place
print(a.resize(3, 2))
print(a)

print(a.reshape(6, -1))

print("--------------")
a = np.floor(rg.random((2, 3)) * 10)
b = np.floor(rg.random((2, 3)) * 100)

print(a)
print(b)
print(np.vstack((a, b)))
print(np.hstack((a, b)))

print("-------------")
a = np.r_[1:5, 1, 2]
print(a)

print("--------------")
a = np.floor(10 * rg.random((2, 3)))
print(a)
print(np.hsplit(a, 3))


print("----------------")
a = np.arange(12) ** 2
i = np.array([1, 1, 3, 7, 5])

print(a)
print(a[i])

j = np.array([[3, 4], [5, 6]])
print(a[j])

print("----------------")
palette = np.array(
    [
        [0, 0, 0],  # black
        [255, 0, 0],  # red
        [0, 255, 0],  # green
        [0, 0, 255],  # blue
        [255, 255, 255],
    ]
)  # white
image = np.array(
    [
        [0, 1, 2, 0],  # each value corresponds to a color in the palette
        [0, 3, 4, 0],
    ]
)
print(palette[image])  # the (2, 4, 3) color image


print("------------")
a = np.arange(12).reshape(3, 4)
print(a)

i = np.array([0, 1, 2])
j = np.array([0, 1, 2])
print(a[i, j])

print(a.argmax(axis=0))
print(a[[2, 2]])
