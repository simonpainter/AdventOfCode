import re, itertools, math,os,sys,string,time

           
pathname = os.path.dirname(sys.argv[0])        
testinput_path1 = pathname + "/testinput1.txt"   
testinput_path2 = pathname + "/testinput2.txt"  
input_path = pathname + "/input.txt"


def parse_input(path):
    with open(path, "r") as inputfile:
        data = inputfile.read()
        pattern = r'Button A: X\+(\d+), Y\+(\d+)\nButton B: X\+(\d+), Y\+(\d+)\nPrize: X=(\d+), Y=(\d+)'
        machines = []
        for match in re.finditer(pattern, data):
            a_x, a_y, b_x, b_y, p_x, p_y = map(int, match.groups())
            machines.append(([a_x, a_y], [b_x, b_y], [p_x, p_y]))
    return machines

def find_min_tokens_bfs(button_a, button_b, target_x, target_y):
    from collections import deque
    
    # State: (a_presses, b_presses)
    start = (0, 0)
    queue = deque([start])
    seen = {start}
    
    while queue:
        a_count, b_count = queue.popleft()
        
        # Calculate current position
        x = a_count * button_a[0] + b_count * button_b[0]
        y = a_count * button_a[1] + b_count * button_b[1]
        
        # Check if we've reached the target
        if x == target_x and y == target_y:
            return a_count * 3 + b_count
        
        # Try pressing A if under 100
        if a_count < 100:
            next_a = (a_count + 1, b_count)
            if next_a not in seen:
                queue.append(next_a)
                seen.add(next_a)
        
        # Try pressing B if under 100
        if b_count < 100:
            next_b = (a_count, b_count + 1)
            if next_b not in seen:
                queue.append(next_b)
                seen.add(next_b)
    
    return None

def solve_machine_maths(button_a, button_b, prize):
    """Solve using simultaneous equations - thanks Andy"""
    a_x, a_y = button_a
    b_x, b_y = button_b
    p_x, p_y = prize
    
    # Multiply equations and subtract to eliminate B
    coefficient = a_x*b_y - a_y*b_x
    if coefficient == 0:
        return None
        
    # Solve for A
    A = (b_y*p_x - b_x*p_y) / coefficient
    
    # Check if A is a positive integer
    if A != int(A) or A < 0:
        return None
    A = int(A)
        
    # Substitute back to find B using equation (1)
    if b_x == 0:
        if a_x == 0:
            return None
        if A * a_x != p_x:
            return None
        B = (p_y - a_y*A) / b_y
    else:
        B = (p_x - a_x*A) / b_x
        
    # Check if B is a positive integer
    if B != int(B) or B < 0:
        return None
    B = int(B)
    
    # Verify both equations are satisfied
    if a_x*A + b_x*B != p_x or a_y*A + b_y*B != p_y:
        return None
        
    return A * 3 + B

def part1(machines):
    total_tokens = 0
    possible_prizes = 0
    
    for i, (button_a, button_b, prize) in enumerate(machines, 1):
        tokens = find_min_tokens_bfs(button_a, button_b, prize[0], prize[1])
        if tokens is not None:
            total_tokens += tokens
            possible_prizes += 1
    
    return total_tokens if possible_prizes > 0 else 0

def part2(machines):
    total_tokens = 0
    possible_prizes = 0
    
    offset = 10000000000000
    modified_machines = []
    for button_a, button_b, prize in machines:
        new_prize = [p + offset for p in prize]
        modified_machines.append((button_a, button_b, new_prize))
    
    for button_a, button_b, prize in modified_machines:
        tokens = solve_machine_maths(button_a, button_b, prize)
        if tokens is not None:
            total_tokens += tokens
            possible_prizes += 1
    
    return total_tokens if possible_prizes > 0 else 0

testresult_part1 = 480
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