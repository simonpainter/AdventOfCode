import re, itertools, math,os,sys,string,time

           
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
		input.append(re.findall(r'(\D) (\d+)',line)[0])
		#input.append(line.split(' '))
	#for group in groups:
		#input.append(group.replace("\n", "")
		#input.append(group.split(' '))

	return input

def follow(head,tail):
	delta_x, delta_y = head[0]-tail[0],head[1]-tail[1]
	if -1 <= delta_x <= 1 and -1 <= delta_y <= 1:
		return tail

	if delta_x < 0:
		tail[0] -= 1
	if delta_x > 0:
		tail[0] += 1

	if delta_y < 0:
		tail[1] -= 1
	if delta_y > 0:
		tail[1] += 1
	return tail




def part1(input):
	history = []
	head = [0,0]
	tail = [0,0]
	for line in input:
		for move in range(1,int(line[1])+1):
			if line[0] == 'U':
				head[1] += 1
			if line[0] == 'D':
				head[1] -= 1
			if line[0] == 'R':
				head[0] += 1
			if line[0] == 'L':
				head[0] -= 1
			tail = follow(head,tail)
			if tail not in history:
				history.append([i for i in tail])
	return len(history)

	
def part2(input):
	rope = []
	for knot in range(0,10):
		rope.append([0,0])
	history = []
	head = [0,0]
	tail = [0,0]
	for line in input:
		for move in range(1,int(line[1])+1):
			if line[0] == 'U':
				head[1] += 1
			if line[0] == 'D':
				head[1] -= 1
			if line[0] == 'R':
				head[0] += 1
			if line[0] == 'L':
				head[0] -= 1
			for knot in range(0,10):
				if knot == 0:
					rope[knot] = head
				else:
					rope[knot] = follow(rope[knot-1],rope[knot])
			if rope[9] not in history:
				history.append([i for i in rope[9]])
	return len(history)

testresult_part1 = 13
testresult_part2 = 1


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