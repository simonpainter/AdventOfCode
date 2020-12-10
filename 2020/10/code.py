import re, itertools, math

with open ("input.txt", "r") as inputfile:
	data = inputfile.read()
	lines = data.split('\n')
	groups = data.split('\n\n')

def bubble(inputlist):
	swapped = True
	while swapped:
		swapped = False
		for i in range(len(inputlist)-1):
			if inputlist[i]>inputlist[i+1]:
				inputlist[i],inputlist[i+1] = inputlist[i+1],inputlist[i]
				swapped = True
	return inputlist

def tri(n):
	result = [0,0,1]
	for i in range(3,n+3):
		result.append(sum(result[-3:]))
	return result[1:]


input = []
for line in lines:
	input.append(int(line))

def part1(input):
	outlet = 0
	store = {}
	store[0] = 0
	store[1] = 0
	store[2] = 0
	store[3] = 0
	adapters = bubble(input)
	device = max(input)+3
	adapters.append(device)
	adapters.insert(0,outlet)

	for i in range (1, len(adapters)):
		store[(adapters[i]-adapters[i-1])] +=1
	return store[1] * store[3]

def part2(input):
	outlet = 0
	adapters = bubble(input)
	device = max(input)+3
	adapters.append(device)
	adapters.insert(0,outlet)
	combinations = []
	streak = 1
	for i in range (0, len(adapters)):
		if adapters[i]-adapters[i-1] == 1:
			streak +=1
		else:
			if streak > 1:
				combinations.append(tri(streak-1)[-1])
				streak = 1
	return math.prod(combinations)

print(part1(input))
print(part2(input))