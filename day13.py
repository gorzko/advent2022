import numpy as np
from functools import cmp_to_key

def read_file(file):
    with open('input\\' + file, 'r') as f:
        input_data = [eval(l.strip()) for l in f.readlines() if l != '\n']
    return input_data

def check_order(left, right):

    if isinstance(left, int) and isinstance(right, int):
        return left < right if left != right else None

    elif isinstance(left, list) and isinstance(right, int):
        right = [right]

    elif isinstance(left, int) and isinstance(right, list):
        left = [left]

    for i in range(np.min([len(left), len(right)])):
        if left[i] != right[i]:
            temp = check_order(left[i], right[i])
            if temp is not None:
                return temp

    if  len(left) != len(right):
        return len(left) < len(right)
    else:
        return None

def day13_1(file):
    input_data = read_file(file)
    input_data = [input_data[x:x + 2] for x in range(len(input_data)) if x % 2 == 0]
    check = np.array([check_order(x[0], x[1]) for x in input_data])
    return np.sum(np.where(check == True)[0]+1)

def day13_2(file):
    input_data = read_file(file)
    divider1 = [[2]]
    divider2 = [[6]]
    input_data = input_data + divider1 + divider2
    input_data.sort(key=cmp_to_key(check_order_int))
    return (input_data.index(divider1[0]) + 1) * (input_data.index(divider2[0]) + 1)

def check_order_int(a, b):
    value = check_order(a, b)
    match value:
        case None:
            return 0
        case True:
            return -1
        case False:
            return 1

if __name__ == '__main__':
    print(day13_2('day13.txt'))