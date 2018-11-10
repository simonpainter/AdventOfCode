with open ("input.txt", "r") as inputfile:
	data=inputfile.readlines()
total = 0

for line in data:
    dimensions = line.strip().split('x')
    l=int(dimensions[0])
    w=int(dimensions[1])
    h=int(dimensions[2])
    ribbon = 0
    dimensions = sorted([l,w,h])
    ribbon += (dimensions[0]+dimensions[1])*2
    bow = l*h*w
    ribbon += bow
    total += ribbon
    print ribbon, total
