import re, itertools, math,os,sys,string,time,functools

           
pathname = os.path.dirname(sys.argv[0])        
testinput_path1 = pathname + "/testinput1.txt"   
testinput_path2 = pathname + "/testinput2.txt"  
input_path = pathname + "/input.txt"


def parse_input(path):
    with open(path, "r") as inputfile:
        data = inputfile.read().strip()
        rules_text, updates_text = data.split('\n\n')
        
        # Store rules in both directions for quick lookup
        rules = {}
        for rule in rules_text.splitlines():
            before, after = map(int, rule.split('|'))
            if before not in rules:
                rules[before] = set()
            if after not in rules:
                rules[after] = set()
            rules[before].add(after)  # before must come before after
        
        # Parse updates into lists of integers
        updates = [list(map(int, update.split(','))) for update in updates_text.splitlines()]
        
        return rules, updates

def is_valid_order(sequence, rules):
    # Create position lookup dictionary for this sequence
    positions = {num: i for i, num in enumerate(sequence)}
    
    # Check all applicable rules
    for page in sequence:
        if page in rules:
            # For each rule where this page must come before another page
            for must_follow in rules[page]:
                # If the other page exists in this sequence
                if must_follow in positions:
                    # Check if the order is correct
                    if positions[page] > positions[must_follow]:
                        return False
                        
    return True

def compare_pages(p1, p2, rules):
    """Custom comparison function for sorting pages based on rules"""
    # If p1 must come before p2
    if p1 in rules and p2 in rules[p1]:
        return -1
    # If p2 must come before p1
    if p2 in rules and p1 in rules[p2]:
        return 1
    # No direct relationship
    return 0

def sort_update(update, rules):
    """Sort update using custom comparison function"""
    return sorted(update, key=functools.cmp_to_key(lambda x, y: compare_pages(x, y, rules)))

def get_middle_number(sequence):
    return sequence[len(sequence) // 2]

def part1(input):
    rules, updates = input
    total = 0
    
    for update in updates:
        # Sort the update and compare with original
        sorted_update = sort_update(update, rules)
        if update == sorted_update:
            total += get_middle_number(update)
    
    return total

def part2(input):
    rules, updates = input
    total = 0
    
    for update in updates:
        # Sort the update
        sorted_update = sort_update(update, rules)
        # Only include if original order was incorrect
        if update != sorted_update:
            total += get_middle_number(sorted_update)
    
    return total

testresult_part1 = 143
testresult_part2 = 123


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