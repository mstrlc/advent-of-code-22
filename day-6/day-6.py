# Advent of Code 2022
# Day 6

# Part 1
file = open("day-6.txt", "r")
data = file.read()

# Find index of first character after sequence of 4 non-repeating characters
last_group = ""
index = 0

for char in data:        
    if(len(list(set(last_group))) == 4):
        print("Part 1: " + str(index) + " characters before first start-of-packet (" + last_group + ").")
        break
    if(len(last_group) == 4):
        last_group = last_group.removeprefix(last_group[0])
    last_group += char
    index += 1

# Part 2

# Find index of first character after sequence of 14 non-repeating characters
last_group = ""
index = 0

for char in data:        
    if(len(list(set(last_group))) == 14):
        print("Part 2: " + str(index) + " characters before first start-of-message (" + last_group + ").")
        break
    if(len(last_group) == 14):
        last_group = last_group.removeprefix(last_group[0])
    last_group += char
    index += 1
    
