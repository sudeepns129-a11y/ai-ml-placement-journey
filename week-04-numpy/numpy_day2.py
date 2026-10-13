import numpy as np

marks = np.array([70, 85, 90, 65, 80, 95])

# Add 5 bonus marks to every student
updated_marks = marks + 5

print("Original marks:", marks)
print("Updated marks:", updated_marks)

import numpy as np

marks = np.array([70, 85, 90, 65, 80, 95])

print("Doubled marks:", marks * 2)

passed_marks = marks[marks >= 80]

print("Marks 80 and above:", passed_marks)