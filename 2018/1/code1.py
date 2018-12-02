with open ("input.txt", "r") as inputfile:
	data=inputfile.readlines()
total = 0

for instruction in data:
    total += int(instruction)

print total
