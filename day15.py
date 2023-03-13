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

    return sensors
def day15_1(file, y):
    sensors = read_file(file)
    ranges = [range(s[0] - deviation, s[0] + deviation + 1) for s in sensors if \
              (deviation := s[4] - abs(y - s[1])) >= 0]
    unique = set()
    for r in ranges:
        unique.update(r)
    beacons = set([b[2] for b in sensors if b[3] == y])
    return len(unique - beacons)

def day15_2(file):
    pass


if __name__ == '__main__':
            print(day15_1('day15.txt', 2000000))