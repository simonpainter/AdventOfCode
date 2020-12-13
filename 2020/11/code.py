import re, itertools, math, copy, operator

with open ("testinput.txt", "r") as inputfile:
	data = inputfile.read()
	lines = data.split('\n')
	groups = data.split('\n\n')

input = []
for line in lines:
	input.append(list(line))
	#input.append(line.split(' '))
#for group in groups:
	#input.append(group.replace("\n", "")
	#input.append(group.split(' '))


def checkneigbour(x,y,seating):
	width = len(seating[0])
	length = len(seating)
	if (0 <= x < width) and (0 <= y < length):
		return seating[y][x]
	else:
		return '*'

def count_seats_1(x, y, seating):
	adjacent = [(-1,-1,),(-1,0,),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
	count = 0
	for i in range(0,8):
		(neighbour_x, neighbour_y) = tuple(map(operator.add, (x,y), adjacent[i]))
		if checkneigbour(neighbour_x, neighbour_y, seating) == '#':
			count +=1
	return count

def count_seats_2(x, y, seating):
	adjacent = [(-1,-1,),(-1,0,),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
	count = 0
	for i in range(0,8):
		(neighbour_x, neighbour_y) = tuple(map(operator.add, (x,y), adjacent[i]))
		if checkneigbour(neighbour_x, neighbour_y, seating) == '#':
			count +=1
	return count

def part1(input):
	new = copy.deepcopy(input)
	old = []
	while new != old:
		old = copy.deepcopy(new) 
		for y in range(0,len(new)):
			for x in range(0,len(new[y])):
				if old[y][x] == '.':
					pass
				elif old[y][x] == 'L':
					if count_seats_1(x, y, old) == 0:
						new[y][x] = '#'
				elif old[y][x] == '#':
					if count_seats_1(x, y, old) >= 4:
						new[y][x] = 'L'
	answer = 0
	for row in new:
		for seat in row:
			if seat == '#':
				answer +=1
	return answer
def part2(input):
	new = copy.deepcopy(input)
	old = []
	while new != old:
		old = copy.deepcopy(new) 
		for y in range(0,len(new)):
			for x in range(0,len(new[y])):
				if old[y][x] == '.':
					pass
				elif old[y][x] == 'L':
					if count_seats_2(x, y, old) == 0:
						new[y][x] = '#'
				elif old[y][x] == '#':
					if count_seats_2(x, y, old) >= 4:
						new[y][x] = 'L'
	answer = 0
	for row in new:
		for seat in row:
			if seat == '#':
				answer +=1
	return answer

print(part1(input))
print(part2(input))