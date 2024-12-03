import re, itertools, math,os,sys,string,time

           
pathname = os.path.dirname(sys.argv[0])        
testinput_path1 = pathname + "/testinput1.txt"   
testinput_path2 = pathname + "/testinput2.txt"  
input_path = pathname + "/input.txt"


def parse_input(path):
    with open(path, "r") as inputfile:
        data = inputfile.read().strip()
    return data

def find_all_instructions(text):
    # Find all mul, do, and don't instructions with their positions
    mul_pattern = r'mul\((\d{1,3}),(\d{1,3})\)'
    do_pattern = r'do\(\)'
    dont_pattern = r'don\'t\(\)'
    
    instructions = []
    
    # Find all multiplications
    for match in re.finditer(mul_pattern, text):
        num1 = int(match.group(1))
        num2 = int(match.group(2))
        instructions.append(('mul', match.start(), num1 * num2))
    
    # Find all do() instructions
    for match in re.finditer(do_pattern, text):
        instructions.append(('do', match.start(), None))
    
    # Find all don't() instructions
    for match in re.finditer(dont_pattern, text):
        instructions.append(('dont', match.start(), None))
    
    # Sort instructions by position
    instructions.sort(key=lambda x: x[1])
    return instructions

def process_instructions(instructions):
    enabled = True  # Start with multiplications enabled
    total = 0
    
    for type, pos, value in instructions:
        if type == 'do':
            enabled = True
        elif type == 'dont':
            enabled = False
        elif type == 'mul' and enabled:
            total += value
    
    return total

def part1(input):
    mul_pattern = r'mul\((\d{1,3}),(\d{1,3})\)'
    matches = re.finditer(mul_pattern, input)
    return sum(int(match.group(1)) * int(match.group(2)) for match in matches)

def part2(input):
    instructions = find_all_instructions(input)
    return process_instructions(instructions)

testresult_part1 = 161
testresult_part2 = 48


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