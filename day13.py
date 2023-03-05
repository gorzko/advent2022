import numpy as np
from functools import cmp_to_key

def read_file(file):
    with open('input\\' + file, 'r') as f:
        input_data = [eval(l.strip()) for l in f.readlines() if l != '\n']
    return input_data

def check_order(left, right):

    if isinstance(left, int) and isinstance(right, int):
        return -1 if left < right else 1 if left > right else 0

    elif isinstance(left, list) and isinstance(right, int):
        right = [right]

    elif isinstance(left, int) and isinstance(right, list):
        left = [left]

    for i in range(np.min([len(left), len(right)])):
        if left[i] != right[i]:
            temp = check_order(left[i], right[i])
            if temp != 0:
                return temp

    if  len(left) != len(right):
        return -1 if len(left) < len(right) else 1
    else:
        return 0

def day13_1(file):
    input_data = read_file(file)
    input_data = [input_data[x:x + 2] for x in range(len(input_data)) if x % 2 == 0]
    check = np.array([check_order(x[0], x[1]) for x in input_data])
    return np.sum(np.where(check == -1)[0]+1)

def day13_2(file):
    input_data = read_file(file)
    dividers = [[2], [6]]
    input_data = input_data + dividers
    input_data.sort(key=cmp_to_key(check_order))
    return (input_data.index(dividers[0]) + 1) * (input_data.index(dividers[1]) + 1)


if __name__ == '__main__':
    print(day13_1('day13t.txt'))