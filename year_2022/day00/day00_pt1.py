with open('input.txt', 'r') as file:
    lines = file.readlines()

bigger_cal_amount = 0
cal = 0

for line in lines:
    if line != '\n':
        cal += int(line)
    else:
        if bigger_cal_amount < cal:
            bigger_cal_amount = cal
        cal = 0

print(bigger_cal_amount)