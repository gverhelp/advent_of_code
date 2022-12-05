with open('input.txt', 'r') as file:
    lines = file.readlines()

result = 0

possibilities = {
    'A Y\n' : 4, # even
    'A X\n' : 3, # loss
    'A Z\n' : 8, # win
    'B Z\n' : 9, # win
    'B Y\n' : 5, # even
    'B X\n' : 1, # loss
    'C X\n' : 2, # loss
    'C Z\n' : 7, # win
    'C Y\n' : 6  # even
}

for line in lines:
    for cond in possibilities:
        if cond == line:
            result += possibilities[cond]
print(result)