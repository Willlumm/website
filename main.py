# flask --app main run -p 8000  

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def main():
    return render_template("main.html")

@app.route("/password", methods=["GET", "POST"])
def password():
    return render_template("password.html")

@app.route("/voting")
def voting():
    global a
    a += 1
    return f"Tally: {a}"

if __name__ == "main":
    a = 0