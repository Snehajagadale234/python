
import numpy as np

a = []
b = []

print("Enter 5 integers for first array:")
for i in range(5):
    n = int(input("Enter integer: "))
    a.append(n)

print("Enter 5 integers for second array:")
for i in range(5):
    n = int(input("Enter integer: "))
    b.append(n)

a = np.array(a)
b = np.array(b)

print("Array A:", a)
print("Array B:", b)
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Modulus:", a % b)
