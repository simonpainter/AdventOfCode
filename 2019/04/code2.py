import re, itertools, math, os, sys, string, time
import collections, heapq, functools
import networkx as nx


'''
Moving this to the new template as it's easier for me to deal with now.
'''

def parse_input(path):
    # For this puzzle, we'll hardcode the range since it's not in a file
    return range(145852, 616943)  # Include end number

def part1(input):
    valid_count = 0
    
    for num in input:
        digits = list(map(int, str(num)))
        
        # Check if digits never decrease
        is_increasing = all(digits[i] <= digits[i+1] for i in range(len(digits)-1))
        
        # Check for adjacent matching digits
        has_adjacent = any(digits[i] == digits[i+1] for i in range(len(digits)-1))
        
        if is_increasing and has_adjacent:
            valid_count += 1
            
    return valid_count

def part2(input):
    valid_count = 0
    
    for num in input:
        digits = list(map(int, str(num)))
        
        # Check if digits never decrease
        is_increasing = all(digits[i] <= digits[i+1] for i in range(len(digits)-1))
        
        # Check for exactly two adjacent matching digits
        has_exact_double = False
        i = 0
        while i < len(digits)-1:
            count = 1
            while i < len(digits)-1 and digits[i] == digits[i+1]:
                count += 1
                i += 1
            if count == 2:
                has_exact_double = True
            i += 1
        
        if is_increasing and has_exact_double:
            valid_count += 1
            
    return valid_count

# Set test results
testresult_part1 = 1767
testresult_part2 = 1192

pathname = os.path.dirname(sys.argv[0])        
testinput_path1 = pathname + "/testinput1.txt"   
testinput_path2 = pathname + "/testinput2.txt"  
input_path = pathname + "/input.txt"

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