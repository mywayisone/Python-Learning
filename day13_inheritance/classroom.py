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

# Define Person class
class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def display_info(self):
        print(f"Name : {self.name}\nAge: {self.age}")

# Define Teacher derived class from Person(Base) class
class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    # Override super(Person) class display_info() method 
    def display_info(self):
        print(f"Name: {self.name}\nAge: {self.age}\nSubject: {self.subject}")

# Define Student derived class from Person(Base) class
class Student(Person):
    # Define the constructor method
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self.grade = grade

    # Override super(Person) class display_info() method 
    def display_info(self):
        print(f"Name: {self.name}\nAge: {self.age}\nGrade: {self.grade}")


class Classroom():
    # Define the constructor method
    def __init__(self, teacher, students):
        self.teacher = teacher
        self.students = students
    
    # Define the add_student() method
    def add_student(self, student):
        self.students += student
    
    # Define the show_class() method
    def show_class(self):
        print(f"Class Teacher: {self.teacher.name}\n")
        for student in self.students:
            print(f" Name: {student.name}, Age: {student.age}, Grade: {student.grade}")

# Define the Entry point - main()
def main():
    teacher = Teacher("Mr Kayode Oluwasegun", 30, "Mathematics" )

    students = [
        Student("Matthew Kayode", 12, "A"),
        Student("Ademola Tunji", 12, "A"),
        Student("Adeniyi Bolanle", 12, "A"),
        Student("Adeya Bukola", 12, "A"),
        Student("Alao Kehinde", 12, "A"),
        Student("Chukwudi Benson", 12, "A"),
        Student("Ikenna Ugo", 12, "A")
    ]
    classroom = Classroom(teacher, students)
    classroom.show_class()

if __name__ == "__main__":
    main()



# 🌟 Extension Challenge (Optional)
# Create a new class:

# Classroom
# Attributes:
# - teacher: an instance of Teacher
# - students: a list of Student objects

# Methods:
# - add_student(student): adds a Student to the list
# - show_class(): prints the teacher’s info and all student info

