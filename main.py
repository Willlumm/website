from flask import Flask, render_template
from password_generator import generate_password

app = Flask(__name__)

@app.route("/")
def main():
    return render_template("main.html")

@app.route("/password")
def password():
    password = generate_password()
    return render_template("password.html", password=password)