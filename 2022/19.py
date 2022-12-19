from collections import deque
import re
from typing import List, NamedTuple
import time

with open('inputs/19') as f:
    lines = f.read().splitlines()

sample = """Blueprint 1:  Each ore robot costs 4 ore.  Each clay robot costs 2 ore.  Each obsidian robot costs 3 ore and 14 clay.  Each geode robot costs 2 ore and 7 obsidian.
Blueprint 2: Each ore robot costs 2 ore. Each clay robot costs 3 ore. Each obsidian robot costs 3 ore and 8 clay. Each geode robot costs 3 ore and 12 obsidian.""".splitlines()


class Material(NamedTuple):
    ore: int
    clay: int
    obsidian: int
    geode: int


class Recipe(NamedTuple):
    ore: int
    clay: int
    obsidian: int
    geode: int
    kind: int


def can_afford(materials: Material, recipe: Material):
    for have, need in zip(materials, recipe):
        if have < need:
            return False
    return True


recipes: List[Recipe] = []


class Status(NamedTuple):
    time: int
    ore: int
    clay: int
    obsidian: int
    geode: int
    robot_ore: int
    robot_clay: int
    robot_obsidian: int
    robot_geode: int


def best_output(time: int, materials: Material, robots: Material):
    q = deque()
    q.append(Status(time, *materials, *robots))
    best = 0
    memo = set()
    max_ore = max([x.ore for x in recipes])

    while q:
        t, ore, clay, obsidian, geode, r_ore, r_clay, r_obsidian, r_geode = x = q.pop()
        if x in memo:
            continue
        memo.add(x)

        need_ore = recipes[0].ore
        need_clay = recipes[1].ore
        need_obs_ore = recipes[2].ore
        need_obs_clay = recipes[2].clay
        need_geo_ore = recipes[3].ore
        need_geo_obs = recipes[3].obsidian

        if t == 0:
            best = max(geode, best)
        elif (time * time - time) / 2 + r_geode + geode < best:
            continue
        else:
            new_ore = ore + r_ore
            new_clay = clay + r_clay
            new_obs = obsidian + r_obsidian
            new_geo = geode + r_geode

            # prioritize geodes
            if need_geo_ore <= ore and need_geo_obs <= obsidian:
                q.append(Status(t - 1, new_ore - need_geo_ore,
                                new_clay,
                                new_obs - need_geo_obs,
                                new_geo,
                                r_ore,
                                r_clay,
                                r_obsidian,
                                r_geode + 1))
                best = max(best, new_geo)
            else:
                build = False
                if robots.obsidian < need_geo_obs and need_obs_ore <= ore and need_obs_clay <= clay:
                    q.append(Status(t - 1, new_ore - need_obs_ore,
                                    new_clay - need_obs_clay,
                                    new_obs,
                                    new_geo,
                                    r_ore,
                                    r_clay,
                                    r_obsidian + 1,
                                    r_geode))
                    build = True
                if robots.clay < need_obs_clay and need_clay <= ore:
                    q.append(Status(t - 1, new_ore - need_clay,
                                    new_clay,
                                    new_obs,
                                    new_geo,
                                    r_ore,
                                    r_clay + 1,
                                    r_obsidian,
                                    r_geode))
                    build = True
                if robots.ore < max_ore and need_ore <= ore:
                    q.append(Status(t - 1,
                                    new_ore - need_ore,
                                    new_clay,
                                    new_obs,
                                    new_geo,
                                    r_ore + 1,
                                    r_clay,
                                    r_obsidian,
                                    r_geode))
                    build = True
                # no build
                if not build:
                    q.append(Status(t - 1,
                                    new_ore,
                                    new_clay,
                                    new_obs,
                                    new_geo,
                                    r_ore,
                                    r_clay,
                                    r_obsidian,
                                    r_geode))
    return best


def part1():
    s = 0
    for l in lines:
        start_time = time.time()
        bp_id, oreCost, clayCost, obsCostOre, obsCostClay, geodeCostOre, geodeCostObs = map(int, re.findall(
            "\d+", l))
        recipes.clear()
        recipes.append(Recipe(oreCost, 0, 0, 0, 0))
        recipes.append(Recipe(clayCost, 0, 0, 0, 1))
        recipes.append(Recipe(obsCostOre, obsCostClay, 0, 0, 2))
        recipes.append(Recipe(geodeCostOre, 0, geodeCostObs, 0, 3))
        v = best_output(24, Material(0, 0, 0, 0),
                        Material(1, 0, 0, 0)) * bp_id
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f'blueprint {bp_id} done in {elapsed_time} s. v = {v}')
        s += v
    print(s)


def part2():
    s = 1
    for l in lines[:3]:
        start_time = time.time()
        bp_id, oreCost, clayCost, obsCostOre, obsCostClay, geodeCostOre, geodeCostObs = map(int, re.findall(
            "\d+", l))
        print(f"starting bp {bp_id}")
        recipes.clear()
        recipes.append(Recipe(oreCost, 0, 0, 0, 0))
        recipes.append(Recipe(clayCost, 0, 0, 0, 1))
        recipes.append(Recipe(obsCostOre, obsCostClay, 0, 0, 2))
        recipes.append(Recipe(geodeCostOre, 0, geodeCostObs, 0, 3))
        v = best_output(32, Material(0, 0, 0, 0),
                        Material(1, 0, 0, 0))
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f'blueprint {bp_id} done in {elapsed_time} s. v = {v}')
        s *= v
    print(s)


if __name__ == "__main__":
    part2()
