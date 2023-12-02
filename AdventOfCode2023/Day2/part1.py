# DAY 2: PART 1, determine which games are possible with 12 red, 13 green and 14 blue cubes.

import operator as op

puzzleInput = open('input.txt').read().split('\n')

RED_MAX = 12
BLUE_MAX = 14
GREEN_MAX = 13

sum = 0
for row in puzzleInput:
    flag = False
    key = row.split(" ")
    for x in range(0, len(key)):
        if key[x].isdigit():
            if op.contains(key[x+1], 'green'):
                if int(key[x]) > GREEN_MAX:
                    flag = True
            elif op.contains(key[x+1], 'blue'):
                if int(key[x]) > BLUE_MAX:
                    flag = True
            elif op.contains(key[x+1], 'red'):
                if int(key[x]) > RED_MAX:
                    flag = True
            else:
                raise Exception('No color was found!! bad')
    if not flag:
        number = int(key[1].split(':')[0])
        sum += int(number)

print(f"Sum total = {sum}")




