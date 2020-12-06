import re

with open ("testinput.txt", "r") as inputfile:
	data=inputfile.readlines()

for line in data:
	a,b = re.findall("^Step (.) must be finished before step (.) can begin",line)[0]
	print(a,b)
