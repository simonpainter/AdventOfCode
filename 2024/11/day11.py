import re, itertools, math,os,sys,string,time

           
pathname = os.path.dirname(sys.argv[0])        
testinput_path1 = pathname + "/testinput1.txt"   
testinput_path2 = pathname + "/testinput2.txt"  
input_path = pathname + "/input.txt"



def parse_input(path):
    with open(path, "r") as inputfile:
        stones = [int(x) for x in inputfile.read().strip().split()]
        # Convert to frequency dict
        counter = {}
        for stone in stones:
            counter[stone] = counter.get(stone, 0) + 1
        return counter

def split_number(n):
    """Split a number into two halves by digits"""
    digits = str(n)
    mid = len(digits) // 2
    left = int(digits[:mid])
    right = int(digits[mid:])
    return left, right

def transform_stones(stones):
    """Transform all stones using frequency counter"""
    new_stones = {}
    
    for stone, count in stones.items():
        # Rule 1: If stone is 0
        if stone == 0:
            new_stones[1] = new_stones.get(1, 0) + count
            
        # Rule 2: If even number of digits
        elif len(str(stone)) % 2 == 0:
            left, right = split_number(stone)
            new_stones[left] = new_stones.get(left, 0) + count
            new_stones[right] = new_stones.get(right, 0) + count
            
        # Rule 3: Multiply by 2024
        else:
            new_val = stone * 2024
            new_stones[new_val] = new_stones.get(new_val, 0) + count
            
    return new_stones

def part1(input):
    stones = input
    for _ in range(25):
        stones = transform_stones(stones)
        
    # Sum all frequencies to get total stone count
    return sum(stones.values())

def part2(input):
    stones = input
    for _ in range(75):
        stones = transform_stones(stones)
        
    # Sum all frequencies to get total stone count
    return sum(stones.values())

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