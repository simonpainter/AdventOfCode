import itertools

expenses = []

with open ("input.txt", "r") as inputfile:
	data=inputfile.readlines()
	for line in data:
		expenses.append(int(line.strip()))
	
for pair in itertools.combinations(expenses,3):
	if pair[0]+pair[1]+pair[2]==2020:
		print(pair[0]*pair[1]*pair[2])