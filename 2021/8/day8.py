import re, itertools, math

with open ("input.txt", "r") as inputfile:
	data = inputfile.read()
	lines = data.split('\n')
	groups = data.split('\n\n')

input = []
for line in lines:
	#input.append(int(line))
	input.append(line.split('|')[1].split(" "))
#for group in groups:
	#input.append(group.replace("\n", "")
	#input.append(group.split(' '))

input = []
for line in lines:
	signal = line.split('|')[0].split(" ")
	output = line.split('|')[1].split(" ")
	input.append([signal,output])

def part1(input):
	output = 0
	for line in input:
		for each in line[1]:
			if (len(each) == 2) or (len(each) == 4) or (len(each) == 3) or (len(each) == 7):
				output +=1
	return output

def part2(input):
	total = 0
	for line in input:
		rosetta = {}
		signals = line[0]
		outputs = line[1]
		for signal in signals:
			#find 1,4,7,8
			if len(signal) == 2:
				rosetta["".join(sorted(signal))] = 1
				rosetta[1] = signal
			if len(signal) == 4:
				rosetta["".join(sorted(signal))] = 4
				rosetta[4] = signal
			if len(signal) == 3:
				rosetta["".join(sorted(signal))] = 7
				rosetta[7] = signal			
			if len(signal) == 7:
				rosetta["".join(sorted(signal))] = 8
				rosetta[8] = signal	
			#find 3				
		for signal in signals:
			if ((len(signal) == 5) and (set(rosetta[1]).intersection(signal)==set(rosetta[1]))):
				rosetta["".join(sorted(signal))] = 3
				rosetta[3] = signal					
			#find 9 - six segments and intersects fully with 4
		for signal in signals:
			if ((len(signal) == 6) and (set(rosetta[4]).intersection(signal)==set(rosetta[4]))):
				rosetta["".join(sorted(signal))] = 9
				rosetta[9] = signal	
			#find 5 - set of 5 and 1 is 9
		for signal in signals:
			if ((len(signal) == 5) and (set(rosetta[1]+signal) == set(rosetta[9]))):
				rosetta["".join(sorted(signal))] = 5
				rosetta[5] = signal	
			#find 2 - five segments and it's not 5 or 3
		for signal in signals:
			if ((len(signal) == 5) and ((signal != rosetta[5]) and (signal != rosetta[3]))):
				rosetta["".join(sorted(signal))] = 2
				rosetta[2] = signal		
		for signal in signals:
			#find 0 - six segments - intersects with 1 but isn't 9
			if ((len(signal) == 6) and ((set(rosetta[1]).intersection(signal)==set(rosetta[1])) and signal != rosetta[9])):
				rosetta["".join(sorted(signal))] = 0
				rosetta[0] = signal	
			#find 6 - six segments - isnt 0 or 9
		for signal in signals:
			if ((len(signal) == 6) and ((signal != rosetta[0]) and (signal != rosetta[9]))):
				rosetta["".join(sorted(signal))] = 6
				rosetta[6] = signal	
		output_str = ""
		for output in outputs:
			output_str += str(rosetta["".join(sorted(output))])
		print(output_str)
		total += int(output_str)
	return total
print(part1(input))
print(part2(input))