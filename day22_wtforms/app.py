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

if __name__ == "__main__":
    app.run(debug=True)