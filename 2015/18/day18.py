import re, itertools, math,os,sys,string,time

           
pathname = os.path.dirname(sys.argv[0])        
testinput_path1 = pathname + "/testinput1.txt"   
testinput_path2 = pathname + "/testinput2.txt"  
input_path = pathname + "/input.txt"


def parse_input(path):
    with open(path, "r") as inputfile:
        data = inputfile.read()
        lines = data.split('\n')
    
    # Convert to 2D list of booleans
    grid = []
    for line in lines:
        if line:
            grid.append([char == '#' for char in line])
    return grid

def count_active_neighbors(grid, x, y):
    neighbors = 0
    rows, cols = len(grid), len(grid[0])
    
    # Check all 8 adjacent positions
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if dx == 0 and dy == 0:  # Skip the light itself
                continue
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < rows and 0 <= new_y < cols:
                neighbors += grid[new_x][new_y]
    
    return neighbors

def simulate_step(grid):
    rows, cols = len(grid), len(grid[0])
    new_grid = [[False] * cols for _ in range(rows)]
    
    for i in range(rows):
        for j in range(cols):
            neighbors = count_active_neighbors(grid, i, j)
            if grid[i][j]:  # Light is on
                new_grid[i][j] = neighbors in [2, 3]
            else:  # Light is off
                new_grid[i][j] = neighbors == 3
    
    return new_grid

def part1(input):
    grid = input
    steps = 100
    
    # Simulate for specified number of steps
    for _ in range(steps):
        grid = simulate_step(grid)
    
    # Count total lights on
    return sum(sum(row) for row in grid)

def part2(input):
    grid = input
    steps = 100
    rows, cols = len(grid), len(grid[0])
    
    # Turn on corner lights initially
    for x, y in [(0, 0), (0, cols-1), (rows-1, 0), (rows-1, cols-1)]:
        grid[x][y] = True
    
    # Simulate for specified number of steps
    for _ in range(steps):
        grid = simulate_step(grid)
        # Keep corners on after each step
        for x, y in [(0, 0), (0, cols-1), (rows-1, 0), (rows-1, cols-1)]:
            grid[x][y] = True
    
    # Count total lights on
    return sum(sum(row) for row in grid)


testresult_part1 = 0
testresult_part2 = 2


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