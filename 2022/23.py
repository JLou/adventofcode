from collections import defaultdict, deque
from typing import Tuple
import itertools


with open('inputs/23') as f:
    lines = f.read().splitlines()

sample = """....#..
..###.#
#...#.#
.#...##
#.###..
##.#.##
.#..#..""".splitlines()


def parse(lines):
    elves = set()

    for i, l in enumerate(lines):
        for j, c in enumerate(l):
            if c == '#':
                elves.add((j, i))

    return elves


def print_map(elves):
    for y in range(-2, 9):
        l = ""
        for x in range(-3, 11):
            if (x, y) in elves:
                l += "#"
            else:
                l += '.'
        print(l)


def run(elves: set, part2=False):
    directions = deque([[(-1, -1), (0, -1), (1, -1)],
                       [(-1, 1), (0, 1), (1, 1)], [(-1, -1), (-1, 0), (-1, 1)], [(1, -1), (1, 0), (1, 1)]])

    i = 1
    while True:
        proposed_moves: defaultdict[Tuple, list] = defaultdict(list)
        for (x, y) in elves:
            u = sum([1 for a, b in itertools.product(
                [-1, 0, 1], repeat=2) if (x+a, y+b) in elves])
            if u > 1:
                for test_dir in directions:
                    in_the_way = False
                    for dx, dy in test_dir:
                        if (x+dx, y+dy) in elves:
                            in_the_way = True
                            continue
                    if not in_the_way:
                        proposed_moves[(x+test_dir[1][0], y+test_dir[1]
                                        [1])].append((x, y))
                        break
        has_moved = False
        for next_move in proposed_moves:
            if len(proposed_moves[next_move]) == 1:
                has_moved = True
                elves.add(next_move)
                elves.remove(proposed_moves[next_move][0])

        directions.rotate(-1)

        # print(f'Round {i+1}')
        # print_map(elves)
        # print(f'{len(elves)} elves left')
        # print("")
        if i == 10:
            min_x = min_y = max_x = max_y = 0
            for (x, y) in elves:
                min_x = min(x, min_x)
                min_y = min(y, min_y)
                max_x = max(x, max_x)
                max_y = max(y, max_y)
            print((max_x + 1 - min_x) * (max_y + 1 - min_y) - len(elves))

        if not has_moved or (not part2 and i == 10):
            break
        i += 1

    print('Finished after round=')
    print(i)
    return elves


def part1(lines):
    elves = parse(lines)
    run(elves)


def part2(lines):
    elves = parse(lines)
    run(elves, True)


# part1(lines)
part2(lines)
