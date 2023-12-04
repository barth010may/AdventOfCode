# DAY 4: https://adventofcode.com/2023/day/4#part2
import re

puzzleInput = open('input.txt').read().split('\n')

example_input = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11""".split("\n")

sum = 0
dict = {}   
dict_copies = {}    
for row in range(len(puzzleInput)):

    input_halfed = puzzleInput[row].split("|")
    input_halfed2 = input_halfed[0].split(":")
    
    winning_numbers = re.findall("[\d]+", input_halfed2[1])
    current_numbers = re.findall("[\d]+", input_halfed[1])
    
    counter = 0
    for number in current_numbers:
        if number in winning_numbers:
            counter += 1
    dict[f"{row+1}"] = counter
    dict_copies[f"{row+1}"] = 0
    
    #print(f"wins in Card {row+1}: {counter}")
    
def get_amount_of_copies(dict, original):
    if dict[f"{original}"] == 0:
        return 1
    sum = 0
    for i in range(original, original + int(dict[f"{original}"])):
        print(i)
        sum += get_amount_of_copies(dict, i+1)
    return sum + 1

for i in dict:
    sum += get_amount_of_copies(dict, int(i))
    
print(f"total sum = {sum}")
