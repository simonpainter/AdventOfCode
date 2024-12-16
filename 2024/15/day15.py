import re, itertools, math,os,sys,string,time

pathname = os.path.dirname(sys.argv[0])        
testinput_path1 = pathname + "/testinput1.txt"   
testinput_path2 = pathname + "/testinput2.txt"  
input_path = pathname + "/input.txt"

def parse_input(path):
    with open(path, "r") as inputfile:
        data = inputfile.read().strip()
    parts = data.split('\n\n')
    map_lines = parts[0].strip().split('\n')
    warehouse_map = [list(line) for line in map_lines]
    moves = ''.join(parts[1].replace('\n', '').split())
    return (warehouse_map, moves)

def expand_map(warehouse_map):
    expanded = []
    for line in warehouse_map:
        new_line = []
        for char in line:
            if char == '#':
                new_line.extend(['#', '#'])
            elif char == 'O':
                new_line.extend(['[', ']'])
            elif char == '.':
                new_line.extend(['.', '.'])
            elif char == '@':
                new_line.extend(['@', '.'])
        expanded.append(new_line)
    return expanded

def find_robot(warehouse_map):
    for y in range(len(warehouse_map)):
        for x in range(len(warehouse_map[0])):
            if warehouse_map[y][x] == '@':
                return (x, y)
    return None

def calculate_gps_sum(warehouse_map):
    total = 0
    for y in range(len(warehouse_map)):
        for x in range(len(warehouse_map[0])):
            if warehouse_map[y][x] == 'O':
                distance_from_top = y 
                distance_from_left = x
                gps = (100 * distance_from_top) + distance_from_left
                total += gps
    return total

def try_move(warehouse_map, robot_pos, dx, dy):
    current_x, current_y = robot_pos
    new_x = current_x + dx
    new_y = current_y + dy
    
    if warehouse_map[new_y][new_x] == '#':
        return False
    
    if warehouse_map[new_y][new_x] == '.':
        warehouse_map[current_y][current_x] = '.'
        warehouse_map[new_y][new_x] = '@'
        return True
    
    if warehouse_map[new_y][new_x] == 'O':
        check_x = new_x
        check_y = new_y
        while warehouse_map[check_y][check_x] == 'O':
            check_x += dx
            check_y += dy
        if warehouse_map[check_y][check_x] == '.':
            warehouse_map[check_y][check_x] = 'O'
            warehouse_map[current_y][current_x] = '.'
            warehouse_map[new_y][new_x] = '@'
            return True
        return False
    return False

def calculate_gps_sum_wide(warehouse_map):
    total = 0
    for y in range(len(warehouse_map)):
        for x in range(len(warehouse_map[0])-1):
            if warehouse_map[y][x] == '[' and warehouse_map[y][x+1] == ']':
                distance_from_top = y
                distance_from_left = x
                gps = (100 * distance_from_top) + distance_from_left
                total += gps
    return total

def try_move_wide_h(warehouse_map, robot_pos, dx, new_y):
    chain = []
    if dx < 0:
        start_x = robot_pos[0] + dx if warehouse_map[new_y][robot_pos[0] + dx] == '[' else robot_pos[0] + dx - 1
        x = start_x
        while x >= 0 and warehouse_map[new_y][x] == '[' and warehouse_map[new_y][x+1] == ']':
            chain.insert(0, (x, x+1))
            x -= 2
        if chain and chain[0][0] >= 1 and warehouse_map[new_y][chain[0][0]-1] == '.':
            for box_x, box_x2 in chain:
                warehouse_map[new_y][box_x] = '.'
                warehouse_map[new_y][box_x2] = '.'
            for box_x, _ in chain:
                warehouse_map[new_y][box_x-1] = '['
                warehouse_map[new_y][box_x] = ']'
            warehouse_map[robot_pos[1]][robot_pos[0]] = '.'
            warehouse_map[new_y][robot_pos[0] + dx] = '@'
            return True
    else:
        start_x = robot_pos[0] + dx
        if warehouse_map[new_y][start_x] == ']':
            start_x -= 1
        x = start_x
        while x < len(warehouse_map[0])-1 and warehouse_map[new_y][x] == '[' and warehouse_map[new_y][x+1] == ']':
            chain.append((x, x+1))
            x += 2
        if chain and chain[-1][1] < len(warehouse_map[0])-2 and warehouse_map[new_y][chain[-1][1]+1] == '.':
            for box_x, box_x2 in reversed(chain):
                warehouse_map[new_y][box_x] = '.'
                warehouse_map[new_y][box_x2] = '.'
            for box_x, _ in reversed(chain):
                warehouse_map[new_y][box_x+1] = '['
                warehouse_map[new_y][box_x+2] = ']'
            warehouse_map[robot_pos[1]][robot_pos[0]] = '.'
            warehouse_map[new_y][robot_pos[0] + dx] = '@'
            return True
    return False

def check_vertical_chain(warehouse_map, x, y, dy, chain=None):
    if chain is None:
        chain = set()
    box_start = None
    if warehouse_map[y][x] == '[':
        if warehouse_map[y][x+1] == ']':
            box_start = x
    elif warehouse_map[y][x] == ']':
        if warehouse_map[y][x-1] == '[':
            box_start = x-1
    if box_start is None:
        return False, chain
    box = (box_start, box_start+1, y)
    if box not in chain:
        chain.add(box)
    next_y = y + dy
    if next_y < 0 or next_y >= len(warehouse_map):
        return False, chain
    if warehouse_map[next_y][box_start] == '.' and warehouse_map[next_y][box_start+1] == '.':
        return True, chain
    if warehouse_map[next_y][box_start] == '#' or warehouse_map[next_y][box_start+1] == '#':
        return False, chain
    for check_x in [box_start, box_start+1]:
        if warehouse_map[next_y][check_x] in ['[', ']']:
            valid, new_chain = check_vertical_chain(warehouse_map, check_x, next_y, dy, chain)
            if not valid:
                return False, chain
    return True, chain

def try_move_wide_v(warehouse_map, robot_pos, dy, new_x):
    current_y = robot_pos[1]
    new_y = current_y + dy
    if warehouse_map[new_y][new_x] not in ['[', ']']:
        return False
    valid, chain = check_vertical_chain(warehouse_map, new_x, new_y, dy)
    if valid and chain:
        box_list = sorted(chain, key=lambda b: b[2], reverse=(dy > 0))
        for start_x, end_x, box_y in box_list:
            warehouse_map[box_y][start_x] = '.'
            warehouse_map[box_y][end_x] = '.'
            warehouse_map[box_y+dy][start_x] = '['
            warehouse_map[box_y+dy][end_x] = ']'
        warehouse_map[current_y][robot_pos[0]] = '.'
        warehouse_map[new_y][new_x] = '@'
        return True
    return False

def try_move_wide(warehouse_map, robot_pos, dx, dy):
    new_x = robot_pos[0] + dx
    new_y = robot_pos[1] + dy
    if warehouse_map[new_y][new_x] == '#':
        return False
    if warehouse_map[new_y][new_x] == '.':
        warehouse_map[robot_pos[1]][robot_pos[0]] = '.'
        warehouse_map[new_y][new_x] = '@'
        return True
    if warehouse_map[new_y][new_x] in ['[', ']']:
        if dx != 0:
            return try_move_wide_h(warehouse_map, robot_pos, dx, new_y)
        else:
            return try_move_wide_v(warehouse_map, robot_pos, dy, new_x)
    return False

def part1(input):
    warehouse_map, moves = input
    move_vectors = {'^': (0, -1), 'v': (0, 1), '<': (-1, 0), '>': (1, 0)}
    for move in moves:
        if move in move_vectors:
            dx, dy = move_vectors[move]
            robot_pos = find_robot(warehouse_map)
            try_move(warehouse_map, robot_pos, dx, dy)
    return calculate_gps_sum(warehouse_map)

def part2(input):
    warehouse_map, moves = input
    expanded_map = expand_map(warehouse_map)
    move_vectors = {'^': (0, -1), 'v': (0, 1), '<': (-1, 0), '>': (1, 0)}
    for move in moves:
        if move in move_vectors:
            dx, dy = move_vectors[move]
            robot_pos = find_robot(expanded_map)
            try_move_wide(expanded_map, robot_pos, dx, dy)
    return calculate_gps_sum_wide(expanded_map)

testresult_part1 = 2028
testresult_part2 = 9021

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