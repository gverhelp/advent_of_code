with open('input.txt', 'r') as file:
    lines = file.readlines()

level = 0
levels = {}
good_files = []

for line in lines:
    if line[0] == '$':
        if line[2:4] == 'cd':
            if line[5:7] == '..':
                print('cd ..')
                if levels[level] <= 100000:
                    good_files.append(levels[level])
                levels[level] = 0
                level -= 1
            elif line[5:6] == '/':
                print('cd /')
                level = 0
                levels[level] = 0
            else:
                print('cd', line[5:], end='')
                level += 1
                levels[level] = 0
            print(level)
        elif line[2:4] == 'ls':
            pass
    elif line[0:3] == 'dir':
        print(line, end='')
    else:
        size_of_file = line[:line.find(' ')]
        for i in range(len(levels)):
            levels[i] = levels[i] + int(size_of_file)

print(sum(good_files))