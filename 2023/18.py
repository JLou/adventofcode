from collections import deque
import queue
from shapely.geometry import Polygon

import numpy as np


with open("./inputs/18", 'r') as f:
    lines = f.read().splitlines()

sample = """R 6 (#70c710)
D 5 (#0dc571)
L 2 (#5713f0)
D 2 (#d2c081)
R 2 (#59c680)
D 2 (#411b91)
L 5 (#8ceee2)
U 2 (#caa173)
L 1 (#1b58a2)
U 2 (#caa171)
R 2 (#7807d2)
U 3 (#a77fa3)
L 2 (#015232)
U 2 (#7a21e3)""".splitlines()

dirs = ["R", "D", "L", "U"]


def parse(instruction: str, part: int):
    dir, length, color = instruction.split(" ")

    if part == 1:
        return (dir, int(length))
    else:
        d = dirs[int(color[-2])]
        l = int(color[2:-2], 16)
        return d, int(l)


m = {
    "D": (0, 1),
    "U": (0, -1),
    "L": (-1, 0),
    "R": (1, 0),
}


def get_diff(direction):
    return m[direction]


def get_neighbours(x, y):
    vectors = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    for dx, dy in vectors:
        yield (x+dx, y+dy)


def area(corners):
    n = len(corners)  # of corners
    area = 0.0
    for i in range(n):
        j = (i + 1) % n
        area += corners[i][0] * corners[j][1]
        area -= corners[j][0] * corners[i][1]
    area = abs(area) / 2.0
    return area


def solve2(input, part=2):
    instructions = [parse(x, part) for x in input]
    x, y = (0, 0)
    points = [(x, y)]
    total_l = 0
    for dir, l in instructions:
        total_l += l
        dx, dy = get_diff(dir)
        x, y = (x + dx*l, y + dy*l)
        points.append((x, y))

    pgon = area(points[:-1])

    return int(pgon + (total_l/2) + 1)


def print_grid(dug, minx, miny, maxx, maxy):
    for y in range(miny-100, maxy+10):
        for x in range(minx-100, maxx+10):
            print("#" if (x, y) in dug else ".", end="")
        print("")
    print("\n")


assert (solve2(sample, 1) == 62)
assert (solve2(sample) == 952408144115)


print("Part 1: ", solve2(lines, 1))
print("Part 2: ", solve2(lines))
