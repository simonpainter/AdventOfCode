import re, itertools, math, os, sys, string, time

pathname = os.path.dirname(sys.argv[0])        
testinput_path1 = pathname + "/testinput1.txt"   
testinput_path2 = pathname + "/testinput2.txt"  
input_path = pathname + "/input.txt"

def parse_input(path):
    with open(path, "r") as inputfile:
        data = inputfile.read()
        lines = data.split('\n')
    return lines

def part1(input):
    mem = {}
    for line in input:
        if line[:2] == 'ma':
            mask = re.search('[X0-1]{36}',line)
            mask_and = int(mask.group(0).replace('1','0').replace('X','1'),2)
            mask_or = int(mask.group(0).replace('X','0'),2)
        elif line[:2] == 'me':
            register = re.search('mem\[(\d+)\] = (\d+)',line)
            memory = int(register.group(1))
            value = int(register.group(2))
            masked_value = value & mask_and
            output_value = masked_value | mask_or
            mem[memory] = output_value
    tot = 0
    for i in mem:
        tot = tot + mem[i]
    return tot

def get_addresses(address, mask):
    addr_bits = format(address, '036b')
    result = ''
    floating_positions = []
    for i, (a, m) in enumerate(zip(addr_bits, mask)):
        if m == '0':
            result += a
        elif m == '1':
            result += '1'
        else:  # m == 'X'
            result += 'X'
            floating_positions.append(i)
    
    addresses = []
    for bits in itertools.product('01', repeat=len(floating_positions)):
        addr = list(result)
        for pos, bit in zip(floating_positions, bits):
            addr[pos] = bit
        addresses.append(int(''.join(addr), 2))
    return addresses

def part2(input):
    mem = {}
    for line in input:
        if line[:2] == 'ma':
            mask = re.search('[X0-1]{36}', line).group(0)
        elif line[:2] == 'me':
            register = re.search('mem\[(\d+)\] = (\d+)', line)
            address = int(register.group(1))
            value = int(register.group(2))
            
            addresses = get_addresses(address, mask)
            for addr in addresses:
                mem[addr] = value
                
    tot = 0
    for i in mem:
        tot = tot + mem[i]
    return tot

testresult_part1 = 165
testresult_part2 = 208

if __name__ == "__main__":
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