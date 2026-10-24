
import numpy as np

a = np.array([45, 12, 78, 23, 56, 9, 34, 67, 15, 90])

print("Original Array:")
print(a)

print("Ascending Order:")
print(np.sort(a))

print("Descending Order:")
print(np.sort(a)[::-1])
