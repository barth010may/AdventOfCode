# Day 9: https://adventofcode.com/2023/day/9

puzzle_input = open("input.txt").read().splitlines()
example_input = open("example.txt").read().splitlines()

def only_zeros(list):
    for x in list:
        if x != 0:
            return False
    return True


sum = 0
for row in puzzle_input:
    map = []
    sequence = [eval(i) for i in row.split(" ")]
    map.append(sequence.copy())
    while not only_zeros(sequence):
        for i in range(len(sequence) - 1):
            diff = int(sequence[i+1]) - int(sequence[i])
            sequence[i] = diff
        sequence.pop(len(sequence) - 1)
        map.append(sequence.copy())
    print(map)

    for i in reversed(range(0, len(map))):
        first = map[i][0]
        map[i - 1] = [map[i - 1][0] - first] + map[i-1]
    sum += map[0][0]

print(f"Total sum = {sum}")