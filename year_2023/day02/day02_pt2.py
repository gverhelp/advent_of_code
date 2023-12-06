with open('input.txt', 'r') as file:
    lines = file.readlines()

def game(line : str):
    greatest_number = {
        'green': 0,
        'red': 0,
        'blue': 0
    }

    turns = [a for a in line[line.find(':')+2:].split('; ')]
    for turn in turns:
        draws = [a.removesuffix('\n') for a in turn.split(', ')]
        for draw in draws:
            if int(draw[:2]) > greatest_number[draw[draw.find(' ')+1:]]:
                greatest_number[draw[draw.find(' ')+1:]] = int(draw[:2])
                
    return greatest_number.get('green') * greatest_number.get('red') * greatest_number.get('blue')

powers = []

for line in lines:
    powers.append(game(line))

print(sum(powers))