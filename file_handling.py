
# Write information to a file
with open("notes.txt", "w") as file:
    file.write("I am learning Python for AI/ML.\n")
    file.write("My goal is to become an AI/ML Engineer.\n")

# Read information from the file
with open("notes.txt", "r") as file:
    content = file.read()

print(content)
