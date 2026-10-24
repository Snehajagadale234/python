
import numpy as np

marks = np.array([75, 80, 65, 90, 85, 70, 95, 60, 88, 92,
                  55, 78, 82, 68, 96, 72, 84, 50, 89, 76])

average = np.mean(marks)

print("Student Marks:", marks)
print("Class Average:", average)
print("Marks Above Average:")
print(marks[marks > average])
