with open ("input.txt", "r") as inputfile:
	data=inputfile.readlines()
paths = []
distances = []
for line in data:
    path = []
    x = 0
    y = 0
    for instruction in line.strip().split(','):
        for i in range(0,int(instruction[1:])):
            if instruction[0] == "U":
                x += 1
            elif instruction[0] == "D":
                x -= 1
            elif instruction[0] == "L":
                y -= 1
            elif instruction[0] == "R":
                y += 1
            current = x,y
            path.append(current)
    paths.append(set(path))
for first in paths[0]:
    for second in paths[1]:
        if first == second:
            distances.append(abs(first[0])+abs(first[1]))

print min(distances)
