import re, itertools, math,os,sys,string,time

           
pathname = os.path.dirname(sys.argv[0])        
testinput_path1 = pathname + "/testinput1.txt"   
testinput_path2 = pathname + "/testinput2.txt"  
input_path = pathname + "/input.txt"

def parse_input(path):
    with open(path, "r") as inputfile:
        lines = inputfile.read().strip().split('\n')
        return [[int(x) for x in line] for line in lines]

def get_neighbors(x, y, max_x, max_y):
    """Get valid neighboring positions (up, down, left, right)"""
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    for dx, dy in directions:
        new_x, new_y = x + dx, y + dy
        if 0 <= new_x < max_x and 0 <= new_y < max_y:
            yield (new_x, new_y)

def find_paths(grid, start_x, start_y):
    """Find all paths that reach height 9, return list of endpoints"""
    from collections import deque
    
    max_y = len(grid)
    max_x = len(grid[0])
    queue = deque([(start_x, start_y, [(start_x, start_y)])])
    endpoints = []
    
    while queue:
        x, y, path = queue.popleft()
        current_height = grid[y][x]
        
        if current_height == 9:
            endpoints.append((x, y))
            continue
            
        for nx, ny in get_neighbors(x, y, max_x, max_y):
            if grid[ny][nx] == current_height + 1:
                new_path = path + [(nx, ny)]
                queue.append((nx, ny, new_path))
    
    return endpoints

def part1(grid):
    max_y = len(grid)
    max_x = len(grid[0])
    total_score = 0
    
    for y in range(max_y):
        for x in range(max_x):
            if grid[y][x] == 0:
                # Convert endpoints to set to get unique count
                endpoints = find_paths(grid, x, y)
                total_score += len(set(endpoints))
    
    return total_score

def part2(grid):
    max_y = len(grid)
    max_x = len(grid[0])
    total_rating = 0
    
    for y in range(max_y):
        for x in range(max_x):
            if grid[y][x] == 0:
                # Count all paths including duplicates
                endpoints = find_paths(grid, x, y)
                total_rating += len(endpoints)
    
    return total_rating

testresult_part1 = 36
testresult_part2 = 81


if testresult_part1 == part1(parse_input(testinput_path1)):
	print("*** Part 1 Test Passed ***")
	start = time.time()
	print("----Part 1 Result: ", part1(parse_input(input_path)))
	end = time.time()
	print("====Part 1 Time ", end - start)

else:
	print("Part 1 Test Failed")
	print("Part 1 Test Result: ", part1(parse_input(testinput_path1)))
	print("Expected ", testresult_part1)
	
if testresult_part2 == part2(parse_input(testinput_path2)):
	print("*** Part 2 Test Passed ***")
	start = time.time()
	print("----Part 2 Result: ", part2(parse_input(input_path)))
	end = time.time()
	print("====Part 2 Time ", end - start)

else:
	print("Part 2 Test Failed")
	print("Part 2 Test Result: ", part2(parse_input(testinput_path2)))
	print("Expected ", testresult_part2)