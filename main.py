#https://adventofcode.com/2022

import numpy
from constant import *

def get_calories():
    calories = []
    next = True
    with open('input\day1.txt', 'r') as f:
        while True:
            l = f.readline()
            if not l:
                break
            if (next):
                calories.append(int(l))
                next = False
            else:
                if (l != '\n'):
                    calories[-1] = calories[-1] + int(l)
                else:
                    next = True
    calories.sort(reverse=True)
    return calories


def day1_1():
    calories = get_calories()
    return calories[0]

def day1_2():
    calories = get_calories()
    calories = numpy.sum(calories[0:3])
    return calories


def get_strategy():
    strategy = []
    with open('input\day2.txt', 'r') as f:
        while True:
            l = f.readline().strip()
            if not l:
                break
            s = l.split(" ")
            t = (s[0], s[1])
            strategy.append(t)
    return strategy


def day2_1():
    strategy = get_strategy()
    result = 0
    for s in strategy:
        result += POINTS[s[1]]
        if WINS.__contains__(s):
            result += 6
        elif DRAWS.__contains__(s):
            result += 3
    return result


def day2_2():
    strategy = get_strategy()
    result = 0
    for s in strategy:
        expected = RESULTS[s[1]]
        result += expected
        them = NORMALIZE[s[0]]
        if expected == 6:
            i = list(WINS2.values()).index(them)
            move = list(WINS2.keys())[i]
        elif expected == 3:
            move = them
        else:
            move = WINS2[them]
        result += POINTS[move]
    return result


if __name__ == "__main__":
    print(day2_2())