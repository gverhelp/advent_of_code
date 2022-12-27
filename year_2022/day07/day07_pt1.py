with open('./input.txt', 'r') as file:
    lines = file.readlines()

map = [line.replace('\n', '') for line in lines]

visible_trees = 0

def check_line(char : str, line : str):

for line in map:
    for char in line:
        check_line(char, line)

# print(map)
print(visible_trees)