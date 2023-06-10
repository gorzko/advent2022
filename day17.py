from operator import lshift, rshift
from collections import namedtuple
import numpy as np
from operator import lshift, rshift
import math
from itertools import cycle


def read_file(file):
    with open('input\\' + file, 'r') as f:
        jets = [j for j in f.read()]
        jets_counter = cycle(range(len(jets)))
        jets = cycle(jets)
    return jets, jets_counter


def get_rock(rocks, chamber, rocks_counter):
    rock = rocks.__next__()
    rocks_counter += 1

    peak = max(chamber.nonzero()[0], default=-1)
    rock_position = peak + 4

    return rock, rock_position, rocks_counter


def push_rock(rock, chamber, rock_position, jets, jets_counter, shifts):
    shift = shifts[jets.__next__()]
    jet_current = jets_counter.__next__()

    temp = [shift.direction(r, 1) for r in rock]
    if not any([r & shift.edge for r in rock]) and \
            not any([r & chamber[i] for i, r in enumerate(temp, rock_position)]):
        rock = temp

    return rock, jet_current


def fall(rock, rocks, chamber, rock_position, rocks_counter):

    if rock_position != 0 and not any([r & chamber[i] for i, r in enumerate(rock, rock_position-1)]):
        rock_position -= 1

    else:
        chamber[np.arange(rock_position, rock_position + len(rock))] = tuple([r ^ chamber[i] for i, r in enumerate(rock, rock_position)])
        rock, rock_position, rocks_counter = get_rock(rocks, chamber, rocks_counter)

    return rock, rock_position, rocks_counter


def cache_chamber(cache, rock, rocks_limit, chamber, rocks_counter, jets_current):
    current = tuple(max(p) if len(p := np.where(chamber & int(math.pow(2, i)))[0]) > 0 else -1 for i in range(7))
    if all(np.array(current) > -1):
        peak = x = max(current)
        current = tuple(x - i for i in current)
        key = current + rock + tuple([jets_current])
        if key in cache:
            cycle_size = rocks_counter - cache[key][0]
            increment = peak - cache[key][1]
            rocks_left = rocks_limit - cache[key][0] + 1
            cycles = int(rocks_left / cycle_size)
            last = [i for i in cache.keys()].index(key) + rocks_left - cycle_size * cycles
            last = [i for i in cache.keys()][last]
            cycles = cycles * increment
            return cycles + cache[last][1]
        else:
            cache[key] = rocks_counter, peak
    return None


def day17(file, rocks_limit):
    chamber = np.zeros(10000, dtype=np.uint8)
    rocks = [
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
    rocks = cycle([r[::-1] for r in rocks])
    rocks_counter = 0
    Shift = namedtuple('Shift', ['direction', 'edge'])
    shifts = {'<': Shift(lshift, 64), '>': Shift(rshift, 1)}
    cache = {}

    jets, jets_counter = read_file(file)
    rock = None

    while rocks_counter <= rocks_limit:
        if not rock:
            rock, rock_position, rocks_counter = get_rock(rocks, chamber, rocks_counter)
        rock, jet_current = push_rock(rock, chamber, rock_position, jets, jets_counter, shifts)
        temp, rock_position, rocks_counter = fall(rock, rocks, chamber, rock_position, rocks_counter)
        if temp != rock:
            total = cache_chamber(cache, temp, rocks_limit, chamber, rocks_counter, jet_current)
            if total:
                break
        rock = temp

    return (total if total else max(chamber.nonzero()[0])) + 1


if __name__ == '__main__':
    print(day17('day17.txt', 1000000000000))
