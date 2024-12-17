import re, itertools, math, os, sys, string, time
import collections, heapq, functools
import networkx as nx


           
pathname = os.path.dirname(sys.argv[0])        
testinput_path1 = pathname + "/testinput1.txt"   
testinput_path2 = pathname + "/testinput2.txt"  
input_path = pathname + "/input.txt"

def parse_input(path):
    with open(path, "r") as inputfile:
        data = inputfile.read()
        lines = data.split('\n')
    return [line.split(',') for line in lines]

def part1(input):
    
    # Create separate graphs for each wire
    g1 = nx.Graph()
    g2 = nx.Graph()
    
    def add_wire_path(wire_moves, graph):
        x, y = 0, 0
        for move in wire_moves:
            direction = move[0]
            distance = int(move[1:])
            prev_x, prev_y = x, y
            
            if direction == 'R':
                x += distance
            elif direction == 'L':
                x -= distance
            elif direction == 'U':
                y += distance
            elif direction == 'D':
                y -= distance
            
            # Add all points along the path
            step_x = 1 if x > prev_x else -1 if x < prev_x else 0
            step_y = 1 if y > prev_y else -1 if y < prev_y else 0
            
            curr_x, curr_y = prev_x, prev_y
            while (curr_x, curr_y) != (x, y):
                curr_x += step_x
                curr_y += step_y
                graph.add_edge((curr_x - step_x, curr_y - step_y), (curr_x, curr_y))
                
    # Add both wires to their respective graphs
    add_wire_path(input[0], g1)
    add_wire_path(input[1], g2)
    
    # Find intersections by looking for common nodes
    intersections = set(g1.nodes()).intersection(set(g2.nodes()))
    if (0, 0) in intersections:
        intersections.remove((0, 0))  # Remove central port
    
    # Find closest intersection by Manhattan distance
    return min(abs(x) + abs(y) for x, y in intersections)


def part2(input):
    import networkx as nx
    
    # Create separate graphs for each wire, with edge weights for steps
    g1 = nx.Graph()
    g2 = nx.Graph()
    
    def add_wire_path(wire_moves, graph):
        x, y = 0, 0
        total_steps = 0
        steps_to_point = {}  # Track first visit to each point
        
        for move in wire_moves:
            direction = move[0]
            distance = int(move[1:])
            prev_x, prev_y = x, y
            
            if direction == 'R':
                x += distance
            elif direction == 'L':
                x -= distance
            elif direction == 'U':
                y += distance
            elif direction == 'D':
                y -= distance
            
            # Add all points along the path
            step_x = 1 if x > prev_x else -1 if x < prev_x else 0
            step_y = 1 if y > prev_y else -1 if y < prev_y else 0
            
            curr_x, curr_y = prev_x, prev_y
            while (curr_x, curr_y) != (x, y):
                curr_x += step_x
                curr_y += step_y
                total_steps += 1
                
                # Only store first visit to each point
                if (curr_x, curr_y) not in steps_to_point:
                    steps_to_point[(curr_x, curr_y)] = total_steps
                
                graph.add_edge((curr_x - step_x, curr_y - step_y), 
                             (curr_x, curr_y))
                
        return steps_to_point
    
    # Add both wires and get steps to each point
    steps_wire1 = add_wire_path(input[0], g1)
    steps_wire2 = add_wire_path(input[1], g2)
    
    # Find intersections by looking for common nodes
    intersections = set(g1.nodes()).intersection(set(g2.nodes()))
    if (0, 0) in intersections:
        intersections.remove((0, 0))  # Remove central port
    
    # Find intersection with minimum combined steps
    return min(steps_wire1[point] + steps_wire2[point] 
              for point in intersections)

testresult_part1 = 6
testresult_part2 = 30


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