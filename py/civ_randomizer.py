import json
import random

def load_data():
    with open("static/json/civ.json") as file:
        return json.load(file)
    
def pick_random(items):
    return random.choice(items)
    
def randomize(options):

    data = load_data()

    leader, civ = pick_random(data["leaders"]).values()

    maps = [map for map in data["maps"] if "tsl" not in map or civ in map["tsl"] ]
    map = pick_random(maps)
    map_type = map["type"]

    map_sizes = map["sizes"] if "sizes" in map else ("Duel", "Tiny", "Small", "Standard", "Large", "Huge")
    map_size = pick_random(map_sizes)

    random_victory_conditions = []
    chosen_victory_conditions = []
    for victory_condition in ("Culture", "Diplomatic", "Domination", "Religious", "Science", "Score"):
        if options[victory_condition] == "never":
            continue
        elif options[victory_condition] == "random":
            random_victory_conditions.append(victory_condition)
        elif options[victory_condition] == "always":
            chosen_victory_conditions.append(victory_condition)
    k = int(options["victory_condition_count"]) - len(chosen_victory_conditions)
    k = min(k, len(random_victory_conditions))
    k = max(k, 0)
    chosen_victory_conditions += sorted(random.sample(random_victory_conditions, k=k))

    random_game_modes = []
    chosen_game_modes= []
    for game_mode in ("Apocalypse", "Barbarian Clans", "Dramatic Ages", "Heroes & Legends", "Monopolies and Corporations", "Secret Societies", "Tech and Civic Shuffle", "Zombie Defense"):
        if options[game_mode] == "never":
            continue
        elif options[game_mode] == "random":
            random_game_modes.append(game_mode)
        elif options[game_mode] == "always":
            chosen_game_modes.append(game_mode)
    k = random.randint(int(options["game_mode_min"]), int(options["game_mode_max"]))
    k = k - len(chosen_game_modes)
    k = min(k, len(random_game_modes))
    k = max(k, 0)
    chosen_game_modes += sorted(random.sample(random_game_modes, k=k))

    return {
        "civ":                      civ,
        "leader":                   leader,
        "map_type":                 map_type,
        "map_size":                 map_size,
        "game_modes":               chosen_game_modes,
        "victory_conditions":       chosen_victory_conditions,
        "civ_img":                  f"static/img/civs/{civ} ({leader}) (Civ6).png",
        "leader_img":               f"static/img/leaders/{leader}.png",
        "map_type_img":             f"static/img/maps/Map {map_type} (Civ6).png",
        "game_mode_imgs":           [f"static/img/modes/{mode}.png" for mode in chosen_game_modes],
        "victory_condition_imgs":   [f"static/img/victories/{victory_condition} Victory (Civ6).png" for victory_condition in chosen_victory_conditions]
    }