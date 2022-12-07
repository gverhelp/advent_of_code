with open('input.txt', 'r') as file:
    lines = file.readlines()

level = 0

for line in lines:
    if line[0] == '$':
        if line[2:4] == 'cd':
            if line[5:7] == '..':
                print('cd ..')
                level -= 1
            elif line[5:6] == '/':
                print('cd /')
                level = 0
            else:
                print('cd', line[5:], end='')
                level += 1
            print(level)
        elif line[2:4] == 'ls':
            pass
    elif line[0:3] == 'dir':
        print(line, end='')
    else:
        size_of_file = line[:line.find(' ')]
        print(size_of_file)

