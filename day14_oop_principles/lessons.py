# 📘 Day 14 – OOP Principles in Depth

# 1️⃣ Encapsulation – “Protecting the data”
# Encapsulation means restricting access to internal details of a class, only exposing what’s necessary.

# ✔ Using Underscores:

# | Syntax       | Meaning                          |
# | ------------ | -------------------------------- |
# | `public`     | Normal attributes/methods        |
# | `_protected` | Intended for internal use        |
# | `__private`  | Strictly internal (name mangled) |

class Account:
    def __init__(self, owner, balance):
        self.owner = owner            # public
        self._bank = "MyBank"         # protected
        self.__balance = balance      # private

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        self.__balance += amount

acct = Account("John", 500)
print(acct.owner)           # John
print(acct._bank)           # MyBank
print(acct.get_balance())   # 500
# print(acct.__balance)     # ❌ Error: private!

# You can still access private members with:
print(acct._Account__balance)  # Name-mangled access


# 2️⃣ Polymorphism – “One interface, many forms”
# Different classes implement the same method, but differently.

class Bird:
    def speak(self):
        print("Chirp")

class Dog:
    def speak(self):
        print("Bark")

def animal_sound(animal):
    animal.speak()

animal_sound(Bird())   # Chirp
animal_sound(Dog())    # Bark

# ✅ One function (animal_sound) works with different objects.


# 3️⃣ Abstraction – “Hiding details, showing the essentials”
# Use abstract classes to define required behavior.

from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass

class Car(Vehicle):
    def start_engine(self):
        print("Engine started!")

# v = Vehicle()  # ❌ Error: abstract class
c = Car()
c.start_engine()

# 🧠 When to use:
# - You want to enforce a contract/interface.
# - You don’t want the base class to be instantiated.


# 📝 Practice Task

# Create an abstract class Appliance:
# __init__(self, brand)
# Abstract method: turn_on()
# Abstract method: turn_off()

# Then create two classes:
# WashingMachine(Appliance) – custom turn_on/turn_off
# Microwave(Appliance) – custom turn_on/turn_off
# Create objects and test their behavior.
