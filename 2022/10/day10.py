import re, itertools, math,os,sys,string,time

           
pathname = os.path.dirname(sys.argv[0])        
testinput_path = pathname + "/testinput.txt"   
input_path = pathname + "/input.txt"



def parse_input(path):
	with open (path, "r") as inputfile:
		data = inputfile.read()
		lines = data.split('\n')
		groups = data.split('\n\n')

	input = lines
	#for line in lines:
		#input.append(int(line))
		#input.append(line.split(' '))
	#for group in groups:
		#input.append(group.replace("\n", "")
		#input.append(group.split(' '))
	return input

def part1(input):
	cycles = []
	registers = [20, 60, 100, 140, 180, 220]
	value = 1
	for line in input:
		extract = re.findall(r'(-?\d+)',line)
		if extract:
			cycles.append(value)
			cycles.append(value)
			value += int(extract[0])
		else:
			cycles.append(value)
	output = 0
	for register in registers:
		output += register * cycles[register-1]
	return output
def part2(input):
	cycles = []
	value = 1
	for line in input:
		extract = re.findall(r'(-?\d+)',line)
		if extract:
			cycles.append(value)
			cycles.append(value)
			value += int(extract[0])
		else:
			cycles.append(value)
	
	output = []
	for row in range(0,6):
		sprite = ''
		for column in range(0,40):
			i = (row * 40) + column
			if cycles[i]-1 <= column <= cycles[i]+1:
				sprite+='#'
			else:
				sprite+=' '
		print (str(sprite))
		
	return output

testresult_part1 = 13140


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
	

print("*** Part 2 Result ***")
start = time.time()
print("----Part 2 Result: ", part2(parse_input(input_path)))
end = time.time()
print("====Part 2 Time ", end - start)

