with open('input.txt', 'r') as file:
    lines = file.readlines()

result = 0

possibilities = {
    'A Y\n' : 8, #win
    'A X\n' : 4, #even
    'A Z\n' : 3, #loss
    'B Z\n' : 9, #win
    'B Y\n' : 5, #even
    'B X\n' : 1, #loss
    'C X\n' : 7, #win
    'C Z\n' : 6, #even
    'C Y\n' : 2  #loss
}

for line in lines:
    for cond in possibilities:
        if cond == line:
            result += possibilities[cond]
print(result)

