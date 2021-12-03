import re, itertools, math, statistics

with open ("input.txt", "r") as inputfile:
	data = inputfile.read()
	lines = data.split('\n')
	groups = data.split('\n\n')

input = []
for line in lines:
	input.append(line)
	#input.append(line.split(' '))
#for group in groups:
	#input.append(group.replace("\n", "")
	#input.append(group.split(' '))

def part1(input):
	mask = (2 ** len(input[0]))-1
	gamma = int(''.join(str(x) for x in [statistics.mode(list(map(int, i))) for i in zip(*input)]), 2)
	epsilon = mask - gamma
	return gamma * epsilon


	
def part2(input):
	o2set = set(range(0,len(input)))
	co2set = set(range(0,len(input)))	
	bit_index = 0
	new_list = input[:]
	while len(o2set)>1:
		old_list = new_list[:]
		new_list = []
		for item in o2set:
			new_list.append(old_list[item])
		transformed = [list(map(int, i)) for i in zip(*new_list)]
		multimodelist = statistics.multimode(transformed[bit_index])
		most = multimodelist[-1]
		o2set = set(range(0,len(new_list)))
		o2setcopy = o2set.copy()
		for i in o2setcopy:
			if (transformed[bit_index][i]!=most):
				o2set.remove(i)

		bit_index+=1



	o2 = int(new_list[list(o2set)[0]],2)

	bit_index = 0
	new_list = input[:]
	while len(co2set)>1:
		old_list = new_list[:]
		new_list = []
		for item in co2set:
			new_list.append(old_list[item])
		transformed = [list(map(int, i)) for i in zip(*new_list)]
		multimodelist = statistics.multimode(transformed[bit_index])
		most = multimodelist[0]

		co2set = set(range(0,len(new_list)))
		co2setcopy = co2set.copy()

		for i in co2setcopy:

			if (transformed[bit_index][i]==most):
				co2set.remove(i)
		bit_index+=1

	co2 = int(new_list[list(co2set)[0]],2)

	return o2 * co2

print(part1(input))
print(part2(input))