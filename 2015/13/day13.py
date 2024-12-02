import re, itertools, math,os,sys,string,time
from itertools import permutations

           
pathname = os.path.dirname(sys.argv[0])        
testinput_path1 = pathname + "/testinput1.txt"   
testinput_path2 = pathname + "/testinput2.txt"  
input_path = pathname + "/input.txt"


def parse_input(path):
    with open(path, "r") as inputfile:
        data = inputfile.read()
        lines = data.split('\n')
    
    happiness = {}
    people = set()
    
    for line in lines:
        if not line: continue
        match = re.match(r'(\w+) would (gain|lose) (\d+) happiness units by sitting next to (\w+)', line)
        if match:
            person1, gainlose, amount, person2 = match.groups()
            amount = int(amount) * (-1 if gainlose == 'lose' else 1)
            
            if person1 not in happiness:
                happiness[person1] = {}
            happiness[person1][person2] = amount
            people.add(person1)
            people.add(person2)
    
    return happiness, list(people)

def calculate_happiness(arrangement, happiness):
    total = 0
    n = len(arrangement)
    
    for i in range(n):
        person = arrangement[i]
        next_person = arrangement[(i + 1) % n]
        total += happiness[person][next_person]
        total += happiness[next_person][person]
    
    return total

def part1(input):
    happiness, people = input
    max_happiness = float('-inf')
    
    # Fix one person's position and permute the rest to avoid duplicate circular arrangements
    first_person = people[0]
    rest_people = people[1:]
    
    for perm in permutations(rest_people):
        arrangement = [first_person] + list(perm)
        happiness_change = calculate_happiness(arrangement, happiness)
        max_happiness = max(max_happiness, happiness_change)
    
    return max_happiness

def part2(input):
    happiness, people = input
    
    # Add yourself with 0 happiness change for all interactions
    happiness['you'] = {person: 0 for person in people}
    for person in people:
        happiness[person]['you'] = 0
    people.append('you')
    
    return part1((happiness, people))

testresult_part1 = 330
testresult_part2 = 286


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