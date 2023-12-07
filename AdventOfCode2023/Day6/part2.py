# DAY 6: https://adventofcode.com/2023/day/6#Part2

import re

puzzle_input = open("input.txt").read().splitlines()

times = re.findall("[\d]+", puzzle_input[0])
distance_records = re.findall("[\d]+", puzzle_input[1])

time = ""
distance_record = ""
for i in range (len(times)):
    time += times[i]
    distance_record += distance_records[i]
    
time = int(time)
distance_record = int(distance_record)
    
print(time, distance_record)

counter = 0
for i in range(int(time)):
    distance = i * (int(time) - i)
    if distance > distance_record:
        counter += 1

print(f"total = {counter}")