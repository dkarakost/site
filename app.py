from flask import Flask, render_template, url_for, request, flash,redirect
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


app = Flask(__name__)
app.secret_key ="mitsiomitsio"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3'

#Initialize the database
db = SQLAlchemy(app)

class User(db.Model,):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    first_name = db.Column(db.String(100))

# Ensure to create a function to return a string when we add something
def __repr__(self):
    return "<User %r>" % self.email

with app.app_context():
    db.create_all()

class Userform(FlaskForm):
    name = StringField("Name", validators = [DataRequired()])


@app.route("/")
def home():
    flash("What's your name")
    return render_template("base.html")

@app.route("/greet", methods=["POST","GET"])
def greet():
    flash("Hello " + str(request.form['name_input'] + ", great to see you"))
    return render_template("base.html")


@app.route("/login", methods=["POST","GET"])
def login():
    return render_template("login.html")

@app.route("/Sign-up", methods = ["POST","GET"])
def Sign_up():
    if request.method == 'POST':
        email = request.form.get("email")
        firstname = request.form.get("firstname")
        password = request.form.get("password")
        password2 = request.form.get("password2")

        if len(email) < 4:
            flash("email should be greater than 4 characters. ", category="error")
        elif len(firstname) < 2:
            flash("First name should be greater than 1 character. ", category="error")
        elif password != password2:
            flash("Passwords dont match. ", category="error")
        elif len(password) < 7:
            flash("Password should have at least 7 characters", category="error")
        else:
            flash("Account created!", category="success")
    return render_template("Sign_up.html")

@app.route("/Products", methods=["GET"])
def Products():
    return render_template("products.html")

@app.route("/Blog",methods=["GET"])
def Blog():
    return render_template("Blog.html")

@app.route("/Contact", methods=["GET"])
def Contact():
    return render_template("contact.html")



if __name__ == '__main__':
    app.run(debug=True)#re-run the server