with open ("input.txt", "r") as inputfile:
	data=inputfile.readlines()
stop = 1
frequency = 0
frequencies =[]
while stop:
    for instruction in data:
        frequency += int(instruction)
        if frequency in frequencies:
            print(frequency)
            stop = 0
            break
        else:
            frequencies.append(frequency)
