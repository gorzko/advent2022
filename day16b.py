import numpy as np
from functools import cache
import timeit

distances = None
mapping = dict()
def read_file(file):
    with open('input\\' + file, 'r') as f:
        valves = f.readlines()
    valves = [(v[1], int(v[4].split('=')[1].strip(';')), [t.strip(',') for t in v[9:]]) for v in [v.split() for v in valves]]
    global mapping
    mapping = {key: value for key, value in[(v[0], i) for i, v in enumerate(valves)]}
    grid = np.zeros((len(mapping), len(mapping)), dtype=np.int8)
    global distances
    distances = grid.copy()
    for v in valves:
        i = mapping[v[0]]
        for t in v[2]:
            j = mapping[t]
            grid[i, j] = 1

    valves = tuple([(v[0], v[1]) for v in valves])

    n = 1
    n_grid = grid.copy()

    while n < n_grid.shape[0]:
        connections = np.where(n_grid > 0)
        for i, j in zip(connections[0], connections[1]):
            if i != j and distances[i, j] == 0:
                distances[i, j] = n
        n_grid = np.matmul(n_grid, grid)
        n += 1

    return valves

@cache
def solve(current, valves, minutes, distance):

    pressure = 0
    batch = tuple((v for v in valves if v != current))

    minutes -= distance + 1
    pressure += current[1] * minutes

    return pressure + max([solve(v, batch, minutes, distances[mapping[current[0]], mapping[v[0]]]) for v in batch], default=0)

def day16_1(file):
    valves = read_file(file)
    minutes = 31
    current = [v for v in valves if v[0] == 'AA'][0]

    return solve(current, tuple((v for v in valves if v[1])), minutes, 0)


def day16_2(file):
    pass


if __name__ == '__main__':
    print(timeit.timeit(stmt="day16_1('day16t.txt')",
                        setup="from __main__ import day16_1",
                        number=10000))
    print(day16_1('day16t.txt'))