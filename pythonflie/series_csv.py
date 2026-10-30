
import pandas as pd
import os

path = os.path.join(os.path.dirname(__file__), "marks.csv")
df = pd.read_csv(path)

series = df["Marks"]

print("Series:")
print(series)