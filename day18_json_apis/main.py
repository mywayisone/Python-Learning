# 🧪 Practice Tasks (Do These in main.py)
# Create a Python dictionary of a student (name, grade, subjects).

# Save it to a file called student.json.

# Read the file back and print only the subject list.

# Convert a JSON string into a Python dictionary and print a value from it.
import json

# 1. Create a Python dictionary of a student (name, grade, subjects).

student = {
    "name": "Kayode",
    "grade": 75,
    "subjects": [
        "Mathematics",
        "English",
        "Economics",
        "Geography",
        "Physics",
        "Chemistry",
        "Agriculture",
        "Biology"
    ]
    }


# 2. Save it to a file called student.json.

with open("student.json", "w") as file:
    json.dump(student, file, indent=4)

# 3. Read the file back and print only the subject list.

with open("student.json", "r") as file:
    json_data = json.load(file)
    print(json_data["subjects"], json_data)

# Convert a JSON string into a Python dictionary and print a value from it.

student_str = '{ "name": "Kayode","grade": 75,"subjects": ["Mathematics","English","Economics","Geography","Physics","Chemistry","Agriculture","Biology"]}'
parsed = json.loads(student_str)
print(parsed["subjects"])

# 🧪 Practice Tasks (in main.py)
# 1. Send a GET request to: https://jsonplaceholder.typicode.com/todos/1
# 2. Print the title and completed status from the JSON response.
# 3. Try to fetch an invalid endpoint and handle the error gracefully.
import requests

response = requests.get("https://jsonplaceholder.typicode.com/todos/1")
print(response.status_code)
print(response.json())

data = response.json()
print(f"Title: {data["title"]}, Completed: {data["completed"]}")

#fetch an invalid endpoint and handle the error gracefully 
response = requests.get("https://jsonplaceholder.typicode.com/todo/39")
if response.status_code != 200:
    print(f"Something went wrong: {response.status_code}")