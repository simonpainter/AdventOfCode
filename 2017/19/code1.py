y = 0
count = 0
north = 0,-1
south = 0,1
east =  1,0
west = -1,0


directionXY = south
direction = "|"
sequence = []
def move(_x,_y, _directionXY):
	global count
	_x += _directionXY[0]
	_y += _directionXY[1]
	count +=1
	return _x,_y


def look(_x,_y,cardinal):
	_x+=cardinal[0]
	_y+=cardinal[1]
	return _x,_y

with open ("input.txt", "r") as inputfile:
        map=inputfile.readlines()
	x = map[y].index("|")
	while map[y][x]!=" ":
		if map[y][x] == "|" or map[y][x] == "-":
			x,y = move(x,y,directionXY)
		elif map[y][x] == "+":
			print("turn")
			if direction == "|":
				direction = "-"
				tmpx,tmpy = look(x,y,east)
				if tmpy < len(map) and tmpx < len(map[tmpy]):
					if map[tmpy][tmpx] != " ":
						directionXY=east
				tmpx,tmpy = look(x,y,west)
				if tmpy < len(map) and tmpx < len(map[tmpy]):
					if map[tmpy][tmpx] != " ":
						directionXY=west
			elif direction == "-":
				direction = "|"
				tmpx,tmpy = look(x,y,north)
				if tmpy < len(map) and tmpx < len(map[tmpy]):
					if map[tmpy][tmpx] != " ":
						directionXY=north
				tmpx,tmpy = look(x,y,south)
				if tmpy < len(map) and tmpx < len(map[tmpy]):
					if map[tmpy][tmpx] != " ":
						directionXY=south
			x,y = move(x,y,directionXY)
		else:
			sequence.append(map[y][x])
			x,y = move(x,y,directionXY)

		print(map[y][x])


	print("".join(sequence))
	print(count)
