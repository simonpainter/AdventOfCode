import re, itertools
from copy import deepcopy

with open ("input.txt", "r") as inputfile:
	data = inputfile.read()
	lines = data.split('\n')
	groups = data.split('\n\n')

input = []
for line in lines:
	input.append(line.split(' '))

def execute_command(command, index, result):
	if command[0] == 'nop':
		index +=1
		return index,result
	elif command[0] == 'acc':
		index +=1
		result += int(command[1])
		return index,result
	elif command[0] == 'jmp':
		index += int(command[1])
		return index,result

def flip_instruction(this_input, flip):
	output = deepcopy(this_input)
	if output[flip][0] == 'nop':
		output[flip][0] = 'jmp'
	elif output[flip][0] == 'jmp':
		output[flip][0] = 'nop'
	return output

def part1(input):
	visited = []
	index = 0
	result = 0
	while index not in visited:
		visited.append(index)
		index,result = execute_command(input[index],index, result)
	return result
def part2(input):
	for flip in range(0,len(input)):
		flipped_input = flip_instruction(input, flip)
		visited = []
		index = 0
		result = 0
		while index not in visited:
			visited.append(index)
			if index >= len(input):
				return 'completed', result
			index,result = execute_command(flipped_input[index],index, result)


print(part1(input))
print(part2(input))