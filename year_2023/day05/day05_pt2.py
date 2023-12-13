with open('input.txt', 'r') as file:
    data = file.read().split('\n\n')

seeds = data[0].split(':')[1].split()

maps = [[line.split() for line in data[a].splitlines()[1:]] for a in range(1, 8)]

all_seeds = []

[all_seeds.append(b for b in range(int(seeds[a]), int(seeds[a]) + int(seeds[a + 1]))) for a in range(0, len(seeds), 2)]

def from_to(seed, map_number):
    if map_number >= len(maps):
        return seed
 
    map = maps[map_number]

    for line in map:
        if int(seed) in range(int(line[1]), int(line[1]) + int(line[2])):
            operation = int(line[1]) - int(line[0])
            new_seed = int(seed) - operation
            return from_to(new_seed, map_number + 1)
    return from_to(seed, map_number + 1)

if __name__ == '__main__':
    res = []

    for seed in all_seeds:
        res.append(from_to(seed, 0))

    print(min(res))
