from functools import reduce

with open('input.txt', 'r') as file:
    data = file.readlines()

cleaned_data = [data[line].split(':')[1].split() for line in range(len(data))]
races = [(int(time), int(distance)) for time, distance in zip(cleaned_data[0], cleaned_data[1])]

ways_to_win = {a : 0 for a in range(len(races))}

def calculate_ways_to_win(race_count: int, race: tuple):
    for time in range(race[0]):
        count = 0
        for _ in range(time, race[0]):
            count += time
        if count > race[1]:
            ways_to_win[race_count] += 1

if __name__ == '__main__':
    [calculate_ways_to_win(race_count, race) for race_count, race in enumerate(races)]

    print(reduce(lambda x, y: x * y, ways_to_win.values(), 1))
