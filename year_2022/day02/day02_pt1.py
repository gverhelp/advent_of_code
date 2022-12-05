with open('input.txt', 'r') as file:
    lines = file.readlines()

all_wrong_items = []

def divide(line):
    comp1 = line[:len(line)//2]
    comp2 = line[len(line)//2:]
    for c in comp1:
        for a in comp2:
            if c == a:
                item = c
                if item.isupper() is True:
                    all_wrong_items.append(ord(item) - 38)
                else:
                    all_wrong_items.append(ord(item) - 96)
                return

if __name__ == "__main__":      
    for line in lines:
        divide(line)
    print(sum(all_wrong_items))