import re, itertools, math,os,sys,string,time

           
pathname = os.path.dirname(sys.argv[0])        
testinput_path1 = pathname + "/testinput1.txt"   
testinput_path2 = pathname + "/testinput2.txt"  
input_path = pathname + "/input.txt"



def parse_input(path):
	with open (path, "r") as inputfile:
		data = inputfile.read()
		lines = data.split('\n')
		groups = data.split('\n\n')


	left_list = []
	right_list = []
	for line in lines:
		left, right = map(int, line.split())
		left_list.append(left)
		right_list.append(right)
	input = [left_list,right_list]
	return input

def part1(input):
	left_list = input[0]
	right_list = input[1]
	left_list.sort()
	right_list.sort()

	total_distance = 0
	for l, r in zip(left_list, right_list):
		distance = abs(l - r)
		total_distance += distance
    
	return total_distance

def part2(input):
	
	left_list = input[0]
	right_list = input[1]

	right_counts = {}
	for num in right_list:
		right_counts[num] = right_counts.get(num, 0) + 1
    
	total_score = 0
	for num in left_list:
		count = right_counts.get(num, 0)
		score = num * count
		total_score += score
	return total_score


testresult_part1 = 11
testresult_part2 = 31


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