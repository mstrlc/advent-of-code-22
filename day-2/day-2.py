# Advent of Code 2022
# Day 2

# Part 1
# Oponent           A for Rock, B for Paper, and C for Scissors
# You should play   X for Rock, Y for Paper, and Z for Scissors
file = open("day-2.txt", "r")
lines = file.read().splitlines()

games = []

for line in lines:
    games.append(line.split())

total_score = 0

for game in games:
    oponent = game[0]
    if (oponent == 'A'):
        oponent = 'Rock'
    elif (oponent == 'B'):
        oponent = 'Paper'
    elif (oponent == 'C'):
        oponent = 'Scissors'

    you = game[1]
    if (you == 'X'):
        you = 'Rock'
    elif (you == 'Y'):
        you = 'Paper'
    elif (you == 'Z'):
        you = 'Scissors'

    if (you == 'Rock'):
        total_score = total_score + 1
    elif (you == 'Paper'):
        total_score = total_score + 2
    elif (you == 'Scissors'):
        total_score = total_score + 3

    if (you == oponent):
        total_score = total_score + 3

    if (you == 'Rock'):
        if (oponent == 'Scissors'):
            total_score = total_score + 6
    if (you == 'Paper'):
        if (oponent == 'Rock'):
            total_score = total_score + 6
    if (you == 'Scissors'):
        if (oponent == 'Paper'):
            total_score = total_score + 6

print("Part 1: Total score would be: " + str(total_score))

# Part 2
# Oponent           A for Rock, B for Paper, and C for Scissors
# Desired outcome   X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win

total_score = 0

for game in games:
    oponent = game[0]
    if (oponent == 'A'):
        oponent = 'Rock'
    elif (oponent == 'B'):
        oponent = 'Paper'
    elif (oponent == 'C'):
        oponent = 'Scissors'

    outcome = game[1]
    if (outcome == 'X'):
        outcome = 'Lose'
    elif (outcome == 'Y'):
        outcome = 'Draw'
    elif (outcome == 'Z'):
        outcome = 'Win'

    if (outcome == 'Draw'):
        you = oponent
    elif (outcome == 'Lose'):
        if (oponent == 'Rock'):
            you = 'Scissors'
        elif (oponent == 'Paper'):
            you = 'Rock'
        elif (oponent == 'Scissors'):
            you = 'Paper'
    elif (outcome == 'Win'):
        if (oponent == 'Rock'):
            you = 'Paper'
        elif (oponent == 'Paper'):
            you = 'Scissors'
        elif (oponent == 'Scissors'):
            you = 'Rock'

    if (oponent == 'Rock'):
        if (you == 'Paper'):
            total_score = total_score + 6
    if(oponent == 'Paper'):
        if (you == 'Scissors'):
            total_score = total_score  + 6
    if(oponent == 'Scissors'):
        if (you == 'Rock'):
            total_score = total_score  + 6

    if (you == 'Rock'):
        total_score = total_score + 1
    elif (you == 'Paper'):
        total_score = total_score + 2
    elif (you == 'Scissors'):
        total_score = total_score + 3

    if (you == oponent):
        total_score = total_score + 3

print("Part 2: Total score would be: " + str(total_score))
