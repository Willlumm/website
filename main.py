# flask --app main run -p 8000  

from flask import Flask, render_template, request

from py import civ_randomizer

app = Flask(__name__)

@app.route("/")
def main():
    return render_template("main.html")

@app.route("/civ", methods=["GET", "POST"])
def civ():
    settings = civ_randomizer.randomize()
    return render_template("civ.html", settings=settings)

@app.route("/password", methods=["GET", "POST"])
def password():
    return render_template("password.html")