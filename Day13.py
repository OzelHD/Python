# 1️⃣ Load a sample CSV file into Pandas (data.csv).
# 2️⃣ Print the first 5 rows of the dataset.
# 3️⃣ Filter and display rows based on a numeric condition (e.g., age > 30).

import pandas as pd


data = pd.read_csv("sample_data.csv")

print(data.head())

print(data[data["Age"] > 30])