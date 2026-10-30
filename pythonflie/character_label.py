
import numpy as np

arr = np.array([10, 20, 30, 40])

labels = np.array(["A", "B", "C", "D"])

for label, value in zip(labels, arr):
    print(label, ":", value)