with open('input.txt', 'r') as file:
    data = file.read()

instructions = data.splitlines()[0]
elements = {key: value.removeprefix('(').removesuffix(')').split(', ') for key, value in (line.split(' = ') for line in data.splitlines()[2:])}

where_to_go = 'AAA'
steps = 0
inst_count = 0

while where_to_go != 'ZZZ':
    left, right = elements[where_to_go]
    where_to_go = left if instructions[inst_count] == 'L' else right
    steps += 1
    inst_count = (inst_count + 1) % len(instructions)

print(steps)

# while inst_count < len(instructions):
#     actual_element = elements[where_to_go]

#     if instructions[inst_count] == 'L':
#         where_to_go = actual_element[0]
#     elif instructions[inst_count] == 'R':
#         where_to_go = actual_element[1]
#     steps += 1
#     if where_to_go == 'ZZZ':
#         break
#     if inst_count == len(instructions) - 1:
#         inst_count = 0
#     else:
#         inst_count += 1