with open('input.txt', 'r') as file:
    content = file.read()

def ifoccurs(str : str):
    a = 0
    while a < len(str):
        b = a + 1
        while b < len(str):
            if str[a] == str[b]:
                return False
            b += 1
        a += 1
    return True

if __name__ == "__main__":
    a = 0
    while a < len(content):
        if ifoccurs(content[a:a+14]) == True:
            print(content[a:a+14])
            print(a+14)
            break 
        a += 1