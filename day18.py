from functools import cache
import operator

def read_file(file):
    with open('input\\' + file, 'r') as f:
        return frozenset(tuple(int(d) for d in l.split(',')) for l in f.readlines())


@cache
def is_offset_one(a, b):
    return abs(a - b) == 1

@cache
def is_adjacent(p):
    return len([i for i in map(operator.eq, p[0], p[1]) if i]) == 2 \
and len([i for i in map(is_offset_one, p[0], p[1]) if i]) == 1


def count_adjacent(p, cubes):
    return len([i for c in cubes if (i := is_adjacent(tuple(sorted([p, c]))))])


def day18(file, part2=False):
    cubes = read_file(file)

    deduct = 0
    if part2:
        for i in range(3):
            for j in range(3):
                for k in range(6):
                    if not (i, j, k) in cubes and count_adjacent((i, j, k), cubes) == 6:
                        print(i, j, k)
                        deduct += 6

    return len(cubes) * 6 - sum([count_adjacent(c, cubes) for c in cubes]) - deduct


if __name__ == '__main__':
    print(day18('day18.txt', True))
