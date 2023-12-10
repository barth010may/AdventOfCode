
# DAY 10: https://adventofcode.com/2023/day/10

#puzzle_input = open("input.txt").read().splitlines()
#example_input = open("example.txt").read().splitlines()
matrix = open("input.txt").read().splitlines()


WIDTH = len(matrix[0])
LENGTH = len(matrix)
class Node:
    def __init__(self, type, index):
        self.type = type
        self.index = index

    def copy(self):
        # Create a new Node instance with the same type and index
        return Node(self.type, self.index)

def get_node_type(i, j):
    return matrix[i][j]

def get_next_path(previous_node, node):
    next_node = None
    if node.type == "-":
        i = node.index[0]
        j = node.index[1]
        if previous_node.type == "F" or previous_node.type == "L":
            next_node = Node(get_node_type(i, j + 1), (i, j + 1))
        elif previous_node.type == "7" or previous_node.type == "J":
            next_node = Node(get_node_type(i, j - 1), (i, j - 1))
        elif (previous_node.type == "-" or previous_node.type == "S") and node.index[1] - previous_node.index[1] == -1:
            next_node = Node(get_node_type(i, j - 1), (i, j - 1))
        elif (previous_node.type == "-" or previous_node.type == "S") and node.index[1] - previous_node.index[1] == 1:
            next_node = Node(get_node_type(i, j + 1), (i, j + 1))

    elif node.type == "|":
        i = node.index[0]
        j = node.index[1]
        if previous_node.type == "F" or previous_node.type == "7":
            next_node = Node(get_node_type(i + 1, j), (i + 1, j))
        elif previous_node.type == "L" or previous_node.type == "J":
            next_node = Node(get_node_type((i - 1), j), (i - 1, j))
        elif (previous_node.type == "|" or previous_node.type == "S") and node.index[0] - previous_node.index[0] == 1:
            next_node = Node(get_node_type(i + 1, j), (i + 1, j))
        elif (previous_node.type == "|" or previous_node.type == "S") and node.index[0] - previous_node.index[0] == -1:
            next_node = Node(get_node_type((i - 1), j), (i - 1, j))

    elif node.type == "L":
        i = node.index[0]
        j = node.index[1]
        if node.index[1] - previous_node.index[1] == -1:
           next_node = Node(get_node_type(i - 1, j), (i - 1, j))
        elif node.index[0] - previous_node.index[0] == 1:
            next_node = Node(get_node_type(i, j + 1), (i, j + 1))

    elif node.type == "J":
        i = node.index[0]
        j = node.index[1]
        if node.index[1] - previous_node.index[1] == 1:
            next_node = Node(get_node_type(i - 1, j), (i - 1, j))
        elif node.index[0] - previous_node.index[0] == 1:
            next_node = Node(get_node_type(i, j - 1), (i, j - 1))

    elif node.type == "7":
        i = node.index[0]
        j = node.index[1]
        if node.index[1] - previous_node.index[1] == 1:
            next_node = Node(get_node_type(i + 1, j), (i + 1, j))
        elif node.index[0] - previous_node.index[0] == -1:
            next_node = Node(get_node_type(i, j - 1), (i, j - 1))

    elif node.type == "F":
        i = node.index[0]
        j = node.index[1]
        if node.index[1] - previous_node.index[1] == -1:
            next_node = Node(get_node_type(i + 1, j), (i + 1, j))
        elif node.index[0] - previous_node.index[0] == -1:
            next_node = Node(get_node_type(i, j + 1), (i, j + 1))

    return next_node

def find_starting_paths(node):
    north = matrix[node.index[0] - 1][node.index[1]]
    south = matrix[node.index[0] + 1][node.index[1]]
    east = matrix[node.index[0]][node.index[1] + 1]
    west = matrix[node.index[0]][node.index[1] - 1]
    paths = []
    if north == "|" or north == "7" or north == "F":
        paths.append(Node(north, (node.index[0] - 1, node.index[1])))
    if south == "|" or south == "L" or south == "J":
        paths.append(Node(south, (node.index[0] + 1, node.index[1])))
    if east == "-" or east == "J" or east == "7":
        paths.append(Node(east, (node.index[0],node.index[1] + 1)))
    if west == "-" or west == "L" or west == "F":
        paths.append(Node(west, (node.index[0], node.index[1] - 1)))
    return paths


start = 0
# Find the starting hole
for j in range(LENGTH):
    if "S" in matrix[j]:
        start = (j, matrix[j].index("S"))

starting_node = Node("S", start)
paths = find_starting_paths(starting_node)
path1 = paths[0]
path2 = paths[1]
previous_node1 = starting_node
previous_node2 = starting_node
steps = 0
while path1.index != path2.index:
    new_node1 = get_next_path(previous_node1, path1)
    previous_node1 = path1.copy()
    path1 = new_node1.copy()

    new_node2 = get_next_path(previous_node2, path2)
    previous_node2 = path2.copy()
    path2 = new_node2.copy()
    steps += 1
steps += 1

print(f"total steps furthest away from start = {steps}")