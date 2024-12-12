import re, itertools, math, os, sys, string, time

pathname = os.path.dirname(sys.argv[0])
testinput_path1 = pathname + "/testinput1.txt"
testinput_path2 = pathname + "/testinput2.txt"
input_path = pathname + "/input.txt"


def parse_input(path):
    with open(path, "r") as inputfile:
        return [list(line.strip()) for line in inputfile]

def find_region(grid, x, y, plant_type, visited):
    max_y = len(grid)
    max_x = len(grid[0])
    region = set()
    perimeter = 0
    
    def dfs(x, y):
        nonlocal perimeter
        if (x, y) in visited or grid[y][x] != plant_type:
            return
        visited.add((x, y))
        region.add((x, y))
        
        sides = 4
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if (0 <= nx < max_x and 0 <= ny < max_y and 
                grid[ny][nx] == plant_type):
                sides -= 1
                if (nx, ny) not in visited:
                    dfs(nx, ny)
        perimeter += sides
    
    dfs(x, y)
    return region, perimeter

def count_cell_corners(x, y, region):
    """Count corners for a cell by checking each corner position independently"""
    corners = []
    
    # Define the four corner positions with their adjacent cells and diagonal
    corner_positions = [
        # (corner_pos, adj1, adj2, diagonal)
        ('TR', (1,0), (0,-1), (1,-1)),  # Top-right corner
        ('BR', (1,0), (0,1), (1,1)),    # Bottom-right corner
        ('BL', (-1,0), (0,1), (-1,1)),  # Bottom-left corner
        ('TL', (-1,0), (0,-1), (-1,-1)) # Top-left corner
    ]
    
    for pos, (dx1, dy1), (dx2, dy2), (diag_x, diag_y) in corner_positions:
        # Check for convex corner (both adjacent cells empty)
        adj1 = (x + dx1, y + dy1) not in region
        adj2 = (x + dx2, y + dy2) not in region
        
        # Check for concave corner (both adjacent filled AND diagonal different)
        adj1_filled = (x + dx1, y + dy1) in region
        adj2_filled = (x + dx2, y + dy2) in region
        diagonal_different = (x + diag_x, y + diag_y) not in region
        
        # Add convex corner
        if adj1 and adj2:
            corners.append((pos, "convex"))
            
        # Add concave corner
        if adj1_filled and adj2_filled and diagonal_different:
            corners.append((pos, "concave"))
    
    return corners

def visualize_region(region, corners_by_pos):
    min_x = min(x for x, y in region)
    max_x = max(x for x, y in region)
    min_y = min(y for x, y in region)
    max_y = max(y for x, y in region)
    
    print("\nRegion visualization:")
    for y in range(min_y-1, max_y+2):
        row = ""
        for x in range(min_x-1, max_x+2):
            if (x, y) in region:
                corners = corners_by_pos.get((x, y), [])
                if corners:
                    row += str(len(corners))
                else:
                    row += "A"
            else:
                row += "."
        print(row)

def count_corners(region):
    total_corners = 0
    for x, y in region:
        total_corners += len(count_cell_corners(x, y, region))
    return total_corners


def part1(input):
    visited = set()
    total_price = 0
    
    for y in range(len(input)):
        for x in range(len(input[0])):
            if (x, y) not in visited:
                plant_type = input[y][x]
                region, perimeter = find_region(input, x, y, plant_type, visited)
                total_price += len(region) * perimeter
    
    return total_price

def part2(input):
    visited = set()
    total_price = 0
    
    for y in range(len(input)):
        for x in range(len(input[0])):
            if (x, y) not in visited:
                plant_type = input[y][x]
                region, _ = find_region(input, x, y, plant_type, visited)
                if len(region) > 0:
                    corners = count_corners(region)
                    total_price += len(region) * corners
    
    return total_price

testresult_part1 = 1930
testresult_part2 = 368

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