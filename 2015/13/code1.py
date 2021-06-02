import re

table = []


with open ("./AdventOfCode/2015/13/testinput.txt", "r") as inputfile:
	data=inputfile.readlines()
for line in data:
	output = re.findall("^([A-z]*) .*(gain|lose) (\d*) .* ([A-z]*)\.$",line)
	output = output[0]
	if output[1] == "gain":
		h = int(output[2])
	else:
		h = 0-int(output[2])
	table.append((output[0],h,output[3]))

print(table)