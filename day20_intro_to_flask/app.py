from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/profile/<name>/<int:age>")
def profile(name, age):
    # user = {
    #     "name" : "Kayode Oluwasegun",
    #     "age" : "30",
    #     "skills" : ["Python","PHP","Javascript","Java"]
    # }
    return render_template("profile.html", name=name, age = age)

@app.route("/contact/<name>")
def contact(name):
    
    return render_template("contact.html", name=name)


if __name__ == "__main__":
    app.run(debug=True)
