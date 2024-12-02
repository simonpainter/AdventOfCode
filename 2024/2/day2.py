import re, itertools, math,os,sys,string,time

           
pathname = os.path.dirname(sys.argv[0])        
testinput_path1 = pathname + "/testinput1.txt"   
testinput_path2 = pathname + "/testinput2.txt"  
input_path = pathname + "/input.txt"



def parse_input(path):
    with open(path, "r") as inputfile:
        data = inputfile.read()
        lines = data.split('\n')
    
    input = []
    for line in lines:
        if line.strip():  # Skip empty lines
            input.append([int(x) for x in line.split()])
    return input

def is_safe_sequence(levels):
    if len(levels) < 2:
        return False
        
    is_increasing = levels[1] > levels[0]
    
    for i in range(len(levels) - 1):
        diff = levels[i + 1] - levels[i]
        
        if abs(diff) < 1 or abs(diff) > 3:
            return False
            
        if is_increasing and diff <= 0:
            return False
        if not is_increasing and diff >= 0:
            return False
    
    return True

def is_safe_with_dampener(levels):
    if is_safe_sequence(levels):
        return True
        
    for i in range(len(levels)):
        dampened_sequence = levels[:i] + levels[i+1:]
        if is_safe_sequence(dampened_sequence):
            return True
            
    return False

def part1(input):
    safe_count = 0
    for sequence in input:
        if is_safe_sequence(sequence):
            safe_count += 1
    return safe_count

def part2(input):
    safe_count = 0
    for sequence in input:
        if is_safe_with_dampener(sequence):
            safe_count += 1
    return safe_count

testresult_part1 = 2
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