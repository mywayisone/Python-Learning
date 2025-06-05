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

# Define the Entry point - main()
def main():
    student = Student("Matthew Kayode", 12, "A")
    teacher = Teacher("Mr Kayode Oluwasegun", 30, "Mathematics" )

    student.display_info()
    teacher.display_info()

if __name__ == "__main__":
    main()
