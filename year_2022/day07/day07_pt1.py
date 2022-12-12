with open('./input.txt', 'r') as file:
    lines = file.readlines()

map = [line.replace('\n', '') for line in lines]

visible_trees = 0

def check_col(char : str, col : int, map : list):
    line = 0
    while (line < len(map[line]) - 1):
        if char <= map[line][col]:
            print(char)
            break
        line += 1

for line in range(len(map)):
    if line == 0 or line == len(map) - 1:
        visible_trees += len(map[line]) - 2
    for col in range(len(map[line])):
        if col == 0 or col == len(map[line]) - 1:
            visible_trees += 1
        else:
            check_col(map[line][col], col, map)

# print(map)
print(visible_trees)