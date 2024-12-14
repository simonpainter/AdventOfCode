import re, itertools, math,os,sys,string,time

           
pathname = os.path.dirname(sys.argv[0])        
testinput_path1 = pathname + "/testinput1.txt"   
testinput_path2 = pathname + "/testinput2.txt"  
input_path = pathname + "/input.txt"



def parse_input(path):
    with open(path, "r") as inputfile:
        robots = []
        for line in inputfile:
            if line.strip() and '=' in line:  # Skip empty lines and non-robot lines
                pos, vel = line.strip().split()
                px, py = map(int, pos[2:].split(','))
                vx, vy = map(int, vel[2:].split(','))
                robots.append((px, py, vx, vy))
        return robots

def simulate_robots(robots, width, height, seconds):
    """Simulate robot movement with wrapping at boundaries"""
    positions = {}  # (x,y) -> count of robots
    
    for px, py, vx, vy in robots:
        # Calculate final position after wrapping
        x = (px + vx * seconds) % width
        y = (py + vy * seconds) % height
        
        # Add to position count
        pos = (x, y)
        positions[pos] = positions.get(pos, 0) + 1
    
    return positions

def count_quadrants(positions, width, height):
    """Count robots in each quadrant, excluding middle lines"""
    mid_x = width // 2
    mid_y = height // 2
    quadrants = [0] * 4  # [top-left, top-right, bottom-left, bottom-right]
    
    for (x, y), count in positions.items():
        # Skip robots on middle lines
        if x == mid_x or y == mid_y:
            continue
            
        # Determine quadrant
        quad_idx = (int(x > mid_x) + 2 * int(y > mid_y))
        quadrants[quad_idx] += count
    
    return quadrants

def has_overlaps(positions):
    """Check if any robots share the same position"""
    return any(count > 1 for count in positions.values())

def print_grid(positions, width, height):
    """Print grid with * for robots"""
    for y in range(height):
        row = ""
        for x in range(width):
            if (x, y) in positions:
                row += "*"
            else:
                row += "."
        print(row)


def part1(robots, width, height):
    # Simulate for 100 seconds
    positions = simulate_robots(robots, width, height, 100)
    
    # Calculate safety factor
    quadrants = count_quadrants(positions, width, height)
    safety_factor = quadrants[0] * quadrants[1] * quadrants[2] * quadrants[3]
    
    return safety_factor

def part2(robots, width, height):
    seconds = 0
    max_seconds = 100000  # Safety limit
    
    while seconds < max_seconds:
        positions = simulate_robots(robots, width, height, seconds)
        if not has_overlaps(positions):
            print(f"\nFound non-overlapping configuration after {seconds} seconds:")
            print_grid(positions, width, height)
            return seconds
        seconds += 1
    
    print(f"No non-overlapping configuration found within {max_seconds} seconds")
    return None

testresult_part1 = 12
testresult_part2 = 0


if testresult_part1 == part1(parse_input(testinput_path1),11,7):
	print("*** Part 1 Test Passed ***")
	start = time.time()
	print("----Part 1 Result: ", part1(parse_input(input_path),101,103))
	end = time.time()
	print("====Part 1 Time ", end - start)

else:
	print("Part 1 Test Failed")
	print("Part 1 Test Result: ", part1(parse_input(testinput_path1),11,7))
	print("Expected ", testresult_part1)
	
if testresult_part2 == part2(parse_input(testinput_path2),11,7):
	print("*** Part 2 Test Passed ***")
	start = time.time()
	print("----Part 2 Result: ", part2(parse_input(input_path),101,103))
	end = time.time()
	print("====Part 2 Time ", end - start)

else:
	print("Part 2 Test Failed")
	print("Part 2 Test Result: ", part2(parse_input(testinput_path2),11,7))
	print("Expected ", testresult_part2)