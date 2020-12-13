import re, itertools, math

departure = 1001287
buses = [13,37,461,17,19,29,739,41,23]


#departure = 939
ids = [7,13,59,31,19]
print('https://www.wolframalpha.com/input/?i=0+%3D+' + '+%3D+'.join(['((n+%2B+{})+mod+{})'.format(i, n) for i, n in enumerate(ids) if n != 'x']))

def part1(departure, buses):
	d, b = 1000,10000
	for bus in buses:
		if (bus - (departure % bus)) <= d:
			d = bus - (departure % bus)
			b = bus
	return d * b

def part2(input):
	pass

print(part1(departure, buses))
print(part2(input))