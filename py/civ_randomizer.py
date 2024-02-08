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

    # Options for distribution?
    counts  = (  0,   1,  2,  3,  4, 5, 6, 7, 8)
    weights = (256, 128, 64, 32, 16, 8, 4, 2, 1)
    count = random.choices(counts, weights=weights, k=1)[0]
    modes = random.sample(data["modes"], k=count)

    counts = (  1,  2, 3, 4, 5, 6)
    weights = (32, 16, 8, 4, 2, 1)
    count = random.choices(counts, weights=weights, k=1)[0]
    victorys = random.sample(data["victorys"], k=count)

    return {
        "civ": civ,
        "leader": leader,
        "leader_img": f"static/img/{leader}.png",
        "map_type": map_type,
        "map_size": map_size,
        "modes": modes,
        "victorys": victorys
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