
import pandas as pd

data = {
    "Name": ["Rahul", "Priya", "Aman", "Sneha"],
    "Marks": [85, 92, 75, 88],
    "Age": [19, 20, 18, 19]
}

df = pd.DataFrame(data)

print("Student Data:")
print(df)

print("\nStudent names:")
print(df["Name"])

print("\nMarks:")
print(df["Marks"])

print("\nAverage marks:")
print(df["Marks"].mean())
