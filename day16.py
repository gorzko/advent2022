import numpy as np
from functools import cache

Distances = np.empty_like
Valves = dict()
Mapping = dict()

def read_file(file):
    with open('input\\' + file, 'r') as f:
        valves = f.readlines()
    valves = [(v[1], int(v[4].split('=')[1].strip(';')), [t.strip(',') for t in v[9:]]) for v in [v.split() for v in valves]]
    global Valves
    Valves = {v[0]: v[1] for v in valves}
    global Mapping
    Mapping = {key: value for key, value in [(v[0], i) for i, v in enumerate(valves)]}
    grid = np.zeros((len(Mapping), len(Mapping)), dtype=np.int8)
    global Distances
    Distances = grid.copy()
    for v in valves:
        i = Mapping[v[0]]
        for t in v[2]:
            j = Mapping[t]
            grid[i, j] = 1

    n = 1
    n_grid = grid.copy()

    while n < n_grid.shape[0]:
        connections = np.where(n_grid > 0)
        for i, j in zip(connections[0], connections[1]):
            if i != j and Distances[i, j] == 0:
                Distances[i, j] = n
        n_grid = np.matmul(n_grid, grid)
        n += 1


# Inspired by this solution: https://www.reddit.com/r/adventofcode/comments/zn6k1l/comment/j0fti6c/?context=3
@cache
def solve(minutes, valves, current='AA'):

    return max([Valves[v] * (minutes - Distances[Mapping[current], Mapping[v]] - 1) +
                solve(
                    minutes - Distances[Mapping[current], Mapping[v]] - 1,
                    valves - {current},
                    v)
                for v in valves if v != current and Distances[Mapping[current], Mapping[v]] < minutes],
               default=0)


def day16_1(file):
    read_file(file)
    minutes = 30

    return solve(minutes, frozenset(v for v in Valves if Valves[v]))


def day16_2(file):
    pass


if __name__ == '__main__':
    print(day16_1('day16.txt'))