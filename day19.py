from collections import namedtuple

Resources = namedtuple('Resources', ['ore', 'clay', 'obsidian', 'geode'], defaults=(0, 0, 0, 0))
def read_file(file):

    to_numbers = lambda x: list(map(int, [a.strip(':') for a in x]))
    blueprints = {i[0]: Resources(Resources(i[1]),  Resources(i[2]), Resources(i[3], i[4]),
                                  Resources(i[5], obsidian=i[6])) for i in \
                  [to_numbers((w[1], w[6], w[12], w[18], w[21], w[27], w[30])) for w in \
                   [l.split() for l in open('input\\' + file, 'r')]]}
    return blueprints


# 0 - ore
# 1 - clay
# 2 - obsidian
# 3 - geode

def get_robots(blueprint: Resources, robots: Resources, resources: Resources):

    r = []

    # If I can afford geode, always buy it
    if resources.ore >= blueprint.geode.ore and resources.obsidian >= blueprint.geode.obsidian:
        return [3]

    # For other resources check if I can afford and if it makes any sense to buy it
    if resources.ore >= blueprint.ore and \
            robots.ore < max(blueprint.ore, blueprint.clay, blueprint.obsidian.ore, blueprint.geode.ore):
        r.append(0)

    if resources.ore >= blueprint.clay and robots.clay < blueprint.obsidian.clay:
        r.append(1)

    if resources.ore >= blueprint.obsidian.ore and resources.clay >= blueprint.obsidian.clay and \
        robots.obsidian < blueprint.geode.obsidian:
        r.append(2)

    return r


def day19_1(file):

    robots = [0, 0, 0, 0]
    pass


def day19_2(file):
    pass


if __name__ == '__main__':
    print(read_file('day19t.txt'))
