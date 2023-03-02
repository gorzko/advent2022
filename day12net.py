import numpy as np
from scipy import sparse

def solve(file, part=1):
    with open(file, 'r') as f:
        lines = f.readlines()
        lines = [entry.strip() for entry in lines]

    grid = np.array([list(row) for row in lines])

    # get coordinates of S and E before replacing them
    start_coord = np.where(grid.flatten() == 'S')[0][0]
    end_coord = np.where(grid.flatten() == 'E')[0][0]

    # replace S with a and E with z
    grid[np.where(grid == 'S')] = 'a'
    grid[np.where(grid == 'E')] = 'z'

    if part==2:
        start_coord = np.where(grid.flatten() == 'a')[0]

    nr_of_fields = grid.shape[0] * grid.shape[1]
    # build an adjacency? matrix to document which fields can be reached from which in one step
    adj_matrix = np.zeros((nr_of_fields, nr_of_fields))
    for i in np.arange(grid.shape[0]):
        for j in np.arange(grid.shape[1]):
            neighbors_indices = find_reachable_neighbors(grid, i, j)
            np.put(adj_matrix[i*grid.shape[1] + j], neighbors_indices, 1)

    target_matrix = sparse.csr_matrix(adj_matrix)
    adj_matrix = sparse.csr_matrix(adj_matrix)
    steps = 1
    while (target_matrix.toarray()[start_coord, end_coord] == 0).all() and steps < 500:
        if steps % 30 == 0:
            print(f"{steps=}")
        target_matrix = target_matrix @ adj_matrix
        steps += 1
    print(steps)

def find_reachable_neighbors(grid, i, j):
    neighbors = []
    grid_length, grid_width = grid.shape
    current_value = grid[i][j]
    if 0 < i and \
        ord(grid[i-1][j]) <= ord(current_value) + 1:
        neighbors.append((i-1)*grid_width + j)
    if i + 1 < grid_length and \
        ord(grid[i+1][j]) <= ord(current_value) + 1:
        neighbors.append((i+1)*grid_width + j)
    if 0 < j and \
        ord(grid[i][j-1]) <= ord(current_value) + 1:
        neighbors.append(i*grid_width + j - 1)
    if j + 1 < grid_width and \
        ord(grid[i][j+1]) <= ord(current_value) + 1:
        neighbors.append(i*grid_width + j + 1)
    return neighbors

if __name__ == '__main__':
    print(solve('input\day12t.txt', 1))