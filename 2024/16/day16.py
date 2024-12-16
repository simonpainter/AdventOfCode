import re, itertools, math, os, sys, string, time
from collections import defaultdict
import heapq
           
pathname = os.path.dirname(sys.argv[0])        
testinput_path1 = pathname + "/testinput1.txt"   
testinput_path2 = pathname + "/testinput2.txt"  
input_path = pathname + "/input.txt"

def parse_input(path):
    with open(path, "r") as inputfile:
        return [line.strip() for line in inputfile if line.strip()]

def find_start_end(grid):
    start_pos = None
    end_pos = None
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == 'S':
                start_pos = (y, x)
            elif grid[y][x] == 'E':
                end_pos = (y, x)
            if start_pos and end_pos:
                return start_pos, end_pos
    return start_pos, end_pos

def part1(grid):
    if not grid or not grid[0]:
        return 0
    
    start_pos, end_pos = find_start_end(grid)
    if not start_pos or not end_pos:
        return 0
    
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    queue = [(0, (start_pos[0], start_pos[1], 0))]
    seen = set()
    costs = defaultdict(lambda: float('inf'))
    costs[(start_pos[0], start_pos[1], 0)] = 0
    
    while queue:
        score, (y, x, dir_idx) = heapq.heappop(queue)
        
        if (y, x) == end_pos:
            return score
            
        state = (y, x, dir_idx)
        if state in seen:
            continue
        seen.add(state)
        
        for new_dir in [(dir_idx - 1) % 4, (dir_idx + 1) % 4]:
            new_state = (y, x, new_dir)
            new_score = score + 1000
            if new_score < costs[new_state]:
                costs[new_state] = new_score
                heapq.heappush(queue, (new_score, new_state))
        
        dy, dx = directions[dir_idx]
        new_y, new_x = y + dy, x + dx
        if (0 <= new_y < len(grid) and 0 <= new_x < len(grid[0]) and grid[new_y][new_x] != '#'):
            new_state = (new_y, new_x, dir_idx)
            new_score = score + 1
            if new_score < costs[new_state]:
                costs[new_state] = new_score
                heapq.heappush(queue, (new_score, new_state))
    
    return float('inf')

def part2(grid):
    if not grid or not grid[0]:
        return 0
    
    start_pos, end_pos = find_start_end(grid)
    if not start_pos or not end_pos:
        return 0
    
    min_score = part1(grid)
    if min_score == float('inf'):
        return 0
        
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    optimal_tiles = set()
    min_cost_to_end = defaultdict(lambda: float('inf'))
    queue = [(0, (start_pos[0], start_pos[1], 0))]
    costs = defaultdict(lambda: float('inf'))
    costs[(start_pos[0], start_pos[1], 0)] = 0
    
    while queue:
        score, (y, x, dir_idx) = heapq.heappop(queue)
        
        if score > min_score:
            continue
            
        state = (y, x, dir_idx)
        
        for new_dir in [(dir_idx - 1) % 4, (dir_idx + 1) % 4]:
            new_state = (y, x, new_dir)
            new_score = score + 1000
            if new_score <= min_score and new_score < costs[new_state]:
                costs[new_state] = new_score
                heapq.heappush(queue, (new_score, new_state))
                if (y, x) == end_pos and new_score == min_score:
                    min_cost_to_end[new_state] = 0
        
        dy, dx = directions[dir_idx]
        new_y, new_x = y + dy, x + dx
        if (0 <= new_y < len(grid) and 0 <= new_x < len(grid[0]) and grid[new_y][new_x] != '#'):
            new_state = (new_y, new_x, dir_idx)
            new_score = score + 1
            if new_score <= min_score and new_score < costs[new_state]:
                costs[new_state] = new_score
                heapq.heappush(queue, (new_score, new_state))
                if (new_y, new_x) == end_pos and new_score == min_score:
                    min_cost_to_end[new_state] = 0
    
    queue = []
    for state, cost in costs.items():
        y, x, dir_idx = state
        if (y, x) == end_pos and cost == min_score:
            queue.append((cost, state))
            optimal_tiles.add((y, x))
    
    seen = set()
    while queue:
        score, (y, x, dir_idx) = heapq.heappop(queue)
        
        if score > min_score:
            continue
            
        if (y, x) not in optimal_tiles:
            optimal_tiles.add((y, x))
            
        state = (y, x, dir_idx)
        if state in seen:
            continue
        seen.add(state)
        
        for prev_dir in range(4):
            if (prev_dir + 1) % 4 == dir_idx or (prev_dir - 1) % 4 == dir_idx:
                prev_state = (y, x, prev_dir)
                prev_score = costs[prev_state]
                if prev_score + 1000 == score:
                    heapq.heappush(queue, (prev_score, prev_state))
            
            dy, dx = directions[prev_dir]
            prev_y, prev_x = y - dy, x - dx
            if (0 <= prev_y < len(grid) and 0 <= prev_x < len(grid[0]) and grid[prev_y][prev_x] != '#'):
                prev_state = (prev_y, prev_x, prev_dir)
                prev_score = costs[prev_state]
                if prev_score + 1 == score:
                    heapq.heappush(queue, (prev_score, prev_state))
    
    return len(optimal_tiles)

testresult_part1 = 7036
testresult_part2 = 45

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