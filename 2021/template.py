import re, itertools, math

def parse_input(path):
	with open (path, "r") as inputfile:
		data = inputfile.read()
		lines = data.split('\n')
		groups = data.split('\n\n')

	input = []
	#for line in lines:
		#input.append(int(line))
		#input.append(line.split(' '))
	#for group in groups:
		#input.append(group.replace("\n", "")
		#input.append(group.split(' '))
	return input

def part1(input):
	pass

def part2(input):
	pass

testresult_part1 = 0
testresult_part2 = 0


if testresult_part1 == part1(parse_input("testinput.txt")):
	print("*** Part 1 Test Passed ***")
	print("----Part 1 Result ", part1(parse_input("input.txt")))
else:
	print("Part 1 Test Failed")
	print("Part 1 Test Result", part1(parse_input("testinput.txt")))
	print("Expected ", testresult_part1)
	
if testresult_part2 == part2(parse_input("testinput.txt")):
	print("*** Part 2 Test Passed ***")
	print("----Part 2 Result ", part2(parse_input("input.txt")))
else:
	print("Part 2 Test Failed")
	print("Part 2 Test Result", part2(parse_input("testinput.txt")))
	print("Expected ", testresult_part2)