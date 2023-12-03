# DAY 3: https://adventofcode.com/2023/day/3
import re

puzzleInput = open('input.txt').read().split('\n')

rows, cols = (len(puzzleInput), len(puzzleInput[0]))

sum = 0

# loops through each row of the input
for j in range(rows):
    # For each row it finds the symbols and saves them in a list of Match Objects
    symbols = re.finditer("[^.0-9]", puzzleInput[j])

    # Check for horizontal adjacent
    for symbol in symbols:
        span = symbol.span()

        # Check for left horizontal
        left = puzzleInput[j][span[0] - 1]
        if left.isdigit():
            left_instance = re.search("[0-9]+", puzzleInput[j][span[0] - 3:span[0]])
            sum += int(left_instance.group())

        # Check for right horizontal
        right = puzzleInput[j][span[0] + 1]
        if right.isdigit():
            right_instance = re.search("[0-9]+", puzzleInput[j][span[0]:span[1] + 3])
            sum += int(right_instance.group())

        # Check for up vertical
        up = puzzleInput[j-1][span[0]]
        up_left = puzzleInput[j-1][span[0] - 1]
        up_right = puzzleInput[j-1][span[0] + 1]
        if up.isdigit():
            up_instance_right = re.search("[0-9]+", puzzleInput[j-1][span[0]:span[1] + 3])
            up_instance_left = re.findall("[0-9]+", puzzleInput[j-1][span[0] - 3:span[1]])
            up_instance_left.reverse()
            up_instance_middle = re.findall("[0-9]+", puzzleInput[j-1][span[0] - 1:span[1]+1])
            number = int(up_instance_right.group()) if int(up_instance_right.group()) > int(up_instance_left[0]) else int(up_instance_left[0])
            number = number if number > int(up_instance_middle[0]) else int(up_instance_middle[0])
            sum += number
        # Check for up diagonal left
        elif up_left.isdigit() or up_right.isdigit():
            if up_left.isdigit():
                left_instance = re.search("[0-9]+", puzzleInput[j-1][span[0] - 3:span[0]])
                sum += int(left_instance.group())
            if up_right.isdigit():
                right_instance = re.search("[0-9]+", puzzleInput[j-1][span[0]:span[1] + 3])
                sum += int(right_instance.group())

        # Check for down vertical
        down = puzzleInput[j + 1][span[0]]
        down_left = puzzleInput[j + 1][span[0] - 1]
        down_right = puzzleInput[j + 1][span[0] + 1]
        if down.isdigit():
            down_instance_right = re.search("[0-9]+", puzzleInput[j+1][span[0]:span[1] + 3])
            down_instance_left = re.findall("[0-9]+", puzzleInput[j+1][span[0] - 3:span[1]])
            down_instance_left.reverse()
            down_instance_middle = re.findall("[0-9]+", puzzleInput[j+1][span[0] - 1:span[1]+1])
            number = int(down_instance_right.group()) if int(down_instance_right.group()) > int(down_instance_left[0]) else int(down_instance_left[0])
            number = number if number > int(down_instance_middle[0]) else int(down_instance_middle[0])
            print(number)
            sum += number
            # Check for up diagonal left
        elif down_left.isdigit() or down_right.isdigit():
            if down_left.isdigit():
                left_instance = re.search("[0-9]+", puzzleInput[j + 1][span[0] - 3:span[0]])
                sum += int(left_instance.group())
            if down_right.isdigit():
                right_instance = re.search("[0-9]+", puzzleInput[j + 1][span[0]:span[1] + 3])
                sum += int(right_instance.group())

print(f"Total Sum = {sum}")

