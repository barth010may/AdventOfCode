# Day 8: https://adventofcode.com/2023/day/8#part2
import re

puzzle_input = open("input.txt").read().splitlines()
example_input = open("example.txt").read().splitlines()

dict = {}
start_list = []
instructions = puzzle_input[0]
current_state = "AAA"
for i in range(2,len(puzzle_input)):
    key = re.search("[0-9]*[A-Z]+", puzzle_input[i].split("=")[0])
    value = tuple(re.findall("[0-9]*[A-Z]+", puzzle_input[i].split("=")[1]))
    if key.group().endswith("A"):
        start_list.append(key.group())
    dict[key.group()] = value

steps = 0
flag = True
while flag:
    for letter in instructions:
        for i in range(len(start_list)):
            if letter == "L":
                values = dict[start_list[i]]
                start_list[i] = values[0]

            elif letter == "R":
                values = dict[start_list[i]]
                start_list[i] = values[1]
        steps += 1
        counter = 0
        for x in start_list:
            if x.endswith("Z"):
                counter += 1
            else:
                break
        if counter == len(start_list):
            flag = False

print(f"steps = {steps}")

