from collections import namedtuple
from functools import cache
import multiprocessing as mp
from time import perf_counter
import cProfile
import pstats

Resources = namedtuple('Resources', ['ore', 'clay', 'obsidian', 'geode'], defaults=(0, 0, 0, 0))

GET_MOVES = 0

def read_file(file):
    to_numbers = lambda x: list(map(int, [a.strip(':') for a in x]))
    blueprints = {i[0]: Resources(Resources(i[1]), Resources(i[2]), Resources(i[3], i[4]),
                                  Resources(i[5], obsidian=i[6])) for i in \
                  [to_numbers((w[1], w[6], w[12], w[18], w[21], w[27], w[30])) for w in \
                   [l.split() for l in open('input\\' + file, 'r')]]}
    return blueprints


# 0 - ore
# 1 - clay
# 2 - obsidian
# 3 - geode


def get_moves(blueprint: Resources, robots: Resources, resources: Resources):

    start = perf_counter()
    moves = []

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

    # Wait one turn if there are no moves or you can buy a robot if you wait
    if not moves or (ore := resources.ore + robots.ore) >= min(blueprint.ore.ore, blueprint.clay.ore) or \
        ore >= blueprint.obsidian.ore and resources.clay + robots.clay >= blueprint.obsidian.clay or \
        ore >= blueprint.geode.ore and resources.obsidian + robots.obsidian >= blueprint.geode.obsidian:
        moves.append(None)

    return moves


@cache
def solve(time, blueprint: Resources, robots: Resources, resources: Resources):

    return max((robots.geode +
                solve(
                    time - 1,
                    blueprint,
                    Resources._make(
                        robots[i] + (1 if i == move else 0) for i in range(4)
                    ),
                    Resources._make(
                        resources[i] + robots[i] - (blueprint[move][i] if move is not None else 0) for i in range(4)
                    )
                )
                for move in (get_moves(blueprint, robots, resources) if time else [])), default=0)


def determine_quality(id, blueprint, time) -> int:

    profiler = cProfile.Profile()
    profiler.enable()

    robots = Resources(1)
    resources = Resources()

    r = solve(time, blueprint, robots, resources) * id

    profiler.disable()
    ps = pstats.Stats(profiler).sort_stats('tottime')
    ps.print_stats()

    return r


def day19_1(file):

    blueprints = read_file(file)

    with mp.Pool(mp.cpu_count() - 1) as p:
        return sum(p.starmap(determine_quality, ((i, blueprints[i], 24) for i in blueprints)))


def day19_2(file):

    blueprints = read_file(file)

    with mp.Pool(mp.cpu_count() - 1) as p:
        return p.starmap(determine_quality, ((1, blueprints[i], 32) for i in range(1, 4) if i in blueprints))


if __name__ == '__main__':
    print(day19_1('day19t.txt'))
