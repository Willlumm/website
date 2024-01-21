# Show state of tourney
# Show match
# Get result of match
# Update state of tourney

# 1: 0
# 2: 1
# 4: 3
# 8: 7

import math as m

def arrange_seed(n):
    seeds = [1, 2]
    for i in range(2, int(m.log(n, 2)) + 1):
        new_seeds = []
        for s in seeds:
            new_seeds += [s, 2**i - s + 1]
        seeds = new_seeds
    return seeds

def generate_bracket(items):
    bracket = []
    for round in range(1, int(m.log(len(items), 2)) + 1):
        bracket_len = len(bracket)
        round_len = len(items) // 2**round
        for i in range(round_len):
            left, right = None, None
            next_match = bracket_len + round_len + i//2
            if round == 1:
                left, right = items[2*i : 2*i+2]
            elif round_len == 1:
                next_match = None
            bracket.append({
                "match": bracket_len + i,
                "round": round,
                "left": left,
                "right": right,
                "left_score": None,
                "right_score": None,
                "next_match": next_match
            })
            print(bracket[-1])
        print()
    return bracket

items = [i for i in range(1, 2**6+1)]
generate_bracket(items)

def get_votes(match):
    print(f"{match[0]} vs {match[1]}")
    votes = input.split(" ")
    return votes
        

def main(items):
    bracket = generate_bracket(items)
    for match in bracket:
        match[2:] = get_votes(match)
    

"""
items = ["a", "b", "c", "d"]
main(items)

while len(items) > 1:

    winners = []
    mid = len(items) // 2

    for a, b in zip(items[:mid], items[mid:]):
        if "1" == "1":
            winners.append(a)
        else :
            winners.append(b)

    items = winners
    print(items)
"""