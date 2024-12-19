with open ("input.txt", "r") as inputfile:
	data=inputfile.readlines()

total = 0

for reading in data:
    while reading > 0:
        reading = (int(reading)//3)-2
        if reading > 0:
            print reading
            total += reading
print total
