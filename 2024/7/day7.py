import re, itertools, math,os,sys,string,time,functools

           
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
        if not line: continue
        test_value, numbers = line.split(': ')
        numbers = [int(x) for x in numbers.split()]
        input.append((int(test_value), numbers))
    return input
def parse_input(path):
    with open(path, "r") as inputfile:
        data = inputfile.read()
        lines = data.split('\n')
    
    input = []
    for line in lines:
        if not line: continue
        test_value, numbers = line.split(': ')
        numbers = [int(x) for x in numbers.split()]
        input.append((int(test_value), numbers))
    return input

def part1(input):
    total = 0
    
    for target, numbers in input:
        if len(numbers) == 1:
            if target == numbers[0]:
                total += target
            continue
            
        found = False
        n_operators = len(numbers) - 1
        
        for ops in itertools.product(['+', '*'], repeat=n_operators):
            result = numbers[0]
            for i, op in enumerate(ops):
                if op == '+':
                    result += numbers[i + 1]
                else:
                    result *= numbers[i + 1]
                    
                if result > target:  # Early exit if we exceed target
                    break
                    
            if result == target:  # Early return on first match
                total += target
                found = True
                break
                
    return total

def part2(input):
    total = 0
    
    for target, numbers in input:
        if len(numbers) == 1:
            if target == numbers[0]:
                total += target
            continue
            
        n_operators = len(numbers) - 1
        found = False
        
        for ops in itertools.product(['+', '*', '||'], repeat=n_operators):
            result = numbers[0]
            valid = True
            
            for i, op in enumerate(ops):
                if not valid:
                    break
                    
                if op == '+':
                    result += numbers[i + 1]
                    # Only exit early if no concatenation is possible later
                    if result > target and '||' not in ops[i+1:]:
                        valid = False
                        
                elif op == '*':
                    result *= numbers[i + 1]
                    # Only exit early if no concatenation is possible later
                    if result > target and '||' not in ops[i+1:]:
                        valid = False
                        
                else:  # op == '||'
                    result = int(str(result) + str(numbers[i + 1]))
            
            if valid and result == target:
                total += target
                break  # Found a valid combination, move to next target
                
    return total


testresult_part1 = 3749
testresult_part2 = 11387


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