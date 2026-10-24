import numpy as np

a = np.random.randint(1, 101, size=(3, 4, 5))

print("Original 3D Array:")
print(a)

b = a.flatten()

print("Flattened Array:")
print(b)

print("Elements greater than 50:")
print(b[b > 50])

print("Even numbers:")
print(b[b % 2 == 0])

avg = np.mean(b)
print("Average:", avg)

print("Elements less than average:")
print(b[b < avg])