
marks = [75, 80, 65, 90, 70]

total = sum(marks)
average = total / len(marks)

print("Total:", total)
print("Average:", average)
print("Highest:", max(marks))
print("Lowest:", min(marks))

if average >= 40:
    print("Pass")
else:
    print("Fail")
