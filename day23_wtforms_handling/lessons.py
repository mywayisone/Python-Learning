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