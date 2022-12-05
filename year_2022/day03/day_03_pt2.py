with open('input.txt', 'r') as file:
    lines = file.readlines()

count = 0

for line in lines:
    first = int(line[:line.find('-')])
    second = int(line[line.find('-') + 1:line.find(',')])
    third = int(line[line.rfind(',') + 1:line.rfind('-')])
    fourth = int(line[line.rfind('-') + 1:])

    first_part = [a for a in range(first, second + 1)]
    second_part = [b for b in range(third, fourth + 1)]

    occurs = set(first_part).intersection(second_part)
    if occurs:
        count += 1

print(count)