with open('input.txt', 'r') as file:
    content = file.read()

a = 0
while a < len(content):
    if content[a] != content[a + 1] and content[a] != content[a + 2] and content[a] != content[a + 3] and content[a + 1] != content[a + 2] and content[a + 1] != content[a + 3] and content[a + 2] != content[a + 3]:
        print(content[a] + content[a + 1] + content[a + 2] + content[a + 3])
        break
    a += 1
print(a + 4)