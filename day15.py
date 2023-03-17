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

def in_area(sensor, x, y):
    return (deviation := sensor[4] - abs(y - sensor[1])) >= 0 and sensor[0] - deviation <= x <= sensor[0] + deviation
def day15_1(file, y):
    sensors = read_file(file)
    ranges = [range(s[0] - deviation, s[0] + deviation + 1) for s in sensors if \
              (deviation := s[4] - abs(y - s[1])) >= 0]
    unique = set()
    for r in ranges:
        unique.update(r)
    beacons = set([b[2] for b in sensors if b[3] == y])
    return len(unique - beacons)

def day15_2(file, ceil):
    sensors = read_file(file)
    unique = set()
    for s in sensors:
        outline = set([((max(0, s[0] - deviation - 1), i), (min(ceil, s[0] + deviation + 1), i)) for i in
                       range(max(0, s[1] - s[4] - 1), min(ceil, s[1] + s[4] + 2)) if
                       (deviation := s[4] - abs(i - s[1])) >= 0])
        outline = [p for p in outline for p in p]
        temp_outline = outline.copy()
        for o in outline:
            for ss in sensors:
                if in_area(ss, o[0], o[1]):
                    temp_outline.remove(o)
                    break
        unique.update(temp_outline)
    unique = list(unique)[0]
    return unique[0] * 4000000 + unique[1]


if __name__ == '__main__':
            print(day15_2('day15t.txt', 20))