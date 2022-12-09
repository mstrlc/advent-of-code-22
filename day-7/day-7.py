# Advent of Code 2022
# Day 7

from collections import defaultdict as dd

def get_size(key) -> int:
    size = 0
    for item in dict[key]:
        if(type(item) == int):
            size += item
        elif(item[0] == '/'):
            size += get_size(item)
    return size

# Part 1
file = open("day-7.txt", "r")
lines = file.readlines()

current_path = []
dict = dd(list)

for line in lines:
    # cd command
    if(line.startswith("$ cd")):
        if(line[5:-1] == ".."):
            current_path.pop()
        else:
            current_path.append(line[5:-1])
    elif(line.startswith("$ ls")):
        continue
    else:
        # File
        path = "".join(current_path)
        if(line.split(" ")[0].isnumeric()):
            dict[path].append(int(line.split(" ")[0]))
        # Directory
        else:
            path = "".join(current_path)
            dict[path].append(path + line.split(" ")[1].strip())

sizes = dd(int)

for key in dict.keys():
    sizes[key] = get_size(key)
    
total_sum = 0
    
for key in sizes.keys():
    if(sizes[key] < 100000):
        total_sum += sizes[key]

print("Part 1: Sum of total sizes of directories smaller than 100000: " + str(total_sum))

# Part 2

total_space = 70000000
needed_space = 30000000
need_to_delete = needed_space - total_space + sizes['/']

to_delete = []

for item in sizes:
    if(sizes[item] > need_to_delete):
        to_delete.append(item)

smallest = total_space
for item in to_delete:
    if(sizes[item] < smallest):
        smallest = sizes[item]
        
print("Part 2: Size of smallest item that will free up enough space: " + str(smallest))
