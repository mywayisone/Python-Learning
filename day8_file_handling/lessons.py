# 📘 Day 8: File Handling in Python
# 🎯 Objectives:
# - Read from and write to files
# - Safely open, read, write, and append
# - Use context managers (with open(...))
# - Create mini file-based projects


# 🧰 1. Opening & Reading Files
# Basic Read:
file = open("data.txt", "r")
content = file.read()
print(content)
file.close()

# Safer with "with":
with open("data.txt", "r") as file:
    content = file.read()
    print(content)
# No need to close manually


# ✍️ 2. Writing & Overwriting Files
with open("log.txt", "w") as file:
    file.write("First log entry\n")
# "w" mode will overwrite file if it exists.

# ➕ 3. Appending to Files
with open("log.txt", "a") as file:
    file.write("Another entry\n")

# 📄 4. Reading Line-by-Line
with open("data.txt", "r") as file:
    for line in file:
        print(line.strip())

# .strip() removes \n from end of lines.

# ✂️ 5. Splitting Lines into Data
# Sample line in file: Ada,80
with open("students.txt", "r") as file:
    for line in file:
        name, score = line.strip().split(",")
        print(name, score)

# 📘 file.readline() – Read One Line at a Time
# Example:
with open("data.txt", "r") as file:
    line1 = file.readline()
    line2 = file.readline()
    print("Line 1:", line1.strip())
    print("Line 2:", line2.strip())
# - Each call to .readline() gives you the next line in the file.
# - It stops at \n (newline).
# - Good for step-by-step reading or reading just the first few lines.

# 📘 file.readlines() – Read All Lines into a List
# Example:
with open("data.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
        print(line.strip())

# - Reads all lines at once and returns a list of lines.
# - Use when:
#   - You want to loop through lines after loading the entire file.
#   - The file isn’t too large (this can use a lot of memory for huge files).

# ✅ Comparison of All File Reading Methods
# | Method         | Description                    | Returns | Use Case                  |
# | -------------- | ------------------------------ | ------- | ------------------------- |
# | `.read()`      | Reads whole file as one string | `str`   | When you need all content |
# | `.readline()`  | Reads one line at a time       | `str`   | Line-by-line processing   |
# | `.readlines()` | Reads all lines into a list    | `list`  | When looping later        |

# ✅ 1. Default File Location
# When you read, write, or append to a file using a relative path, Python looks in the:
# 💡 Current Working Directory (CWD) — typically, this is the folder where your script is being run.
# Example:
with open("notes.txt", "w") as file:
    file.write("Hello")
# If you're running main.py from: /home/user/projects/day8_file_handling/
# Then notes.txt will be created (or written to) in that same folder.

# 📍 2. Accessing Files in Other Locations
# To access a file anywhere on your system, use an absolute path.
# Windows Example:
with open("C:/Users/John/Desktop/data.txt", "r") as file:
    content = file.read()

# macOS/Linux Example:
with open("/home/john/documents/data.txt", "r") as file:
    content = file.read()
# ✅ Use forward slashes (/) even on Windows — Python handles it well.

# 🛡️ 3. Using os to Be Location-Safe
# Why use it?
# - Helps build paths that work across platforms
# - Avoids hardcoding messy paths

# Example:

import os

file_path = os.path.join("data", "notes.txt")
with open(file_path, "a") as file:
    file.write("Note added")
# This will write to data/notes.txt inside your current working folder.

# 🧪 Bonus Tip: Checking Your Current Working Directory
import os
print(os.getcwd())
# Use this if you’re unsure where your script is reading or writing.


# 🛠️ Day 8 Exercises
# Create a folder day8_file_handling/ and add the following scripts:

# 1. write_greeting.py
# - Ask user for their name
# - Write: "Hello, [name]!" to a file called greeting.txt

# 2. append_notes.py
# - Ask user to type a note
# - Append the note to a file called notes.txt
# - Add timestamp using datetime module (optional)

# 3. read_notes.py
# - Read and print all notes from notes.txt

# 4. students_average.py
# - Given a file students.txt:
#   - Ada,80
#   - Chidi,60
#   - Grace,75

# - Read file, calculate average score, print highest and lowest


# 💡 Mini Project: Simple To-Do List App
# Create 3 scripts:

# add_task.py
# - Ask user for task name
# - Append it to todo.txt

# view_tasks.py
# - Show all tasks in todo.txt

# delete_task.py
# - Let user choose a task number to remove from the file

# 🚀 Bonus (Optional)
# Use os module to check if file exists before reading

# Use try/except to handle errors gracefully


