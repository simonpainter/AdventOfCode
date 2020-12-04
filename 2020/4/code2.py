parsed = []
count = 0

import re

def validate(key,value):
	if key == "byr":
		if re.search("^[0-9]{4}$", value):
			if 1920 <= int(value) <= 2002:
				return 1 
	if key == "iyr":
		if re.search("^[0-9]{4}$", value):
			if 2010 <= int(value) <= 2020:
				return 1 		
	if key == "eyr":
		if re.search("^[0-9]{4}$", value):
			if 2020 <= int(value) <= 2030:
				return 1 		
	if key == "hgt":
		if re.search("^([0-9]{2,3})((in)|(cm))$",value):
			hgt = re.search("^([0-9]{2,3})((in)|(cm))$",value)
			if hgt[2] == 'cm':
				if 150 <= int(hgt[1]) <= 193:
					return 1
			elif hgt[2] == 'in':
				if 59 <= int(hgt[1]) <= 76:
					return 1

	if key == "hcl":
		if re.search("^#([0-9]|[a-f]){6}$",value):
			return 1
	if key == "ecl":
		accepted_ecl = {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}
		if value in accepted_ecl:
			return 1
	if key == "pid":
		if re.search("^[0-9]{9}$",value):
			return 1
	return 0




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
			fieldcount += validate(field,entry[field])
	if fieldcount == 7: 
		count += 1

print(count)