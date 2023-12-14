import math

with open('input.txt', 'r') as file:
    data = file.readlines()

race = [int(data[line].split(':')[1].replace(' ', '').strip()) for line in range(len(data))]

time = race[0]
distance = race[1]
exact_acceleration = (time - math.sqrt((time**2 - 4*distance))) / 2
min_acceleration = int(exact_acceleration + 1)
print(time - 2*min_acceleration + 1)