import re
import pandas as pd


def get_rucksacks():
    rucksacks = []
    with open('input\day3.txt', 'r') as f:
        while True:
            l = f.readline().strip()
            if not l:
                break
            rucksack_size = int(l.__len__())
            comp_size = int(rucksack_size / 2)
            r = (l[0:comp_size], l[comp_size:rucksack_size])
            rucksacks.append(r)
    return rucksacks


def get_misplaced(rucksacks: list[tuple[str, str]]):
    misplaced = []
    for r in rucksacks:
        for i in r[0]:
            if r[1].__contains__(i):
                misplaced.append(i)
                break
    return misplaced


def get_priority(c: chr):
    if re.search("[a-z]", c):
        return ord(c) - 96
    elif re.search("[A-Z]", c):
        return ord(c) - 38
    else:
        raise Exception("Wrong input")


def day3_1():
    result = 0
    rucksacks = get_rucksacks()
    for m in get_misplaced(rucksacks):
        result += get_priority(m)
    return result


def get_rucksack_items(rucksacks: list[tuple[str, str]]):
    rucksack_items = []
    for r in rucksacks:
        items = r[0] + r [1]
        items = list(items)
        items = pd.Series(items).unique()
        items.sort()
        items = ''.join(items)
        rucksack_items.append(items)
    return rucksack_items


def get_groups(rucksacks: list):
    groups_number = int(len(rucksacks) / 3)
    groups = []
    for i in range(0, groups_number):
        group = rucksacks[i * 3: i * 3 + 3]
        groups.append(group)
    return groups


def day3_2():
    result = 0
    rucksacks = get_rucksacks()
    items = get_rucksack_items(rucksacks)
    for g in get_groups(items):
        for i in g[0]:
            if g[1].__contains__(i) & g[2].__contains__(i):
                result += get_priority(i)
                break
    return result

