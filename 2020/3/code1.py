slope = []
down,across = 0,0
count = 0

with open ("input.txt", "r") as inputfile:
	data=inputfile.readlines()

for line in data:
	slope.append(line.strip())


for i in range(0,len(slope)-1):
	down +=1
	across +=3
	if across >= len(slope[0]):
		across -= len(slope[0])
	if slope[down][across] == '#':
		count += 1

print(count)