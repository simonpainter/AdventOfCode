import re, itertools
import networkx as nx

with open ("input.txt", "r") as inputfile:
	data = inputfile.read()
	lines = data.split('\n')
	groups = data.split('\n\n')

input = []
for line in lines:
	contentlist = {}

	bag = line.split(' bags contain')
	for contents in bag[1].split(","):
		r = re.findall('(\d|no) (.*) bag',contents.strip('.').strip(' '))
		if r[0][0] != 'no':
			contentlist[r[0][1]] = r[0][0]
	appendlist = bag[0],contentlist
	input.append(appendlist)


def part1(input):
	bags = nx.DiGraph()
	for bag in input:
		for contents in bag[1]:
			bags.add_edge(bag[0],contents)
	return len(nx.ancestors(bags,'shiny gold'))
def part2(input):
	bags = nx.DiGraph()
	for bag in input:
		for contents in bag[1]:
			bags.add_edge(bag[0],contents,  weight=int(bag[1][contents]))
	def dfs_cost(node):
		cost = 0
		for n, weight in bags[node].items():
			cost = cost + weight['weight'] + weight['weight'] * dfs_cost(n)
		return cost
	return dfs_cost('shiny gold')

print(part1(input))
print(part2(input))