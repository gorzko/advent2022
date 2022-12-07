def get_pairs(file: str):
    pairs = []
    with open('input\\' + file, 'r') as f:
        while True:
            l = f.readline().strip()
            if not l:
                break
            assignements = l.split(',')
            a1 = assignements[0].split('-')
            a1 = (int(a1[0]), int(a1[1]))
            a2 = assignements[1].split('-')
            a2 = (int(a2[0]), int(a2[1]))
            pairs.append((a1, a2))
    return pairs


def contains(a1: tuple[int, int], a2: tuple[int, int]):
    return (a1[0] >= a2[0]) and (a1[1] <= a2[1]) or (a1[0] <= a2[0]) and (a1[1] >= a2[1])


def overlaps(a1: tuple[int, int], a2: tuple[int, int]):
    return a1[0] >= a2[0] and a1[0] <= a2[1] \
        or a1[1] >= a2[0] and a1[1] <= a2[1] \
        or a2[1] >= a1[0] and a2[1] <= a1[1]

def day4_1(file: str):
    contained = 0
    pairs = get_pairs(file)
    for p in pairs:
        if contains(p[0], p[1]):
            contained += 1
    return contained

def day4_2(file: str):
    overlaped = 0
    pairs = get_pairs(file)
    for p in pairs:
        if overlaps(p[0], p[1]):
            overlaped += 1
    return overlaped

if __name__ == "__main__":
    print(day4_2("day4.txt"))