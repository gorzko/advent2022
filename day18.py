from functools import cache
import operator

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

    directions = [(-1, lambda x, y: x > -1), (1, lambda x, y: x < y)]

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

    if not part2:
        return sum([6 - count_adjacent(c, cubes) for c in cubes])

    # Own solution with modifications inspired by https://www.reddit.com/r/adventofcode/comments/zoqhvy/comment/j0oul0u

    if part2:

        boundaries = [0, 0, 0]

        for i in range(3):
            boundaries[i] = max([x[i] for x in cubes]) + 1

        boundaries = tuple(boundaries)

        queue = {(0, 0, 0)}
        outside = queue.copy()

        while queue:
            p = queue.pop()
            neighbours = get_neighbours(p, cubes | outside, boundaries)
            outside.update(neighbours)
            queue.update(neighbours)

        return sum([(n in outside) for c in cubes for n in get_neighbours(c, cubes, boundaries)])


if __name__ == '__main__':
    print(day18('day18.txt', True))
