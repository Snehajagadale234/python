
import pandas as pd
import os

path = os.path.join(os.path.dirname(__file__), "students.csv")
df = pd.read_csv(path)

print("Student DataFrame:")
print(df)