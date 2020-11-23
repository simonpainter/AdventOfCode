position = [0,0,0]
instruction_string = "R5, L2, L1, R1, R3, R3, L3, R3, R4, L2, R4, L4, R4, R3, L2, L1, L1, R2, R4, R4, L4, R3, L2, R1, L4, R1, R3, L5, L4, L5, R3, L3, L1, L1, R4, R2, R2, L1, L4, R191, R5, L2, R46, R3, L1, R74, L2, R2, R187, R3, R4, R1, L4, L4, L2, R4, L5, R4, R3, L2, L1, R3, R3, R3, R1, R1, L4, R4, R1, R5, R2, R1, R3, L4, L2, L2, R1, L3, R1, R3, L5, L3, R5, R3, R4, L1, R3, R2, R1, R2, L4, L1, L1, R3, L3, R4, L2, L4, L5, L5, L4, R2, R5, L4, R4, L2, R3, L4, L3, L5, R5, L4, L2, R3, R5, R5, L1, L4, R3, L1, R2, L5, L1, R4, L1, R5, R1, L4, L4, L4, R4, R3, L5, R1, L3, R4, R3, L2, L1, R1, R2, R2, R2, L1, L1, L2, L5, L3, L1"
instructions = instruction_string.split(",")

log = []

for instruction in instructions:
	turn = instruction.strip()[:1]
	distance = int(instruction.strip()[1:])
	if (turn == "R"):
		position[2] += 1
	else:
		position[2] -= 1
	if (position[2]<=-1):
                position[2]+=4
	if (position[2]>=4):
		position[2]-=4

	if (position[2]==0):
		for x in range(0, distance):
			position[1]+=1
			location = position[0],position[1]
			if location in log:
				print(location)
			log.append(location)
	elif (position[2]==1):
		for x in range(0, distance):
			position[0]+=1
			location = position[0],position[1]
			if location in log:
				print(location)
			log.append(location)
	elif (position[2]==2):
		for x in range(0, distance):
			position[1]-=1
			location = position[0],position[1]
			if location in log:
				print(location)
			log.append(location)
	elif (position[2]==3):
		for x in range(0, distance):
			position[0]-=1
			location = position[0],position[1]
			if location in log:
				print(location)
			log.append(location)
	



