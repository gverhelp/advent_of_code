with open('input.txt', 'r') as file:
    lines = file.readlines()

stacks = [line.replace('\n', '').split(' ') for line in lines[10:19]]
commands = [line.replace('\n', '') for line in lines[20:521]]

for command in commands:
    how_many = int(command[command.find(' ') + 1:command.find(' from')])
    _from = int(command[command.find('from ') + 5:command.find(' to')]) - 1
    _to = int(command[command.rfind('to ') + 3:]) - 1

    for move in range(how_many):
        stacks[_to].append(stacks[_from][-1])
        del stacks[_from][-1]

for stack in stacks:
    print(stack[-1][1], end='')