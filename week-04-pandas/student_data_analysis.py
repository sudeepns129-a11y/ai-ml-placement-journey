
from pathlib import Path

import numpy as np
import pandas as pd

# Create student dataset
data = {
    "Name": ["Arun", "Meera", "Kiran", "Priya", "Rahul", "Sneha"],
    "Marks": [70, 95, 82, 55, 88, 45],
    "Age": [18, 19, 20, 18, 19, 20],
    "Department": ["CSE", "AIML", "CSE", "AIML", "CSE", "AIML"]
}

df = pd.DataFrame(data)

# Display all students
print("=== STUDENT DATASET ===")
print(df)

# Calculate statistics using NumPy
marks = np.array(df["Marks"])

print("\n=== MARKS STATISTICS ===")
print("Total marks:", np.sum(marks))
print("Average marks:", np.mean(marks))
print("Highest marks:", np.max(marks))
print("Lowest marks:", np.min(marks))
print("Median marks:", np.median(marks))

# Find students scoring 75 or more
print("\n=== TOP PERFORMERS (75 OR MORE) ===")
print(df[df["Marks"] >= 75])

# Sort students by marks, highest first
print("\n=== RANKING ===")
print(df.sort_values(by="Marks", ascending=False))

# Count students by department
print("\n=== DEPARTMENT COUNT ===")
print(df["Department"].value_counts())

# Count students who scored 40 or more
passed = df[df["Marks"] >= 40]
print("\nStudents who passed:", len(passed))

# Save the dataset to a CSV file
analysis_path = Path(__file__).with_name("student_analysis.csv")
df.to_csv(analysis_path, index=False)
print("\nDataset saved to student_analysis.csv")
