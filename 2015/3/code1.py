with open ("input.txt", "r") as inputfile:
	data=inputfile.readlines()

instructions = data[0].strip()
x = 0
y = 0
visits = []
visits.append(tuple([x,y]))

for instruction in instructions:
    if instruction == "^":
        x+=1
    elif instruction == "<":
        y-=1
    elif instruction == ">":
        y+=1
    elif instruction == "v":
        x-=1
    visits.append(tuple([x,y]))

print len(set(visits))
