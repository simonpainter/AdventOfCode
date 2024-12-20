import re, itertools, math, os, sys, string, time
import collections, heapq, functools
import networkx as nx
from itertools import combinations
           
pathname = os.path.dirname(sys.argv[0])        
testinput_path1 = pathname + "/testinput1.txt"   
testinput_path2 = pathname + "/testinput2.txt"  
input_path = pathname + "/input.txt"


def parse_input(path):
    with open(path, "r") as f:
        return f.read().splitlines()

def create_graph_from_map(grid):
    """Create a networkx graph from the grid and find start/end points"""
    G = nx.Graph()
    start = end = None

    for y, row in enumerate(grid):
        for x, char in enumerate(row):
            if char != '#':
                if char == 'S':
                    start = (x, y)
                elif char == 'E':
                    end = (x, y)
                
                for dx, dy in [(1,0), (0,1)]:
                    new_x, new_y = x + dx, y + dy
                    if (new_y < len(grid) and 
                        new_x < len(grid[0]) and 
                        grid[new_y][new_x] != '#'):
                        G.add_edge((x,y), (new_x,new_y))

    return G, start, end

def manhattan_distance(p1, p2):
    """Calculate Manhattan distance between two points"""
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

def count_valid_cheats(path, max_cheat_dist):
    """Find valid cheats using position combinations"""
    valid_cheats = 0
    
    for (i, pos1), (j, pos2) in combinations(enumerate(path), 2):
        normal_distance = j - i
        cheat_distance = manhattan_distance(pos1, pos2)
        if (cheat_distance <= max_cheat_dist and 
            normal_distance - cheat_distance >= 100):
            valid_cheats += 1
            
    return valid_cheats

def part1(grid):
    G, start, end = create_graph_from_map(grid)
    path = nx.shortest_path(G, start, end)
    return count_valid_cheats(path, 2)

def part2(grid):
    G, start, end = create_graph_from_map(grid)
    path = nx.shortest_path(G, start, end)
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