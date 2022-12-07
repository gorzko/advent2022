from constant import *


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
