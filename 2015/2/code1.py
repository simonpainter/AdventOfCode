with open ("input.txt", "r") as inputfile:
	data=inputfile.readlines()
total = 0

for line in data:
    dimensions = line.strip().split('x')
    l=int(dimensions[0])
    w=int(dimensions[1])
    h=int(dimensions[2])
    box = 0
    box += 2*l*w
    box += 2*w*h
    box += 2*l*h
    dimensions = [l,w,h]
    box += sorted(dimensions)[0]*sorted(dimensions)[1]
    total += box
    print box,total


print total
