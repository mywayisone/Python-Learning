# 🧱 Here's What You've Mastered So Far:
# | Feature                       | Status |
# | ----------------------------- | ------ |
# | Routing                       | ✅      |
# | Templates + Jinja2            | ✅      |
# | Template inheritance          | ✅      |
# | Variables passed to templates | ✅      |
# | Forms with `POST` method      | ✅      |
# | `request.form` usage          | ✅      |
# | Flash messages                | ✅      |
# | Redirects & URL building      | ✅      |
# | Saving to text file           | ✅      |


# ⏭️ What's Next?
# You now have two solid steps:

# 🔸 Step 1: Dive into WTForms
# Professional form handling for Flask apps
# Comes with:
# Built-in validators (e.g., email, required, length)
# Field classes (e.g., StringField, TextAreaField)
# CSRF protection
# Great for building real-world apps

# 🔹 Step 2: Build a Mini Project
# Let’s consolidate your knowledge so far.
# Example idea: Feedback Collector or Guestbook App using your form logic.

# 🔍 What is WTForms?
# WTForms is a flexible library for building and validating web forms in Python. Flask integrates it through Flask-WTF, which gives you:
# Declarative form creation (like defining a class)
# Built-in validators
# CSRF protection (security against form hijacking)
# Cleaner templates with less manual error checking

# 📦 Step 1: Install Flask-WTF
# Activate your virtual environment and run: pip install flask-wtf
# Then confirm installation: pip freeze | grep flask-wtf

# 📁 Step 2: Set Up Folder Structure (in day20_wtforms/)
# Here’s the layout:
# day20_wtforms/
# │
# ├── app.py
# ├── forms.py
# ├── messages.txt
# ├── templates/
# │   ├── base.html
# │   ├── contact.html

# 🧱 Step 3: Create the Form Class in forms.py
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email, Length

class ContactForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired(), Length(min=2)])
    email = StringField("Email", validators=[DataRequired(), Email()])
    message = TextAreaField("Message", validators=[DataRequired(), Length(min=10)])
    submit = SubmitField("Send")

# 🚀 Step 4: Create the App in app.py
from flask import Flask, render_template, redirect, url_for, flash
from forms import ContactForm

app = Flask(__name__)
app.secret_key = "supersecretkey"

@app.route("/", methods=["GET", "POST"])
def contact():
    form = ContactForm()

    if form.validate_on_submit():
        name = form.name.data.strip()
        email = form.email.data.strip()
        message = form.message.data.strip()

        # Save to file
        with open("messages.txt", "a") as f:
            f.write(f"{name} | {email} | {message}\n")

        flash("Message sent successfully!", "success")
        return redirect(url_for("contact"))

    return render_template("contact.html", form=form)

# 🧠 Step 5: Templates

# base.html:   

# <!DOCTYPE html>
# <html>
# <head>
#     <title>Flask WTForms</title>
# </head>
# <body>
#     <h1>📨 Contact Us</h1>

#     {% with messages = get_flashed_messages(with_categories=true) %}
#       {% if messages %}
#         {% for category, msg in messages %}
#           <p style="color: green;">{{ msg }}</p>
#         {% endfor %}
#       {% endif %}
#     {% endwith %}

#     {% block content %}{% endblock %}
# </body>
# </html>


# contact.html:
# {% extends "base.html" %}
# {% block content %}
#   <form method="POST">
#     {{ form.hidden_tag() }}

#     <p>
#       {{ form.name.label }}<br>
#       {{ form.name(size=32) }}<br>
#       {% for error in form.name.errors %}
#         <span style="color: red;">{{ error }}</span>
#       {% endfor %}
#     </p>

#     <p>
#       {{ form.email.label }}<br>
#       {{ form.email(size=32) }}<br>
#       {% for error in form.email.errors %}
#         <span style="color: red;">{{ error }}</span>
#       {% endfor %}
#     </p>

#     <p>
#       {{ form.message.label }}<br>
#       {{ form.message(rows=4, cols=32) }}<br>
#       {% for error in form.message.errors %}
#         <span style="color: red;">{{ error }}</span>
#       {% endfor %}
#     </p>

#     <p>{{ form.submit() }}</p>
#   </form>
# {% endblock %}

# ✅ Your To-Do:
# - Set up the folder and files as shown
# - Install flask-wtf
# - Run the app and test form validation
# - Push to GitHub

# Once complete, we’ll move on to the mini project using WTForms.

# NOTE: IN CASE YOU ENCOUNTER EXCEPTION ERROR: Exception: "Install 'email_validator' for email validation support."

# ✅ Step-by-Step Fix
# 🔧 1. Install email-validator
# Activate your virtual environment and run: pip install email-validator
# Then confirm it installed: pip show email-validator

# 🧪 2. Re-run Your Flask App
# Once the package is installed, your Email() validator will work correctly:
from wtforms.validators import Email

email = StringField("Email", validators=[Email()])


# 📌 Why this matters
# - The Email() validator internally uses email-validator to:
# - Properly parse and validate real email addresses
# - Catch formatting mistakes like user@com or no-at-symbol.com
# - Support internationalized domain names and Unicode characters




