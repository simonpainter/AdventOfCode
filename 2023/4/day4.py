import re, itertools, math,os,sys,string,time

           
pathname = os.path.dirname(sys.argv[0])        
testinput_path1 = pathname + "/testinput1.txt"   
testinput_path2 = pathname + "/testinput2.txt"  
input_path = pathname + "/input.txt"

def parse_input(path):
    with open(path, "r") as inputfile:
        cards = []
        for line in inputfile:
            card_id, numbers = line.split(":")
            winning_numbers, my_numbers = numbers.split("|")
            winning_numbers = set(int(x) for x in winning_numbers.split())
            my_numbers = set(int(x) for x in my_numbers.split())
            cards.append((winning_numbers, my_numbers))
        return cards

def part1(cards):
    total_points = 0
    
    for winning_numbers, my_numbers in cards:
        matches = len(winning_numbers & my_numbers)
        
        if matches > 0:
            points = 1 << (matches - 1)  
            total_points += points
            
    return total_points

def part2(cards):
    card_counts = [1] * len(cards)
    
    for i, (winning_numbers, my_numbers) in enumerate(cards):
        matches = len(winning_numbers & my_numbers)
        
        for j in range(matches):
            if i + j + 1 < len(cards):
                card_counts[i + j + 1] += card_counts[i]
    
    return sum(card_counts)

testresult_part1 = 13
testresult_part2 = 30

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