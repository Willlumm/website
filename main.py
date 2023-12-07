# flask --app main run -p 8000  

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def main():
    return render_template("main.html")

@app.route("/password", methods=["GET", "POST"])
def password():
    chars = "".join([chr(i) for i in range(33, 126)])
    length = 64
    if request.method == "POST":
        chars = request.form["chars"]
        length = int(request.form["length"])
    return render_template("password.html", password=password, chars=chars, length=length)