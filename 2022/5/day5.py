import re, itertools, math,os,sys,string,time

           
pathname = os.path.dirname(sys.argv[0])        
testinput_path = pathname + "/testinput.txt"   
input_path = pathname + "/input.txt"



def parse_input(path):
	with open (path, "r") as inputfile:
		data = inputfile.read()
		layout, moves = data.split('\n\n')
	
	moves = moves.split('\n')
	instructions = []
	for move in moves:
		each = re.findall(r'\d+', move)
		each = list(map(int,each))
		instructions.append(each)
	layout = layout.split('\n')
	number = max(map(int, layout.pop().split()))
	stacks = {i: [] for i in range(1, number + 1)}
	for line in layout:
		position = -3
		for i in range(1, number + 1):
			position += 4
			if line[position] != ' ':
				stacks[i].insert(0,line[position])
			
	return stacks,instructions

def part1(input):
	stacks = input[0]
	for move in input[1]:
		for i in range(move[0]):
			stacks[move[2]].append(stacks[move[1]].pop())
	result = ''
	for stack in stacks:
		result+=stacks[stack][-1]
	return result

def part2(input):
	stacks = input[0]
	for move in input[1]:
		crane_lift = []
		for i in range(move[0]):
			crane_lift.append(stacks[move[1]].pop())
		crane_lift.reverse()
		for crate in crane_lift:
			stacks[move[2]].append(crate)
	result = ''
	for stack in stacks:
		result+=stacks[stack][-1]
	return result

testresult_part1 = 'CMZ'
testresult_part2 = 'MCD'


if testresult_part1 == part1(parse_input(testinput_path)):
	print("*** Part 1 Test Passed ***")
	start = time.time()
	print("----Part 1 Result: ", part1(parse_input(input_path)))
	end = time.time()
	print("====Part 1 Time ", end - start)

else:
	print("Part 1 Test Failed")
	print("Part 1 Test Result: ", part1(parse_input(testinput_path)))
	print("Expected ", testresult_part1)
	
if testresult_part2 == part2(parse_input(testinput_path)):
	print("*** Part 2 Test Passed ***")
	start = time.time()
	print("----Part 2 Result: ", part2(parse_input(input_path)))
	end = time.time()
	print("====Part 2 Time ", end - start)

else:
	print("Part 2 Test Failed")
	print("Part 2 Test Result: ", part2(parse_input(testinput_path)))
	print("Expected ", testresult_part2)