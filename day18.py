from functools import cache
import operator
from collections import deque

def read_file(file):
    with open('input\\' + file, 'r') as f:
        return set(tuple(int(d) for d in l.split(',')) for l in f.readlines())


@cache
def is_offset_one(a, b):
    return abs(a - b) == 1


@cache
def is_adjacent(p):
    return len([i for i in map(operator.eq, p[0], p[1]) if i]) == 2 \
and len([i for i in map(is_offset_one, p[0], p[1]) if i]) == 1


def get_neighbours(p, exclusions, boundaries):

    directions = [(-1, lambda x, y: x > 1), (1, lambda x, y: x < y)]

    neighbours = set()
    p = list(p)

    for i in range(3):
        for d in directions:
            if d[1](p[i], boundaries[i]):
                x = p.copy()
                x[i] += d[0]
                x = tuple(x)
                if not x in exclusions:
                    neighbours.add(x)

    return neighbours


def count_adjacent(p, cubes):
    return len([i for c in cubes if (i := is_adjacent(tuple(sorted([p, c]))))])


def day18(file, part2=False):
    cubes = read_file(file)

    deduct = 0
    if part2:
        boundaries = (3, 3, 6)

        queue = {(1, 1, 1)}
        outside = queue.copy()

        while queue:
            p = queue.pop()
            neighbours = get_neighbours(p, cubes | outside, boundaries)
            outside.update(neighbours)
            queue.update(neighbours)

        grid = set()

        for i in range(boundaries[0]):
            for j in range(boundaries[1]):
                for k in range(boundaries[2]):
                    grid.add((i + 1, j + 1, k + 1))

        for p in (p for p in grid if not p in cubes and not p in outside):
            deduct += count_adjacent(p, cubes)

    return len(cubes) * 6 - sum([count_adjacent(c, cubes) for c in cubes]) - deduct


if __name__ == '__main__':
    print(day18('day18t.txt', True))
