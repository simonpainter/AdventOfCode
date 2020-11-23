import scratchlib
with open ("input.txt", "r") as inputfile:
	data=inputfile.read()
base_program = []
for item in data.strip().split(','):
    base_program.append(int(item))


for n in range(0,100):
    for v in range(0,100):
		o = base_program[:]
		if scratchlib.intcode(o,n,v) == 19690720:
			print n*100 + v
