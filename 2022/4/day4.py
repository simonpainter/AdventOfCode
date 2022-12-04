import re, itertools, math,os,sys,string,time
from operator import methodcaller
           
pathname = os.path.dirname(sys.argv[0])        
testinput_path = pathname + "/testinput.txt"   
input_path = pathname + "/input.txt"



def parse_input(path):
	with open (path, "r") as inputfile:
		data = inputfile.read()
		lines = data.split('\n')
	
	input = []

	for line in lines:
		pairs = []
		pair = line.split(',')
		for each in pair:
			each = each.split('-')
			each = list(map(int,each))
			pairs.append(each)
		input.append(pairs)
	return input

def part1(input):
	total = 0
	for pair in input:
		if set(range(pair[0][0],pair[0][1]+1)).issubset(range(pair[1][0],pair[1][1]+1)) \
		or set(range(pair[1][0],pair[1][1]+1)).issubset(range(pair[0][0],pair[0][1]+1)):
			total += 1
	return total

def part2(input):
	total = 0
	for pair in input:
		if set(range(pair[0][0],pair[0][1]+1)) & set(range(pair[1][0],pair[1][1]+1)):
			total += 1
	return total

testresult_part1 = 2
testresult_part2 = 4


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