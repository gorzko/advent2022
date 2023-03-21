import numpy as np

def read_file(file):
    with open('input\\' + file, 'r') as f:
        valves = f.readlines()
    valves = [(v[1], int(v[4].split('=')[1].strip(';')), [t.strip(',') for t in v[9:]]) for v in [v.split() for v in valves]]
    mapping = {key: value for key, value in[(v[0], i) for i, v in enumerate(valves)]}
    grid = np.zeros((len(mapping), len(mapping)), dtype=np.int8)
    distances = grid.copy()
    for v in valves:
        i = mapping[v[0]]
        for t in v[2]:
            j = mapping[t]
            grid[i, j] = 1

    n = 1
    n_grid = grid.copy()

    while n < n_grid.shape[0]:
        connections = np.where(n_grid > 0)
        for i, j in zip(connections[0], connections[1]):
            if i != j and distances[i, j] == 0:
                distances[i, j] = n
        n_grid = np.matmul(n_grid, grid)
        n += 1

    return valves, mapping, distances

def day16_1(file):
    valves, mapping, distances = read_file(file)
    minutes = 30
    current = valves[0]
    threshold = np.mean([v[1] for v in valves])
    first = [v for v in valves if v[1] > threshold]
    last = [v for v in valves if v not in first and v[1] > 0]
    batch = first.copy()
    pressure = 0

    while minutes > 0:
        if not batch:
            if last:
                batch, last = last.copy(), []
            else:
                minutes = 0
        for x in range(1, len(valves)):
            i = valves.index(current)
            jj = [x for x in np.where(distances[i,] == x)[0].tolist() if valves[x] in batch]
            values = [valves[j][1] for j in jj]
            if values:
                j = jj[values.index(max(values))]
                minutes -= distances[i,j] + 1
                current = valves[j]
                pressure += current[1] * minutes
                batch.remove(current)
                break
    return pressure


def day16_2(file):
    pass


if __name__ == '__main__':
    print(day16_1('day16t.txt'))
