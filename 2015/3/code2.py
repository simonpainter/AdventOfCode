with open ("input.txt", "r") as inputfile:
	data=inputfile.readlines()

instructions = data[0].strip()
x=[0,0]
y=[0,0]
actor=0
visits = []
visits.append(tuple([x[actor],y[actor]]))

for instruction in instructions:

    if instruction == "^":
        x[actor]+=1
    elif instruction == "<":
        y[actor]-=1
    elif instruction == ">":
        y[actor]+=1
    elif instruction == "v":
        x[actor]-=1
    visits.append(tuple([x[actor],y[actor]]))
    if actor==1:
        actor=0
    else:
        actor=1
print len(set(visits))
