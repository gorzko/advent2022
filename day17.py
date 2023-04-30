# ROCKS = [
#     [
#         [(3, 2), (3, 5)],
#     ],
#     [
#         (3, 3),
#         [(4, 2), (4, 4)],
#         (5, 3),
#     ],
#     [
#         [(3, 2), (3, 4)],
#         (4, 4),
#         (5, 4),
#     ],
#     [
#         (3, 2),
#         (4, 2),
#         (5, 2),
#         (6, 2),
#     ],
#     [
#         [(3, 2), (3, 3)],
#         [(4, 2), (4, 3)],
#     ],
# ]

from collections import deque

CHAMBER = {i : 0 for i in range(7)}

ROCKS = [
    {0: (0, 0), 1: (0, 0), 2: (1, 3), 3: (1, 3), 4: (1, 3), 5: (1, 3), 6: (0, 0)},
    {0: (0, 0), 1: (0, 0), 2: (1, 4), 3: (3, 3), 4: (1, 4), 5: (0, 0), 6: (0, 0)},
    {0: (0, 0), 1: (0, 0), 2: (1, 3), 3: (1, 3), 4: (3, 3), 5: (0, 0), 6: (0, 0)},
    {0: (0, 0), 1: (0, 0), 2: (4, 3), 3: (0, 0), 4: (0, 0), 5: (0, 0), 6: (0, 0)},
    {0: (0, 0), 1: (0, 0), 2: (2, 3), 3: (2, 3), 4: (0, 0), 5: (0, 0), 6: (0, 0)},
]

def read_file(file):
    with open('input\\' + file, 'r') as f:
        jets = deque([1 if j == '>' else -1 for j in f.read()])
    return jets

def day17_1(file):
    jets = read_file(file)

    rocks_counter = 0

    for j in jets:
        if rocks_counter == 2022:
            break


def day17_2(file):
    pass


if __name__ == '__main__':
    print(day17_1('day17t.txt'))