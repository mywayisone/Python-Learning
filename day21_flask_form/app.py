from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = "supersecretkey" # Needed for flashing

@app.route("/")
def contact():
    return render_template("contact.html")

@app.route("/submit", methods=["POST"])
def submit():
    name = request.form.get("name")
    email = request.form.get("email")
    message = request.form.get("message")

    if not name or not email or not message:
        flash("All fields are required!")
        redirect(url_for('contact'))

    flash(f"Thank you {name}, we received your message.")
    return redirect(url_for("contact"))

if __name__ == "__main__":
    app.run(debug=True)
