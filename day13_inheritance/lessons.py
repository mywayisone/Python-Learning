# 🧱 1. What is Inheritance?
# Inheritance allows one class (child/derived) to use the properties and methods of another class (parent/base).

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("The animal makes a sound")

class Dog(Animal):
    def speak(self):
        print(f"{self.name} says Woof!")

# Test:
dog1 = Dog("Buddy")
dog1.speak()         # Buddy says Woof!
print(dog1.name)     # Buddy (inherited from Animal)

# ✅ Dog inherits from Animal but also overrides speak().


# 🎯 2. super() – Calling the Parent
# Use super() to call the constructor or method of the parent class.
class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name)   # Call Animal's __init__
        self.color = color

# 🔐 3. Key OOP Principles

# | Principle         | Meaning                                                               |
# | ----------------- | --------------------------------------------------------------------- |
# | **Encapsulation** | Hiding internal data, exposing only what’s necessary (`private` data) |
# | **Inheritance**   | One class inherits from another                                       |
# | **Polymorphism**  | Same method name, different behaviors                                 |
# | **Abstraction**   | Hiding complex logic, showing only essentials                         |

# Python uses:

# _variable: protected (suggested private)

# __variable: private (name-mangled)


# 🧪 Practice Task – Inheritance

# Create a base class Person:
# - name and age attributes
# - display_info() method

# Create a derived class Teacher(Person):
# - Extra subject attribute
# - Override display_info() to also show subject

# Create another class Student(Person):
# - Extra grade attribute
# - Override display_info() to also show grade

# Test by creating:
# - A teacher
# - A student
# - Call display_info() on both