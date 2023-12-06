# 12 red cubes, 13 green cubes, and 14 blue cubes
with open('input.txt', 'r') as file:
    lines = file.readlines()

loaded_cubes = [
    ('red', 12),
    ('green', 13),
    ('blue', 14)
]

games_count = 0
good_games_list = []

for line in lines:
    games_count += 1
    bad_game = 0
    turns = [a for a in line[line.find(':')+2:].split('; ')]
    for turn in turns:
        draws = [a.removesuffix('\n') for a in turn.split(', ')]
        for draw in draws:
            for color, number in loaded_cubes:
                if color == draw[draw.find(color):]:
                    if int(draw[:draw.find(color)-1]) > number:
                        bad_game = 1
    if not bad_game:
       good_games_list.append(games_count)

print(sum(good_games_list))



