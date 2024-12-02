import re, itertools, math,os,sys,string,time

           
pathname = os.path.dirname(sys.argv[0])        
testinput_path1 = pathname + "/testinput1.txt"   
testinput_path2 = pathname + "/testinput2.txt"  
input_path = pathname + "/input.txt"

def parse_input(path):
    with open(path, "r") as inputfile:
        data = inputfile.read()
        lines = data.split('\n')
    
    reindeer = {}
    for line in lines:
        if not line: continue
        parts = line.split()
        name = parts[0]
        speed = int(parts[3])
        fly_time = int(parts[6])
        rest_time = int(parts[-2])
        reindeer[name] = {'speed': speed, 'fly_time': fly_time, 'rest_time': rest_time}
    
    return reindeer

def calculate_distance(reindeer_stats, time):
    speed = reindeer_stats['speed']
    fly_time = reindeer_stats['fly_time']
    rest_time = reindeer_stats['rest_time']
    
    cycle_time = fly_time + rest_time
    complete_cycles = time // cycle_time
    remaining_time = min(fly_time, time % cycle_time)
    
    distance = speed * (complete_cycles * fly_time + remaining_time)
    return distance

def calculate_points(reindeer, total_time):
    points = {name: 0 for name in reindeer}
    
    for second in range(1, total_time + 1):
        # Calculate distance for each reindeer at this second
        current_distances = {name: calculate_distance(stats, second) 
                           for name, stats in reindeer.items()}
        
        # Find max distance
        max_distance = max(current_distances.values())
        
        # Award points to leaders
        for name, distance in current_distances.items():
            if distance == max_distance:
                points[name] += 1
    
    return points

def part1(input):
    race_time = 2503
    distances = {name: calculate_distance(stats, race_time) 
                for name, stats in input.items()}
    return max(distances.values())

def part2(input):
    race_time = 2503
    points = calculate_points(input, race_time)
    return max(points.values())

# Set test results for example with 1000 seconds
testresult_part1 = 2660
testresult_part2 = 1564



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