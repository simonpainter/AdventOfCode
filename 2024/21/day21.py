import re, itertools, math, os, sys, string, time
import collections, heapq, functools
from functools import cache
import networkx as nx
           
pathname = os.path.dirname(sys.argv[0])        
testinput_path1 = pathname + "/testinput1.txt"   
testinput_path2 = pathname + "/testinput2.txt"  
input_path = pathname + "/input.txt"

def parse_input(path):
    with open(path, "r") as inputfile:
        return [line.strip() for line in inputfile if line.strip()]

K1 = ["789", "456", "123", "X0A"]
K2 = ["X^A", "<v>"]

def create_graph(keypad):
    G = nx.Graph()
    positions = {}
    for r, row in enumerate(keypad):
        for c, key in enumerate(row):
            if key != "X":
                positions[key] = (r, c)
                
    for k1, (r1, c1) in positions.items():
        for k2, (r2, c2) in positions.items():
            if abs(r1 - r2) + abs(c1 - c2) == 1:
                G.add_edge(k1, k2)
    return G

def get_shortest_paths(from_key, to_key, keypad):
    if from_key == to_key:
        return [""]
    
    G = create_graph(keypad)
    sequences = []
    for path in nx.all_shortest_paths(G, from_key, to_key):
        sequence = []
        for i in range(len(path)-1):
            curr, nxt = path[i], path[i+1]
            r1, c1 = [(r,c) for r,row in enumerate(keypad) for c,k in enumerate(row) if k == curr][0]
            r2, c2 = [(r,c) for r,row in enumerate(keypad) for c,k in enumerate(row) if k == nxt][0]
            
            if r2 > r1: sequence.append("v")
            elif r2 < r1: sequence.append("^")
            elif c2 > c1: sequence.append(">")
            else: sequence.append("<")
        sequences.append("".join(sequence))
    return sequences

def get_sequence_paths(sequence, keypad):
    result = []
    current = 'A'
    for target in sequence:
        paths = get_shortest_paths(current, target, keypad)
        result.append([path + "A" for path in paths])
        current = target
    return result

@cache
def find_minimal_sequence(sequence, depth):
    if depth == 1:
        return len(sequence)
    
    keypad = K1 if any(c in sequence for c in "0123456789") else K2
    
    total = 0
    for paths in get_sequence_paths(sequence, keypad):
        total += min(find_minimal_sequence(path, depth - 1) for path in paths)
    return total



def part1(input):
    total_complexity = 0
    for code in input:
        sequence_length = find_minimal_sequence(code, 4)
        numeric_part = int(''.join(c for c in code if c.isdigit()).lstrip('0') or '0')
        total_complexity += sequence_length * numeric_part
    return total_complexity

def part2(input):
    total_complexity = 0
    for code in input:
        sequence_length = find_minimal_sequence(code, 27)
        numeric_part = int(''.join(c for c in code if c.isdigit()).lstrip('0') or '0')
        total_complexity += sequence_length * numeric_part
    return total_complexity

testresult_part1 = 126384
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