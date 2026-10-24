
import numpy as np

a = np.array([10, 25, 35, 55, 60, 45, 70, 80, 20, 90])

print("Original Array:")
print(a)

a[a > 50] = 0

print("Array after replacing elements greater than 50 with 0:")
print(a)
