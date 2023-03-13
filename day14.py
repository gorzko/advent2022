import numpy as np

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
    for line in input_data:
        for point in line:
            if point[0] > max_x:
                max_x = point[0]
            if point[1] > max_y:
                max_y = point[1]

    grid = np.zeros((max_y + 1, 1000), dtype=np.uint8)

    for path in input_data:
        for i in range(len(path) - 1):
            x = sorted([path[i][0], path[i + 1][0]])
            x0, x1 = x[0], x[1]
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

    return grid

def stretch_grid(grid, left=False):
    column = np.zeros((grid.shape[0], 1))
    column[-1] = 1
    if left:
        return np.concatenate((column, grid), axis=1)
    else:
        return np.concatenate((grid, column), axis=1)
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

def day14(file, part=1):

    grid = read_file(file)

    if part == 2:
        width = grid.shape[1]
        grid = np.concatenate((grid, np.zeros((1, width)), np.ones((1, width))))
    n = 0
    while grid[0,500] == 0:
        row = grid[:,500].nonzero()[0]
        if len(row) != 0:
            xy = sand_fall(grid, 500, row[0]-1)
            if xy:
                grid[xy[1], xy[0]] = 2
            else:
                break
        n += 1
    return n


if __name__ == '__main__':
    print(day14('day14.txt', 2))