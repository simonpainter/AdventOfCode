import re, itertools, math, string

with open ("input.txt", "r") as inputfile:
	data = inputfile.read()
	lines = data.split('\n')
	groups = data.split('\n\n')

input = []
for line in lines:
	#input.append(int(line))
	input.append(line.replace('-','').strip(']').split('['))
#for group in groups:
	#input.append(group.replace("\n", "")
	#input.append(group.split(' '))

def caesar(str, shift):
	intab = string.ascii_lowercase
	outtab = intab[shift:] + intab[:shift]
	trantab = str.maketrans(intab, outtab)
	return str.translate(trantab)

def part1(input):
	sectors = 0
	valid = []
	for room in input:
		log = {}
		name = sorted(room[0][:-3])
		sector = room[0][-3:]
		checksum = room[1]
		for i in range(0,len(name)):
			log[name[i]] = name.count(name[i])
		sorted_log = sorted(log.items(), key=lambda x: (100-x[1],x[0]))
		sorted_log = sorted_log[:5]
		check = ''
		for x in sorted_log:
			check += x[0]
		if sorted(check) == sorted(checksum):
			sectors+= int(sector)
			confirmed = (room[0][:-3],room[0][-3:])
			valid.append(confirmed)
	return valid

def part2(input):
	for room in input:
		name = room[0]
		sector = int(room[1])
		shift = sector % 26
		if caesar(name,shift) == 'northpoleobjectstorage':
			return sector


print(part2(part1(input)))