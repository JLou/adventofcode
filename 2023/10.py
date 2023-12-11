from collections import deque
import math


with open("./inputs/10", 'r') as f:
    lines = f.read().splitlines()

alphabet = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGH#JKLMNOPQRSTUVWXYZ"


def print_grid(grid):
    print("")
    for line in grid:
        for c in line:
            print(c, end="")
        print("")


def get_neighbours(x: int, y: int, xmax: int, ymax: int):
    vectors = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    for dx, dy in vectors:
        if 0 <= x+dx <= xmax and 0 <= y+dy <= ymax:
            yield (x+dx, y+dy)


start_x, start_y = (104, 18)
x, y = start_x, start_y - 1


# lines = """FF7FSF7F7F7F7F7F---7
# L|LJ||||||||||||F--J
# FL-7LJLJ||||||LJL-77
# F--JF--7||LJLJ7F7FJ-
# L---JF-JLJ.||-FJLJJ7
# |F|F-JF---7F7-L7L|7|
# |FFJF7L7F-JF7|JL---7
# 7-L-JL7||F7|L7F-7F7|
# L.L7LFJ|||||FJL7||LJ
# L7JLJL-JLJLJL--JLJ.L""".splitlines()

# start_x, start_y = (4, 0)
# x, y = start_x, start_y + 1

parcours = [list(l) for l in lines]

diff_map = {
    "|": [(0, -1), (0, 1)],
    "-": [(-1, 0), (1, 0)],
    "L": [(0, -1), (1, 0)],
    "J": [(0, -1), (-1, 0)],
    "7": [(0, 1), (-1, 0)],
    "F": [(0, 1), (1, 0)],
}

count = 0
seen = set()
seen.add((x, y))
seen.add((start_x, start_y))

loop = []
loop.append((start_x, start_y))

while True:
    if x == start_x and y == start_y:
        break

    loop.append((x, y))
    parcours[y][x] = alphabet[count % 10]

    seen.add((x, y))
    count += 1
    curr_x, curr_y = x, y

    for diff_x, diff_y in diff_map[lines[curr_y][curr_x]]:
        new_x, new_y = (curr_x + diff_x, curr_y + diff_y)
        if (start_x, start_y) == (new_x, new_y):
            x, y = (new_x, new_y)
            continue

        if ((new_x, new_y) not in seen):
            x, y = (new_x, new_y)
            break

# print_grid(parcours)

print("Part 1:", math.ceil(count/2))


def is_on_edge(x, y):
    return x == 0 or y == 0 or y == ymax or x == xmax


def has_neighbour_outside_loop(x, y):
    return any(lines[new_y][new_x] != '.' and (new_x, new_y) not in loop for new_x, new_y in get_neighbours(x, y, xmax, ymax))


outside = set()


def count_inside(y):
    count = 0
    total = 0
    prev_in_loop = None
    for i in range(len(lines[y])):
        c = lines[y][i]
        if c == 'S':
            c = '|'

        if (i, y) in loop:
            if c == '|':
                count += 1
                prev_in_loop = None
            elif prev_in_loop == 'L' and (c == '7') or (prev_in_loop == 'F' and (c == 'J')):
                prev_in_loop = None
            elif prev_in_loop == 'L' and (c == 'J') or (prev_in_loop == 'F' and (c == '7')):
                prev_in_loop = None
                count += 1
            elif prev_in_loop == None:
                count += 1
                prev_in_loop = c

        elif (i, y) not in loop:
            prev_in_loop = None
            if count % 2 == 1:
                parcours[y][i] = 'I'
                total += 1
            else:
                parcours[y][i] = 'O'

    return total


inside = 0

xmax = len(lines[0]) - 1
ymax = len(lines) - 1

for y in range(len(lines)):
    inside += count_inside(y)


print_grid(parcours)
print("Part 2:", inside)
