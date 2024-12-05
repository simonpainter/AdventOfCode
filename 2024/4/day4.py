import re, itertools, math,os,sys,string,time

           
pathname = os.path.dirname(sys.argv[0])        
testinput_path1 = pathname + "/testinput1.txt"   
testinput_path2 = pathname + "/testinput2.txt"  
input_path = pathname + "/input.txt"

def parse_input(path):
    with open(path, "r") as inputfile:
        return [line.strip() for line in inputfile if line.strip()]

def rotate_90(grid):
    """Rotate grid 90 degrees clockwise"""
    return [''.join(col) for col in zip(*grid[::-1])]
    
def get_diagonals(grid):
    """Get all diagonals from current orientation"""
    height = len(grid)
    width = len(grid[0])
    diagonals = []
    
    # Get all possible diagonals
    for k in range(-(height-1), width):
        diagonal = []
        for i in range(height):
            j = k + i
            if 0 <= j < width:
                diagonal.append(grid[i][j])
        if len(diagonal) >= 4:  # Only include diagonals long enough for XMAS
            diagonals.append(''.join(diagonal))
    return diagonals

def find_xmas(text):
    return text.count('XMAS')



def check_xmas_pattern(grid, row, col):
    """Check if there's an X-MAS pattern centered at position (row,col)"""
    height = len(grid)
    width = len(grid[0])
    
    # Return False if we can't fit a full X pattern
    if (row == 0 or row >= height-1 or 
        col == 0 or col >= width-1):
        return False
    
    # Check center is 'A'
    if grid[row][col] != 'A':
        return False
        
    # Count valid MAS sequences through the center
    count = 0
    
    # Check top-left to bottom-right MAS
    if (grid[row-1][col-1] == 'M' and grid[row+1][col+1] == 'S'):
        count += 1
    if (grid[row-1][col-1] == 'S' and grid[row+1][col+1] == 'M'):
        count += 1
        
    # Check top-right to bottom-left MAS
    if (grid[row-1][col+1] == 'M' and grid[row+1][col-1] == 'S'):
        count += 1
    if (grid[row-1][col+1] == 'S' and grid[row+1][col-1] == 'M'):
        count += 1
    
    # Return True if we found at least two MAS sequences forming an X
    return count >= 2


def part1(input):
    if not input:
        return 0
        
    count = 0
    grid = input[:]
    
    # Check all 4 orientations (0, 90, 180, 270 degrees)
    for _ in range(4):
        # Check rows in current orientation
        for row in grid:
            count += find_xmas(row)
            
        # Check diagonals in current orientation
        diagonals = get_diagonals(grid)
        for diag in diagonals:
            count += find_xmas(diag)
            
        # Rotate grid 90 degrees for next iteration
        grid = rotate_90(grid)
    
    return count

def part2(input):
    if not input:
        return 0
        
    count = 0
    grid = input[:]
    
    # Check each possible center position
    for row in range(1, len(grid)-1):
        for col in range(1, len(grid[0])-1):
            if check_xmas_pattern(grid, row, col):
                count += 1
    
    return count

testresult_part1 = 18
testresult_part2 = 9


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