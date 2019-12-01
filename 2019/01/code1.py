with open ("input.txt", "r") as inputfile:
	data=inputfile.readlines()

total = 0

for reading in data:
    reading = (int(reading)//3)-2
    total += reading

print total
