import re, itertools, math,os,sys,string,time

           
pathname = os.path.dirname(sys.argv[0])        
testinput_path1 = pathname + "/testinput1.txt"   
testinput_path2 = pathname + "/testinput2.txt"  
input_path = pathname + "/input.txt"



def parse_input(path):
    with open(path, "r") as file:
        lines = file.readlines()
        # Part 1 parsing
        times = [int(x) for x in lines[0].split(':')[1].split()]
        distances = [int(x) for x in lines[1].split(':')[1].split()]
        
        # Part 2 parsing
        big_time = int(''.join(lines[0].split(':')[1].split()))
        big_distance = int(''.join(lines[1].split(':')[1].split()))
        
        return (list(zip(times, distances)), (big_time, big_distance))

def calculate_distance(hold_time, total_time):
    """Calculate distance traveled given hold time and total race time"""
    speed = hold_time
    travel_time = total_time - hold_time
    return speed * travel_time if travel_time > 0 else 0

def find_winning_range(race_time, record_distance):
    """Find the range of winning hold times using quadratic formula"""
    # Distance = hold_time * (race_time - hold_time)
    # Distance = hold_time * race_time - hold_time^2
    # hold_time^2 - race_time*hold_time + record_distance = 0
    
    a = 1  # coefficient of hold_time^2
    b = -race_time  # coefficient of hold_time
    c = record_distance  # constant term
    
    # Quadratic formula: (-b ± √(b² - 4ac)) / 2a
    discriminant = b*b - 4*a*c
    if discriminant < 0:
        return 0  # No solutions
        
    # Find roots
    from math import sqrt, ceil, floor
    min_hold = (-b - sqrt(discriminant)) / (2*a)
    max_hold = (-b + sqrt(discriminant)) / (2*a)
    
    # Convert to integers and adjust for strict inequality
    min_hold = ceil(min_hold + 0.000001)  # Add small value to handle exact matches
    max_hold = floor(max_hold - 0.000001)
    
    return max_hold - min_hold + 1

def part1(puzzle_input):
    races, _ = puzzle_input
    result = 1
    for race_time, record_distance in races:
        ways_to_win = find_winning_range(race_time, record_distance)
        result *= ways_to_win
    return result

def part2(puzzle_input):
    _, (race_time, record_distance) = puzzle_input
    return find_winning_range(race_time, record_distance)

# Test results from the examples
testresult_part1 = 288
testresult_part2 = 71503


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