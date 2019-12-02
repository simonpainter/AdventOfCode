with open ("input.txt", "r") as inputfile:
	data=inputfile.read()
base_program = []
for item in data.strip().split(','):
    base_program.append(int(item))

def intcode(noun, verb):
    opcodes = base_program[:]
    opcodes[1] = noun
    opcodes[2] = verb
    position = 0
    while opcodes[position] != 99:
        #print position, opcodes[position], opcodes[position+1], opcodes[position+2], opcodes[position+3]
        #print position, opcodes[opcodes[position+1]] ,opcodes[opcodes[position+2]] , opcodes[opcodes[position+3]]
        if opcodes[position] == 1:
            opcodes[opcodes[position+3]] = opcodes[opcodes[position+1]] + opcodes[opcodes[position+2]]
        elif int(opcodes[position]) == 2:
            opcodes[opcodes[position+3]] = opcodes[opcodes[position+1]] * opcodes[opcodes[position+2]]
        position +=4
    return opcodes

for n in range(0,100):
    for v in range(0,100):
        if intcode(n,v)[0] == 19690720:
            print n*100 + v
