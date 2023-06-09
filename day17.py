from operator import lshift, rshift
from collections import deque, namedtuple
import numpy as np
from operator import lshift, rshift
import math

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
JETS = deque()
CACHE = {}

Shift = namedtuple('Shift', ['direction', 'edge'])
SHIFTS = {'<': Shift(lshift, 64), '>': Shift(rshift, 1)}
COLUMNS = [pow(2, i) for i in range(7)]


def read_file(file):
    global JETS, ROCKS
    with open('input\\' + file, 'r') as f:
        JETS = deque([j for j in f.read()])
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

def cache_chamber(rock):
    current = tuple(max(p) if len(p := np.where(CHAMBER & int(math.pow(2, i)))[0]) > 0 else -1 for i in range(7))
    if all(np.array(current) > -1):
        peak = x = max(current)
        current = tuple(x - i for i in current)
        key = current + rock + tuple(JETS)
        if key in CACHE:
            cycle = ROCKS_COUNTER - CACHE[key][0]
            increment = peak - CACHE[key][1]
            rocks_left = 2023 - CACHE[key][0]
            cycles = int(rocks_left / cycle)
            last = [i for i in CACHE.keys()].index(key) + rocks_left - cycle * cycles
            last = [i for i in CACHE.keys()][last]
            cycles = cycles * increment
            total = cycles + CACHE[last][1]
            print(total)
        else:
            CACHE[key] = ROCKS_COUNTER, peak

def push_rock(rock):
    global JETS
    shift = SHIFTS[JETS[0]]
    JETS.append(JETS.popleft())

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
        cache_chamber(rock)

    return rock

def day17(file, rocks_limit):
    global CHAMBER, ROCKS, ROCKS_COUNTER
    read_file(file)
    rock = None

    while ROCKS_COUNTER <= rocks_limit:
        if not rock:
            rock = get_rock()
        rock = push_rock(rock)
        rock = fall(rock)

    return max(CHAMBER.nonzero()[0]) + 1
def day17_2(file):
    pass


if __name__ == '__main__':
    print(day17('day17t.txt', 2022))
