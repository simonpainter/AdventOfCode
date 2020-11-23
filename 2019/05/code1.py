import scratchlib

with open ("input.txt", "r") as inputfile:
	data=inputfile.read()
program = data.strip().split(',')

print scratchlib.intcode(program,1)
