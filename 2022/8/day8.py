import re, itertools, math,os,sys,string,time

           
pathname = os.path.dirname(sys.argv[0])        
testinput_path = pathname + "/testinput.txt"   
input_path = pathname + "/input.txt"



def parse_input(path):
	with open (path, "r") as inputfile:
		data = inputfile.read()
		lines = data.split('\n')
		groups = data.split('\n\n')

	input = lines
	#for line in lines:
		#input.append(int(line))
		#input.append(line)
	#for group in groups:
		#input.append(group.replace("\n", "")
		#input.append(group.split(' '))
	return input

def part1(input):
	forest = [[int(tree) for tree in line.strip()] for line in input]
	forest_rotated = list(zip(*forest))

	seen = 0
	for y in range(len(forest[0])):
		for x in range(len(forest)):
			tree = forest[y][x]
			if all(look < tree for look in forest[y][0:x]) or \
				all(look < tree for look in forest[y][x+1:]) or \
            	all(look < tree for look in forest_rotated[x][0:y]) or \
            	all(look < tree for look in forest_rotated[x][y+1:]):
				seen += 1

	return(seen)

def view_dist(my_tree, view):
    view_dist = 0
    for tree in view:
        view_dist += 1
        if tree >= my_tree:
            break
    return view_dist

def part2(input):
	forest = [[int(tree) for tree in line.strip()] for line in input]
	forest_rotated = list(zip(*forest))
	seen = 0
	for y in range(len(forest[0])):
		for x in range(len(forest)):
			tree = forest[y][x]
			sx1 = view_dist(tree, forest[y][0:x][::-1])
			sx2 = view_dist(tree, forest[y][x+1:])
			sy1 = view_dist(tree, forest_rotated[x][0:y][::-1])
			sy2 = view_dist(tree, forest_rotated[x][y+1:])
			score = sx1 * sx2 * sy1 * sy2
			if score > seen:
				seen = score
	return(seen)

testresult_part1 = 21
testresult_part2 = 8


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