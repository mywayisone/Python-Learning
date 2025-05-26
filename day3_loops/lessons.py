# 🎯 Objectives:
# Understand and use for and while loops

# Learn how to repeat tasks

# Build real-world mini programs like counters, summations, and a guessing game
# ____________________________________________________________


# 🧩 1. The for Loop
# Use for when you know how many times to loop.

for i in range(5):
    print("Hello", i)

# Print numbers 1 to 5
for i in range(1, 6):
    print(i)

# Print each character
for char in "python":
    print(char)


# 🧩 2. The while Loop
# Use while when the number of iterations is unknown — loop until a condition is false.

i = 1
while i <= 5:
    print(i)
    i += 1


# 🛑 Infinite Loop (Be Careful!)
while True:
    print("This goes forever!")
# Break it with:
    break

# if condition:
#     break



# 🧪 Exercises (In day3_loops/ Folder)
# 1. Count from 1 to 10
# Use a for loop to print numbers 1–10.

# 2. Even Numbers Between 1 and 50
# Use for and if to print only even numbers between 1–50.

# 3. Sum of Numbers
# Ask the user for a number n and calculate the sum from 1 to n.

# 4. Multiplication Table
# Ask the user for a number and print its multiplication table (1 to 12).

# 5. Countdown Timer
# Use a while loop to count down from 10 to 1, then print "Blast off!".


# 🎯 Mini Project: Number Guessing Game 🎯
# 🕹 Game Idea:
# - Program picks a number (e.g. 7)
# - User tries to guess it
# - Program gives hints: too low, too high, or correct

# 📦 Deliverables
# - Create folder day3_loops/
# - Save all exercises & mini project
# - Push to your GitHub repo

# 🧠 Optional Challenge
# Let the user choose the difficulty by picking the range (e.g. 1–50 or 1–100), 
# and use random.randint() to generate the secret number.