# 🔹 JSON (JavaScript Object Notation)
# JSON is a lightweight data format often used to store and exchange data between a server and a client.

# In Python, we use the built-in json module to work with it.

# 📘 1. Importing the json Module
import json

# 📤 2. Writing (Serializing) JSON to a File
data = {
    "name": "Alice",
    "age": 25,
    "is_active": True,
    "skills": ["Python", "Git", "APIs"]
}

with open("data.json", "w") as file:
    json.dump(data, file, indent=4)

# This creates a file called data.json that stores the dictionary in JSON format.
# 📥 3. Reading (Deserializing) JSON from a File
with open("data.json", "r") as file:
    loaded_data = json.load(file)

print(loaded_data["name"])  # Output: Alice

# 🔁 4. Converting Between Python and JSON Strings
# Python to JSON string
json_string = json.dumps(data, indent=4)
print(json_string)

# JSON string to Python dict
json_data = '{"name": "Bob", "age": 30}'
parsed = json.loads(json_data)
print(parsed["age"])  # Output: 30


# 🔹 Part 2: Working with APIs using requests
# To interact with APIs, you need the requests library. It allows your program to make HTTP calls (GET, POST, etc.).

# ✅ Step 1: Install requests
# If you haven't already:
# pip install requests


# 🌐 1. Making a Simple GET Request
import requests

response = requests.get("https://api.github.com")

print(response.status_code)  # 200 means OK
print(response.json())       # Convert the response to a Python dictionary


# 🔍 2. Handling Response Data
data = response.json()
print("Current User URL:", data["current_user_url"])


# ⚠️ 3. Handling Errors
bad_response = requests.get("https://api.github.com/invalid-endpoint")

if bad_response.status_code != 200:
    print("Something went wrong:", bad_response.status_code)

# 🧪 Practice Tasks (in main.py)
# 1. Send a GET request to: https://jsonplaceholder.typicode.com/todos/1
# 2. Print the title and completed status from the JSON response.
# 3. Try to fetch an invalid endpoint and handle the error gracefully.

# 🌟 Mini Project: Weather App (weather_app.py)
# You’ll build a simple weather-fetching app using the Open-Meteo API (no API key required).

# API Endpoint (GET):https://api.open-meteo.com/v1/forecast?latitude=6.5244&longitude=3.3792&current_weather=true
# This returns weather for Lagos, Nigeria

# 🧩 What to Do in weather_app.py:
# 1. Make a GET request to the above URL
# 2. Extract and print:
# - Temperature
# - Wind speed
# - Time of the weather update
# 3. Add error handling (e.g., if the server is down)