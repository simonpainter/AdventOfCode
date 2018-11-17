import re

with open ("input.txt", "r") as inputfile:
	data=inputfile.readlines()

start = 0
encoded = 0

for line in data:
    line = line[:len(line)-1]
    start += len(line)
    print line
    regex = re.compile(r'\\')
    line = regex.sub('##',line)
    print line
    regex = re.compile(r'\"')
    line = regex.sub('\\"',line)
    print line

    encoded += len(line)+2


print encoded - start
