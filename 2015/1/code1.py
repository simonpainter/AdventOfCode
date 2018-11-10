with open ("input.txt", "r") as inputfile:
	data=inputfile.readlines()

floor = 0
for instruction in data[0]:
    if instruction == '(':
        floor +=1
    elif instruction == ')':
        floor -=1
    print floor
