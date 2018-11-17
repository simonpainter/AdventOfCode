import re

with open ("input.txt", "r") as inputfile:
	data=inputfile.readlines()

clean = 0
total = 0

for line in data:
    total +=(len(line)-1)
    print line
    line = line[1:len(line)-2]
    print line
    regex = re.compile(r"\\x[0-9 a-f]{2}")
    line = regex.sub("#",line)
    print line
    regex = re.compile(r'\\"')
    line = regex.sub("#",line)
    print line
    regex = re.compile(r'\\\\')
    line = regex.sub("#",line)
    print line
    clean += len(line)
    print total,clean

print total - clean
