import re, itertools, math,os,sys,string,time

           
pathname = os.path.dirname(sys.argv[0])        
testinput_path1 = pathname + "/testinput1.txt"   
testinput_path2 = pathname + "/testinput2.txt"  
input_path = pathname + "/input.txt"

def parse_input(path):
    with open(path, "r") as inputfile:
        data = inputfile.read()
        lines = data.split('\n')
    
    aunts = {}
    for line in lines:
        if not line: continue
        # Split on ':' to separate Sue N from properties
        parts = line.split(':', 1)
        sue_num = int(parts[0].split()[1])
        # Parse properties
        properties = {}
        for prop in parts[1].strip().split(','):
            name, value = prop.strip().split(': ')
            properties[name] = int(value)
        aunts[sue_num] = properties
    
    return aunts

def part1(input):
    # MFCSAM readings
    mfcsam = {
        'children': 3,
        'cats': 7,
        'samoyeds': 2,
        'pomeranians': 3,
        'akitas': 0,
        'vizslas': 0,
        'goldfish': 5,
        'trees': 3,
        'cars': 2,
        'perfumes': 1
    }
    
    # Check each aunt against the readings
    for sue_num, properties in input.items():
        matches = True
        for prop, value in properties.items():
            if mfcsam[prop] != value:
                matches = False
                break
        if matches:
            return sue_num
    
    return None

def part2(input):
    # MFCSAM readings
    mfcsam = {
        'children': 3,
        'cats': 7,
        'samoyeds': 2,
        'pomeranians': 3,
        'akitas': 0,
        'vizslas': 0,
        'goldfish': 5,
        'trees': 3,
        'cars': 2,
        'perfumes': 1
    }
    
    # Check each aunt against the readings
    for sue_num, properties in input.items():
        matches = True
        for prop, value in properties.items():
            # Special cases for cats and trees (greater than)
            if prop == 'cats' or prop == 'trees':
                if value <= mfcsam[prop]:
                    matches = False
                    break
            # Special cases for pomeranians and goldfish (fewer than)
            elif prop == 'pomeranians' or prop == 'goldfish':
                if value >= mfcsam[prop]:
                    matches = False
                    break
            # All other properties must match exactly
            elif mfcsam[prop] != value:
                matches = False
                break
        if matches:
            return sue_num
    
    return None

testresult_part1 = None
testresult_part2 = None

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