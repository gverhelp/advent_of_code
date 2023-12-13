with open('input.txt', 'r') as file:
    data = [line.removesuffix('\n') for line in file.readlines()]

seeds = data[0].split(':')[1].split()

maps = [
    [a.split() for a in data[3:26]],
    [a.split() for a in data[28:59]],
    [a.split() for a in data[61:87]],
    [a.split() for a in data[89:129]],
    [a.split() for a in data[131:173]],
    [a.split() for a in data[175:210]],
    [a.split() for a in data[212:249]]
]

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
    res = []

    for seed in seeds:
        res.append(from_to(seed, 0))

    print(min(res))
