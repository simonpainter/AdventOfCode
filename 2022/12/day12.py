import re, itertools, math,os,sys,string,time
from collections import deque

           
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
		ord_line = [ord(item) for item in line]
		input.append(list(ord_line))
	#for group in groups:
		#input.append(group.replace("\n", "")
		#input.append(group.split(' '))
	return input


def part1(input):
	len_x = len(input[0])
	len_y = len(input)
	start, end = [[(y, x) for x in range(len_x) for y in range(len_y) if input[y][x] == c][0] for c in (ord("S"), ord("E"))]

	
	fifo_queue = deque(((0,start),))
	loop_avoidance = set()
	input[start[0]][start[1]] = ord("a")
	input[end[0]][end[1]] = ord("z")

	while fifo_queue:
		directions = [(1,0),(-1,0),(0,1),(0,-1)]
		count,next = fifo_queue.popleft()
		if next in loop_avoidance:
			continue
		loop_avoidance.add(next)
		y,x = next
		if next == end:
			return count
		new_count = count +1
		for direction in directions:
			new_x = x + direction[1]
			new_y = y + direction[0]
			if 0 <= new_x < len_x and 0 <= new_y < len_y and (new_y,new_x) not in loop_avoidance and input[new_y][new_x] - input[y][x] <=1 :
				fifo_queue.append((new_count,(new_y,new_x)))
				

	





def part2(input):
	len_x = len(input[0])
	len_y = len(input)
	start, end = [[(y, x) for x in range(len_x) for y in range(len_y) if input[y][x] == c][0] for c in (ord("S"), ord("E"))]

	
	fifo_queue = deque(((0,end),))
	loop_avoidance = set()
	input[start[0]][start[1]] = ord("a")
	input[end[0]][end[1]] = ord("z")

	while fifo_queue:
		directions = [(1,0),(-1,0),(0,1),(0,-1)]
		count,next = fifo_queue.popleft()
		if next in loop_avoidance:
			continue
		loop_avoidance.add(next)
		y,x = next
		if input[y][x] == ord("a"):			
			return count
		new_count = count +1
		for direction in directions:
			new_x = x + direction[1]
			new_y = y + direction[0]
			if 0 <= new_x < len_x and 0 <= new_y < len_y and (new_y,new_x) not in loop_avoidance and input[y][x] - input[new_y][new_x] <=1 :
				fifo_queue.append((new_count,(new_y,new_x)))
				


testresult_part1 = 31
testresult_part2 = 29


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