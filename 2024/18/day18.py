import re, itertools, math, os, sys, string, time
import collections, heapq, functools
import networkx as nx

pathname = os.path.dirname(sys.argv[0])
testinput_path1 = pathname + "/testinput1.txt"
testinput_path2 = pathname + "/testinput2.txt"
input_path = pathname + "/input.txt"

def parse_input(path):
    with open(path, "r") as inputfile:
        return [(int(x), int(y)) for x,y in [line.split(',') for line in inputfile.read().split('\n') if line.strip()]]

def part1(input):
    G = nx.grid_2d_graph(71, 71)
    G.remove_nodes_from(set(input[:1024]))
    try:
        return len(nx.shortest_path(G, (0,0), (70,70))) - 1
    except nx.NetworkXNoPath:
        return None

def part2(input):
    max_size = 6 if max(max(x for x,y in input), max(y for x,y in input)) <= 6 else 70
    for i, pos in enumerate(input):
        G = nx.grid_2d_graph(max_size + 1, max_size + 1)
        G.remove_nodes_from(set(input[:i + 1]))
        try:
            nx.shortest_path(G, (0,0), (max_size,max_size))
        except nx.NetworkXNoPath:
            return f"{pos[0]},{pos[1]}"
    return "No blocking position found"

testresult_part1 = 146
testresult_part2 = "6,1"

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