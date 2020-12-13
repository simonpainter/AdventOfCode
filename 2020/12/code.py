import re, itertools, math

with open ("input.txt", "r") as inputfile:
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

def move(direction,distance,x,y,v):
	vectors = {0:'N', 1:'E', 2:'S', 3:'W'}
	if direction == 'N':
		x += distance
	if direction == 'E':
		y += distance
	if direction == 'S':
		x -= distance
	if direction == 'W':
		y -= distance
	if direction == 'R':
		v =  (v + (distance/90)) %4
	if direction == 'L':
		v -= (distance/90)
		while v < 0:
			v+=4
	if direction == 'F':
		x,y,v = move(vectors[v], distance, x,y,v )
	return x,y,v




def move2(direction,distance,wx, wy, sx, sy):
	if direction == 'N':
		wy += distance
	if direction == 'E':
		wx += distance
	if direction == 'S':
		wy -= distance
	if direction == 'W':
		wx -= distance
	if direction == 'R':
		rotates = int(distance / 90)
		for i in range(0,rotates):
			wx,wy = wy,wx*-1
	if direction == 'L':
		rotates = int(distance / 90)
		for i in range(0,rotates):
			wx,wy = wy*-1,wx
	if direction == 'F':
		sx, sy = sx + wx * distance, sy + wy * distance
	return wx, wy, sx, sy

def part1(input):
	x,y,v = 0,0,1
	for movement in input:
		x,y,v = move(movement[0:1],int(movement[1:]), x, y, v)
	return abs(x) + abs(y)
def part2(input):
	wx, wy, sx, sy = 10, 1, 0, 0
	for movement in input:
		wx, wy, sx, sy = move2(movement[0:1],int(movement[1:]), wx, wy, sx, sy)
		print (sx, sy, wx, wy)
	return abs(sx) + abs(sy)

print(part1(input))
print(part2(input))