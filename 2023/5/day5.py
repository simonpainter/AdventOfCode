import re, itertools, math,os,sys,string,time

           
pathname = os.path.dirname(sys.argv[0])        
testinput_path1 = pathname + "/testinput1.txt"   
testinput_path2 = pathname + "/testinput2.txt"  
input_path = pathname + "/input.txt"


def parse_input(path):
    with open(path, "r") as file:
        sections = file.read().strip().split("\n\n")
        
        if "seeds:" not in sections[0]:
            return None, None
            
        # Parse seeds differently for part1 and part2
        raw_seeds = list(map(int, sections[0].split(":")[1].strip().split()))
        
        # Maps stay the same for both parts
        maps = []
        for section in sections[1:]:
            ranges = []
            for line in section.split("\n")[1:]:
                dest_start, src_start, length = map(int, line.split())
                ranges.append((dest_start, src_start, length))
            maps.append(sorted(ranges, key=lambda x: x[1]))
            
        return raw_seeds, maps

def apply_mapping(number, ranges):
    """Apply a single mapping step to a number"""
    for dest_start, src_start, length in ranges:
        if src_start <= number < src_start + length:
            return dest_start + (number - src_start)
    return number

def find_location(seed, maps):
    """Follow a single seed through all mapping steps to find its final location"""
    current = seed
    for mapping in maps:
        current = apply_mapping(current, mapping)
    return current

def apply_range_mapping(range_start, range_end, mapping_ranges):
    """Map a range through a single mapping step, possibly splitting into multiple ranges"""
    result = []
    current = range_start
    
    while current < range_end:
        mapped = False
        
        for dest_start, src_start, length in mapping_ranges:
            src_end = src_start + length
            
            if current >= src_end:
                continue
                
            if current < src_start:
                result.append((current, min(src_start, range_end)))
                current = src_start
                if current >= range_end:
                    break
                continue
            
            mapped = True
            overlap_end = min(src_end, range_end)
            offset = dest_start - src_start
            result.append((current + offset, overlap_end + offset))
            current = overlap_end
            break
            
        if not mapped:
            result.append((current, range_end))
            break
            
    return result

def find_min_location_range(seed_range, maps):
    """Find minimum location for a range of seeds"""
    current_ranges = [seed_range]
    
    for mapping in maps:
        next_ranges = []
        for start, end in current_ranges:
            mapped_ranges = apply_range_mapping(start, end, mapping)
            next_ranges.extend(mapped_ranges)
        current_ranges = next_ranges
    
    return min(start for start, end in current_ranges)

def part1(puzzle_input):
    seeds, maps = puzzle_input
    return min(find_location(seed, maps) for seed in seeds)

def part2(puzzle_input):
    seeds, maps = puzzle_input
    seed_ranges = [(seeds[i], seeds[i] + seeds[i+1]) for i in range(0, len(seeds), 2)]
    return min(find_min_location_range(seed_range, maps) for seed_range in seed_ranges)

testresult_part1 = 35
testresult_part2 = 46


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