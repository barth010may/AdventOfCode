# DAY 4: https://adventofcode.com/2023/day/4

import re

puzzleInput = open('input.txt').read().split('\n')
sum = 0
for row in puzzleInput:
    input_halfed = row.split("|")
    input_halfed2 = input_halfed[0].split(":")
    
    winning_numbers = re.findall("[\d]+", input_halfed2[1])
    current_numbers = re.findall("[\d]+", input_halfed[1])
    
    flag = True
    counter = 0
    for number in current_numbers:
        if number in winning_numbers:
            if flag:
                counter += 1
                flag = False
            else:
                counter *= 2
            print(sum)
    sum += counter
    
print(f"total sum = {sum}")