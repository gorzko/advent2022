from collections import deque
import numpy as np

CHAMBER = np.zeros((10000, 7), dtype=np.int8)

ROCKS = deque([
    [(3, 2), (3, 3), (3, 4), (3, 5)],
    [(4, 2), (3, 3), (4, 3), (5, 3), (4, 4)],
    [(3, 2), (3, 3), (3, 4), (4, 4), (5, 4)],
    [(3, 2), (4, 2), (5, 2), (6, 2)],
    [(3, 2), (4, 2), (3, 3), (4, 3)],
])

ROCKS_COUNTER = 0

JETS = deque()

def read_file(file):
    global JETS
    with open('input\\' + file, 'r') as f:
        JETS = deque([1 if j == '>' else -1 for j in f.read()])

def get_rock():
    global ROCKS, ROCKS_COUNTER, CHAMBER
    rock = ROCKS[0].copy()
    ROCKS.append(ROCKS.popleft())
    ROCKS_COUNTER += 1

    rock = [(r[0] + (max(np.where(CHAMBER == 1)[0], default=-1) + 1 if r[1] > 0 else 0), r[1]) for r in rock]

    return rock

def push_rock(rock):
    global JETS
    direction = JETS[0]
    JETS.append(JETS.popleft())

    temp = [(r[0], r[1] + direction) for r in rock]

    if not any([r[1]< 0 or r[1] >= CHAMBER.shape[1] or CHAMBER[r] for r in temp]):
            rock = temp

    return rock

def fall(rock):
    global CHAMBER

    temp = [(r[0] - 1, r[1]) for r in rock]

    if not any([r[0] < 0 or CHAMBER[r] for r in temp]):
        rock = temp

    else:
        CHAMBER[(np.array([r[0] for r in rock]), np.array([r[1] for r in rock]))] = 1
        rock = get_rock()

    return rock

def day17(file, rocks_limit):
    global CHAMBER, ROCKS, ROCKS_COUNTER
    read_file(file)
    rock = None

    while ROCKS_COUNTER <= rocks_limit:
        print(ROCKS_COUNTER)
        if not rock:
            rock = get_rock()
        rock = push_rock(rock)
        rock = fall(rock)

    return max(np.where(CHAMBER == 1)[0], default=0) + 1
def day17_2(file):
    pass


if __name__ == '__main__':
    print(day17('day17t.txt', 2022))
