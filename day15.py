import numpy as np
from scipy import sparse
def read_file(file):
    with open('input\\' + file, 'r') as f:
        file = f.readlines()
    sensors = []
    min_x = min_y = max_x = max_y = 0
    for l in file:
        sensor = [int(c[2:]) for c in l[10:l.index(':')].split(', ')]
        beacon = [int(c[2:]) for c in l[l.index('is at '):][6:].split(', ')]
        distance = abs(sensor[0] - beacon[0]) + abs(sensor[1] - beacon[1])
        sensors.append((sensor[0], sensor[1], beacon[0], beacon[1], distance))
        min_x = min(min_x, sensor[0] - distance, beacon[0] - distance)
        max_x = max(max_x, sensor[0] + distance, beacon[0] + distance)
        min_y = min(min_y, sensor[1] - distance, beacon[1] - distance)
        max_y = max(max_y, sensor[1] + distance, beacon[1] + distance)

    # min_x = np.clip([min(s[0], s[2]) - s[4] for s in sensors], None, 0).min()
    # max_x = np.array([max(s[0], s[2]) + s[4] for s in sensors]).max()
    # min_y = np.clip([min(s[1], s[3]) - s[4] for s in sensors], None, 0).min()
    # max_y = np.array([max(s[1], s[3]) + s[4] for s in sensors]).max()

    grid = sparse.lil_matrix((max_y + abs(min_y) + 1, max_x + abs(min_x) + 1), dtype=np.uint8)

    for s in sensors:
        rows = np.array([], dtype=np.int64)
        columns = np.array([], dtype=np.int64)
        # for i in range(-s[4], s[4] + 1):
        #     deviation = (2 * s[4] + 1 - 2 * abs(i)) // 2
        #     deviation = range(s[1] - deviation, s[1] + deviation + 1)
        #     for x in deviation:
        #         rows = np.append(rows, x)
        #         columns = np.append(columns, i + s[0])
        # deviations = [
        #     range(s[1] - ((2 * s[4] + 1 - 2 * abs(i)) // 2), s[1] + ((2 * s[4] + 1 - 2 * abs(i)) // 2) + 1) for i in
        #     range(-s[4], s[4] + 1)]
        # rows = np.concatenate([list(deviation) for deviation in deviations])
        # columns = np.concatenate(
        #     [[i + s[0]] * len(deviation) for i, deviation in zip(range(-s[4], s[4] + 1), deviations)])
        rows, columns = np.meshgrid(
            np.arange(-s[4], s[4] + 1) + s[1],
            np.arange(-s[4], s[4] + 1) + s[0],
            indexing='ij',
            sparse=True
        )
        rows = rows.ravel()
        columns = columns.ravel()
        grid[rows + abs(min_y), columns + abs(min_x)] = 1
        grid[s[3] + abs(min_y), s[2] + abs(min_x)] = 0

    return grid, min_x, min_y

def day15_1(file, y):
    grid, min_x, min_y = read_file(file)
    return len(grid[y + abs(min_y)].nonzero()[0])

def day15_2(file):
    pass


if __name__ == '__main__':
            print(day15_1('day15.txt', 2000000))