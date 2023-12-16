with open('input.txt', 'r') as file:
    data = file.read()

groups = data.split(',')

boxes = [{} for _ in range(0, 256)]

for group in groups:
    res = 0
    for char in group:
        if char == '=':
            boxes[res][group[:group.find('=')]] = group[group.find('=') + 1:]
            break
        if char == '-':
            for box in boxes:
                for gr in box:
                    if group[:group.find('=')] == gr:
                        boxes[res].pop(gr)
                        break
        res = ((res+ord(char))*17)&0xFF

result = 0
for box_count in range(len(boxes)):
    if len(boxes[box_count]) > 0:
        for group_count, group in enumerate(boxes[box_count]):
            result += (box_count + 1) * (group_count + 1) * int(boxes[box_count][group])

print(result)
