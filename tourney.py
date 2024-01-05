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

items = [i for i in range(1, 2**8+1)]
print(arrange_seed(len(items)))

"""
def generate_bracket(items):
    # round, a_name, b_name, a_score, b_score, destination
    bracket = []
    i = len(items)
    r = 0
    while i > 1:
        round = []
        for j in range(i//2):
            round.append([r, None, None, None, None, i//2 + (j - i//2)])
        i //= 2
        r += 1
    return bracket

def get_votes(match):
    print(f"{match[0]} vs {match[1]}")
    votes = input.split(" ")
    return votes
        

def main(items):
    bracket = generate_bracket(items)
    for match in bracket:
        match[2:] = get_votes(match)
    


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