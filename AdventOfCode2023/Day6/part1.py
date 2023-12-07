# DAY 6: https://adventofcode.com/2023/day/6

import re

puzzle_input = open("input.txt").read().splitlines()

times = re.findall("[\d]+", puzzle_input[0])
distance_records = re.findall("[\d]+", puzzle_input[1])

multiplier = 1
for time in times:
    counter = 0
    for i in range(int(time)):
        distance = i * (int(time) - i)
        if distance > int(distance_records[times.index(time)]):
            counter += 1
    multiplier *= counter
    
print(f"the total = {multiplier}")