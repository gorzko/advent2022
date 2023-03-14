def read_file(file):
    with open('input\\' + file, 'r') as f:
        file = f.readlines()
    sensors = []
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

def day15_2(file, max):
    sensors = read_file(file)
    max += 1
    for i in range(max):
        ranges = [range(s[0] - deviation, s[0] + deviation + 1) for s in sensors if \
                  (deviation := s[4] - abs(i - s[1])) >= 0]
        unique = set()
        for r in ranges:
            unique.update(r)
        unique = [r for r in unique if 0 <= r < max]
        if len(unique) < max:
            return [x for x in range(max) if x not in unique][0] * 4000000 + i

    return sensors


if __name__ == '__main__':
            print(day15_2('day15t.txt', 20))