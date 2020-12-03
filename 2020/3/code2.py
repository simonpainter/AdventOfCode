slope = []


with open ("input.txt", "r") as inputfile:
	data=inputfile.readlines()

for line in data:
	slope.append(line.strip())

def checkslope(downnum, acrossnum,slope):
	down,across = 0,0
	count = 0
	for i in range(0,int((len(slope)-1)/downnum)):
		down +=downnum
		across +=acrossnum
		if across >= len(slope[0]):
			across -= len(slope[0])
		if slope[down][across] == '#':
			count += 1
	return count


print(checkslope(1,1,slope)*checkslope(1,3,slope)*checkslope(1,5,slope)*checkslope(1,7,slope)*checkslope(2,1,slope))