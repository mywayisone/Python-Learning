from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    posts = [
        {"title": "Flask Basics", "author": "John"},
        {"title": "Understanding Jinja", "author": "Mary"},
        {"title": "Web Dev with Python", "author": "Ada"},
    ]
    return render_template("index.html", posts=posts)

@app.route("/users")
def users():
    users = [
        {"name": "Kayode Segun", "email": "example@gmail.com", "is_admin" : False},
        {"name": "Matthew King", "email": "example@gmail.com",  "is_admin": True},
        {"name": "Gbenga Priest", "email": "example@gmail.com", "is_admin": True}, 
    ]    
    return render_template("users.html", users=users)

@app.errorhandler(404)
def not_found(e):
    return render_template("404.html"), 404


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
