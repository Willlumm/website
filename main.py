from flask import Flask, render_template, request
from password_generator import generate_password

app = Flask(__name__)

@app.route("/")
def main():
    return render_template("main.html")

@app.route("/password", methods=["GET", "POST"])
def password():
    length = 64
    if request.method == "POST":
        length = int(request.form["length"])
    password = generate_password(length)
    return render_template("password.html", password=password, length=length)

@app.route("/voting")
def voting():
    global a
    a += 1
    return f"Tally: {a}"

if __name__ == "main":
    a = 0