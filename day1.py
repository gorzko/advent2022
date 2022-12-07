import numpy


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
