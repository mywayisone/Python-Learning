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

# 🧠 What You Just Did:
# * __init__() is the constructor — it runs automatically when you create an object.
# * self refers to the current object.
# * Student("Alice", 20, "300") creates an instance of Student.
# * .introduce() is an instance method that belongs to that student.

# 🔍 __init__: The Constructor Method
# What is it?
#  - __init__ is a special method (called a "dunder method" because of the double underscores) that automatically runs when a new object is created from a class.
#  - It initializes the object’s properties (also called attributes).

def __init__(self, param1, param2):
    self.param1 = param1
    self.param2 = param2

# Example:
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

dog1 = Dog("Bingo", "Labrador")

# What happens here:

# - When you call Dog("Bingo", "Labrador"), Python automatically runs __init__.
# - It assigns "Bingo" to self.name and "Labrador" to self.breed.

# 🔍 self: The Current Object
# What is it?
# - self is a reference to the object itself.
# - It allows you to access the object’s attributes and methods from inside the class.
# - Think of it as “this object” (like this in JavaScript or Java).

# Why use it?
# - So that each object has its own unique data.

# Example:
class Cat:
    def __init__(self, name):
        self.name = name

    def meow(self):
        print(f"{self.name} says Meow!")

cat1 = Cat("Whiskers")
cat2 = Cat("Luna")

cat1.meow()  # Whiskers says Meow!
cat2.meow()  # Luna says Meow!

# ✅ Here, self.name ensures that cat1 and cat2 keep their individual names.

# | Keyword    | Purpose                                        |
# | ---------- | ---------------------------------------------- |
# | `__init__` | Constructor that sets up new object properties |
# | `self`     | Refers to the current object inside the class  |


# 🔸 Today’s Goals:
# - We'll cover the following key OOP concepts:
# - Class Methods
# - Instance vs Class Variables
# - More Realistic Examples
# - Practice Task


# 🔹 1. Class Methods (Defining More Functions in Classes)
# You’ve already seen __init__, but we can define any number of methods to make our objects behave.

class Car:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def accelerate(self):
        self.speed += 10
        print(f"{self.brand} accelerates to {self.speed} km/h")

    def brake(self):
        self.speed -= 5
        print(f"{self.brand} slows down to {self.speed} km/h")
# Test:

car1 = Car("Toyota", 50)
car1.accelerate()
car1.brake()


# 🔹 2. Instance Variables vs Class Variables
# ✅ Instance Variables:
# - Defined in __init__ or methods with self
# - Unique to each object

# ✅ Class Variables:
# - Defined outside any method, usually at the top inside the class
# - Shared by all instances

class Employee:
    company_name = "TechCorp"  # Class variable

    def __init__(self, name):
        self.name = name  # Instance variable

# 🔹 3. Realistic Example: Bank Account

class BankAccount:
    bank_name = "Python National Bank"  # Class variable

    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"{self.owner} deposited ${amount}. New balance: ${self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds")
        else:
            self.balance -= amount
            print(f"{self.owner} withdrew ${amount}. New balance: ${self.balance}")

# Test:

acc1 = BankAccount("Alice", 100)
acc1.deposit(50)
acc1.withdraw(30)

acc2 = BankAccount("Bob")
acc2.deposit(200)
print(acc2.bank_name)  # Accessing class variable

# 🔹 4. 📝 Your Practice Task
# Create a class Student with:

# - __init__ method that accepts name, age, and grade.
# - A method display_info() that prints the student’s info.
# - A method is_passed() that checks if grade >= 50.

# Bonus: Create multiple students and loop through them to check who passed.


# Create a class BankAccount with:

# __init__ method that takes: owner_name, balance (default to 0).
# deposit(amount) method to add money.
# withdraw(amount) method to subtract if sufficient balance.
# display_balance() method to print current balance.

# Bonus:
# Prevent withdrawal of negative amounts or values greater than balance.
# Add a method transfer_to(other_account, amount) to transfer money to another account.