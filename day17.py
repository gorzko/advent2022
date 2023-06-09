from operator import lshift, rshift
from collections import deque, namedtuple
import numpy as np
from operator import lshift, rshift
import math
from itertools import cycle

CHAMBER = np.zeros(1000000, dtype=np.uint8)

ROCKS = [
    (
        0b0011110,
    ),
    (
        0b0001000,
        0b0011100,
        0b0001000,
    ),
    (
        0b0000100,
        0b0000100,
        0b0011100,
    ),
    (
        0b0010000,
        0b0010000,
        0b0010000,
        0b0010000,
    ),
    (
        0b0011000,
        0b0011000,
    ),
]

ROCK_POSITION = 0
ROCKS_COUNTER = 0
JETS = None
JETS_COUNTER = None
JET_CURRENT = 0
CACHE = {}

Shift = namedtuple('Shift', ['direction', 'edge'])
SHIFTS = {'<': Shift(lshift, 64), '>': Shift(rshift, 1)}
COLUMNS = [pow(2, i) for i in range(7)]


def read_file(file):
    global JETS, JETS_COUNTER, ROCKS
    with open('input\\' + file, 'r') as f:
        jets = [j for j in f.read()]
        JETS = cycle(jets)
        JETS_COUNTER = cycle(range(len(jets)))
    ROCKS = deque([r[::-1] for r in ROCKS])

def get_rock():
    global ROCKS, ROCKS_COUNTER, ROCK_POSITION, CHAMBER
    rock = ROCKS[0]
    ROCKS.append(ROCKS.popleft())
    ROCKS_COUNTER += 1

    peak = max(CHAMBER.nonzero()[0], default=-1)
    ROCK_POSITION = peak + 4

    if ROCKS_COUNTER % 100000 == 0:
        print(ROCKS_COUNTER)

    return rock

def cache_chamber(rock, rocks_limit):
    global JET_CURRENT
    current = tuple(max(p) if len(p := np.where(CHAMBER & int(math.pow(2, i)))[0]) > 0 else -1 for i in range(7))
    if all(np.array(current) > -1):
        peak = x = max(current)
        current = tuple(x - i for i in current)
        key = current + rock + tuple([JET_CURRENT])
        if key in CACHE:
            cycle = ROCKS_COUNTER - CACHE[key][0]
            increment = peak - CACHE[key][1]
            rocks_left = rocks_limit - CACHE[key][0] + 1
            cycles = int(rocks_left / cycle)
            last = [i for i in CACHE.keys()].index(key) + rocks_left - cycle * cycles
            last = [i for i in CACHE.keys()][last]
            cycles = cycles * increment
            return cycles + CACHE[last][1]
        else:
            CACHE[key] = ROCKS_COUNTER, peak
    return None
def push_rock(rock):
    global JETS, JETS_COUNTER, JET_CURRENT
    shift = SHIFTS[JETS.__next__()]
    JET_CURRENT = JETS_COUNTER.__next__()

    temp = [shift.direction(r, 1) for r in rock]
    if not any([r & shift.edge for r in rock]) and \
            not any([r & CHAMBER[i] for i, r in enumerate(temp, ROCK_POSITION)]):
        rock = temp

    return rock

def fall(rock):
    global CHAMBER, ROCK_POSITION

    if ROCK_POSITION != 0 and not any([r & CHAMBER[i] for i, r in enumerate(rock, ROCK_POSITION-1)]):
        ROCK_POSITION -= 1

    else:
        CHAMBER[np.arange(ROCK_POSITION, ROCK_POSITION + len(rock))] = tuple([r ^ CHAMBER[i] for i, r in enumerate(rock, ROCK_POSITION)])
        rock = get_rock()

    return rock

def day17(file, rocks_limit):
    global CHAMBER, ROCKS, ROCKS_COUNTER
    read_file(file)
    rock = None

    while ROCKS_COUNTER <= rocks_limit:
        if not rock:
            rock = get_rock()
        rock = push_rock(rock)
        temp = fall(rock)
        if temp != rock:
            total = cache_chamber(temp, rocks_limit)
            if total:
                break
        rock = temp

    return (total if total else max(CHAMBER.nonzero()[0])) + 1
def day17_2(file):
    pass


if __name__ == '__main__':
    print(day17('day17.txt', 2022))
