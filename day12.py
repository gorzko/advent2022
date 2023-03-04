import numpy as np
from scipy import sparse

def read_file(file):
    with open('input\\' + file, 'r') as f:
        height_map = np.array([list(l.strip()) for l in f.readlines()])
        start = np.where(height_map == 'S')
        height_map[start[0], start[1]] = 'a'
        start = start[0][0]* height_map.shape[1] + start[1][0]
        end = np.where(height_map == 'E')
        height_map[end[0], end[1]] = 'z'
        end = end[0][0] * height_map.shape[1] + end[1][0]
    return height_map, start, end

def get_adjacency_matrix(height_map):

    adjacency_matrix = sparse.lil_matrix((height_map.size, height_map.size), dtype=np.int32)

    for i in range(height_map.shape[0]):
        for j in range(height_map.shape[1]):
            current_xy = i * height_map.shape[1] + j
            current = ord(height_map[i, j])
            left, right, up, down = None, None, None, None
            if j > 0:
                left_xy = i, j - 1
                left = ord(height_map[left_xy])
            if j < height_map.shape[1] - 1:
                right_xy = i, j + 1
                right = ord(height_map[right_xy])
            if i > 0:
                up_xy = i - 1, j
                up = ord(height_map[up_xy])
            if i < height_map.shape[0] - 1:
                down_xy = i + 1, j
                down = ord(height_map[down_xy])

            if left and left - current < 2:
                left_xy = left_xy[0] * height_map.shape[1] + left_xy[1]
                adjacency_matrix[current_xy, left_xy] = 1

            if right and right - current < 2:
                right_xy = right_xy[0] * height_map.shape[1] + right_xy[1]
                adjacency_matrix[current_xy, right_xy] = 1

            if up and up - current < 2:
                up_xy = up_xy[0] * height_map.shape[1] + up_xy[1]
                adjacency_matrix[current_xy, up_xy] = 1

            if down and down - current < 2:
                down_xy = down_xy[0] * height_map.shape[1] + down_xy[1]
                adjacency_matrix[current_xy, down_xy] = 1
    return adjacency_matrix

def find_path(adjacency_matrix, start, end, stop_after=-1):
    multiplicated_matrix = adjacency_matrix.copy()
    n = 1
    while stop_after == -1 or n < stop_after:
        if n % 50 == 0:
            print(n)
        n += 1
        multiplicated_matrix = multiplicated_matrix @ adjacency_matrix
        if multiplicated_matrix[start, end] > 0:
            break
    return n

def day12_1(file):
    height_map, start, end = read_file(file)
    adjacency_matrix = get_adjacency_matrix(height_map)
    return find_path(adjacency_matrix, start, end)

def get_starting_points(border, start, row, index):
    starting_points = np.where(border == 'a')
    for i in range(starting_points[0].size):
        if row:
            start.add((index, starting_points[0][i]))
        else:
            start.add((starting_points[0][i], index))
    return start
def day12_2(file):
    height_map, start, end = read_file(file)
    adjacency_matrix = get_adjacency_matrix(height_map)
    start = set()
    start = get_starting_points(height_map[0,], start, True, 0)
    start = get_starting_points(height_map[-1, 0:], start, True, height_map.shape[0]-1)
    start = get_starting_points(height_map[0:, 0], start, False, 0)
    start = get_starting_points(height_map[0:, -1], start, False, height_map.shape[1]-1)

    shortest = 339
    for s in [s[0] * height_map.shape[1] + s[1] for s in start]:
        path = find_path(adjacency_matrix, s, end, shortest)
        if path < shortest:
            shortest = path
    return shortest

if __name__ == '__main__':
    print(day12_2('day12.txt'))
