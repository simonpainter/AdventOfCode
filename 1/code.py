output = []
with open ("input.txt", "r") as inputfile:
	data=inputfile.readlines()
	string = data[0].strip()
for i in range(0, len(string)):
	if string[i]==string[i-1]:
		output.append(int(string[i]))
s=sum(output)
print(s)
