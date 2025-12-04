import re, itertools, math, os, sys, string, time
import collections, heapq, functools

           
pathname = os.path.dirname(sys.argv[0])        
testinput_path1 = pathname + "/testinput1.txt"   
testinput_path2 = pathname + "/testinput2.txt"  
input_path = pathname + "/input.txt"



def parse_input(path):
	with open (path, "r") as inputfile:
		data = inputfile.read()
		lines = data.split('\n')
		groups = data.split('\n\n')

	input = []
	for line in lines:
		input.append(str(line))
		#input.append(line.split(' '))
	#for group in groups:
		#input.append(group.replace("\n", "")
		#input.append(group.split(' '))
	return input


def part1(input):
	total = 0
	formatted = []
	length = 1
	for line in input:
		battery = []
		list_line = list(map(int,list(line)))
		for index in range(length, -1, -1):
			unit = max(list_line[:-index]) if index != 0 else max(list_line)
			battery.append(unit)
			list_line = list_line[list_line.index(unit) + 1 :]
		joltage = int(''.join(map(str, battery)))
		total += joltage
	return total

def part2(input):
	total = 0
	formatted = []
	length = 11
	for line in input:
		battery = []
		list_line = list(map(int,list(line)))
		for index in range(length, -1, -1):
			unit = max(list_line[:-index]) if index != 0 else max(list_line)
			battery.append(unit)
			list_line = list_line[list_line.index(unit) + 1 :]
		joltage = int(''.join(map(str, battery)))
		total += joltage
	return total

testresult_part1 = 357
testresult_part2 = 3121910778619


if testresult_part1 == part1(parse_input(testinput_path1)):
	print("*** Part 1 Test Passed ***")
	start = time.time()
	print("----Part 1 Result: ", part1(parse_input(input_path)))
	end = time.time()
	print("====Part 1 Time ", end - start)

else:
	print("Part 1 Test Failed")
	print("Part 1 Test Result: ", part1(parse_input(testinput_path1)))
	print("Expected ", testresult_part1)
	
if testresult_part2 == part2(parse_input(testinput_path2)):
	print("*** Part 2 Test Passed ***")
	start = time.time()
	print("----Part 2 Result: ", part2(parse_input(input_path)))
	end = time.time()
	print("====Part 2 Time ", end - start)

else:
	print("Part 2 Test Failed")
	print("Part 2 Test Result: ", part2(parse_input(testinput_path2)))
	print("Expected ", testresult_part2)