with open('input.txt', 'r') as file:
    cards = file.readlines()

points = 0

for card in cards:
    matching_numbers = []
    winning_numbers, tirages = [part.split() for part in card[card.find(':') + 2:].split(' | ')]

    for a in range(len(tirages)):
        if tirages[a] in winning_numbers:
            matching_numbers.append(tirages[a])

    points += 1 * 2 ** (len(matching_numbers) - 1) if len(matching_numbers) > 0 else 0

print(points)



# with open('input.txt', 'r') as file:
#     cards = file.readlines()

# points = sum(
#     1 * 2 ** (len([num for num in tirages.split() if num in winning_numbers.split()]) - 1) for card in cards for winning_numbers, tirages in [card.split(': ')[1].strip().split(' | ')]
# )

# print(points)
