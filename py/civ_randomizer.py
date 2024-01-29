import json
import random

def load_leaders():
    with open("json/civ/leaders.json") as file:
        return json.load(file)
    
def pick_random(items):
    return random.choice(items)
    
def randomize():
    leaders = load_leaders()
    return pick_random(leaders)