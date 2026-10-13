import numpy as np

marks = np.array([45, 78, 92, 35, 67, 88, 50])

passed_marks = marks[marks >= 60]

print("Marks:", marks)
print("Marks 60 and above:", passed_marks)