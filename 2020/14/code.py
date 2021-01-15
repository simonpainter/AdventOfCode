import re, itertools, math

with open ("testinput.txt", "r") as inputfile:
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

def part1(input):
	mem = {}
	for line in lines:
		if line[:2] == 'ma':
			mask = re.search('[X0-1]{36}',line)
			mask_and = int(mask.group(0).replace('1','0').replace('X','1'),2)
			mask_or = int(mask.group(0).replace('X','0'),2)
		elif line[:2] == 'me':
			register = re.search('mem\[(\d+)\] = (\d+)',line)
			memory = int(register.group(1))
			value = int(register.group(2))
			masked_value = value & mask_and
			output_value = masked_value | mask_or
			mem[memory] = output_value
	tot=0
	for i in mem:
		tot=tot+mem[i]
	return tot

def part2(input):
	for line in lines:
		if line[:2] == 'ma':
			mask = re.search('[X0-1]{36}',line)
		elif line[:2] == 'me':
			register = re.search('mem\[(\d+)\] = (\d+)',line)
			memory = int(register.group(1))
			value = int(register.group(2))

#print(part1(input))
print(part2(input))