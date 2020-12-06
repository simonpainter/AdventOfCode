with open ("input.txt", "r") as inputfile:
	data=inputfile.read()
result = 0
for group in data.split('\n\n'):
	questions = 'abcdefghijklmnopqrstuvwxyz'
	for item in group.split('\n'):
		questions = ''.join(set(questions).intersection(set(item)))
	result += len(questions)

print(result)