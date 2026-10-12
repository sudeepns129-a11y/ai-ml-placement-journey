expenses = []

for i in range(3):
    amount = float(input("Enter expense amount: "))
    expenses.append(amount)

total = sum(expenses)
average = total / len(expenses)

print("All expenses:", expenses)
print("Total expenses:", total)
print("Average expense:", average)