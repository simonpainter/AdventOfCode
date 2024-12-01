import re, itertools, math,os,sys,string,time

           
pathname = os.path.dirname(sys.argv[0])        
testinput_path1 = pathname + "/testinput1.txt"   
testinput_path2 = pathname + "/testinput2.txt"  
input_path = pathname + "/input.txt"



def parse_input(path):
	with open (path, "r") as inputfile:
		data = inputfile.read()
		lines = data.strip().split('\n')
		return lines

	input = []
	#for line in lines:
		#input.append(int(line))
		#input.append(line.split(' '))
	#for group in groups:
		#input.append(group.replace("\n", "")
		#input.append(group.split(' '))
	return input

def is_game_possible(game_string, max_red=12, max_green=13, max_blue=14):
    game_id_part, sets_part = game_string.split(':')
    game_id = int(game_id_part.split()[1])
    
    sets = sets_part.split(';')
    for cube_set in sets:
        red = green = blue = 0
        
        for cube_count in cube_set.strip().split(','):
            count, color = cube_count.strip().split()
            count = int(count)
            
            if color == 'red':
                red = count
            elif color == 'green':
                green = count
            elif color == 'blue':
                blue = count
        
        if red > max_red or green > max_green or blue > max_blue:
            return False, game_id
    
    return True, game_id

def get_minimum_cubes(game_string):
    _, sets_part = game_string.split(':')
    min_red = min_green = min_blue = 0
    
    sets = sets_part.split(';')
    for cube_set in sets:
        red = green = blue = 0
        
        for cube_count in cube_set.strip().split(','):
            count, color = cube_count.strip().split()
            count = int(count)
            
            if color == 'red':
                red = count
            elif color == 'green':
                green = count
            elif color == 'blue':
                blue = count
        
        min_red = max(min_red, red)
        min_green = max(min_green, green)
        min_blue = max(min_blue, blue)
    
    return min_red, min_green, min_blue
def part1(input):
    total = 0
    for line in input:
        possible, game_id = is_game_possible(line)
        if possible:
            total += game_id
    return total


def part2(input):
    total_power = 0
    for line in input:
        red, green, blue = get_minimum_cubes(line)
        power = red * green * blue
        total_power += power
    return total_power

testresult_part1 = 8
testresult_part2 = 2286


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