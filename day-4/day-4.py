# Advent of Code 2022
# Day 4

# Part 1
file = open("day-4.txt", "r")
lines = file.read().splitlines()

data = []

for line in lines:
    contents = line.split(",")
    contents[0] = contents[0].split("-")
    contents[0][0] = int(contents[0][0])
    contents[0][1] = int(contents[0][1])
    contents[1] = contents[1].split("-")
    contents[1][0] = int(contents[1][0])
    contents[1][1] = int(contents[1][1])
    data.append(contents)

count = 0

# Check if one range is within another
for pair in data:
    # pair[0] is fully in pair[1]
    if pair[0][0] >= pair[1][0] and pair[0][1] <= pair[1][1]:
        count += 1
    # pair[1] is fully in pair[0]
    elif pair[1][0] >= pair[0][0] and pair[1][1] <= pair[0][1]:
        count += 1
        
print("Part 1: One range fully contains the other in " + str(count) + "pairs.")

# Part 2

count = 0

# Check if the ranges overlap
for pair in data:
    print(pair[0][0], pair[0][1],",", pair[1][0], pair[1][1])
    if ((pair[1][0] <= pair[0][0] <= pair[1][1])
        or (pair[1][0] <= pair[0][1] <= pair[1][1])
        or (pair[0][0] <= pair[1][0] <= pair[0][1])
        or (pair[0][0] <= pair[1][1] <= pair[0][1])):
        count += 1
            
print("Part 2: The ranges overlap in " + str(count) + " pairs.")