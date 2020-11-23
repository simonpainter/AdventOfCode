with open ("input.txt", "r") as inputfile:
	data=inputfile.readlines()
	x,y = 0,0
	code = []
	for line in data:
		instructions = line.strip()
		print(instructions)

		for instruction in instructions:

			if instruction=="U":
				y += 1
			elif instruction=="D":
				y -= 1
			elif instruction=="L":
				x -= 1
			elif instruction=="R":
				x += 1
			if y>1:
				y=1
			if y<-1:
				y=-1
			if x>1:
				x=1
			if x<-1:
				x=-1

		print(x,y)
		if (x,y)==(-1,1):
			code.append(1)
		if (x,y)==(0,1):
			code.append(2)
		if (x,y)==(1,1):
			code.append(3)
		if (x,y)==(-1,0):
			code.append(4)
		if (x,y)==(0,0):
			code.append(5)
		if (x,y)==(1,0):
			code.append(6)
		if (x,y)==(-1,-1):
			code.append(7)
		if (x,y)==(0,-1):
			code.append(8)
		if (x,y)==(1,-1):
			code.append(9)
print(code)