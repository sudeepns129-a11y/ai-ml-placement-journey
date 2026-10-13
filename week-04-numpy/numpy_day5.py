
import numpy as np

marks = np.array([70, 85, 90, 65, 80, 95, 85])

print("Marks:", marks)
print("Total:", np.sum(marks))
print("Average:", np.mean(marks))
print("Median:", np.median(marks))
print("Highest:", np.max(marks))
print("Lowest:", np.min(marks))
print("Standard deviation:", np.std(marks))
print("Sorted marks:", np.sort(marks))
