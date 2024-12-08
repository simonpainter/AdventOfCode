import re, itertools, math,os,sys,string,time

           
pathname = os.path.dirname(sys.argv[0])        
testinput_path1 = pathname + "/testinput1.txt"   
testinput_path2 = pathname + "/testinput2.txt"  
input_path = pathname + "/input.txt"



def parse_input(path):
    with open(path, "r") as inputfile:
        data = inputfile.read()
        lines = data.split('\n')
    
    containers = []
    for line in lines:
        if line:
            containers.append(int(line))
    return containers

def find_combinations(containers, target, current_combo=None, start_index=0):
    if current_combo is None:
        current_combo = []
    
    # Base cases
    current_sum = sum(current_combo)
    if current_sum == target:
        return [current_combo[:]]  # Found a valid combination
    if current_sum > target or start_index >= len(containers):
        return []  # Invalid combination
    
    combinations = []
    
    # Try including the current container
    current_combo.append(containers[start_index])
    combinations.extend(find_combinations(containers, target, current_combo, start_index + 1))
    current_combo.pop()
    
    # Try without the current container
    combinations.extend(find_combinations(containers, target, current_combo, start_index + 1))
    
    return combinations

def part1(input):
    target_liters = 150
    combinations = find_combinations(input, target_liters)
    return len(combinations)

def part2(input):
    target_liters = 150
    combinations = find_combinations(input, target_liters)
    
    if not combinations:
        return 0
    
    # Find the minimum number of containers used
    min_containers = min(len(combo) for combo in combinations)
    
    # Count combinations using minimum number of containers
    return sum(1 for combo in combinations if len(combo) == min_containers)

# Test result for the example given (25 liters with containers [20, 15, 10, 5, 5])

testresult_part1 = 0
testresult_part2 = 0


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