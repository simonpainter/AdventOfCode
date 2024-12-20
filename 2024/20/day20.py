import re, itertools, math, os, sys, string, time
import collections, heapq, functools

           
pathname = os.path.dirname(sys.argv[0])        
testinput_path1 = pathname + "/testinput1.txt"   
testinput_path2 = pathname + "/testinput2.txt"  
input_path = pathname + "/input.txt"



def parse_input(path):
    with open(path, "r") as f:
        return f.read().splitlines()

def find_start_end(grid):
    start = end = None
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell == 'S':
                start = (x, y)
            elif cell == 'E':
                end = (x, y)
    return start, end

def get_path(grid):
    """Find the single valid path through the maze"""
    start, _ = find_start_end(grid)
    path = [start]
    current = start
    
    while True:
        x, y = current
        # Check all four directions
        for dx, dy in [(0,1), (1,0), (0,-1), (-1,0)]:
            next_x, next_y = x + dx, y + dy
            # Check if position is valid and not already in path
            if (0 <= next_y < len(grid) and 
                0 <= next_x < len(grid[0]) and 
                grid[next_y][next_x] != '#' and 
                (next_x, next_y) not in path):
                path.append((next_x, next_y))
                current = (next_x, next_y)
                break
        # If we couldn't find a next step, we're done
        else:
            break
    
    return path

def manhattan_distance(p1, p2):
    """Calculate Manhattan distance between two points"""
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

def count_valid_cheats(path, max_cheat_dist):
    """Count valid cheats based on minimum time saved"""
    count = 0
    path_length = len(path)
    
    # Look at all pairs of positions
    for i in range(path_length):
        for j in range(i + 2, path_length):  # Must be at least 2 steps away
            # Normal path length is difference in indices
            normal_distance = j - i
            
            # Check if Manhattan distance allows for valid cheat
            cheat_distance = manhattan_distance(path[i], path[j])
            if cheat_distance <= max_cheat_dist:
                # Calculate time saved
                time_saved = normal_distance - cheat_distance
                if time_saved >= 100:
                    count += 1
    
    return count

def part1(grid):
    path = get_path(grid)
    # For part 1, check cheats with max distance of 2
    return count_valid_cheats(path, 2)

def part2(grid):
    path = get_path(grid)
    # For part 2, check cheats with max distance of 20
    return count_valid_cheats(path, 20)

testresult_part1 = 0
testresult_part2 = 0


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