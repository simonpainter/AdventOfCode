instructions = []
values = {}
history = []
with open ("input.txt", "r") as inputfile:
        data=inputfile.readlines()
for line in data:
	instruction = []
	for element in line.split(" "):
		instruction.append(element.strip())
	instructions.append(instruction)

#create the keys in values{}
temp = []
for instruction in instructions:
	temp.append(instruction[0])
	temp.append(instruction[4])
for key in list(set(temp)):
	values[key] = 0
OPERATORS = {
"<=" : lambda x, y : x <= y,
">=" : lambda x, y : x >= y,
"==" : lambda x, y : x == y,
"!=" : lambda x, y : x != y,
">" : lambda x, y : x > y,
"<" : lambda x, y : x < y
}

def instruct(var1,op,val1,var2,compar,val2):
	output = 0
	if OPERATORS[compar](int(values[var2]),int(val2)):
		if op=="inc":
			op=1
		else:
			op=-1
		output = op * int(val1)
	return output

for instruction in instructions:
	values[instruction[0]]+= instruct(instruction[0],instruction[1],instruction[2],instruction[4],instruction[5],instruction[6])
	history.append(max(values.values()))
print(history)
print(max(history))
