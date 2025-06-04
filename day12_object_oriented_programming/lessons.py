# 🧠 What Is OOP?
# OOP helps you organize code around real-world entities like Car, Student, BankAccount, etc., by bundling data and behavior together.

# Instead of writing everything in functions and variables, we create objects from classes.

# 🔧 PART 1: Your First Python Class
# Let’s start with a basic class and object.

# 📄 Example: student_class.py
class Student:
    def __init__(self, name, age, level):
        self.name = name
        self.age = age
        self.level = level

    def introduce(self):
        print(f"Hi, I’m {self.name}, {self.age} years old, in level {self.level}.")

# Create instances (objects)
student1 = Student("Alice", 20, "300")
student2 = Student("Bob", 22, "400")

# Call method
student1.introduce()
student2.introduce()
