import numpy as np
def read_file(file):
    with open('input\\' + file, 'r') as f:
        file = f.readlines()
        sensors = []
        min_x = min_y = max_x = max_y = 0
        for l in file:
            sensor = [int(c[2:]) for c in l[10:l.index(':')].split(', ')]
            sensor = sensor[0], sensor[1]
            beacon = [int(c[2:]) for c in l[l.index('is at '):][6:].split(', ')]
            beacon = beacon[0], beacon[1]
            sensors.append((sensor, beacon))
            min_x = min(min_x, sensor[0], beacon[0])
            max_x = max(max_x, sensor[0], beacon[0])
            min_y = min(min_y, sensor[1], beacon[1])
            max_y = max(max_y, sensor[1], beacon[1])

        grid = np.zeros((max_y + abs(min_y) + 1, max_x + abs(min_x) + 1), dtype=np.uint8)

        for s in sensors:
            distance = abs(s[0][0] - s[1][0]) + abs(s[0][1] - s[1][1])
            rows = np.array([], dtype=np.int64)
            columns = np.array([], dtype=np.int64)
            for i in range(-distance, distance + 1):
                deviation = (2 * distance + 1 - 2 * abs(i)) // 2
                deviation = range(s[0][1] - deviation, s[0][1] + deviation + 1)
                for x in deviation:
                    rows = np.append(rows, x)
                    columns = np.append(columns, i + s[0][0])
            # grid[s[0][1] + abs(min_y), s[0][0] + abs(min_x)] = 1

    return sensors, min_x, min_y

def day15_1(file):
    pass

def day15_2(file):
    pass


if __name__ == '__main__':
            print(read_file('day15t.txt'))