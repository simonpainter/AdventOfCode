import re, itertools, math

with open ("input.txt", "r") as inputfile:
	data = inputfile.read()
	lines = data.split('\n')
	groups = data.split('\n\n')

input = []
for line in lines:
	input.append(int(line))
	#input.append(line.split(' '))
#for group in groups:
	#input.append(group.replace("\n", "")
	#input.append(group.split(' '))

def part1(input):
	count = 0
	for i in range(1, len(input)):
		if input[i] > input[i-1]:
			count+=1
	return count
def part2(input):
	count = 0
	for i in range(3, len(input)):
		if (input[i-2]+input[i-1]+input[i] ) > (input[i-3]+input[i-2]+input[i-1] ):
			count+=1
	return count

print(part1(input))
print(part2(input))