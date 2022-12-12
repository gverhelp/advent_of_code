with open('input.txt', 'r') as file:
    content = file.read()

def ifoccurs(str : str):
    for a in range(len(str)):
        for b in range(a + 1, len(str)):
            if str[a] == str[b]:
                return False
    return True

if __name__ == "__main__":
    a = 0
    for a in range(len(content)):
        if ifoccurs(content[a:a+14]) == True:
            print(content[a:a+14])
            print(a+14)
            break 