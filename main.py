# flask --app main run -p 8000  

from flask import Flask, render_template, request

from py import civ_randomizer

app = Flask(__name__)

@app.route("/")
def main():
    return render_template("main.html")

@app.route("/civ", methods=["GET", "POST"])
def civ():
    if request.form:
        settings = request.form
    else:
        settings = None
    result = civ_randomizer.randomize(settings)
    return render_template("civ.html", settings=settings, result=result)

@app.route("/password", methods=["GET", "POST"])
def password():
    return render_template("password.html")