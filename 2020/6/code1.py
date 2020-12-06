with open ("input.txt", "r") as inputfile:
	data=inputfile.read()
result = 0
for group in data.split('\n\n'):
	result += len(set(group.replace("\n", "")))


print(result)