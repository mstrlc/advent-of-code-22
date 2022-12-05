# Advent of Code 2022
# Day 5

# Part 1
file = open("day-5.txt", "r")
lines = file.read().splitlines()

container = [[] for i in range(9)]

# Parse container in input
i = 0
for line in lines:
    if (i < 8):
        container[0].append(line[1])
        container[1].append(line[5])
        container[2].append(line[9])
        container[3].append(line[13])
        container[4].append(line[17])
        container[5].append(line[21])
        container[6].append(line[25])
        container[7].append(line[29])
        container[8].append(line[33])
    i += 1

# Reverse to correct order          
for i in range(9):
    container[i].reverse()    

for line in lines:
    if(line.__contains__("move")):
        line = line.split(" ")
        count = int(line[1])
        frm = int(line[3])-1
        to = int(line[5])-1
        for j in range(0, count):
            top = container[frm].pop()
            while(top == " "):
                top = container[frm].pop()
            container[to].append(top)

print("Part 1: Top of each container: ", end="")
# print last non-empty element of each container
for i in range(len(container)):
    print(container[i][-1], end="")

print()

# Part 2
# Create empty array of 9 empty linked lists
container_2 = [[] for i in range(9)]

i = 0
for line in lines:
    if (i < 8):
        container_2[0].append(line[1])
        container_2[1].append(line[5])
        container_2[2].append(line[9])
        container_2[3].append(line[13])
        container_2[4].append(line[17])
        container_2[5].append(line[21])
        container_2[6].append(line[25])
        container_2[7].append(line[29])
        container_2[8].append(line[33])
    i += 1

# Reverse to correct order   
       
for i in range(9):
    container_2[i].reverse()    

for line in lines:
    if(line.__contains__("move")):
        line = line.split(" ")
        count = int(line[1])
        frm = int(line[3])-1
        to = int(line[5])-1
        moved_container = []
        for j in range(0, count):
            top = container_2[frm].pop()
            while(top == " "):
                top = container_2[frm].pop()
            moved_container.append(top)
        for k in range(0, count):
            container_2[to].append(moved_container.pop())

print("Part 2: Top of each container: ", end="")
# print last non-empty element of each container
for i in range(len(container_2)):
    print(container_2[i][-1], end="")

print()