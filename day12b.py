# Uses A* algorithm and is much faster than my first approach

import numpy as np


def read_file(file, part=1):
    with open('input\\' + file, 'r') as f:
        grid = np.array([list(l.strip()) for l in f.readlines()])
        start = np.where(grid == 'S')
        grid[np.where(grid == 'S')] = 'a'
        if part == 2:
            start = np.where(grid == 'a')
        end = np.where(grid == 'E')
        grid[np.where(grid == 'E')] = 'z'
    return grid, start, end


def get_taxicab_distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] + b[1])


def get_neighbours(grid, node):
    neighbours = []
    if node[0] > 0:
        neighbours.append((node[0] - 1, node[1]))
    if node[0] < grid.shape[0] - 1:
        neighbours.append((node[0] + 1, node[1]))
    if node[1] > 0:
        neighbours.append((node[0], node[1] - 1))
    if node[1] < grid.shape[1] - 1:
        neighbours.append((node[0], node[1] + 1))
    return neighbours


def is_traversable(fr, to, grid):
    fr = ord(grid[fr[0], fr[1]])
    to = ord(grid[to[0], to[1]])
    return fr >= to or to - fr == 1


def find_path(grid, start, end):
    end = (end[0][0], end[1][0])
    open_nodes = []
    closed_nodes = []
    parents = dict()
    costs = dict()

    for s in [(i, j) for i, j in zip(start[0], start[1])]:
        open_nodes.append(s)
        parents[s] = None
        costs[s] = (0, get_taxicab_distance(s, end))

    while open_nodes:
        min_f = min([sum(costs[n]) for n in open_nodes])
        min_g = min([costs[n][0] for n in open_nodes if sum(costs[n]) == min_f])
        current = [n for n in open_nodes if sum(costs[n]) == min_f and costs[n][0] == min_g][0]
        open_nodes.remove(current)
        closed_nodes.append(current)

        if current == end:
            return costs[current][0]

        for node in get_neighbours(grid, current):
            if not is_traversable(current, node, grid) or node in closed_nodes:
                continue

            potential_cost = (costs[current][0] + 1, get_taxicab_distance(node, end))
            if node not in open_nodes or sum(costs[node]) > sum(potential_cost):
                costs[node] = potential_cost
                parents[node] = current
                if node not in open_nodes:
                    open_nodes.append(node)

def day12(file, part):
    grid, start, end = read_file(file, part)
    return find_path(grid, start, end)


if __name__ == '__main__':
    print(day12('day12.txt', 2))
