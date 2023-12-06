with open("input.txt", 'r') as file:
    lines = file.readlines()

calibration_values = []

word_digit_pairs = [
    ('twone', '21'),
    ('oneight', '18'),
    ('eightwo', '82'),
    ('one', '1'),
    ('two', '2'),
    ('three', '3'),
    ('four', '4'),
    ('five', '5'),
    ('six', '6'),
    ('seven', '7'),
    ('eight', '8'),
    ('nine', '9')
]

for line in lines:
    for word, digit in word_digit_pairs:
        line = line.replace(word, digit)
    numbers = ''.join(value for value in line if value.isdigit())
    calibration_values.append((int(numbers[::len(numbers)-1])) if (len(numbers)-1 != 0) else (int(numbers + numbers)))

print(sum(calibration_values))