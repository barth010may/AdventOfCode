# DAY 2: Part 2, find the minimum set of colors for each game and sum the power of those numbers
import operator as op

puzzleInput = open('input.txt').read().split('\n')
sum = 0
for row in puzzleInput:
    green_max = 1
    blue_max = 1
    red_max = 1

    key = row.split(" ")
    for x in range(0, len(key)):
        if key[x].isdigit():
            if op.contains(key[x + 1], 'green'):
                num = int(key[x])
                green_max = num if num > green_max else green_max
            elif op.contains(key[x + 1], 'blue'):
                num = int(key[x])
                blue_max = num if num > blue_max else blue_max
            elif op.contains(key[x + 1], 'red'):
                num = int(key[x])
                red_max = num if num > red_max else red_max
            else:
                raise Exception('No color was found!! bad')
    power = green_max * blue_max * red_max
    sum += power

print(f"Total sum = {sum}")
