import re, itertools, math, os, sys, string, time
import collections, heapq, functools

           
pathname = os.path.dirname(sys.argv[0])        
input_path = pathname + "/input.txt"

from intcode import IntCodeComputer

def parse_input(path):
    with open(path, "r") as inputfile:
        data = inputfile.read().strip()
        return [int(x) for x in data.split(',')]

def part1(input):
    computer = IntCodeComputer(input, [1])  # System ID 1 for air conditioner
    computer.execute()
    # Last output is the diagnostic code
    return computer.get_output()[-1]

def part2(input):
    computer = IntCodeComputer(input, [5])  # System ID 5 for thermal radiator
    computer.execute()
    # Only output should be the diagnostic code
    return computer.get_output()[-1]

# Known answers from the puzzle
testresult_part1 = 12896948
testresult_part2 = 7704130

# For test cases from puzzle description
def test_comparison_programs():
    # Equal to 8 (position mode)
    prog1 = [3,9,8,9,10,9,4,9,99,-1,8]
    comp = IntCodeComputer(prog1, [8])
    comp.execute()
    assert comp.get_output()[0] == 1
    
    comp = IntCodeComputer(prog1, [7])
    comp.execute()
    assert comp.get_output()[0] == 0
    
    # Less than 8 (position mode)
    prog2 = [3,9,7,9,10,9,4,9,99,-1,8]
    comp = IntCodeComputer(prog2, [7])
    comp.execute()
    assert comp.get_output()[0] == 1
    
    # Equal to 8 (immediate mode)
    prog3 = [3,3,1108,-1,8,3,4,3,99]
    comp = IntCodeComputer(prog3, [8])
    comp.execute()
    assert comp.get_output()[0] == 1



start = time.time()
print("----Part 1 Result: ", part1(parse_input(input_path)))
end = time.time()
print("====Part 1 Time ", end - start)


start = time.time()
print("----Part 2 Result: ", part2(parse_input(input_path)))
end = time.time()
print("====Part 2 Time ", end - start)
