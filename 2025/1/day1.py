import re, itertools, math, os, sys, string, time
import collections, heapq, functools

           
pathname = os.path.dirname(os.path.abspath(__file__))        
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
		if line.strip():  # Skip empty lines
			input.append(line)
		#input.append(line.split(' '))
	#for group in groups:
		#input.append(group.replace("\n", "")
		#input.append(group.split(' '))
	return input

def part1(input):
	dial = list(range(0,100))
	count = 0
	position = 50
	for line in input:
		direction, steps = re.search(r'([LR])(\d+)', line).groups()
		if direction == 'L':
			position = (position - int(steps)) % 100
		if direction == 'R':
			position = (position + int(steps)) % 100
		if dial[position] == 0:
			count += 1
	return count

def part2(input):
	dial = list(range(0,100))
	count = 0
	position = 50
	for line in input:
		direction, steps = re.search(r'([L|R])(\d+)', line).groups()
		steps = int(steps)
		
		count += steps // 100
		
		remaining = steps % 100
		new_position = None
		
		if direction == 'L':
			new_position = (position - steps) % 100
			if remaining > 0 and position > 0 and (position - remaining) < 0:
				count += 1
			position = new_position
		if direction == 'R':
			new_position = (position + steps) % 100
			if remaining > 0 and (position + remaining) >= 100:
				if new_position != 0:
					count += 1
			position = new_position
		if dial[position] == 0:
			count += 1
	return count

testresult_part1 = 3
testresult_part2 = 6


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