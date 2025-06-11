# 🔜 Coming Up: Day 20 – Intro to Flask
# Next, we’ll begin your journey into web development with Python, starting with:

# 🔹 What Flask is and why it’s popular
# 🔹 Setting up a simple Flask web server
# 🔹 Handling routes and templates
# 🔹 Returning HTML pages
# 🔹 A mini project: Build a simple quote viewer with Flask

#  Since you already have your virtual environment set up in the python_learning/ directory, we’ll simply install Flask inside that environment.

# ✅ Step 1: Activate Your Virtual Environment
# If you're on:

# 🔹 Windows (Command Prompt or PowerShell): venv\Scripts\activate

# 🔹 macOS / Linux: source venv/bin/activate
# You should see (venv) at the beginning of your terminal prompt — that means it's active.

# ✅ Step 2: Install Flask
# Once the environment is active, run: pip install Flask

# After it's installed, you can verify with:flask --version

# ✅ Step 3: Optional — Freeze Requirements
# To keep track of your dependencies: pip freeze > requirements.txt

# This makes it easy to reinstall packages later with: pip install -r requirements.txt


# 🚀 Day 20: Getting Started with Flask
# 🔍 What You’ll Learn
# What Flask is
# - How to create a basic Flask app
# - Running a development server
# - Handling routes and returning HTML
# - Dynamic content with route parameters
# - Mini Project: Simple Quote Viewer

# 📁 Folder Structure
# Inside day20_flask_intro/, set up like this:

# day20_intro_to_flask/
# │
# ├── app.py
# ├── requirements.txt
# └── templates/
#     └── index.html

# 🧠 Step-by-Step
# 1️⃣ Create app.py
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)

# 2️⃣ Create templates/index.html
# <!DOCTYPE html>
# <html>
# <head>
#     <title>Quote Viewer</title>
# </head>
# <body>
#     <h1>Welcome to the Quote Viewer</h1>
#     <p>This is a simple Flask app!</p>
# </body>
# </html>

# ▶️ How to Run the App
# Activate your virtual environment and run: python app.py

# Visit: http://127.0.0.1:5000
# You should see the welcome message rendered from index.html.



# 📄 app.py — Full Code:

# 🔍 Line-by-Line Explanation:
# "from flask import Flask, render_template"
# - Flask is the main class from the Flask framework. It’s used to create your web application.
# - render_template is a helper function that looks for HTML files inside the templates/ folder and returns them to the browser.

# app = Flask(__name__)
# This creates an instance of your Flask application.
# __name__ is a built-in Python variable. In this context, it tells Flask where to find your code and resources.
# If you're running app.py directly, __name__ will be "__main__", and Flask knows this file is the entry point.

# @app.route("/")
# - This is a decorator that tells Flask:
# - “Whenever someone visits the homepage (/), run the following function.”
# - / is the root URL (like http://localhost:5000/).

# def home():
# - This defines a view function (or "route handler").
# - When someone visits /, Flask calls this home() function.

# return render_template("index.html")
# - This sends an HTML page to the user's browser.
# - render_template("index.html") looks inside the templates/ folder for a file named index.html and returns it as a response.

# if __name__ == "__main__":
# - This block checks whether the file is being run directly (python app.py) or being imported elsewhere.
# - If run directly, the app will start the web server.

# app.run(debug=True)
# - Starts the built-in Flask development server.

# debug=True enables:
# - Auto-reload: Restarts the server on code changes.
# - Debugger: Shows helpful error messages in the browser.

# | Part                        | Purpose                      |
# | --------------------------- | ---------------------------- |
# | `Flask(__name__)`           | Creates your web app         |
# | `@app.route("/")`           | Defines a route (URL)        |
# | `render_template()`         | Renders HTML files           |
# | `if __name__ == "__main__"` | Starts the server            |
# | `debug=True`                | Helps you during development |
