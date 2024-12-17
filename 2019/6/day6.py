import re, itertools, math, os, sys, string, time
import collections, heapq, functools
import networkx as nx

           
pathname = os.path.dirname(sys.argv[0])        
testinput_path1 = pathname + "/testinput1.txt"   
testinput_path2 = pathname + "/testinput2.txt"  
input_path = pathname + "/input.txt"


def parse_input(path):
    with open(path, "r") as inputfile:
        return [line.strip().split(')') for line in inputfile]

def build_orbit_graph(orbit_pairs):
    # Create a directed graph
    G = nx.DiGraph()
    
    # Add edges - direction is from orbited to orbiter
    for orbited, orbiter in orbit_pairs:
        G.add_edge(orbited, orbiter)
        
    return G

def count_orbits(G):
    total = 0
    # For each node in the graph
    for node in G.nodes():
        # Count the number of ancestors (all objects it orbits directly or indirectly)
        # Length of shortest path gives us the number of steps to COM
        try:
            paths = nx.shortest_path_length(G, 'COM', node)
            total += paths
        except nx.NetworkXNoPath:
            # If no path to COM exists, skip (shouldn't happen in valid input)
            continue
    return total

def part1(input):
    G = build_orbit_graph(input)
    return count_orbits(G)

def part2(input):
    G = build_orbit_graph(input)
    
    # First find what YOU and SAN are orbiting
    you_orbit = next(G.predecessors('YOU'))
    san_orbit = next(G.predecessors('SAN'))
    
    # For transfers, we can move in both directions, so convert to undirected graph
    UG = G.to_undirected()
    
    # Find shortest path length between the two objects
    return nx.shortest_path_length(UG, you_orbit, san_orbit)


# Test result from example in instructions
testresult_part1 = 42
testresult_part2 = 4


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