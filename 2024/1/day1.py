#!/usr/bin/env python3
# Advent of Code - Day 1
# Processes pairs of numbers to calculate distances and scores

import os
import sys
import time
import unittest


# File paths setup
pathname = os.path.dirname(os.path.abspath(__file__))
testinput_path1 = os.path.join(pathname, "testinput1.txt")
testinput_path2 = os.path.join(pathname, "testinput2.txt")
input_path = os.path.join(pathname, "input.txt")


def parse_input(path):
    """
    Parse the input file into two lists of numbers.
    
    Args:
        path: Path to the input file
        
    Returns:
        A list containing two lists: [left_numbers, right_numbers]
    """
    with open(path, "r") as inputfile:
        data = inputfile.read()
        lines = data.split('\n')
        # Note: groups is unused but kept for potential future use
        groups = data.split('\n\n')

    left_list = []
    right_list = []
    for line in lines:
        if line.strip():  # Skip empty lines
            left, right = map(int, line.split())
            left_list.append(left)
            right_list.append(right)
            
    return [left_list, right_list]


def part1(input):
    """
    Calculate the total distance between sorted corresponding elements.
    
    Args:
        input: List containing [left_numbers, right_numbers]
        
    Returns:
        Total distance (sum of absolute differences)
    """
    left_list = input[0]
    right_list = input[1]
    
    # Sort both lists independently
    left_list.sort()
    right_list.sort()

    total_distance = 0
    for l, r in zip(left_list, right_list):
        distance = abs(l - r)
        total_distance += distance
    
    return total_distance


def part2(input):
    """
    Calculate score based on frequency matching between lists.
    For each number in left_list, multiply by its frequency in right_list.
    
    Args:
        input: List containing [left_numbers, right_numbers]
        
    Returns:
        Total score from frequency matching
    """
    left_list = input[0]
    right_list = input[1]

    # Count occurrences of each number in right_list
    right_counts = {}
    for num in right_list:
        right_counts[num] = right_counts.get(num, 0) + 1
    
    # Calculate score by multiplying each left number by its frequency in right_list
    total_score = 0
    for num in left_list:
        count = right_counts.get(num, 0)
        score = num * count
        total_score += score
        
    return total_score


# Expected test results
testresult_part1 = 11
testresult_part2 = 31


# Unit tests
class TestDay1(unittest.TestCase):
    """Unit tests for Day 1 functions"""
    
    def test_parse_input(self):
        """Test input parsing function"""
        result = parse_input(testinput_path1)
        self.assertEqual(len(result), 2, "Should return two lists")
        self.assertEqual(len(result[0]), 6, "Left list should have 6 elements")
        self.assertEqual(len(result[1]), 6, "Right list should have 6 elements")
        self.assertEqual(result[0][0], 3, "First element in left list should be 3")
        self.assertEqual(result[1][0], 4, "First element in right list should be 4")
    
    def test_part1(self):
        """Test part1 function with test input"""
        test_input = parse_input(testinput_path1)
        result = part1(test_input)
        self.assertEqual(result, testresult_part1, f"Expected {testresult_part1}, got {result}")
    
    def test_part2(self):
        """Test part2 function with test input"""
        test_input = parse_input(testinput_path2)
        result = part2(test_input)
        self.assertEqual(result, testresult_part2, f"Expected {testresult_part2}, got {result}")
    
    def test_custom_input(self):
        """Test with a simple custom input"""
        custom_input = [[1, 2, 3], [3, 2, 1]]
        
        # Part 1 should sum the absolute differences of sorted lists
        # After sorting: [1, 2, 3] and [1, 2, 3]
        # Differences: 0 + 0 + 0 = 0
        self.assertEqual(part1(custom_input), 0)
        
        # Part 2 should multiply each left number by its count in the right list
        # 1 appears once in right list: 1*1 = 1
        # 2 appears once in right list: 2*1 = 2
        # 3 appears once in right list: 3*1 = 3
        # Total: 1 + 2 + 3 = 6
        self.assertEqual(part2(custom_input), 6)


# Run the main program only if not being imported
if __name__ == "__main__":
    # Run unit tests if requested
    if len(sys.argv) > 1 and sys.argv[1] == "--test":
        unittest.main(argv=['first-arg-is-ignored'], exit=False)
        sys.exit(0)
        
    # Run part 1
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

    # Run part 2
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