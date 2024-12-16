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

def part1(input):
    warehouse_map, moves = input
    move_vectors = {
        '^': (0, -1),
        'v': (0, 1),
        '<': (-1, 0),
        '>': (1, 0)
    }
    
    for move in moves:
        if move in move_vectors:
            dx, dy = move_vectors[move]
            robot_pos = find_robot(warehouse_map)
            try_move(warehouse_map, robot_pos, dx, dy)
    
    return calculate_gps_sum(warehouse_map)

def part2(input):
    pass

testresult_part1 = 2028
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