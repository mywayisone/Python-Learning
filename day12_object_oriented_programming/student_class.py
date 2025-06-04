# 🔹 📝 Your Practice Task
# Create a class Student with:

# - __init__ method that accepts name, age, and grade.
# - A method display_info() that prints the student’s info.
# - A method is_passed() that checks if grade >= 50.

# Bonus: Create multiple students and loop through them to check who passed.

class Student:
    
    def __init__(self, name:str, age : int, grade: float):
        try:
            self.name = name
            self.age = age
            self.grade = grade
        except ValueError as e:
            print("Numerical values are expected for Age and Grade: ", e)
        except Exception as e:
            print("Error Occurred: ", e)
        
    def display_info(self):
        print(f"{self.name} is {self.age} years old and has {self.grade} as grade")

    def is_passed(self):
        if self.grade >= 50:
            print("You passed!")
        else: print("Sorry! You didn't get up to cut-off")
            
# Define main() function
def main():
    student1 = Student("Matthew", 23, 75)
    student2 = Student("Olakunle", 23, 50)
    student3 = Student("Eunice", 23, 45)

    students = [student1, student2, student3]

    for student in students:
        student.display_info()
        student.is_passed()

if __name__ == "__main__":
    main()


