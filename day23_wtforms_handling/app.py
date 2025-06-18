from flask import Flask, render_template, redirect, url_for, flash
from forms import ContactForm
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)  # Needed for form security

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

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html", user="Segun")

if __name__ == "__main__":
    app.run(debug=True)
