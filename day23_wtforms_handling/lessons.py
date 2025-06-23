# 🔍 What You'll Learn Next
# - Handling form submission using POST method
# - Preserving form data on error
# - Showing success and error messages
# - Adding Bootstrap form styling (optional)

# 🔧 Update app.py to Handle Form Submission
# Here's the updated version of app.py that:
# Handles GET and POST.
# Validates form data.
# Redirects on success.

from flask import Flask, render_template, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)  # Needed for form security

class ContactForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email()])
    message = TextAreaField("Message", validators=[DataRequired()])
    submit = SubmitField("Send")

@app.route("/contact", methods=["GET", "POST"])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        # Form passed validation
        flash("Message sent successfully!", "success")
        return redirect(url_for("success"))
    return render_template("contact.html", form=form)

@app.route("/success")
def success():
    return render_template("success.html")

if __name__ == "__main__":
    app.run(debug=True)


# ✨ What to Do Next
# Update contact.html
# Use the Jinja form rendering and include error messages.

# Create success.html
# A simple page that thanks the user.

# Below are the updated templates for contact.html and success.html, using Bootstrap and Jinja for clean form rendering and feedback.

# 🔧 templates/contact.html
# {% extends "layout.html" %}

# {% block title %}Contact Us{% endblock %}

# {% block content %}
# <div class="container mt-5">
#   <h2>Contact Us</h2>

#   {% with messages = get_flashed_messages(with_categories=true) %}
#     {% if messages %}
#       {% for category, message in messages %}
#         <div class="alert alert-{{ category }} alert-dismissible fade show" role="alert">
#           {{ message }}
#           <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
#         </div>
#       {% endfor %}
#     {% endif %}
#   {% endwith %}

#   <form method="POST">
#     {{ form.hidden_tag() }}

#     <div class="mb-3">
#       {{ form.name.label(class="form-label") }}
#       {{ form.name(class="form-control", placeholder="Enter your name") }}
#       {% if form.name.errors %}
#         <div class="text-danger">{{ form.name.errors[0] }}</div>
#       {% endif %}
#     </div>

#     <div class="mb-3">
#       {{ form.email.label(class="form-label") }}
#       {{ form.email(class="form-control", placeholder="Enter your email") }}
#       {% if form.email.errors %}
#         <div class="text-danger">{{ form.email.errors[0] }}</div>
#       {% endif %}
#     </div>

#     <div class="mb-3">
#       {{ form.message.label(class="form-label") }}
#       {{ form.message(class="form-control", rows=4, placeholder="Your message") }}
#       {% if form.message.errors %}
#         <div class="text-danger">{{ form.message.errors[0] }}</div>
#       {% endif %}
#     </div>

#     {{ form.submit(class="btn btn-primary") }}
#   </form>
# </div>
# {% endblock %}


# ✅ templates/success.html
# {% extends "layout.html" %}

# {% block title %}Success{% endblock %}

# {% block content %}
# <div class="container mt-5 text-center">
#   <h2>✅ Message Sent!</h2>
#   <p>Thank you for contacting us. We'll get back to you shortly.</p>
#   <a href="{{ url_for('contact') }}" class="btn btn-secondary mt-3">Send Another Message</a>
# </div>
# {% endblock %}

# ✅ Now What?
# 1. Test the form submission with:
# - Empty fields (to see validation errors)
# - A valid submission (to see the success page)
# 2. Push your updated files to GitHub.

# Those classes like container, mt-5, and text-center come from Bootstrap, a popular CSS framework. If you're seeing that they "are not defined," it's likely because Bootstrap isn't yet linked in your layout.html.
# Let’s fix that. Here's how to add Bootstrap via CDN:

# ✅ Update templates/layout.html
# Ensure your layout.html has the following:

# <!DOCTYPE html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <meta name="viewport" content="width=device-width, initial-scale=1.0">
#     <title>{% block title %}Flask App{% endblock %}</title>
    
#     <!-- ✅ Bootstrap CSS CDN -->
#     <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
# </head>
# <body>

#     {% block content %}{% endblock %}

#     <!-- ✅ Bootstrap JS (for things like alerts and collapses) -->
#     <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script>
# </body>
# </html>

# ✅ Explanation
# - container – Adds horizontal padding and centers the content on larger screens.
# - mt-5 – Adds top margin (mt = margin top, 5 = spacing size).
# - text-center – Centers text horizontally.

# 🔧 Let’s Wrap Up Jinja Templates:
# Now that we’ve scaffolded and styled the layout, we’ll move into Jinja2 advanced usage, which includes:

# 🔹 1. Template Inheritance Recap
# - ✅ layout.html: The base template
# - ✅ Other pages extend it: {% extends "layout.html" %}

# 🔹 2. Includes
# Use {% include "filename.html" %} to reuse chunks like navbars or footers.
# Example (create a reusable navbar.html):

# <!-- templates/navbar.html -->
# <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
#   <div class="container-fluid">
#     <a class="navbar-brand" href="#">FlaskSite</a>
#     <div>
#       <ul class="navbar-nav me-auto mb-2 mb-lg-0">
#         <li class="nav-item"><a class="nav-link" href="/">Home</a></li>
#         <li class="nav-item"><a class="nav-link" href="/about">About</a></li>
#         <li class="nav-item"><a class="nav-link" href="/contact">Contact</a></li>
#       </ul>
#     </div>
#   </div>
# </nav>

# Then in base.html, right after <body>, add: 
# {% include "navbar.html" %}

# 🔹 3. Conditionals and Loops in Templates
# You can use Python-like logic:

# {% if user %}
#   <h2>Welcome, {{ user }}</h2>
# {% else %}
#   <h2>Welcome, Guest!</h2>
# {% endif %}

# <ul>
# {% for item in items %}
#   <li>{{ item }}</li>
# {% endfor %}
# </ul>

# 🔹 4. Filters
# Useful for formatting:

# {{ price | round(2) }}
# {{ name | upper }}
# {{ text | length }}

# 🚀 Your Mini Task:
# 1. Create a navbar.html.
# 2. Include it in layout.html.
# 3. Pass a variable like user = "Segun" to one of your pages and display a conditional greeting using Jinja.

# Example in app.py:
@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html", user="Segun")
