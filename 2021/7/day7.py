import re, itertools, math, statistics

with open ("input.txt", "r") as inputfile:
	data = inputfile.read()
	lines = data.split('\n')
	groups = data.split('\n\n')

input =  []
for line in lines:
	#input.append(int(line))
	for data in line.split(","):
		input.append(int(data))
#for group in groups:
	#input.append(group.replace("\n", "")
	#input.append(group.split(' '))

def part1(input):
	output = 0
	target = statistics.median(input)
	for data in input:
		output += abs(target - data)
	return output



def part2(input):
	results = {}
	for target in range(max(input)):
		fuel = 0
		for crab in input:
			distance = abs(target - crab)
			fuel += (distance * (distance + 1))/2
		results[target] = fuel
	return min(results.values())


print(part1(input))
print(part2(input))