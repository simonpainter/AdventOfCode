with open ("input.txt", "r") as inputfile:
	data=inputfile.readlines()
import re
count = 0
prog1 = re.compile(r".*[aeiou].*[aeiou].*[aeiou].*")
prog2 = re.compile(r"(.)\1")
prog3 = re.compile(r"(ab|cd|pq|xy)")


for line in data:
	result1 = prog1.search(line)
	result2 = prog2.search(line)
	result3 = prog3.search(line)
	print result1, result2, result3
	if result1!=None and result2!=None and result3==None:
		count +=1

print count
