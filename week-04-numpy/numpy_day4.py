
import numpy as np

marks = np.array([
    [80, 75, 90],
    [70, 85, 88],
    [95, 92, 96]
])

print("All marks:")
print(marks)

print("First student:", marks[0])
print("Maths marks:", marks[:, 0])
print("Shape:", marks.shape)
print("Average of all marks:", np.mean(marks))
print("Second student:", marks[1])
print("Python marks:", marks[:, 2])
print("Highest marks:", np.max(marks))