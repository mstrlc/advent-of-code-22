# Advent of Code 2022
# Day 1

# Part 1
file = open("day-1.txt", "r")
file = file.read().splitlines()

elves = []
calories = []

for line in file:
    if (line != ''):
        calories.append(int(line))
    else:
        elves.append(calories)
        calories = []
elves.append(calories)

sums = []
for elf in elves:
    sums.append(sum(elf))

sums.sort(reverse=True)

print("Part 1: Elf with the most calories: " + str(sums[0]))

# Part 2
top_three = sums[0] + sums[1] + sums[2]
print("Part 2: Top three elves: " + str(top_three))
