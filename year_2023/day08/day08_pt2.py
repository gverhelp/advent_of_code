from math import lcm

with open('input.txt', 'r') as file:
    data = file.read()

instructions = data.splitlines()[0]
elements = {key: value.removeprefix('(').removesuffix(')').split(', ') for key, value in (line.split(' = ') for line in data.splitlines()[2:])}

nodes = [elem for elem in elements if elem.endswith('A')]

def next(node: str):
    steps = 0
    inst_count = 0
    while not node.endswith('Z'):
        left, right = elements[node]
        node = left if instructions[inst_count] == 'L' else right
        inst_count = (inst_count + 1) % len(instructions)
        steps += 1
    return steps

lcms = [next(node) for node in nodes]
print(lcm(*lcms))


### Brutforce ###

# steps = 0
# inst_count = 0
# while not all(elem.endswith('Z') for elem in node):
#     count_elem = 0
#     while count_elem < len(node):
#         left, right = elements[node[count_elem]]
#         node[count_elem] = left if instructions[inst_count] == 'L' else right
#         count_elem += 1
#     inst_count = (inst_count + 1) % len(instructions)
#     steps += 1
#     print(node)

# print(steps)