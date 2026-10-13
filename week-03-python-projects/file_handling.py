
from pathlib import Path

notes_path = Path(__file__).with_name("notes.txt")

# Write information to a file
with open(notes_path, "w") as file:
    file.write("I am learning Python for AI/ML.\n")
    file.write("My goal is to become an AI/ML Engineer.\n")

# Read information from the file
with open(notes_path, "r") as file:
    content = file.read()

print(content)
