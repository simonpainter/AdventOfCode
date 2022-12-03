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
	anomalies = []
	total = 0
	for bag in input:
		compartments = [bag[:len(bag)//2],bag[len(bag)//2:]]
		result = ''
		for char in compartments[0]:
			if char in compartments[1] and not char in result:
				result+=char
		anomalies.append(result)
	for each in anomalies:
		total += (string.ascii_letters.find(each) + 1)
	return total



def part2(input):
	elf_groups = []
	badges = []
	total = 0
	for i in range(0, len(input), 3):
		elf_groups.append(input[i:i + 3])
	for elf_group in elf_groups:
		common = set.intersection(*map(set,elf_group))
		badges.append(list(common)[0])
	for each in badges:
		total += (string.ascii_letters.find(each) + 1)
	return total		





testresult_part1 = 157
testresult_part2 = 70

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