import re, itertools, math,os,sys,string,time

           
pathname = os.path.dirname(sys.argv[0])        
testinput_path1 = pathname + "/testinput1.txt"   
testinput_path2 = pathname + "/testinput2.txt"  
input_path = pathname + "/input.txt"


def parse_input(path):
    with open(path, "r") as inputfile:
        grid = [list(line.strip()) for line in inputfile if line.strip()]
        
        # Find starting position and direction
        for y in range(len(grid)):
            for x in range(len(grid[y])):
                if grid[y][x] in '^>v<':
                    start_pos = (x, y)
                    if grid[y][x] == '^':
                        start_dir = (0, -1)
                    elif grid[y][x] == '>':
                        start_dir = (1, 0)
                    elif grid[y][x] == 'v':
                        start_dir = (0, 1)
                    else:  # <
                        start_dir = (-1, 0)
                    grid[y][x] = '.'
        
        return grid, start_pos, start_dir

def turn_right(direction):
    """Turn current direction 90 degrees right"""
    dx, dy = direction
    return (-dy, dx)

def is_inside_grid(pos, grid):
    """Check if position is within grid bounds"""
    x, y = pos
    return 0 <= y < len(grid) and 0 <= x < len(grid[0])

def track_guard_path(grid, start_pos, start_dir):
    """Track guard's complete path until exit, return path and states"""
    path = []  # List of positions
    states = []  # List of (position, direction) tuples
    pos = start_pos
    direction = start_dir
    
    while True:
        path.append(pos)
        states.append((pos, direction))
        
        next_pos = (pos[0] + direction[0], pos[1] + direction[1])
        if not is_inside_grid(next_pos, grid):
            break
            
        if grid[next_pos[1]][next_pos[0]] == '#':
            direction = turn_right(direction)
        else:
            pos = next_pos
            
    return path, states

def check_for_loop(grid, start_pos, start_dir, obstacle_pos):
    """Check if placing obstacle at given position creates a loop"""
    if obstacle_pos == start_pos:
        return False
        
    # Add obstacle temporarily
    x, y = obstacle_pos
    grid[y][x] = '#'
    
    # Track states to detect loops
    pos = start_pos
    direction = start_dir
    seen_states = {(pos, direction)}
    
    while True:
        next_pos = (pos[0] + direction[0], pos[1] + direction[1])
        if not is_inside_grid(next_pos, grid):
            grid[y][x] = '.'  # Remove obstacle
            return False
            
        if grid[next_pos[1]][next_pos[0]] == '#':
            direction = turn_right(direction)
        else:
            pos = next_pos
            
        state = (pos, direction)
        if state in seen_states:
            grid[y][x] = '.'  # Remove obstacle
            return True
            
        seen_states.add(state)
    
def find_loop_positions(grid, start_pos, start_dir):
    """Find all positions where adding an obstacle creates a loop"""
    path, states = track_guard_path(grid, start_pos, start_dir)
    loop_positions = set()
    
    # Check positions adjacent to path
    for pos, direction in states:
        # Check position ahead (where guard would turn if blocked)
        next_pos = (pos[0] + direction[0], pos[1] + direction[1])
        if (is_inside_grid(next_pos, grid) and 
            grid[next_pos[1]][next_pos[0]] == '.' and 
            next_pos != start_pos):
            if check_for_loop(grid, start_pos, start_dir, next_pos):
                loop_positions.add(next_pos)
    
    return loop_positions

def part1(input):
    grid, start_pos, start_dir = input
    path, _ = track_guard_path(grid, start_pos, start_dir)
    return len(set(path))

def part2(input):
    grid, start_pos, start_dir = input
    loop_positions = find_loop_positions(grid, start_pos, start_dir)
    return len(loop_positions)

testresult_part1 = 41
testresult_part2 = 6

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