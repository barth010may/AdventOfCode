# --- Day 11: Cosmic Expansion --- : https://adventofcode.com/2023/day/11
import re

puzzle =  open("C:/Users/Borup/Personal/AdventOfCode/AdventOfCode2023/Day11/input.txt").read().splitlines()

LENGTH = len(puzzle)
WIDTH = len(puzzle[0])

def string_contains_only(s, char):
    return all(c == char for c in s)

def column_contains_only(array, col_index, char):
    for row in array:
        if row[col_index] != char:
            return False
    return True

expanded_rows = []
for i in range(len(puzzle)):
    if string_contains_only(puzzle[i], "."):
        expanded_rows.append(puzzle[i])
        expanded_rows.append(puzzle[i])
    else:
        expanded_rows.append(puzzle[i])

# Ugly ass method of finding the amount of rows that need expanding
counter = 0
for j in range(WIDTH):
    if column_contains_only(expanded_rows, j, "."):
        counter += 1

expanded_input = ["" for j in range(WIDTH + counter - 1)]


for j in range(WIDTH):
    if column_contains_only(expanded_rows, j, "."):
        for i in range(len(expanded_rows)):
            expanded_input[i] += "."
        for i in range(len(expanded_rows)):
            expanded_input[i] += "."
    else:
        for i in range(len(expanded_rows)):
            expanded_input[i] += expanded_rows[i][j]


galaxies = []
for j in range(len(expanded_input)):
    matches = re.finditer("#", expanded_input[j])
    for m in matches:
        galaxies.append((j, m.start()))

from collections import deque

# Got some help from chatGPT to create this path finding algorithm
def bfs(matrix, start, end):
    rows, cols = len(matrix), len(matrix[0])
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]  # Down, Up, Right, Left
    queue = deque([(start, 0)])  # (position, distance)
    visited = set([start])

    while queue:
        (x, y), distance = queue.popleft()
        if (x, y) == end:
            return distance

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and (nx, ny) not in visited:
                visited.add((nx, ny))
                queue.append(((nx, ny), distance + 1))

    return -1  # if no path is found

# Example usage
matrix = [
    [1, 1, 1, 1],
    [1, 1, 1, 1],
    [1, 1, 1, 1]
]
start_point = (0, 0)  # Starting at top-left corner
end_point = (2, 3)    # Target is bottom-right corner

#galaxies = [(0, 4),(1, 9),(2, 0), (5, 8), (6, 1), (7, 12), (10, 9), (11, 0), (11, 5)]
class Galaxy:
    def __init__(self, number, index):
        self.number = number
        self.index = index

for j in range(len(galaxies)):
    galaxies[j] = Galaxy(j, galaxies[j])
    #print(galaxies[j].index)

pairs = []
seen_pairs = set()  # Set to keep track of pairs already added

# Iterate through the galaxies to form pairs
for i in range(len(galaxies)):
    for j in range(len(galaxies)):
        if i != j:
            # Create a sorted tuple of galaxy numbers to check for uniqueness
            pair_numbers = tuple(sorted([galaxies[i].number, galaxies[j].number]))

            if pair_numbers not in seen_pairs:
                seen_pairs.add(pair_numbers)
                pairs.append((galaxies[i], galaxies[j]))

sum = 0
for pair in pairs:
    sum += bfs(expanded_input, pair[0].index, pair[1].index)

print(f"Total sum of shortest distances = {sum}")
