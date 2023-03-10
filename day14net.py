import numpy as np

def register_rock_tiles(file):
    with open(file, 'r') as f:
        lines = f.readlines()
        lines = [entry.strip() for entry in lines]

    grid = np.zeros((200, 1000))
    end_of_rock_field = 0
    min_x = max_x = 0
    for line in lines:
        corners = line.split(' -> ')
        for i in range(len(corners) - 1):
            start_corner, end_corner = corners[i], corners[i + 1]
            xs = [int(start_corner.split(',')[0]), int(end_corner.split(',')[0])]
            ys = [int(start_corner.split(',')[1]), int(end_corner.split(',')[1])]
            for x in range(min(xs), max(xs) + 1):
                if min_x == 0 or x < min_x:
                    min_x = x
                if x > max_x:
                    max_x = x
                for y in range(min(ys), max(ys) + 1):
                    if y > end_of_rock_field:
                        end_of_rock_field = y
                    grid[y, x] = 1
    return grid, end_of_rock_field, 0

def add_sand_particle(grid, end_of_rock_field, offset):
    sand = (0,500-offset)
    while sand[0] <= end_of_rock_field:
        # down
        if grid[sand[0]+1, sand[1]] == 0:
            sand = (sand[0]+1, sand[1])
        # left down
        elif grid[sand[0]+1, sand[1]-1] == 0:
            sand = (sand[0]+1, sand[1]-1)
        # right down
        elif grid[sand[0]+1, sand[1]+1] == 0:
            sand = (sand[0]+1, sand[1]+1)
        else:
            return sand
    return -1, -1

def solve1(file):
    grid, end_of_rock_field, offset = register_rock_tiles(file)

    sand_tiles = 0
    new_sand = add_sand_particle(grid, end_of_rock_field, offset)
    while new_sand != (-1, -1):
        grid[new_sand[0], new_sand[1]] = 1
        sand_tiles +=1
        new_sand = add_sand_particle(grid, end_of_rock_field, offset)
    print(sand_tiles)

if __name__ == '__main__':
    print(solve1('input\\day14.txt'))