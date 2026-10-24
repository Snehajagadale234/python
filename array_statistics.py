
import numpy as np

a = []

for i in range(10):
    n = int(input("Enter a number: "))
    a.append(n)

arr = np.array(a)

print("Array:", arr)
print("Maximum:", np.max(arr))
print("Minimum:", np.min(arr))
print("Sum:", np.sum(arr))
print("Average:", np.mean(arr))
