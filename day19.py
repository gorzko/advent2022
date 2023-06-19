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

def get_moves(blueprint: Resources, robots: Resources, resources: Resources):

    moves = [None]

    # If I can afford geode, always buy it
    if resources.ore >= blueprint.geode.ore and resources.obsidian >= blueprint.geode.obsidian:
        return [3]

    # For other resources check if I can afford and if it makes any sense to buy it
    if resources.ore >= blueprint.ore.ore and \
            robots.ore < max(blueprint.ore.ore, blueprint.clay.ore, blueprint.obsidian.ore, blueprint.geode.ore):
        moves.append(0)

    if resources.ore >= blueprint.clay.ore and robots.clay < blueprint.obsidian.clay:
        moves.append(1)

    if resources.ore >= blueprint.obsidian.ore and resources.clay >= blueprint.obsidian.clay and \
        robots.obsidian < blueprint.geode.obsidian:
        moves.append(2)

    return moves


def solve(time, blueprint: Resources, robots: Resources, resources: Resources):

    if time:

        resources = Resources._make(resources[i] + robots[i] for i in range(4))

        return max([robots.geode +
                    solve(time-1, blueprint, robots, resources)
                    for m in get_moves(blueprint, robots, resources)], default=0)

    else:

        return 0

def day19_1(file):

    blueprints = read_file(file)
    robots = Resources(1)
    resources = Resources()

    return solve(24, blueprints[1], robots, resources)


def day19_2(file):
    pass


if __name__ == '__main__':
    print(day19_1('day19t.txt'))
