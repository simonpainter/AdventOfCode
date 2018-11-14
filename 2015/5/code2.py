with open ("input.txt", "r") as inputfile:
	data=inputfile.readlines()
import re
count = 0
prog1 = re.compile(r"(.{2}).*\1")
prog2 = re.compile(r"((.).)\2")



for line in data:
	result1 = prog1.search(line)
	result2 = prog2.search(line)

	print result1, result2
	if result1!=None and result2!=None:
		count +=1

print count
