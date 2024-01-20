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
    # match, round, a_name, b_name, a_score, b_score, destination
    bracket = []
    i = len(items)
    r = 0
    while i > 1:
        round = []
        for j in range(i//2):
            a, b = None, None
            dest = len(bracket) + i//2 + (j//2)
            if r == 0:
                a, b = items[2*j : 2*j+2]
            elif i == 2:
                dest = None
            round.append([r, a, b, None, None, dest])
            print(round[-1])
        i //= 2
        r += 1
        bracket.extend(round)
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