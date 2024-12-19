import re, itertools, math, os, sys, string, time
from math import gcd
from functools import reduce

pathname = os.path.dirname(sys.argv[0])        
testinput_path1 = pathname + "/testinput1.txt"   
testinput_path2 = pathname + "/testinput2.txt"  
input_path = pathname + "/input.txt"

def parse_input(path):
    with open(path, "r") as inputfile:
        data = inputfile.read()
        lines = data.split('\n')
    departure = int(lines[0])
    buses = [int(x) if x != 'x' else 'x' for x in lines[1].split(',')]
    return departure, buses

def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a * b, n)
    
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod

def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a % b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1

def part1(departure, buses):
    # Filter out 'x' entries if they exist in buses
    active_buses = [bus for bus in buses if bus != 'x']
    
    d, b = float('inf'), 0
    for bus in active_buses:
        wait_time = bus - (departure % bus)
        if wait_time < d:
            d = wait_time
            b = bus
    return d * b

def part2(buses):
    # Create list of (index, bus_id) tuples, excluding 'x' entries
    schedule = [(i, bus) for i, bus in enumerate(buses) if bus != 'x']
    
    # Prepare inputs for Chinese Remainder Theorem
    n = [bus for _, bus in schedule]  # moduli
    a = [(-i % bus) for i, bus in schedule]  # remainders
    
    return chinese_remainder(n, a)

# Test values from the puzzle
testresult_part1 = 295  # 59 * 5
testresult_part2 = 1068781

if __name__ == "__main__":
    if testresult_part1 == part1(*parse_input(testinput_path1)):
        print("*** Part 1 Test Passed ***")
        start = time.time()
        print("----Part 1 Result: ", part1(*parse_input(input_path)))
        end = time.time()
        print("====Part 1 Time ", end - start)
    else:
        print("Part 1 Test Failed")
        print("Part 1 Test Result: ", part1(*parse_input(testinput_path1)))
        print("Expected ", testresult_part1)
        
    if testresult_part2 == part2(parse_input(testinput_path1)[1]):
        print("*** Part 2 Test Passed ***")
        start = time.time()
        print("----Part 2 Result: ", part2(parse_input(input_path)[1]))
        end = time.time()
        print("====Part 2 Time ", end - start)
    else:
        print("Part 2 Test Failed")
        print("Part 2 Test Result: ", part2(parse_input(testinput_path1)[1]))
        print("Expected ", testresult_part2)