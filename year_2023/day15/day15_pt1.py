with open('input.txt', 'r') as file:
    data = file.read()

groups = data.split(',')
total = 0

for group in groups:
    res = 0
    for char in group:
        res = ((res+ord(char))*17)&0xFF
    total += res

print(total)