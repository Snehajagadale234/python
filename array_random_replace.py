import numpy as np

a = np.random.randint(1, 101, size=(2, 3, 4))

print("Original 3D Array:")
print(a)

a[a > 50] = 0

print("Array after replacing values greater than 50 with 0:")
print(a)