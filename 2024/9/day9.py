import re, itertools, math,os,sys,string,time

           
pathname = os.path.dirname(sys.argv[0])        
testinput_path1 = pathname + "/testinput1.txt"   
testinput_path2 = pathname + "/testinput2.txt"  
input_path = pathname + "/input.txt"


def parse_input(path):
    with open(path, "r") as inputfile:
        return inputfile.read().strip()

def create_initial_disk(disk_map):
    file_id = 0
    blocks = []
    file_sizes = {}
    
    for i, length in enumerate(disk_map):
        length = int(length)
        if i % 2 == 0:  # File
            blocks.extend([file_id] * length)
            file_sizes[file_id] = length
            file_id += 1
        else:  # Free space
            blocks.extend(['.'] * length)
    
    return blocks, file_sizes

def find_leftmost_space(blocks):
    try:
        return blocks.index('.')
    except ValueError:
        return -1

def find_rightmost_file(blocks):
    for i in range(len(blocks)-1, -1, -1):
        if blocks[i] != '.':
            return i
    return -1

def move_block(blocks):
    target = find_leftmost_space(blocks)
    if target == -1:
        return False
        
    source = find_rightmost_file(blocks)
    if source == -1 or source < target:
        return False
        
    file_id = blocks[source]
    blocks[target] = file_id
    blocks[source] = '.'
    
    return True

def move_whole_file(blocks, file_id, file_size):
    # Find current position of file
    start = -1
    end = -1
    for i in range(len(blocks)):
        if blocks[i] == file_id:
            if start == -1:
                start = i
            end = i + 1
    if start == -1:
        return False
        
    # Find leftmost space that can fit the file
    pos = 0
    while pos < start:
        if blocks[pos] == '.':
            # Check if we have enough contiguous space
            space_size = 0
            for i in range(pos, min(pos + file_size, len(blocks))):
                if blocks[i] != '.':
                    break
                space_size += 1
            if space_size >= file_size:
                # Move the file
                file_blocks = [file_id] * file_size
                free_blocks = ['.'] * file_size
                blocks[start:end] = free_blocks
                blocks[pos:pos+file_size] = file_blocks
                return True
            pos += space_size
        else:
            pos += 1
            
    return False

def calculate_checksum(blocks):
    total = 0
    for pos, block_id in enumerate(blocks):
        if block_id != '.':
            total += pos * int(block_id)
    return total

def part1(input):
    blocks, _ = create_initial_disk(input)
    while move_block(blocks):
        pass
    return calculate_checksum(blocks)

def part2(input):
    blocks, file_sizes = create_initial_disk(input)
    
    # Process files in descending ID order
    for file_id in range(len(file_sizes) - 1, -1, -1):
        move_whole_file(blocks, file_id, file_sizes[file_id])
    
    return calculate_checksum(blocks)

testresult_part1 = 1928
testresult_part2 = 2858


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