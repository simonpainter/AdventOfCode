part1 = []
part2 = []
with open ("input.txt", "r") as inputfile:
	data=inputfile.readlines()
	string = data[0].strip()
for i in range(0, len(string)):
	if string[i]==string[i-1]:
		part1.append(int(string[i]))
	if string[i]==string[i-(len(string)/2)]:
		part2.append(int(string[i]))

print(sum(part1))
print(sum(part2))
