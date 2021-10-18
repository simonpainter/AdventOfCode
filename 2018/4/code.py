import re, itertools, math

with open ("input.txt", "r") as inputfile:
	data = inputfile.read()
	lines = data.split('\n')
	groups = data.split('\n\n')

unsorted_input = {}
for line in lines:
	timestamp = re.findall("^\[(.*)\]",line)
	unsorted_input[timestamp[0]]=line
input = sorted(unsorted_input.items())
#for group in groups:
	#input.append(group.replace("\n", "")
	#input.append(group.split(' '))

def part1(input):
	return input

def part2(input):
	pass

print(part1(input))
print(part2(input))