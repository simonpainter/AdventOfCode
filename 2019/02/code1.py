with open ("input.txt", "r") as inputfile:
	data=inputfile.read()
position = 0
opcodes = data.strip().split(',')

while int(opcodes[position]) != 99:
    if int(opcodes[position]) == 1:
        opcodes[int(opcodes[position+3])]=int(opcodes[int(opcodes[position+1])]) + int(opcodes[int(opcodes[position+2])])
    elif int(opcodes[position]) == 2:
        opcodes[int(opcodes[position+3])]=int(opcodes[int(opcodes[position+1])]) * int(opcodes[int(opcodes[position+2])])
    position +=4

print opcodes
