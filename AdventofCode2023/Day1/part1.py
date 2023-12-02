# Day 1: https://adventofcode.com/2023/day/1

puzzleInput = open('input.txt').read().split('\n')

sum = 0
for row in puzzleInput:
    string = ""
    first_digit = 0
    second_digit = 0
    for char in row:
        if (char.isdigit() and first_digit == 0):
            first_digit = int(char)
        elif char.isdigit():
            second_digit = int(char)
    if second_digit == 0:
        second_digit = first_digit
    string += str(first_digit) + str(second_digit)
    sum += int(string)
    print(sum)

print(f"Total Sum = {sum}")
