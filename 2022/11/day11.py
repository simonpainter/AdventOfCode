import re, itertools, math,os,sys,string,time

           
pathname = os.path.dirname(sys.argv[0])        
testinput_path = pathname + "/testinput.txt"   
input_path = pathname + "/input.txt"



def parse_input(path):
	with open (path, "r") as inputfile:
		data = inputfile.read()
		lines = data.split('\n')
		groups = data.split('\n\n')

	input = []

	for group in groups:
		line = group.split('\n')
		monkey_data = {}
		monkey_data['items'] = list(map(int,str(re.findall(r'Starting items: (.*)', line[1])[0]).split(',')))
		monkey_data['operation'] = re.findall(r'Operation: new = (.*)',line[2])[0]
		monkey_data['test'] = int(re.findall(r'\d+',line[3])[0])
		monkey_data['true'] = int(re.findall(r'\d+',line[4])[0])
		monkey_data['false'] = int(re.findall(r'\d+',line[5])[0])
		input.append(monkey_data)
	return input

class Monkey():
	def __init__(self,monkey_data):
		self.monkey_data = monkey_data
		self.items = self.monkey_data['items']
		self.monkey_inspection_count = 0
	def inspect(self,item_number,relax = True):
			self.monkey_inspection_count +=1
			old = self.items[item_number]
			self.items[item_number] = eval(self.monkey_data['operation'])
			if relax:
				self.items[item_number] //= 3
			if  self.items[item_number]% self.monkey_data['test'] == 0:
				thrown = self.items.pop(item_number)
				return thrown, self.monkey_data['true']
			else:
				thrown = self.items.pop(item_number)
				return thrown, self.monkey_data['false']

def part1(input):
	trees = []
	for data in input:
		monkey = Monkey(data)
		trees.append(monkey)
	for round in range(0,20):
		for monkey in trees:
			while len(monkey.items):
				thrown,to = monkey.inspect(0)
				trees[to].items.append(thrown)
	return math.prod(sorted([monkey.monkey_inspection_count for monkey in trees],reverse=True)[0:2])
def part2(input):
	trees = []
	for data in input:
		monkey = Monkey(data)
		trees.append(monkey)
	product = math.prod([monkey.monkey_data['test'] for monkey in trees])
	for round in range(0,10000):
		for monkey in trees:
			while len(monkey.items):
				thrown,to = monkey.inspect(0,relax=False)
				trees[to].items.append(thrown%product)
	return math.prod(sorted([monkey.monkey_inspection_count for monkey in trees],reverse=True)[0:2])


testresult_part1 = 10605
testresult_part2 = 2713310158


if testresult_part1 == part1(parse_input(testinput_path)):
	print("*** Part 1 Test Passed ***")
	start = time.time()
	print("----Part 1 Result: ", part1(parse_input(input_path)))
	end = time.time()
	print("====Part 1 Time ", end - start)

else:
	print("Part 1 Test Failed")
	print("Part 1 Test Result: ", part1(parse_input(testinput_path)))
	print("Expected ", testresult_part1)
	
if testresult_part2 == part2(parse_input(testinput_path)):
	print("*** Part 2 Test Passed ***")
	start = time.time()
	print("----Part 2 Result: ", part2(parse_input(input_path)))
	end = time.time()
	print("====Part 2 Time ", end - start)

else:
	print("Part 2 Test Failed")
	print("Part 2 Test Result: ", part2(parse_input(testinput_path)))
	print("Expected ", testresult_part2)