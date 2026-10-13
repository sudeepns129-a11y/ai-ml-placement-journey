
import numpy as np

marks = np.array([45, 78, 92, 35, 67, 88, 50])

print("Original marks:", marks)
print("After adding 5:", marks + 5)
print("After subtracting 5:", marks - 5)
print("After multiplying by 2:", marks * 2)
print("Average marks:", np.mean(marks))
print("Passed marks:", marks[marks >= 60])
