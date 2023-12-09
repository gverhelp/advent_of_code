with open('input.txt', 'r') as file:
    cards  = file.readlines()

points = 0

for card in cards:
    matching_numbers = []
    winning_numbers, tirages = card[card.find(':') + 2:].split(' | ')
    tirages_list = [a for a in tirages.split()]
    winning_numbers_list = [a for a in winning_numbers.split()]

    for a in range(len(tirages_list)):
        if tirages_list[a] in winning_numbers_list:
            matching_numbers.append(tirages_list[a])

    t_n = 0
    for a in range(1, len(matching_numbers) + 1):
        t_n = 1 * 2 ** (len(matching_numbers) - 1)

    points += t_n

print(points)



# with open('input.txt', 'r') as file:
#     cards = file.readlines()

# points = sum(
#     1 * 2 ** (len([num for num in tirages.split() if num in winning_numbers.split()]) - 1) for card in cards for winning_numbers, tirages in [card.split(': ')[1].strip().split(' | ')]
# )

# print(points)