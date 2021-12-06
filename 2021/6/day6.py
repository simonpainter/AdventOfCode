import re, itertools, math
import timeit

with open ("input.txt", "r") as inputfile:
	data = inputfile.read()
	lines = data.split('\n')
	groups = data.split('\n\n')

input = []
for data in lines[0].split(','):
	input.append(int(data))
#for line in lines:
	#input.append(int(line))
	#input.append(line.split(','))
#for group in groups:
	#input.append(group.replace("\n", "")
	#input.append(group.split(' '))

# Part 1 was easy to brute force across all fish. 

def part1(input):
	current = input[:] 
	for day in range(0, 80):
		start_time = timeit.default_timer()
		new = []
		for fish in current:
			fish -= 1
			if fish < 0:
				fish = 6
				new.append(8)
			new.append(fish)
		current = new[:]
		elapsed = timeit.default_timer() - start_time
		print(elapsed,len(current))

	return len(current)

# Exponential nature of problem made brute force on a per fish basis impossible for part 2 so changed it to use cohorts of fish

def part2(input):
	start_time = timeit.default_timer()
	fish_current_population = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0}
	for fish in input:
		fish_current_population[fish] +=1
	fish_new_population = {}
	for day in range(0, 256):
		for age in range(8,0,-1):
			fish_new_population[age-1] = fish_current_population[age]
		fish_new_population[6] += fish_current_population[0]
		fish_new_population[8] = fish_current_population[0]
		fish_current_population = dict(fish_new_population)
		elapsed = timeit.default_timer() - start_time
	print(elapsed)
	return sum(fish_current_population.values())
#print(part1(input))
part2(input)