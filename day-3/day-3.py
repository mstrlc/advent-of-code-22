# Advent of Code 2022
# Day 3

# Part 1
file = open("day-3.txt", "r")
lines = file.read().splitlines()

data = []

for line in lines:
    contents = [line[0: int(len(line)/2)], line[int(len(line)/2):len(line)]]
    data.append(contents)

sum = 0    

for item in data:
    for i in range(0, len(item[0])):
        for j in range(0, len(item[1])):
            if (item[0][i] == item[1][j]):
                common = item[0][i]
                break
    if(common >= 'a' and common <= 'z'):
        sum = sum + (ord(common) - ord('a') + 1)
    elif(common >= 'A' and common <= 'Z'):
        sum = sum + (ord(common) - ord('A') + 1 + 26)

print("Part 1: Sum of priorities is: " + str(sum))

# Part 2
sum = 0

for i in range(0, len(lines), 3):
    for j in range(0, len(lines[i])):
        for k in range(0, len(lines[i+1])):
            for l in range(0, len(lines[i+2])):
                if (lines[i][j] == lines[i+1][k] == lines[i+2][l]):
                    common = lines[i][j]
                    break
    if(common >= 'a' and common <= 'z'):
        sum = sum + (ord(common) - ord('a') + 1)
    elif(common >= 'A' and common <= 'Z'):
        sum = sum + (ord(common) - ord('A') + 1 + 26)

print("Part 2: Sum of priorities is: " + str(sum))