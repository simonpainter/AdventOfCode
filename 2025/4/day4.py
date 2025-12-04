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
	#for line in lines:
		#input.append(int(line))
		#input.append(line.split(' '))
	#for group in groups:
		#input.append(group.replace("\n", "")
		#input.append(group.split(' '))
	return lines

def part1(input):
	count = 0
	for x in range(len(input)):
		for y in range(len(input[x])):
			if input[x][y] == '@':
				bales = 0
				for spot in [(x, y + 1), (x, y - 1), (x + 1, y + 1), (x + 1, y - 1),(x - 1, y + 1), (x - 1, y - 1), (x - 1, y), (x + 1, y)]:
					if spot[0] >= 0 and spot[1] >= 0 and spot[0] < len(input) and spot[1] < len(input[spot[0]]):
						if input[spot[0]][spot[1]] == '@':
							bales += 1
				if bales <4:

					count += 1
	return count


def part2(input):
	count = 0
	count_last = count-1
	newinput = input
	while count != count_last:
		input = newinput
		count_last = count
		for x in range(len(input)):
			for y in range(len(input[x])):
				if input[x][y] == '@':
					bales = 0
					for spot in [(x, y + 1), (x, y - 1), (x + 1, y + 1), (x + 1, y - 1),(x - 1, y + 1), (x - 1, y - 1), (x - 1, y), (x + 1, y)]:
						if spot[0] >= 0 and spot[1] >= 0 and spot[0] < len(input) and spot[1] < len(input[spot[0]]):
							if input[spot[0]][spot[1]] == '@':
								bales += 1
					if bales <4:
						count += 1
						newinput[x] = input[x][:y] + '*' + input[x][y + 1:]



	return count


testresult_part1 = 13
testresult_part2 = 43


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