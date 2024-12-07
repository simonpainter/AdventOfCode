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

def evaluate_expression_p1(numbers, operators):
    """Evaluate expression left to right with only + and * operators"""
    result = numbers[0]
    for i, op in enumerate(operators):
        if op == '+':
            result += numbers[i + 1]
        else:  # op == '*'
            result *= numbers[i + 1]
    return result

def can_make_value_p1(target, numbers):
    """Check if target can be made with any combination of + and * operators"""
    if len(numbers) == 1:
        return target == numbers[0]
    
    # Generate all possible combinations of + and * operators
    n_operators = len(numbers) - 1
    for ops in itertools.product(['+', '*'], repeat=n_operators):
        if evaluate_expression_p1(numbers, ops) == target:
            return True
    return False


def evaluate_expression_p2(numbers, operators):
    result = numbers[0]
    for i, op in enumerate(operators):
        if op == '+':
            result += numbers[i + 1]
        elif op == '*':
            result *= numbers[i + 1]
        else:  # op == '||'
            result = int(str(result) + str(numbers[i + 1]))
    return result

def can_make_value_p2(target, numbers):
    if len(numbers) == 1:
        return target == numbers[0]
    
    n_operators = len(numbers) - 1
    for ops in itertools.product(['+', '*', '||'], repeat=n_operators):
        result = numbers[0]
        for i, op in enumerate(ops):
            if op == '+':
                result += numbers[i + 1]
                if result > target and '||' not in ops[i+1:]:  # Early exit if we exceed target and no concatenation ahead
                    break
            elif op == '*':
                result *= numbers[i + 1]
                if result > target and '||' not in ops[i+1:]:  # Early exit if we exceed target and no concatenation ahead
                    break
            else:  # op == '||'
                result = int(str(result) + str(numbers[i + 1]))
                
        if result == target:  # Early return on first match
            return True
            
    return False




def part1(input):
    total = 0
    for target, numbers in input:
        if can_make_value_p1(target, numbers):
            total += target
    return total


def part2(input):
    return sum(target for target, numbers in input if can_make_value_p2(target, numbers))


# Set test results based on examples
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