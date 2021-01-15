import re, itertools, math

with open ("testinput.txt", "r") as inputfile:
	data = inputfile.read()
	lines = data.split('\n')
	groups = data.split('\n\n')

input = data.split(',')

def part1(input,count):
	elf_memory = {}
	for i in range(0,len(input)-1):
		elf_memory[int(input[i])] = i+1
	print(elf_memory)

	last = input[len(input)-1]
	for g in range(len(input)+1,count):
		if last in elf_memory.keys():
			next = (g-1) - elf_memory[last]
			elf_memory[last] = g-1
			spoken = ''			

		else:
			next = 0
			elf_memory[last] = g-1
			spoken = 'not '
		print('Turn %s last number spoken %s and was %sspoken so next number is %s' % (g, last,spoken, next)) 
		last = next
print(part1(input,2025))
