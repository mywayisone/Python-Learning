# 🚀 What’s Next?
# Let’s level up your web app skills with Form Handling in Flask!

# 🔍 What You’ll Learn
# - GET vs POST requests
# - Using HTML forms with Flask
# - Receiving and validating user input
# - Redirects and url_for()
# - Flash messages (bonus)

# 🧪 Mini Project: Contact Form App
# We'll build a contact form that:
# - Takes name, email, and message
# - Validates input (basic)
# - Displays a success page

# ✅ Step 1: Scaffold
# Please create this directory structure under day21_flask_forms:
# day21_flask_forms/
# │
# ├── app.py
# ├── templates/
# │   ├── base.html
# │   ├── contact.html
# │   └── success.html

# Once you're done scaffolding, let me know — and I’ll walk you through each part line by line.

# 🔹 Step-by-Step Breakdown
# ✅ 1. app.py – Basic Setup
# We'll begin by setting up app.py to handle two routes:
# - "/" – shows the contact form (GET)
# - "/submit" – handles the form submission (POST)

# Paste the following into app.py:
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/")
def contact():
    return render_template("contact.html")

@app.route("/submit", methods=["POST"])
def submit():
    name = request.form.get("name")
    email = request.form.get("email")
    message = request.form.get("message")

    if not name or not email or not message:
        return "All fields are required!", 400

    # Here you could save to a database or send an email
    return render_template("success.html", name=name)

if __name__ == "__main__":
    app.run(debug=True)

# ✅ 2. templates/base.html
# This is the layout template. It wraps around every page.
# <!DOCTYPE html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <title>Flask Contact App</title>
#     <style>
#         body { font-family: Arial, sans-serif; padding: 2rem; }
#         form { max-width: 400px; margin: auto; }
#         input, textarea { width: 100%; margin-bottom: 1rem; padding: 0.5rem; }
#     </style>
# </head>
# <body>
#     <h1>📨 Contact Us</h1>
#     {% block content %}{% endblock %}
# </body>
# </html>

# ✅ 3. templates/contact.html
# This is the page where the user fills out the form.

# {% extends "base.html" %}

# {% block content %}
# <form action="{{ url_for('submit') }}" method="POST">
#     <label>Name:</label>
#     <input type="text" name="name" required>

#     <label>Email:</label>
#     <input type="email" name="email" required>

#     <label>Message:</label>
#     <textarea name="message" rows="5" required></textarea>

#     <button type="submit">Send</button>
# </form>
# {% endblock %}

# ✅ 4. templates/success.html
# This is the success message page.

# {% extends "base.html" %}

# {% block content %}
# <p>✅ Thank you, {{ name }}. Your message has been received!</p>
# <a href="{{ url_for('contact') }}">Back to contact form</a>
# {% endblock %}

# 🧪 Test it Out
# Run your app: python app.py

# Visit http://127.0.0.1:5000
# Fill and submit the form
# See the success message

# ✅ Understanding the Flow
# Let’s break down what’s happening in your form:

# 🔁 Request Flow
# User visits / (GET) → Renders contact.html form
# User submits form (POST to /submit)
# Flask grabs data from request.form
# Server renders success.html and shows the user's name

# 🧠 Let’s Add Deeper Concepts
# 🔹 1. request.form
# request.form is a dictionary-like object containing form data.

# Access values with .get("field_name")
# You can add .strip() to clean user input: name = request.form.get("name", "").strip()

# 🔹 2. GET vs POST
# GET: for retrieving data (e.g., show a form)
# POST: for sending data (e.g., submit a form)
# By using methods=["POST"], Flask knows to expect form data securely.

# 🔹 3. Using flash() for Messages
# Want to show friendly user messages?
# Update your app:
from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = "supersecretkey"  # Needed for flashing

@app.route("/")
def contact():
    return render_template("contact.html")

@app.route("/submit", methods=["POST"])
def submit():
    name = request.form.get("name", "").strip()
    email = request.form.get("email", "").strip()
    message = request.form.get("message", "").strip()

    if not name or not email or not message:
        flash("All fields are required!")
        return redirect(url_for("contact"))

    flash(f"Thank you {name}, we received your message.")
    return redirect(url_for("contact"))

# Then, update base.html to show flashed messages:

# <body>
#     <h1>📨 Contact Us</h1>

#     {% with messages = get_flashed_messages() %}
#       {% if messages %}
#         <ul>
#         {% for msg in messages %}
#           <li style="color: green;">{{ msg }}</li>
#         {% endfor %}
#         </ul>
#       {% endif %}
#     {% endwith %}

#     {% block content %}{% endblock %}
# </body>
# No more separate success.html! You redirect back to the form and show a flash message instead.

# 🔹 4. Optional: Save Messages to File (basic persistence)
# Inside submit() route:

# with open("messages.txt", "a") as f:
    # f.write(f"{name} | {email} | {message}\n")

# Now all messages are saved in messages.txt.

# 🧪 Your Practice Task (Optional)
# Add these:

# Flash messages instead of success.html

# Save submitted messages to a .txt file

# Prevent duplicate submissions by trimming and checking input