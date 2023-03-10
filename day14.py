import numpy as np
from scipy import sparse

def read_file(file):
    with open('input\\' + file, 'r') as f:
        input_data = []
        while True:
            line = f.readline().strip()
            if not line:
                break
            line = [eval('(' + p + ')') for p in line.split(' -> ')]
            input_data.append(line)
    max_x = max_y = 0
    offset = None
    for line in input_data:
        for point in line:
            if point[0] > max_x:
                max_x = point[0]
            if point[1] > max_y:
                max_y = point[1]
            if offset is None or point[0] < offset:
                offset = point[0]

    grid = sparse.lil_matrix(np.zeros((max_y + 1, max_x + 1 - offset), dtype=np.uint8))

    for path in input_data:
        for i in range(len(path) - 1):
            x = sorted([path[i][0], path[i + 1][0]])
            x0, x1 = x[0] - offset, x[1] - offset
            y = sorted([path[i][1], path[i + 1][1]])
            y0 = y[0]
            y1 = y[1]

            if x0 == x1:
                column = np.arange(y0, y1 + 1)
                row = np.array([x0] * (y1 - y0 + 1))
            else:
                column = np.array([y0] * (abs(x0 - x1) + 1))
                row = np.arange(x0, x1 + 1)

            grid[column, row] = 1

    return grid, 500 - offset

def sand_fall(grid, x, y):
    while y < grid.shape[0] - 1:
        if grid[y+1, x] == 0:
            y += 1
        elif grid[y+1, x-1] == 0:
            y += 1
            x -= 1
        elif grid[y+1, x+1] == 0:
            y += 1
            x += 1
        else:
            return x, y
    return None

def day14_1(file):

    grid, source = read_file(file)
    n = 0
    while True:
        row = grid.getcol(source).nonzero()[0]
        if len(row) != 0:
            xy = sand_fall(grid, source, row[0]-1)
            if xy:
                grid[xy[1], xy[0]] = 2
            else:
                break
        n += 1
    return n


if __name__ == '__main__':
    print(day14_1('day14.txt'))