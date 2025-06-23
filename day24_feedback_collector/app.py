from flask import Flask, render_template, redirect, url_for, flash
from forms import FeedbackForm

app = Flask(__name__)
app.secret_key = "your_secret_key"

@app.route("/", methods=["GET", "POST"])
def index():
    form = FeedbackForm()
    if form.validate_on_submit():
        with open("feedbacks.txt", "a") as f:
            f.write(f"{form.name.data} | {form.email.data} | {form.feedback.data}\n")
        flash("Feedback submitted successfully!", "success")
        return redirect(url_for("success"))
    return render_template("index.html", form=form)

@app.route("/success")
def success():
    return render_template("success.html")

@app.route("/dashboard")
def dashboard():
    feedbacks = []
    try:
        with open("feedbacks.txt", "r") as f:
            feedbacks = [line.strip().split(" | ") for line in f.readlines()]
    except FileNotFoundError:
        pass
    return render_template("dashboard.html", feedbacks=feedbacks)

if __name__ == "__main__":
    app.run(debug=True)
