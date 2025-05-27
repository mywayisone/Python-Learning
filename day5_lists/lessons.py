# 📘 Day 5: Lists & Collections
# 🎯 Objectives:
#   - Understand how to store and work with multiple values using lists
#   - Learn common list operations
#   - Use for loops with lists
#   - Build real-world mini-apps like a to-do list and a shopping cart
# _____________________________________________________________________

# 🧩 1. What is a List?
# A list is a collection of ordered, changeable items.

fruits = ["apple", "banana", "orange"]
print(fruits[0])  # Output: apple


# 🛠️ Common List Operations:

# Add an item
fruits.append("mango")

# Remove an item
fruits.remove("banana")

# Replace an item
fruits[1] = "grape"

# Loop through a list
for fruit in fruits:
    print(fruit)

# Check if an item exists
if "apple" in fruits:
    print("Yes!")

# Get length
print(len(fruits))

# 📂 Other Data Collections (Overview)
# | Type    | Description                                     |
# | ------- | ----------------------------------------------- |
# | `list`  | Ordered, changeable (e.g. `["a", "b", "c"]`)    |
# | `tuple` | Ordered, **unchangeable** (`("a", "b")`)        |
# | `set`   | Unordered, unique items (`{"a", "b"}`)          |
# | `dict`  | Key-value pairs (`{"name": "Jane", "age": 30}`) |
# We'll go deep into dict tomorrow — focus on lists today.


# 🧠 Python Lists – The Full Guide
# A list in Python is:
#  - Ordered (items have a defined order and position)
#  - Mutable (you can change items)
#  - Heterogeneous (can contain different data types)
#  - Indexed (you can access elements by position)

# 🔹 Creating Lists
empty_list = []
numbers = [1, 2, 3, 4]
mixed = [1, "hello", True, 3.5]

# 🔹 Accessing List Items
fruits = ["apple", "banana", "cherry"]
print(fruits[0])     # apple
print(fruits[-1])    # cherry (last item)

# 🔹 Updating List Items
fruits[1] = "mango"
print(fruits)  # ["apple", "mango", "cherry"]

# 🔹 Adding Items to a List
# | Method          | What It Does             |
# | --------------- | ------------------------ |
# | `.append(x)`    | Adds item to the **end** |
# | `.insert(i, x)` | Adds item at index `i`   |
# | `+`             | Joins two lists          |

fruits.append("orange")
fruits.insert(1, "kiwi")
fruits += ["pineapple"]

# 🔹 Removing Items from a List
# | Method       | What It Does                              |
# | ------------ | ----------------------------------------- |
# | `.remove(x)` | Removes **first occurrence** of value     |
# | `.pop(i)`    | Removes item at index `i` (default: last) |
# | `.clear()`   | Empties the entire list                   |

fruits.remove("banana")
fruits.pop()        # removes last item
fruits.pop(0)       # removes first item
fruits.clear()

# 🔹 Looping Through a List

#   - Using for loop:
for fruit in fruits:
    print(fruit)

#   - Using index:
for i in range(len(fruits)):
    print(fruits[i])


# 🔹 Checking Existence
if "apple" in fruits:
    print("Found!")


# 🔹 List Functions & Methods
# | Operation                | Description               |
# | ------------------------ | ------------------------- |
# | `len(list)`              | Number of items           |
# | `min(list)`, `max(list)` | Minimum/maximum value     |
# | `sum(list)`              | Total of all numbers      |
# | `sorted(list)`           | Returns a new sorted list |
# | `list.sort()`            | Sorts in place            |
# | `list.reverse()`         | Reverses in place         |
# | `list.index(x)`          | Finds index of `x`        |
# | `list.count(x)`          | Counts occurrences of `x` |

# 🔹 Slicing a List
numbers = [0, 1, 2, 3, 4, 5]

print(numbers[1:4])   # [1, 2, 3]
print(numbers[:3])    # [0, 1, 2]
print(numbers[-2:])   # [4, 5]

# 🔹 Nesting Lists (List of Lists)
matrix = [
    [1, 2, 3],
    [4, 5, 6]
]

print(matrix[0][1])  # 2

# 🧪 Example: List Utilities
def get_average(scores):
    return sum(scores) / len(scores)

grades = [90, 80, 85, 100]
print("Average:", get_average(grades))

# 🧰 Real-World Uses of Lists
# | App Feature           | Uses List? |
# | --------------------- | ---------- |
# | Contact lists         | ✅          |
# | To-do items           | ✅          |
# | Shopping cart items   | ✅          |
# | Quiz question bank    | ✅          |
# | Leaderboard of scores | ✅          |



# 🛠️ Tips for Working With Lists
# 1. Use .copy() if you want to clone a list without linking it:

a = [1, 2, 3]
b = a.copy()  # b is now independent of a

# 2. Lists grow automatically; no need to define their size ahead of time.
# 3. Don’t modify a list while looping through it — it can lead to bugs. Instead, build a new one:
old_list = []
new_list = [x for x in old_list if x > 10]


# ✅ Summary Table
# | Concept | Example                               |
# | ------- | ------------------------------------- |
# | Create  | `my_list = [1, 2, 3]`                 |
# | Access  | `my_list[0]`                          |
# | Add     | `my_list.append(4)`                   |
# | Remove  | `my_list.pop()` or `remove(x)`        |
# | Length  | `len(my_list)`                        |
# | Loop    | `for item in my_list:`                |
# | Sort    | `sorted(my_list)` or `my_list.sort()` |
# | Slice   | `my_list[1:4]`                        |



# 🧪 Exercises (In day5_lists/ folder)
# 1. Create a list of 5 favorite movies
#  - Print each movie using a loop

# 2. Add and remove items
#  - Start with a list of 3 fruits
#  - Add 2 more using .append()
#  - Remove one with .remove()

# 3. Sum a list of numbers
numbers = [5, 10, 20, 7]
# Calculate total sum

# 4. Find the largest number in a list
#  - Use a loop or max()

# 5. Sort a list of strings
names = ["Zara", "Andy", "Mike"]
# Sort alphabetically


# 🏆 Mini Project: To-Do List Manager

# Build a simple command-line to-do list app:
# - Show a menu:
#   1. Add task
#   2. View tasks
#   3. Remove task
#   4. Exit
# - Store tasks in a list
# - Use a loop to keep showing the menu