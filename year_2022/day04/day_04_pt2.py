with open('input.txt', 'r') as file:
    lines = file.readlines()

stacks = [line.replace('\n', '').split(' ') for line in lines[10:19]]
commands = [line.replace('\n', '') for line in lines[20:521]]

for command in commands:
    how_many = int(command[command.find(' ') + 1:command.find(' from')])
    _from = int(command[command.find('from ') + 5:command.find(' to')]) - 1
    _to = int(command[command.rfind('to ') + 3:]) - 1

    stacks[_to].extend(stacks[_from][-how_many:])
    del stacks[_from][-how_many:]

for stack in stacks:
    print(stack[-1][1], end='')