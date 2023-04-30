from collections import deque

CHAMBER = {i : 0 for i in range(7)}

ROCKS = deque([
    deque([(0, 0), (0, 0), (1, 3), (1, 3), (1, 3), (1, 3), (0, 0)]),
    deque([(0, 0), (0, 0), (1, 4), (3, 3), (1, 4), (0, 0), (0, 0)]),
    deque([(0, 0), (0, 0), (1, 3), (1, 3), (3, 3), (0, 0), (0, 0)]),
    deque([(0, 0), (0, 0), (4, 3), (0, 0), (0, 0), (0, 0), (0, 0)]),
    deque([(0, 0), (0, 0), (2, 3), (2, 3), (0, 0), (0, 0), (0, 0)]),
])

ROCKS_COUNTER = 0

JETS = deque()

def read_file(file):
    global JETS
    with open('input\\' + file, 'r') as f:
        JETS = deque([1 if j == '>' else -1 for j in f.read()])

def get_rock():
    global ROCKS, ROCKS_COUNTER
    rock = ROCKS[0].copy()
    ROCKS.append(ROCKS.popleft())
    ROCKS_COUNTER += 1
    # set rock values here
    return rock

def push_rock(rock):
    global JETS
    direction = JETS[0]
    JETS.append(JETS.popleft())

    if direction == -1:
        if rock[0][0] == 0:
            rock.append(rock.popleft())
    else:
        if rock[-1][0] == 0:
            rock.appendleft(rock.pop())

def day17_1(file):
    global CHAMBER, ROCKS, ROCKS_COUNTER
    read_file(file)
    rock = None

    while ROCKS_COUNTER < 2022:
        if not rock:
            rock = get_rock()
        push_rock(rock)


def day17_2(file):
    pass


if __name__ == '__main__':
    print(day17_1('day17t.txt'))
