import re, itertools, math,os,sys,string,time

           
pathname = os.path.dirname(sys.argv[0])        
testinput_path1 = pathname + "/testinput1.txt"   
testinput_path2 = pathname + "/testinput2.txt"  
input_path = pathname + "/input.txt"



def parse_input(path):
    with open(path, "r") as inputfile:
        return [line.strip() for line in inputfile.readlines()]

def is_symbol(char):
    return char != '.' and not char.isdigit()

def check_adjacent_symbols(schematic, row, start_col, end_col):
    rows, cols = len(schematic), len(schematic[0])
    row_start = max(0, row - 1)
    row_end = min(rows, row + 2)
    col_start = max(0, start_col - 1)
    col_end = min(cols, end_col + 1)
    
    for r in range(row_start, row_end):
        for c in range(col_start, col_end):
            if is_symbol(schematic[r][c]):
                return True
    return False

def get_number_at_position(schematic, row, col):
    # If we're not on a digit, return None
    if not schematic[row][col].isdigit():
        return None, None, None
    
    # Find the start of the number
    start = col
    while start > 0 and schematic[row][start-1].isdigit():
        start -= 1
    
    # Find the end of the number
    end = col
    while end < len(schematic[row]) and schematic[row][end].isdigit():
        end += 1
    
    return int(schematic[row][start:end]), start, end

def find_adjacent_numbers(schematic, gear_row, gear_col):
    rows, cols = len(schematic), len(schematic[0])
    numbers = set()  # Use set to avoid duplicates
    
    # Check all adjacent positions
    for r in range(max(0, gear_row - 1), min(rows, gear_row + 2)):
        for c in range(max(0, gear_col - 1), min(cols, gear_col + 2)):
            result = get_number_at_position(schematic, r, c)
            if result[0] is not None:
                numbers.add((result[0], r, result[1]))  # Store number and its position
    
    return [num[0] for num in numbers]  # Return just the numbers

def part1(schematic):
    total = 0
    rows, cols = len(schematic), len(schematic[0])
    
    for row in range(rows):
        numbers = re.finditer(r'\d+', schematic[row])
        for match in numbers:
            number = int(match.group())
            start_col = match.start()
            end_col = match.end()
            if check_adjacent_symbols(schematic, row, start_col, end_col):
                total += number
    
    return total

def part2(schematic):
    total = 0
    rows, cols = len(schematic), len(schematic[0])
    
    # Find all gears (*) and their adjacent numbers
    for row in range(rows):
        for col in range(cols):
            if schematic[row][col] == '*':
                adjacent_numbers = find_adjacent_numbers(schematic, row, col)
                if len(adjacent_numbers) == 2:
                    gear_ratio = adjacent_numbers[0] * adjacent_numbers[1]
                    total += gear_ratio
    
    return total

testresult_part1 = 4361
testresult_part2 = 467835



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