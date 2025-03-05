# 1️⃣ Plot a line graph showing a relationship (e.g., years vs. salary).
# 2️⃣ Generate and plot a scatter plot with 30 random points.
# 3️⃣ Plot a histogram using the Age column from your CSV file.

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
data = pd.read_csv("sample_data.csv")


data_sorted_by_age = data.sort_values('Age')

plt.plot(data_sorted_by_age['Age'], data_sorted_by_age['Salary'], marker="o")
plt.title("Age-Salary Plot")
plt.xlabel("Age")
plt.ylabel("Salary")
plt.show()




x = np.random.rand(30) * 10
y = x * 2 + np.random.rand(30) * 5

plt.scatter(x, y, color="red")
plt.title("Scatter Plot Example")
plt.xlabel("Feature X")
plt.ylabel("Feature Y")
plt.show()



plt.hist(data["Age"], bins=8, edgecolor="black")
plt.title("Age Distribution")
plt.xlabel("Age Groups")
plt.ylabel("Count")
plt.show()
