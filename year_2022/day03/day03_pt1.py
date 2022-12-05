with open('input.txt', 'r') as file:
    lines = file.readlines()

count = 0

for line in lines:
    first = int(line[:line.find('-')])
    second = int(line[line.find('-') + 1:line.find(',')])
    third = int(line[line.rfind(',') + 1:line.rfind('-')])
    fourth = int(line[line.rfind('-') + 1:])

    if (first <= third) and (second >= fourth):
        count += 1
    elif (first >= third) and (second <= fourth):
        count += 1
    else:
        pass
    
print(count)