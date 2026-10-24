
import numpy as np

a = np.array([[[1, 2, 3, 4],
               [5, 6, 7, 8],
               [9, 10, 11, 12]],

              [[13, 14, 15, 16],
               [17, 18, 19, 20],
               [21, 22, 23, 24]]])

print("3D Array:")
print(a)

print("First element:", a[0, 0, 0])
print("Last element:", a[-1, -1, -1])
print("Element at index [0,1,2]:", a[0, 1, 2])
print("Element at index [1,2,3]:", a[1, 2, 3])
