# AI/ML Placement Journey

## Project goal

This repository contains beginner-level exercises and small projects created while preparing for an AI/ML engineering placement. The roadmap builds from Python fundamentals to introductory NumPy and pandas work. A script is a record of practice, not a claim of mastery.

## Learning roadmap

- **Weeks 1–2 — Python fundamentals:** small programs and challenges covering input, variables, conditions, loops, strings, lists, dictionaries, functions, modules, and basic error handling.
- **Week 3 — Python projects:** a command-line calculator, a file-handling exercise, and Expense Tracker 2.0, which saves expenses in a local JSON file.
- **Week 4 — NumPy and pandas:** array creation and calculations, filtering, basic DataFrame operations, reading a sample CSV, and a student-data analysis that writes a CSV report.

## Folder structure

```text
ai-ml-placement-journey/
|-- README.md
|-- requirements.txt
|-- .gitignore
|-- week-01-02-python-basics/
|   |-- main.py
|   |-- even_odd.py
|   |-- largest_number.py
|   |-- multiplication_table.py
|   |-- expense_tracker.py
|   |-- challenge1.py ... challenge5.py
|   |-- error_handling.py
|   |-- lists_practice.py
|   |-- modules_practice.py
|   `-- strings_practice.py
|-- week-03-python-projects/
|   |-- calculator.py
|   |-- file_handling.py
|   |-- notes.txt
|   |-- expense_tracker_v2.py
|   `-- expenses.json (local data; ignored by Git)
|-- week-04-numpy/
|   |-- numpy_day1.py ... numpy_day5.py
|   |-- numpy_filter.py
|   |-- student_marks.py
|   `-- student_marks_analyzer.py
`-- week-04-pandas/
    |-- pandas_day1.py ... pandas_day4.py
    |-- students.csv
    |-- student_data_analysis.py
    `-- student_analysis.csv
```

## Setup on Windows

Open PowerShell in the repository folder. Check that Python is available with `python --version` (or use `py` instead of `python` if that is the command installed on your computer). Install the project dependencies with:

```powershell
python -m pip install -r requirements.txt
```

## Run example scripts

Run commands from the repository root. For example:

```powershell
python .\week-01-02-python-basics\even_odd.py
python .\week-03-python-projects\calculator.py
python .\week-03-python-projects\expense_tracker_v2.py
python .\week-04-numpy\numpy_day1.py
python .\week-04-pandas\pandas_day3.py
python .\week-04-pandas\student_data_analysis.py
```

The scripts that ask for input will prompt in the terminal. `pandas_day3.py` reads the sample `students.csv` in its own folder. `student_data_analysis.py` writes `student_analysis.csv` beside that script.

Expense Tracker 2.0 stores its data in `week-03-python-projects\expenses.json`. This file is ignored by Git so local expense details are not added to commits. Keep a backup if the data matters to you.

The local-only `personal_details.py` and `dictionary_practice.py` exercises contain personal details and are excluded from the public repository by `.gitignore`.

## Concepts practised

- Python values, input, type conversion, conditions, loops, and functions
- Strings, lists, dictionaries, imports, and basic exception handling
- Reading and writing text and JSON files
- NumPy arrays, arithmetic, filtering, summary statistics, and sorting
- pandas DataFrames, CSV input/output, filtering, sorting, and summary operations

## Projects completed or started

- **Expense Tracker:** a short exercise that totals three entered expenses.
- **Expense Tracker 2.0:** a menu-based program for adding, viewing, and totaling expenses saved as JSON.
- **Calculator:** performs basic arithmetic on two entered numbers.
- **Student-data exercises:** create and inspect small sample datasets, calculate marks summaries, and save an analysis CSV.
- **File handling:** writes and reads a short learning note.

These are learning exercises and small command-line projects; they are not complete production applications.

## Future learning goals

Continue with statistics and probability, then introductory machine learning. After that, build practical AI/ML projects using real-world datasets and document how each model is evaluated.
