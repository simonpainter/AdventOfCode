import re, itertools, math,os,sys,string,time

           
pathname = os.path.dirname(sys.argv[0])        
testinput_path1 = pathname + "/testinput1.txt"   
testinput_path2 = pathname + "/testinput2.txt"  
input_path = pathname + "/input.txt"


def parse_input(path):
    with open(path, "r") as inputfile:
        data = inputfile.read()
        lines = data.split('\n')
    
    grid = []
    for line in lines:
        if line:
            grid.append(list(line))
            
    return grid

def part1(input):
    # Map antennas to positions and positions to frequencies
    antennas = {}
    antenna_positions = {}
    max_y = len(input)
    max_x = len(input[0])
    
    for y, row in enumerate(input):
        for x, char in enumerate(row):
            if char != '.':
                if char not in antennas:
                    antennas[char] = []
                antennas[char].append((x, y))
                antenna_positions[(x, y)] = char
    
    antinodes = set()
    
    # For each frequency and pair of antennas
    for freq in antennas:
        positions = antennas[freq]
        for i, pos1 in enumerate(positions):
            for pos2 in positions[i+1:]:
                x1, y1 = pos1
                x2, y2 = pos2
                
                # Vector between antennas
                dx = x2 - x1
                dy = y2 - y1
                
                # Find the two antinode positions one full vector away
                antinode1 = (x1 - dx, y1 - dy)
                antinode2 = (x2 + dx, y2 + dy)
                
                # Add antinodes if they're in bounds and not on same frequency antenna
                for node in [antinode1, antinode2]:
                    x, y = node
                    # First check if in bounds
                    if 0 <= x < max_x and 0 <= y < max_y:
                        # Then check antenna conditions only if in bounds
                        if node not in antenna_positions or antenna_positions[node] != freq:
                            antinodes.add(node)
    

                    
    return len(antinodes)

def are_collinear(p1, p2, p3):
    """Check if three points are collinear using cross product"""
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3
    # Calculate the cross product of vectors (p2-p1) and (p3-p1)
    return (y2 - y1) * (x3 - x1) == (y3 - y1) * (x2 - x1)

def part2(input):
    antennas = {}
    antenna_positions = {}
    max_y = len(input)
    max_x = len(input[0])
    
    # Find all antennas
    for y, row in enumerate(input):
        for x, char in enumerate(row):
            if char != '.':
                if char not in antennas:
                    antennas[char] = []
                antennas[char].append((x, y))
                antenna_positions[(x, y)] = char
    
    antinodes = set()
    
    # For each frequency
    for freq in antennas:
        positions = antennas[freq]
        if len(positions) < 2:  # Skip if only one antenna of this frequency
            continue
            
        # For each pair of antennas
        for i, pos1 in enumerate(positions):
            for j, pos2 in enumerate(positions[i+1:], i+1):
                # Add the antenna positions themselves as they're collinear with others
                antinodes.add(pos1)
                antinodes.add(pos2)
                
                # Check every position in the grid
                for y in range(max_y):
                    for x in range(max_x):
                        if (x, y) != pos1 and (x, y) != pos2 and are_collinear(pos1, pos2, (x, y)):
                            antinodes.add((x, y))
                   
    return len(antinodes)


testresult_part1 = 14
testresult_part2 = 34

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