import re
from typing import List, NamedTuple, Tuple

with open('inputs/22') as f:
    lines = [x.ljust(150, ' ') for x in f.read().splitlines()]

sample = """        ...#
        .#..
        #...
        ....
...#.......#
........#...
..#....#....
..........#.
        ...#....
        .....#..
        .#......
        ......#.

10R5L5R10L4R5L5
""".splitlines()


class Instruction(NamedTuple):
    dist: int
    turn: str


def parse(input):
    instruction_line = input[-1]
    match = re.findall("\d+[RL]", instruction_line)
    instructions = [Instruction(int(x[:-1]), x[-1]) for x in match]

    puzzle_map = input[:-2]

    return (instructions, puzzle_map)


def parse_cube(input):
    faces = [[] for x in range(7)]
    for l in input[:50]:
        faces[1].append(l[50:100])
        faces[2].append(l[100:])
    for l in input[50:100]:
        faces[3].append(l[50:100])
    for l in input[100:150]:
        faces[5].append(l[0:50])
        faces[4].append(l[50:100])
    for l in input[150:200]:
        faces[6].append(l[0:50])

    instruction_line = input[-1]
    match = re.findall("\d+[RL]", instruction_line)
    instructions = [Instruction(int(x[:-1]), x[-1]) for x in match]
    instructions.append(Instruction(int(instruction_line[-2:]), ''))
    return instructions, faces


def find_next_tile(map, x, y, dir):
    dx, dy = dir

    next_x = x+dx
    next_y = y+dy

    # warp down
    if next_y >= len(map):
        for j in range(next_y):
            if map[j][next_x] != ' ':
                return (next_x, j)
    # warp up
    if next_y < 0:
        for i in range(len(map) - 1, 0, -1):
            if map[i][next_x] != ' ':
                return (next_x, i)

    # wrap right
    if next_x >= len(map[next_y]):
        for i in range(next_x):
            if map[next_y][i] != ' ':
                return (i, next_y)
    # warp left
    if next_x < 0:
        for i in range(len(map[next_y]) - 1, 0, -1):
            if map[next_y][i] != ' ':
                return (i, next_y)

    while map[next_y][next_x] == ' ':
        next_x, next_y = find_next_tile(map, next_x, next_y, dir)

    return (next_x, next_y)


RIGHT = 0
DOWN = 1
LEFT = 2
UP = 3


def find_next_tile_cube(cube: List[List[str]], face: int, x: int, y: int, dir: Tuple[int, int], currentDir: int):
    dx, dy = dir

    next_x = x+dx
    next_y = y+dy

    curr_zone = cube[face]

    if next_y >= len(curr_zone):
        if face == 1:
            return (3, next_x, 0, DOWN)
        elif face == 2:
            return (3, 49, next_x, LEFT)
        elif face == 3:
            return (4, next_x, 0, DOWN)
        elif face == 4:
            return (6, 49, next_x, LEFT)
        elif face == 5:
            return (6, next_x, 0, DOWN)
        else:
            return (2, next_x, 0, DOWN)
    # warp up
    if next_y < 0:
        if face == 1:
            return (6, 0, next_x, RIGHT)
        elif face == 2:
            return (6, next_x, 49, UP)
        elif face == 3:
            return (1, next_x, 49, UP)
        elif face == 4:
            return (3, next_x, 49, UP)
        elif face == 5:
            return (3, 0, next_x, RIGHT)
        else:
            return (5, next_x, 49, UP)

    # wrap right
    if next_x >= len(curr_zone[0]):
        if face == 1:
            return (2, 0, next_y, RIGHT)
        elif face == 2:
            return (4, 49, 49-next_y, LEFT)
        elif face == 3:
            return (2, next_y, 49, UP)
        elif face == 4:
            return (2, 49, 49-next_y, LEFT)
        elif face == 5:
            return (4, 0, next_y, RIGHT)
        else:
            return (4, next_y, 49, UP)

        # warp left
    if next_x < 0:
        if face == 1:
            return (5, 0, 49-next_y, RIGHT)
        elif face == 2:
            return (1, 49, next_y, LEFT)
        elif face == 3:
            return (5, next_y, 0, DOWN)
        elif face == 4:
            return (5, 49, next_y, LEFT)
        elif face == 5:
            return (1, 0, 49-next_y, RIGHT)
        else:
            return (1, next_y, 0, DOWN)

    return face, next_x, next_y, currentDir


def run(instructions: List[Instruction], map: List[str]):
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    y = 0
    x = map[y].index('.')
    direction = 0

    for dist, rotate in instructions:
        for i in range(0, dist):
            dx, dy = directions[direction]

            next_x, next_y = find_next_tile(map, x, y, (dx, dy))
            next_tile = map[next_y][next_x]

            if next_tile == '#':
                break
            else:
                x, y = next_x, next_y
        direction += 1 if rotate == 'R' else -1
        direction %= 4

    return x, y, direction


def print_cube(cube):
    for i in range(50):
        print((" " * 50) + "".join(cube[1][i]) + "".join(cube[2][i]))
    for i in range(50):
        print((" " * 50) + "".join(cube[3][i]))
    for i in range(50):
        print("".join(cube[5][i]) + "".join(cube[4][i]))
    for i in range(50):
        print("".join(cube[6][i]))


def run2(instructions: List[Instruction], cube: List[str]):
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    y = 0
    face = 1
    x = cube[face][y].index('.')
    direction = RIGHT

    copy = [[[c for c in line] for line in face] for face in cube]
    chars = ['>', 'V', '<', '^']
    copy[face][y][x] = chars[direction]
    u = 0
    for dist, rotate in instructions:
        for i in range(0, dist):
            dx, dy = directions[direction]

            next_face, next_x, next_y, next_dir = find_next_tile_cube(
                cube, face, x, y, (dx, dy), direction)
            next_tile = cube[next_face][next_y][next_x]

            if next_tile == '#':
                break
            else:
                face, direction, x, y = next_face, next_dir, next_x, next_y
                copy[face][y][x] = chars[direction]
        if rotate != '':
            direction += 1 if rotate == 'R' else -1
            direction %= 4
        u += 1

        # if u % 20 == 0:
        #     print_cube(copy)
        #     print(" ")
    # for i, f in enumerate(copy):
    #     print(f"face {i}")
    #     for l in f:
    #         print("".join(l))
    #     print("")

    return face, x, y, direction


def part1(input):
    instructions, map = parse(input)
    x, y, dir = run(instructions, map)
    print((y+1) * 1000 + (x+1) * 4 + dir)


def part2(input):
    instructions, cube = parse_cube(input)
    face, x, y, direction = run2(instructions, cube)

    print(face, x, y, direction)
    print((y + 1) * 1000 + (x + 100 + 1) * 4 + direction)


part2(lines)
