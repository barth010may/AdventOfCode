# Day 1: https://adventofcode.com/2023/day/1

puzzleInput = open('input.txt').read().split(' ')

# TODO: FIx this shit xD
sum = 0
for row in puzzleInput:
    first_digit = 0
    second_digit = 0
    for char in row:
        if (char.isdigit() and first_digit == 0):
            first_digit = int(char)
        elif char.isdigit():
            second_digit = int(char)
        print(first_digit, second_digit)
    sum += first_digit + second_digit
    print(sum)     
    
print(f"Total Sum = {sum}")            
