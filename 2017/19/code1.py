y = 0
directionXY = 0,+1


def move(x,y, directionXY):
	x += directionXY[0]
	y += directionXY[1]


	return x,y


with open ("testinput.txt", "r") as inputfile:
        map=inputfile.readlines()
	x = map[y].index("|")
	while map[y][x]!=" ":
		print map[y][x]
		x,y = move(x,y,directionXY)




