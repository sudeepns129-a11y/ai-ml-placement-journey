
import pandas as pd

data = {
    "Name": ["Arun", "Meera", "Kiran", "Priya", "Rahul"],
    "Marks": [70, 95, 82, 55, 88],
    "Age": [18, 19, 20, 18, 19]
}

df = pd.DataFrame(data)

print("Original Data:")
print(df)

# 1. Filter students scoring 80 or more
print("\nStudents scoring 80 or more:")
print(df[df["Marks"] >= 80])

# 2. Filter students who passed (marks >= 40)
print("\nStudents who passed:")
print(df[df["Marks"] >= 40])

# 3. Sort students by marks, highest first
print("\nStudents sorted by marks:")
print(df.sort_values(by="Marks", ascending=False))
