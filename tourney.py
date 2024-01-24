# Show state of tourney
# Show match
# Get result of match
# Update state of tourney

import json
import math

def arrange_seed(n):
    seeds = [1, 2]
    for i in range(2, int(math.log(n, 2)) + 1):
        new_seeds = []
        for s in seeds:
            new_seeds += [s, 2**i - s + 1]
        seeds = new_seeds
    return seeds

def generate_bracket(items):
    bracket = []
    for round in range(1, int(math.log(len(items), 2)) + 1):
        bracket_len = len(bracket)
        round_len = len(items) // 2**round
        for i in range(round_len):
            game_items = []
            next_game = bracket_len + round_len + i//2
            if round == 1:
                game_items = items[2*i : 2*i+2]
            elif round_len == 1:
                next_game = None
            bracket.append({
                "game": bracket_len + i,
                "round": round,
                "items": game_items,
                "scores": [],
                "next_game": next_game
            })
    return bracket

def save_bracket(bracket):
    with open("bracket.json", "w") as file:
        json.dump(bracket, file)

def get_scores(items):
    print(" vs ".join([str(item) for item in items]))
    scores = [int(score) for score in input().split(" ")]
    return scores
        
def main(items):
    bracket = generate_bracket(items)
    save_bracket(bracket)
    for game in bracket:
        scores = get_scores(game["items"])
        game["scores"] = scores
        winner = game["items"][scores.index(max(scores))]
        next_game = game["next_game"]
        if next_game:
            bracket[next_game]["items"].append(winner)
        save_bracket(bracket)

items = [i for i in range(1, 2**3+1)]
main(items)