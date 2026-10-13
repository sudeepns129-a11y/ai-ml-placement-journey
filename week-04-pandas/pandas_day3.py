
from pathlib import Path

import pandas as pd

# Read data from a CSV file
students_path = Path(__file__).with_name("students.csv")
df = pd.read_csv(students_path)

print("Original Data:")
print(df)

# Check for missing values
print("\nMissing values:")
print(df.isnull().sum())

# Fill missing marks with the average marks
df["Marks"] = df["Marks"].fillna(df["Marks"].mean())

# Fill missing ages with the average age
df["Age"] = df["Age"].fillna(df["Age"].mean())

print("\nData after filling missing values:")
print(df)

# Calculate average marks
print("\nAverage marks:", df["Marks"].mean())
