# 📘 Day 7(i): Loops & Control Flow
# 🎯 Objectives:
# - Master for and while loops
# - Understand break, continue, and else
# - Practice nested loops
# - Combine loops with lists and dictionaries
# - Build loop-driven mini projects

# 🔁 1. for Loop — Iterating Over Sequences
names = ["Ada", "John", "Jane"]
for name in names:
    print(name)
# - Works on iterables: lists, strings, dicts, etc.

# 🔁 2. while Loop — Repeat As Long As Condition is True
count = 0
while count < 5:
    print("Counting:", count)
    count += 1
# - Use when you don’t know how many times to loop

# ⛔ 3. break and continue
# break: exits loop immediately
for i in range(10):
    if i == 5:
        break
    print(i)

# continue: skip to next iteration
for i in range(5):
    if i == 2:
        continue
    print(i)

# 🎯 4. else in Loops
for i in range(3):
    print(i)
else:
    print("Loop finished normally!")
# else runs only if loop didn’t break

# 🔁 5. Looping with range()
for i in range(5):  # 0 to 4
    print(i)

for i in range(1, 10, 2):  # Start=1, End=10, Step=2
    print(i)

# 🔂 6. Nested Loops
for i in range(3):
    for j in range(2):
        print(f"i={i}, j={j}")
# Used in:
# - Grids (like tic-tac-toe)
# - Combinations
# - Tables

# 🔗 7. Looping with Dictionaries
person = {"name": "Ada", "age": 30}
for key, value in person.items():
    print(f"{key}: {value}")

# 🔁 Day 7(ii) – Advanced Loop Applications
# 🎯 Objectives:
# - Practice real-world problems that depend on loops
# - Combine loops with functions and dictionaries
# - Build your first text-based game fully driven by loops

# ✅ Plan for Today
# 1. Nested Loop Challenge — multiplication_table.py
# Print a well-formatted multiplication table from 1 to 12:
# 1  2  3  4  ...
# 2  4  6  8
# 3  6  9 12
# ...

# 2. Interactive Loop + while + break — guessing_game.py
# Guess a random number between 1 and 100:
# - Use random.randint()
# - Use a while loop
# - Use break when guessed correctly
# - Count number of attempts

# 3. Data Loop Project — word_frequency.py
sentence = "This is a test this is only a test"
# Convert to: {"this": 2, "is": 2, "a": 2, "test": 2, "only": 1}

# 4. Loop + Dictionary Mini-App — student_scores.py
# - Ask user for student names and scores
# - Stop when user types "done"
# - Print total, average, highest, lowest

# 🧠 Bonus: Looping with zip() and enumerate()
# Using enumerate
names = ["Ada", "John", "Jane"]
for index, name in enumerate(names):
    print(f"{index + 1}: {name}")

# Using zip
scores = [90, 85, 78]
for name, score in zip(names, scores):
    print(f"{name}: {score}")



# 🧪 Day 7 Exercises
# Create a folder day7_loops/ and complete the following:

# 1. print_numbers.py
# - Print numbers from 1 to 10 using a for loop

# 2. countdown.py
# - Print numbers from 10 to 1 using a while loop

# 3. skip_even.py
# - Loop 1–20, print only odd numbers using continue

# 4. sum_numbers.py
# - Ask user to enter numbers until they type "done"
# - Use while to keep summing the input

# 5. multiplication_table.py
# - Use nested loop to print 1–12 multiplication table

# 🛠️ Mini Project: Number Guessing Game
# 1. Generate random number between 1–100
# 2. Ask user to guess until correct
# 3. Show "Too high" or "Too low" for wrong guesses
# 4. Track number of attempts

# Hints:
# - Use random.randint(1, 100)
# - Use a while loop
# - Add break when guessed correctly


# 📦 Deliverables
# Folder: day7_loops/
# Files: One for each exercise + guessing_game.py
# Push to GitHub when done

