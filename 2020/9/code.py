import re, itertools

with open ("input.txt", "r") as inputfile:
	data = inputfile.read()
	lines = data.split('\n')
	groups = data.split('\n\n')
preamble = 25
input = []
for line in lines:
	input.append(int(line))

def part1(input,preamble):
	log = []
	for index in range(preamble, len(input)-preamble):
		combinations = itertools.combinations(input[index-preamble:index],2)
		for combination in combinations:
			if (int(combination[0]) + int(combination[1])) == int(input[index]):
				log.append(int(input[index]))
		if int(input[index]) not in log:
			return input[index]
	return log
def part2(input, preamble):
	target = part1(input,preamble)
	for index in range(0, len(input)):
		for i in range(2, len(input)):
			if sum(input[index:i]) == target:
				answer = input[index:i]
				return min(answer) + max(answer)




print(part1(input,preamble))
print(part2(input,preamble))