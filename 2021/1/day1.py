import re, itertools, math

def parse_input(path):
	with open (path, "r") as inputfile:
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
	return input

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


testresult_part1 = 7
testresult_part2 = 5


if testresult_part1 == part1(parse_input("testinput.txt")):
	print("Part 1 Test Passed")
	print("Part 1 answer ", part1(parse_input("input.txt")))
else:
	print("Part 1 Test Failed")
	print("Part 1 Test ", part1(parse_input("testinput.txt")))
	print("Expected ", testresult_part1)
	
if testresult_part2 == part2(parse_input("testinput.txt")):
	print("Part 2 Test Passed")
	print("Part 2 answer ", part2(parse_input("input.txt")))
else:
	print("Part 2 Test Failed")
	print("Part 2 Test ", part2(parse_input("testinput.txt")))
	print("Expected ", testresult_part2)