import numpy as np

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


def day12_1(file):
    height_map, start, end = read_file(file)
    adjacency_matrix = np.array([[0] * height_map.size] * height_map.size)

    for i in range(height_map.shape[0]):
        for j in range(height_map.shape[1]):
            current_xy = i * height_map.shape[0] + j
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

    multiplicated_matrix = adjacency_matrix.copy()
    n = 1
    while True:
        n += 1
        print(n)
        multiplicated_matrix = multiplicated_matrix @ adjacency_matrix
        if multiplicated_matrix[start, end] > 0:
            break

    return n


if __name__ == '__main__':
    print(day12_1('day12t.txt'))
