# --- Day 11: Cosmic Expansion --- : https://adventofcode.com/2023/day/11#part2
# potential solution is to use A* algorithm instead of bfs, as its generally more efficient.
# Current problem is that im not sure if the 1 mil cols and rows are added correctly, and if the A* algo works.
# Currently even sample input is taking way too long to compute

import re
import heapq

puzzle =  open("C:/Users/Borup/Personal/AdventOfCode/AdventOfCode2023/Day11/example.txt").read().splitlines()

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
        for k in range(1000000):
            expanded_rows.append(puzzle[i])
    else:
        expanded_rows.append(puzzle[i])

# Ugly ass method of finding the amount of rows that need expanding
counter = 0
for j in range(WIDTH):
    if column_contains_only(expanded_rows, j, "."):
        counter += 1

expanded_input = ["" for j in range(WIDTH + (counter - 1) * 1000000)]


for j in range(WIDTH):
    if column_contains_only(expanded_rows, j, "."):
        for k in range(1000000):
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

class Node:
    def __init__(self, position, parent=None, g=0, h=0):
        self.position = position
        self.parent = parent
        self.g = g
        self.h = h
        self.f = g + h

    def __lt__(self, other):
        return self.f < other.f

def heuristic(a, b):
    return abs(b[0] - a[0]) + abs(b[1] - a[1])  # Manhattan distance

def astar(matrix, start, end):
    rows, cols = len(matrix), len(matrix[0])
    start_node = Node(start, None, 0, heuristic(start, end))
    end_node = Node(end, None)

    open_list = []
    heapq.heappush(open_list, start_node)
    closed_list = set()

    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Right, Down, Left, Up

    while open_list:
        current_node = heapq.heappop(open_list)
        closed_list.add(current_node.position)

        if current_node.position == end_node.position:
            path = []
            while current_node is not None:
                path.append(current_node.position)
                current_node = current_node.parent
            return len(path) - 1  # Return reversed path

        (x, y) = current_node.position
        for dx, dy in directions:
            next_position = (x + dx, y + dy)
            if 0 <= next_position[0] < rows and 0 <= next_position[1] < cols:
                neighbor = Node(next_position, current_node, current_node.g + 1, heuristic(next_position, end))

                if next_position in closed_list:
                    continue

                if neighbor not in open_list or current_node.g + 1 < neighbor.g:
                    heapq.heappush(open_list, neighbor)

    return None  # Path not found

# Example usage
matrix = [
    [1, 1, 1, 1],
    [1, 1, 1, 1],
    [1, 1, 1, 1]
]
start_point = (0, 0)
end_point = (2, 3)

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
    sum += astar(expanded_input, pair[0].index, pair[1].index)

print(f"Total sum of shortest distances = {sum}")
