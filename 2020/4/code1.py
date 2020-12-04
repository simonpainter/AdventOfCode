parsed = []
count = 0
mandatory = ["hcl","iyr","eyr","ecl","pid","byr","hgt"]
with open ("input.txt", "r") as inputfile:
	data=inputfile.readlines()

entry = {}
for line in data:
	if line.strip() != "":
		for pair in line.strip().split():
			key,value = pair.split(":")
			entry[key] = value
	else:
		parsed.append(entry)
		entry = {}


for entry in parsed:
	fieldcount = 0
	for field in mandatory:
		if field in entry:
			fieldcount +=1
	if fieldcount == 7: 
		count += 1

print (count)