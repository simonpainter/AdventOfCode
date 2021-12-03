import re, itertools, math

with open ("input.txt", "r") as inputfile:
	data = inputfile.read()
	lines = data.split('\n')
	groups = data.split('\n\n')

input = []
for line in lines:
	#input.append(int(line))
	input.append(line.split(' '))
#for group in groups:
	#input.append(group.replace("\n", "")
	#input.append(group.split(' '))

def part1(input):
	distance = 0
	depth = 0
	for command in input:
		if command[0] == "forward":
			distance += int(command[1])
		elif command[0] == "down":
			depth += int(command[1])
		elif command[0] == "up":
			depth -= int(command[1])
	return distance * depth

def part2(input):
	distance = 0
	depth = 0
	aim = 0
	for command in input:
		if command[0] == "forward":
			distance += int(command[1])
			depth += aim * int(command[1])
		elif command[0] == "down":
			aim += int(command[1])
		elif command[0] == "up":
			aim -= int(command[1])
	return distance * depth

print(part1(input))
print(part2(input))