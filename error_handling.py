
try:
    amount = float(input("Enter expense amount: "))

    if amount <= 0:
        print("Expense must be greater than zero")
    else:
        print("Valid expense")

except ValueError:
    print("Please enter a valid number")
