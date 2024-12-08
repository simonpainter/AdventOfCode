import re, itertools, math,os,sys,string,time

           
pathname = os.path.dirname(sys.argv[0])        
testinput_path1 = pathname + "/testinput1.txt"   
testinput_path2 = pathname + "/testinput2.txt"  
input_path = pathname + "/input.txt"



def parse_input(path):
    with open(path, "r") as inputfile:
        data = inputfile.read()
        lines = data.split('\n')
    
    ingredients = {}
    for line in lines:
        if not line: continue
        parts = line.split(':')
        name = parts[0]
        props = {}
        for prop in parts[1].split(','):
            prop_name, value = prop.strip().split()
            props[prop_name] = int(value)
        ingredients[name] = props
    
    return ingredients

def calculate_score(ingredients, amounts):
    # Initialize properties to 0
    properties = {'capacity': 0, 'durability': 0, 'flavor': 0, 'texture': 0}
    
    # Calculate total for each property
    for ingredient, amount in amounts.items():
        for prop in properties:
            properties[prop] += ingredients[ingredient][prop] * amount
    
    # If any property is negative, score is 0
    if any(value <= 0 for value in properties.values()):
        return 0
    
    # Multiply all properties together
    score = 1
    for value in properties.values():
        score *= value
    
    return score

def find_combinations(total, n):
    if n == 1:
        yield (total,)
        return
    
    for i in range(total + 1):
        for j in find_combinations(total - i, n - 1):
            yield (i,) + j

def part1(input):
    max_score = 0
    ingredient_names = list(input.keys())
    
    # Try all combinations that sum to 100
    for combo in find_combinations(100, len(ingredient_names)):
        amounts = dict(zip(ingredient_names, combo))
        score = calculate_score(input, amounts)
        max_score = max(max_score, score)
    
    return max_score

def part2(input):
    max_score = 0
    ingredient_names = list(input.keys())
    
    # Try all combinations that sum to 100
    for combo in find_combinations(100, len(ingredient_names)):
        amounts = dict(zip(ingredient_names, combo))
        
        # Calculate calories
        calories = sum(input[ing]['calories'] * amt 
                      for ing, amt in amounts.items())
        
        # Only consider combinations with exactly 500 calories
        if calories == 500:
            score = calculate_score(input, amounts)
            max_score = max(max_score, score)
    
    return max_score

# Test result for the example given
testresult_part1 = 62842880
testresult_part2 = 57600000


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