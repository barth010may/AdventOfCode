# Day 8: https://adventofcode.com/2023/day/8
import re

puzzle_input = open("input.txt").read().splitlines()
example_input = open("example.txt").read().splitlines()

dict = {}
instructions = puzzle_input[0]
current_state = "AAA"
for i in range(2,len(puzzle_input)):
    key = re.search("[A-Z]+", puzzle_input[i].split("=")[0])
    value = tuple(re.findall("[A-Z]+", puzzle_input[i].split("=")[1]))
    dict[key.group()] = value

steps = 0
current_value = "AAA"
while current_value != "ZZZ":
    for letter in instructions:
        if letter == "L":
            values = dict[current_value]
            current_value = values[0]
            steps += 1
            if current_value == "ZZZ":
                break
        elif letter == "R":
            values = dict[current_value]
            current_value = values[1]
            steps += 1
            if current_value == "ZZZ":
                break


print(f"Total Sum = {steps}")

