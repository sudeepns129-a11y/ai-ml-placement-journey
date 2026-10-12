
import json
from pathlib import Path

FILE_NAME = "expenses.json"


def load_expenses():
    if not Path(FILE_NAME).exists():
        return []

    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except (json.JSONDecodeError, OSError):
        print("Could not read expenses.json. Starting with an empty list.")
        return []


def save_expenses(expenses):
    with open(FILE_NAME, "w") as file:
        json.dump(expenses, file, indent=4)


def add_expense(expenses):
    try:
        amount = float(input("Enter expense amount: "))

        if amount <= 0:
            print("Amount must be greater than zero.")
            return

        category = input("Enter category: ").strip()

        if not category:
            print("Category cannot be empty.")
            return

        expense = {
            "amount": amount,
            "category": category
        }

        expenses.append(expense)
        save_expenses(expenses)
        print("Expense saved successfully!")

    except ValueError:
        print("Please enter a valid number.")


def view_expenses(expenses):
    if not expenses:
        print("No expenses recorded yet.")
        return

    print("\n--- All Expenses ---")

    for index, expense in enumerate(expenses, start=1):
        print(
            f"{index}. {expense['category']}: "
            f"Rs. {expense['amount']:.2f}"
        )


def show_total(expenses):
    total = sum(expense["amount"] for expense in expenses)
    print(f"Total spending: Rs. {total:.2f}")


def main():
    expenses = load_expenses()

    while True:
        print("\n=== Expense Tracker ===")
        print("1. Add expense")
        print("2. View expenses")
        print("3. Show total spending")
        print("4. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            show_total(expenses)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please choose 1–4.")


if __name__ == "__main__":
    main()
