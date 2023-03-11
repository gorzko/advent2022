import numpy as np
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

        grid = np.zeros((max_y + abs(min_y) + 1, max_x + abs(min_x) + 1), dtype=np.uint8)

        for s in sensors:
            rows = np.array([], dtype=np.int64)
            columns = np.array([], dtype=np.int64)
            for i in range(-s[4], s[4] + 1):
                deviation = (2 * s[4] + 1 - 2 * abs(i)) // 2
                deviation = range(s[1] - deviation, s[1] + deviation + 1)
                for x in deviation:
                    rows = np.append(rows, x)
                    columns = np.append(columns, i + s[0])
            grid[rows + abs(min_y), columns + abs(min_x)] = 1
            grid[s[3] + abs(min_y), s[2] + abs(min_x)] = 0

    return grid, min_x, min_y

def day15_1(file, y):
    grid, min_x, min_y = read_file(file)
    return len(grid[y + abs(min_y)].nonzero()[0])

def day15_2(file):
    pass


if __name__ == '__main__':
            print(read_file('day15t.txt', 10))