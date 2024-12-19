import re, itertools, math, os, sys, string, time, copy, operator

pathname = os.path.dirname(sys.argv[0])        
testinput_path1 = pathname + "/testinput1.txt"   
testinput_path2 = pathname + "/testinput2.txt"  
input_path = pathname + "/input.txt"

def parse_input(path):
    with open(path, "r") as inputfile:
        data = inputfile.read()
        lines = data.split('\n')
    input = []
    for line in lines:
        input.append(list(line))
    return input

def checkneighbour(x, y, seating):
    width = len(seating[0])
    length = len(seating)
    if (0 <= x < width) and (0 <= y < length):
        return seating[y][x]
    else:
        return '.'

def count_seats_1(x, y, seating):
    adjacent = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]
    count = 0
    for dx, dy in adjacent:
        neighbour_x = x + dx
        neighbour_y = y + dy
        if checkneighbour(neighbour_x, neighbour_y, seating) == '#':
            count += 1
    return count

def checkvisible(x, y, dx, dy, seating):
    width = len(seating[0])
    length = len(seating)
    x += dx
    y += dy
    while (0 <= x < width) and (0 <= y < length):
        if seating[y][x] in ['#', 'L']:
            return seating[y][x]
        x += dx
        y += dy
    return '.'

def count_seats_2(x, y, seating):
    directions = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]
    count = 0
    for dx, dy in directions:
        if checkvisible(x, y, dx, dy, seating) == '#':
            count += 1
    return count

def part1(input):
    new = copy.deepcopy(input)
    old = []
    while new != old:
        old = copy.deepcopy(new) 
        for y in range(0, len(new)):
            for x in range(0, len(new[y])):
                if old[y][x] == '.':
                    pass
                elif old[y][x] == 'L':
                    if count_seats_1(x, y, old) == 0:
                        new[y][x] = '#'
                elif old[y][x] == '#':
                    if count_seats_1(x, y, old) >= 4:
                        new[y][x] = 'L'
    return sum(row.count('#') for row in new)

def part2(input):
    new = copy.deepcopy(input)
    old = []
    while new != old:
        old = copy.deepcopy(new) 
        for y in range(0, len(new)):
            for x in range(0, len(new[y])):
                if old[y][x] == '.':
                    pass
                elif old[y][x] == 'L':
                    if count_seats_2(x, y, old) == 0:
                        new[y][x] = '#'
                elif old[y][x] == '#':
                    if count_seats_2(x, y, old) >= 5:
                        new[y][x] = 'L'
    return sum(row.count('#') for row in new)

# Test results from the puzzle description
testresult_part1 = 37
testresult_part2 = 26

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