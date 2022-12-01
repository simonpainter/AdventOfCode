import re, itertools, math,os,sys

           
pathname = os.path.dirname(sys.argv[0])        
testinput_path = pathname + "/testinput.txt"   
input_path = pathname + "/input.txt"



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

testresult_part1 = 15
testresult_part2 = 0

if testresult_part1 == part1(parse_input(testinput_path)):
	print("*** Part 1 Test Passed ***")
	print("----Part 1 Result ", part1(parse_input(input_path)))
else:
	print("Part 1 Test Failed")
	print("Part 1 Test Result", part1(parse_input(testinput_path)))
	print("Expected ", testresult_part1)
	
if testresult_part2 == part2(parse_input(testinput_path)):
	print("*** Part 2 Test Passed ***")
	print("----Part 2 Result ", part2(parse_input(input_path)))
else:
	print("Part 2 Test Failed")
	print("Part 2 Test Result", part2(parse_input(testinput_path)))
	print("Expected ", testresult_part2)