with open('input.txt', 'r') as file:
    cards  = file.readlines()

scratchcards_count = {a : 1 for a in range(1, 204)}

for card_count, card in enumerate(cards, start=1):
    matching_numbers = []
    winning_numbers, tirages = [part.split() for part in card.split(':')[1].split(' | ')]

    for a in range(len(tirages)):
        if tirages[a] in winning_numbers:
            matching_numbers.append(tirages[a])

    for _ in range(scratchcards_count[card_count]):
        for a in range(1, len(matching_numbers) + 1):
            scratchcards_count[card_count + a] += 1


print(sum(scratchcards_count.values()))



# with open('input.txt', 'r') as file:
#     cards = file.readlines()

# scratchcards_count = {a: 1 for a in range(1, 204)}

# for card_count, card in enumerate(cards, start=1):
#     matching_numbers = [num for num in card.split(': ')[1].split(' | ')[1].split() if num in card.split(': ')[1].split(' | ')[0].split()]

#     for _ in range(scratchcards_count[card_count]):
#         scratchcards_count.update({card_count + a: scratchcards_count.get(card_count + a, 0) + 1 for a in range(1, len(matching_numbers) + 1)})

# print(sum(scratchcards_count.values()))
