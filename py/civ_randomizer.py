import json
import random

def load_data():
    with open("static/json/civ.json") as file:
        return json.load(file)
    
def pick_random(items):
    return random.choice(items)
    
def randomize():

    data = load_data()

    leader, civ = pick_random(data["leaders"]).values()

    map = pick_random(data["maps"])

    map_type = map["type"]

    map_sizes = map["sizes"] if "sizes" in map else ("Duel", "Tiny", "Small", "Standard", "Large", "Huge")
    map_size = pick_random(map_sizes)

    return {
        "civ": civ,
        "leader": leader,
        "map_type": map_type,
        "map_size": map_size
    }

print(randomize())

"""
        // https://civilization.fandom.com/wiki/Starting_a_new_game_(Civ6)

        // Basic

        // Ruleset
        // Civ
        // Leader
        // Difficulty
        // Game speed
        // Map type
        // Map size
        // Game modes
        // Disaster intensity
        
        // Advanced

        // Start era
        // Number of city-states
        // Resource abundance
        // World age
        // Start position
        // Temperature
        // Rainfall
        // Sea level
        // Victory conditions
"""