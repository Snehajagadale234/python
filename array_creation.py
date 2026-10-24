
import numpy as np

a = []

for i in range(10):
    n = int(input("Enter an integer: "))
    a.append(n)

arr = np.array(a)

print("Array:", arr)
print("Size of array:", arr.size)
print("Data type:", arr.dtype)
print("Number of dimensions:", arr.ndim)
