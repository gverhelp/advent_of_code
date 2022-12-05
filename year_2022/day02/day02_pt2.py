with open('input.txt', 'r') as file:
    lines = file.readlines()

badges = []

def find_occurs(group):
    for a in group[0]:
        for b in group[1]:
            for c in group[2]:
                if a != '\n' and a == b == c:
                    if a.isupper() is True:
                        badges.append(ord(a) - 38)
                    else:
                        badges.append(ord(a) - 96)
                    return
            

if __name__ == "__main__":
    group = []
    for line in lines:
        group.append(line)
        if len(group) == 3:
            find_occurs(group)
            group = []
    print(sum(badges))