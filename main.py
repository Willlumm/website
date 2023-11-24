from flask import Flask, render_template, request
from password_generator import generate_password

app = Flask(__name__)

@app.route("/")
def main():
    return render_template("main.html")

@app.route("/password", methods=["GET", "POST"])
def password():
    length = int(request.form["length"]) if request.method == "POST" else 64
    password = generate_password(length)
    return render_template("password.html", password=password, length=length)