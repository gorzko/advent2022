def read_file(file: str):
    with open('input\\' + file, 'r') as f:
        grid = f.readlines()
    grid = [l.strip() for l in grid]
    grid = [list(l) for l in grid]
    grid = [list(map(int, x)) for x in grid]
    return grid

def check_vertically(grid: list[list[int]], row: int, column: int):
    last_row = len(grid) - 1
    visible = True
    for r in range(0, row):
        if grid[r][column] >= grid[row][column]:
            visible = False
            break
    if not visible:
        visible = True
        for r in range(row + 1, last_row + 1):
            if grid[r][column] >= grid[row][column]:
                visible = False
                break
    return visible

def count_visible(grid: list[list[int]]):
    visible = 0
    last_row = len(grid) - 1
    last_column = len(grid[0]) - 1
    for r in range(1, last_row):
        for c in range(1, last_column):
            if len([x for x in grid[r][0:c] if x >= grid[r][c]]) == 0 or \
                len([x for x in grid[r][c+1:last_column+1] if x >= grid[r][c]]) == 0 or \
                check_vertically(grid, r, c) :
                visible += 1
            else:
                pass
    return visible

def day8_1(file: str):
    grid = read_file(file)
    last_row = len(grid)
    last_column = len(grid[0])

    visible = last_row * 2 + last_column * 2 - 4
    visible += count_visible(grid)

    return visible

def calculate_scenic_score(grid: list[list[int]], row: int, col: int):
    left = 0
    right = 0
    up = 0
    down = 0
    score = 0
    value = grid[row][col]
    last_row = len(grid)
    last_column = len(grid[0])

    for c in range(col - 1, -1, -1):
        score += 1
        if grid[row][c] >= value:
            break
    left, score = score, 0

    for c in range(col + 1, last_column):
        score += 1
        if grid[row][c] >= value:
            break
    right, score = score, 0

    for r in range(row - 1, -1, -1):
        score += 1
        if grid[r][col] >= value:
            break
    up, score = score, 0

    for r in range(row + 1, last_row):
        score += 1
        if grid[r][col] >= value:
            break
    down = score

    return left * right * up * down

def day8_2(file: str):
    grid = read_file(file)
    last_row = len(grid) - 1
    last_column = len(grid[0]) - 1
    max_scenic_score = 0

    for r in range(1, last_row):
        for c in range(1, last_column):
            score = calculate_scenic_score(grid, r, c)
            if score > max_scenic_score:
                max_scenic_score = score

    return max_scenic_score

if __name__ == "__main__":
    print(day8_2("day8.txt"))
