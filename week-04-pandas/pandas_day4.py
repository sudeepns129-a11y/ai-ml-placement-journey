
import pandas as pd

data = {
    "Name": ["Arun", "Meera", "Kiran", "Priya", "Rahul"],
    "Marks": [70, 95, 82, 55, 88],
    "Age": [18, 19, 20, 18, 19],
    "Department": ["CSE", "AIML", "CSE", "AIML", "CSE"]
}

df = pd.DataFrame(data)

# Display the complete dataset
print("Student Dataset:")
print(df)

# Show basic information about the dataset
print("\nDataset Information:")
df.info()

# Show statistical summary
print("\nStatistical Summary:")
print(df.describe())

# Count students in each department
print("\nStudents per Department:")
print(df["Department"].value_counts())

# Display the first three rows
print("\nFirst Three Students:")
print(df.head(3))
