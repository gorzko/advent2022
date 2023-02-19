def read_file(file: str):
    with open('input\\' + file, 'r') as f:
        grid = f.readlines()
    grid = [l.strip() for l in grid]
    grid = [list(l) for l in grid]
    grid = [list(map(int, x)) for x in grid]
    return grid

def check_vertically(grid: list[int], row: int, column: int):
    last_row = len(grid) - 1
    last_column = len(grid[0]) - 1
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
def count_visible(grid: list[int]):
    visible = 0
    last_row = len(grid) - 1
    last_column = len(grid[0]) - 1
    for r in range(1, last_row):
        for c in range(1, last_column):
            if len([x for x in grid[r][0:c] if x >= grid[r][c]]) == 0 or \
                len([x for x in grid[r][c+1:last_column+1] if x >= grid[r][c]]) == 0 or \
                check_vertically(grid, r, c) :
                # print((r))
                # print(r[c])
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


if __name__ == "__main__":
    #print(day8_1("day8t.txt"))
    l = [[3, 0, 3, 7, 3],
         [2, 5, 5, 1, 2],
         [6, 5, 3, 3, 2],
         [3, 3, 5, 4, 9],
         [3, 5, 3, 9, 0]]
    print(count_visible(l))