with open("input.txt", 'r') as file:
    lines = file.readlines()

calibration_values = []

for line in lines:
    numbers = ''.join(value for value in line if value.isdigit())
    calibration_values.append((int(numbers[::len(numbers)-1])) if (len(numbers)-1 != 0) else (int(numbers + numbers)))

print(sum(calibration_values))