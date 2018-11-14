with open ("input.txt", "r") as inputfile:
	data=inputfile.readlines()
errors = 1
wires = {}
import sys

while errors >= 1:
    errors = 0
    for line in data:
        try:
            instruction = line.split()
            if len(instruction) == 3:
                if instruction[0].isdigit():
                    wires[instruction[2]] = int(instruction[0])
                else:
                    wires[instruction[2]] = int(wires[instruction[0]])
            if len(instruction) == 4:
                if instruction[1].isdigit():
                    wires[instruction[3]] = int(instruction[1])^65535
                else:
                    wires[instruction[3]] = int(wires[instruction[1]])^65535
            if len(instruction) == 5:
                if instruction[1]=='AND':
                    if instruction[0].isdigit():
                        wires[instruction[4]] = int(instruction[0]) & int(wires[instruction[2]])
                    else:
                        wires[instruction[4]] = int(wires[instruction[0]]) & int(wires[instruction[2]])
                elif instruction[1]=='OR':
                    if instruction[0].isdigit():
                        wires[instruction[4]] = int(instruction[0]) | int(wires[instruction[2]])
                    else:
                        wires[instruction[4]] = int(wires[instruction[0]]) | int(wires[instruction[2]])
                elif instruction[1]=='LSHIFT':
                    wires[instruction[4]] = int(wires[instruction[0]]) << int(instruction[2])
                elif instruction[1]=='RSHIFT':
                    wires[instruction[4]] = int(wires[instruction[0]]) >> int(instruction[2])

        except:
            pass
            errors +=1
            print instruction
    print wires
    print errors


print wires
print wires['a']
