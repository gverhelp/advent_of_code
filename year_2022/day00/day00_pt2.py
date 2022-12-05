with open('input.txt', 'r') as file:
    lines = file.readlines()

bigger_cal_amount = 0
result = 0
cal = 0
elves_list = []

for line in lines:
    if line != '\n':
        cal += int(line)
    else:
        if bigger_cal_amount < cal:
            bigger_cal_amount = cal
        elves_list.append(cal)
        cal = 0

for i in range(3):
    result += max(elves_list)
    elves_list.remove(max(elves_list))

print(result)