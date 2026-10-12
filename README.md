# 💰 Python Expense Tracker 2.0

A beginner-friendly Python project that helps users record expenses, view saved expenses, and calculate total spending. This project uses JSON to store expense data, so the information remains available even after the program is closed and restarted.

## 🎯 Project Objective

The goal of this project is to improve my Python programming skills by building a practical, menu-driven application with data persistence and error handling.

## ✨ Features

- **Add Expenses:** Enter an expense amount and category.
- **View Expenses:** Display all saved expenses with their categories and amounts.
- **Calculate Total:** Calculate the total amount spent.
- **Save Data:** Store expenses in a JSON file.
- **Load Data:** Load previously saved expenses when the program starts.
- **Input Validation:** Handle invalid amounts and reject zero or negative expenses.
- **Category Validation:** Prevent empty expense categories.
- **Error Handling:** Handle invalid numeric input and file-reading errors.
- **Menu-Driven Interface:** Choose actions using a simple command-line menu.
- **Persistent Storage:** Keep expenses saved between program runs.

## 🛠️ Technologies Used

- Python 3
- JSON
- `pathlib` module
- Exception handling
- Functions and loops
- Lists and dictionaries
- File handling

## 📁 Project Structure

```text
ai-ml-placement-journey/
├── expense_tracker_v2.py
├── expenses.json
└── README.md
```

**Note:** `expenses.json` is created automatically when expenses are saved. Do not upload real personal financial data to a public repository.

## 🚀 How to Run the Project

### 1. Install Python

Install Python 3 from the official website:

https://www.python.org/downloads/

### 2. Clone the Repository

Open your terminal and run:

```bash
git clone https://github.com/sudeepns129-a11y/ai-ml-placement-journey.git
```

### 3. Open the Project Folder

```bash
cd ai-ml-placement-journey
```

### 4. Run the Expense Tracker

```bash
python expense_tracker_v2.py
```

If the `python` command does not work on Windows, try:

```bash
py expense_tracker_v2.py
```

## 📖 How to Use

When you run the program, a menu appears:

```text
=== Expense Tracker ===
1. Add expense
2. View expenses
3. Show total spending
4. Exit
```

- Enter `1` to add an expense.
- Enter `2` to view all saved expenses.
- Enter `3` to calculate total spending.
- Enter `4` to exit the program.

The program validates the input and saves valid expenses in `expenses.json`.

## 🧠 Python Concepts Learned

Through this project, I practised:

- Variables and data types
- User input using `input()`
- Type conversion using `float()`
- Conditional statements (`if`, `elif`, `else`)
- Loops using `while`
- Lists and dictionaries
- Functions and function parameters
- File handling using `open()`
- JSON data storage using `json`
- Exception handling using `try` and `except`
- Working with file paths using `pathlib`
- Calculating totals using `sum()`
- Iterating through lists using `enumerate()`
- Organizing code using the `main()` function

## 🧪 Testing

The following tests have been completed:

- Added an expense successfully.
- Viewed saved expenses.
- Calculated the total spending.
- Tested invalid expense amounts.
- Verified that expenses persist after restarting the program.

Additional checks include empty categories, invalid menu choices, and file-reading error handling.

## 🔮 Future Improvements

- Add expense dates.
- Filter expenses by category.
- Display monthly spending summaries.
- Set a monthly budget and show remaining balance.
- Export expense reports to CSV.
- Add a graphical user interface.
- Build a web version using React and a Python backend.

## 👨‍💻 About This Project

This project is part of my **AI/ML Engineer Placement Preparation Journey**. I am building practical projects to strengthen my Python fundamentals, problem-solving skills, and software development experience.

**GitHub:** https://github.com/sudeepns129-a11y/ai-ml-placement-journey

---

*Built with Python as part of my continuous learning journey toward becoming an AI/ML Engineer.*