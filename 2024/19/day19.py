import re, itertools, math, os, sys, string, time
import collections, heapq, functools

           
pathname = os.path.dirname(sys.argv[0])        
testinput_path1 = pathname + "/testinput1.txt"   
testinput_path2 = pathname + "/testinput2.txt"  
input_path = pathname + "/input.txt"


def parse_input(path):
    with open(path, "r") as inputfile:
        data = inputfile.read()
        patterns, designs = data.split('\n\n')
        available_towels = tuple(p.strip() for p in patterns.split(','))
        design_patterns = [d.strip() for d in designs.splitlines() if d.strip()]
    return available_towels, design_patterns


@functools.cache
def can_make_design(design, available_towels):
    if not design:  # Empty string means we've matched everything
        return True
        
    # Try each available towel pattern
    for towel in available_towels:
        if design.startswith(towel):
            if can_make_design(design[len(towel):], available_towels):
                return True
    return False

@functools.cache
def count_ways(design, available_towels):
    if not design:  # Empty string means we've matched everything
        return 1
        
    total = 0
    # Try each available towel pattern
    for towel in available_towels:
        if design.startswith(towel):
            total += count_ways(design[len(towel):], available_towels)
    return total

def part1(input):
    available_towels, designs = input
    return sum(1 for design in designs if can_make_design(design, available_towels))

def part2(input):
    available_towels, designs = input
    return sum(count_ways(design, available_towels) for design in designs)

testresult_part1 = 6
testresult_part2 = 16

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