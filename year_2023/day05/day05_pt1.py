with open('input.txt', 'r') as file:
    data = file.read().split('\n\n')

seeds = data[0].split(':')[1].split()

maps = [[line.split() for line in data[a].splitlines()[1:]] for a in range(1, 8)]

def from_to(seed, map_number):
    if map_number >= len(maps):
        return seed
 
    map = maps[map_number]

    for dst, src, length in map:
        if int(seed) in range(int(src), int(src) + int(length)):
            operation = int(src) - int(dst)
            new_seed = int(seed) - operation
            return from_to(new_seed, map_number + 1)
    return from_to(seed, map_number + 1)

if __name__ == '__main__':
    res = [from_to(seed, 0) for seed in seeds]

    print(min(res))
