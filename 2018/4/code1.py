with open ("input.txt", "r") as inputfile:
	data=inputfile.readlines()
lines = []
for line in data:
	 line = line.strip().split()
	 line = line[0].strip("[") + " " + line[1].strip("]") + " " + line[3]
	 lines.append(line)

for line in sorted(lines):
	print line
