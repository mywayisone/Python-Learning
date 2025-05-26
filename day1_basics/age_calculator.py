# This exercise calculates user's age

current_year = 2025

birth_year = input("Enter your birth year: ")
print(f"Your age is {current_year - birth_year}") if birth_year.isdigit() else print("Enter a valid year") 