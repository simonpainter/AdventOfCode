import re

with open ("input.txt", "r") as inputfile:
	data=inputfile.readlines()
total = []
regex = re.compile(r"-*[0-9]+")
output = regex.findall(data[0])

for each in output:
    total.append(int(each))

print sum(total)
