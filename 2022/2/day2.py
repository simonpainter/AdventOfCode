import re, itertools, math,os,sys,time

           
pathname = os.path.dirname(sys.argv[0])        
testinput_path = pathname + "/testinput.txt"   
input_path = pathname + "/input.txt"



def parse_input(path):
	with open (path, "r") as inputfile:
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
	return input

def part1(input):
	score = 0
	for game in input:
		if game == ['A','X']:
			score += 4
		if game == ['A','Y']:
			score += 8
		if game == ['A', 'Z']:
			score += 3
		if game == ['B','X']:
			score += 1
		if game == ['B','Y']:
			score += 5
		if game == ['B', 'Z']:
			score += 9
		if game == ['C','X']:
			score += 7
		if game == ['C','Y']:
			score += 2
		if game == ['C', 'Z']:
			score += 6
	return score


def part2(input):
	score = 0
	for game in input:
		if game == ['A','X']:
			score += 3
		if game == ['A','Y']:
			score += 4
		if game == ['A', 'Z']:
			score += 8
		if game == ['B','X']:
			score += 1
		if game == ['B','Y']:
			score += 5
		if game == ['B', 'Z']:
			score += 9
		if game == ['C','X']:
			score += 2
		if game == ['C','Y']:
			score += 6
		if game == ['C', 'Z']:
			score += 7
	return score

testresult_part1 = 15
testresult_part2 = 12


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
	print("====Part 1 Time ", end - start)

else:
	print("Part 2 Test Failed")
	print("Part 2 Test Result: ", part2(parse_input(testinput_path)))
	print("Expected ", testresult_part2)