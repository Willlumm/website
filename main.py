# flask --app main run -p 8000  

from flask import Flask, render_template, request

from py import civ_randomizer

app = Flask(__name__)

@app.route("/")
def main():
    return render_template("main.html")

@app.route("/civ", methods=["GET", "POST"])
def civ():
    if request.method == "GET":
        options = {
            "victory_condition_count":      "1",
            "game_mode_min":                "0",
            "game_mode_max":                "8",
            "Culture":                      "random",
            "Diplomatic":                   "random",
            "Domination":                   "random",
            "Religious":                    "random",
            "Science":                      "random",
            "Score":                        "never",
            "Apocalypse":                   "random",
            "Barbarian Clans":              "random", 
            "Dramatic Ages":                "random", 
            "Heroes & Legends":             "random", 
            "Monopolies and Corporations":  "random", 
            "Secret Societies":             "random", 
            "Tech and Civic Shuffle":       "random",
            "Zombie Defense":               "random"
        }
    elif request.method == "POST":
        options = request.form
    result = civ_randomizer.randomize(options)
    return render_template("civ.html", options=options, result=result)

@app.route("/password", methods=["GET", "POST"])
def password():
    return render_template("password.html")