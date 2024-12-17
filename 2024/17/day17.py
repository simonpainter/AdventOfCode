import re, itertools, math,os,sys,string,time

pathname = os.path.dirname(sys.argv[0])        
testinput_path1 = pathname + "/testinput1.txt"   
testinput_path2 = pathname + "/testinput2.txt"  
input_path = pathname + "/input.txt"

def parse_input(path):
    with open(path, "r") as inputfile:
        data = inputfile.read().strip()
        lines = [line for line in data.split('\n') if line]
        registers = {}
        for line in lines[:3]:
            name, value = line.split(': ')
            registers[name.split()[-1]] = int(value)
        program = lines[-1].split(': ')[1]
        return [registers, program]

def run_program(program, a_val, b_val, c_val):
    A = a_val
    B = b_val
    C = c_val
    
    if isinstance(program, str):
        program = [int(x) for x in program.split(',')]
    
    outputs = []
    ip = 0
    
    while ip < len(program):
        if ip + 1 >= len(program):
            break
            
        opcode = program[ip]
        operand = program[ip + 1]
        
        def get_combo_value(op):
            if op <= 3: return op
            elif op == 4: return A
            elif op == 5: return B
            elif op == 6: return C
            return 0
        
        if opcode == 0: A = A // (2 ** get_combo_value(operand))
        elif opcode == 1: B = B ^ operand
        elif opcode == 2: B = get_combo_value(operand) % 8
        elif opcode == 3:
            if A != 0:
                ip = operand
                continue
        elif opcode == 4: B = B ^ C
        elif opcode == 5: outputs.append(str(get_combo_value(operand) % 8))
        elif opcode == 6: B = A // (2 ** get_combo_value(operand))
        elif opcode == 7: C = A // (2 ** get_combo_value(operand))
            
        ip += 2
    
    return ','.join(outputs)

def find_next_value(target, program, prev_value, prev_diff,registers):
    if prev_diff == 0:
        base = prev_value + 1
        predicted = base + 1000
    else:
        predicted = prev_value + (prev_diff * 8)
        base = max(prev_value + 1, predicted - 1000)
    
    while True:
        output = run_program(program, base, registers['B'], registers['C'])
        if output.endswith(target):
            return base
        base += 1
        if base > predicted + 1000:
            break
    
    base = prev_value
    while True:
        base += 1
        output = run_program(program, base, registers['B'], registers['C'])
        if output.endswith(target):
            return base

def part1(input):
    registers, program = input
    return run_program(program, registers['A'], registers['B'], registers['C'])

def part2(input):
    registers, program = input
    current_target = "3,0"
    current_a = find_next_value(current_target, program, 0, 0,registers)
    
    target_parts = program.split(',')
    current_length = 2
    prev_value = current_a
    prev_diff = 0
    
    while current_length < len(target_parts):
        next_digit = target_parts[-(current_length + 1)]
        current_target = next_digit + "," + current_target
        new_value = find_next_value(current_target, program, prev_value, prev_diff,registers)
        prev_diff = new_value - prev_value
        prev_value = new_value
        current_a = new_value
        current_length += 1
        
    return current_a

testresult_part1 = "4,6,3,5,6,3,5,2,1,0"
testresult_part2 = 117440

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