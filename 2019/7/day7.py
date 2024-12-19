import re, itertools, math, os, sys, string, time
import collections, heapq, functools
from intcode import IntCodeComputer

           
pathname = os.path.dirname(sys.argv[0])        
testinput_path1 = pathname + "/testinput1.txt"   
testinput_path2 = pathname + "/testinput2.txt"  
input_path = pathname + "/input.txt"


def parse_input(path):
    with open(path, "r") as inputfile:
        data = inputfile.read().strip()
        return [int(x) for x in data.split(',')]




def part1(input):
    max_signal = 0
    computer = IntCodeComputer(input.copy())
    
    for phases in itertools.permutations(range(5)):
        signal = 0
        for phase in phases:
            computer.reset(input.copy())
            computer.add_input([phase, signal])
            computer.execute()
            signal = computer.outputs[-1]
        max_signal = max(max_signal, signal)
    return max_signal

def part2(input):
     pass


testresult_part1 = 43210
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