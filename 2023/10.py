import math


with open("./inputs/10", 'r') as f:
    lines = f.read().splitlines()

alphabet = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"


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


lines = """...........
.S-------7.
.|F-----7|.
.||.....||.
.||.....||.
.|L-7.F-J|.
.|..|.|..|.
.L--J.L--J.
...........""".splitlines()

start_x, start_y = (1, 1)
x, y = start_x + 1, start_y

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

print_grid(parcours)

print("Part 1:", math.ceil(count/2))


def is_on_edge(x, y):
    return x == 0 or y == 0 or y == ymax or x == xmax


def has_neighbour_outside_loop(x, y):
    return any(lines[new_y][new_x] != '.' and (new_x, new_y) not in loop for new_x, new_y in get_neighbours(x, y, xmax, ymax))


outside = set()


def is_outside(x, y, seen):

    # refacto:
    # partir d'un point et faire un parcours arbre classique
    # a la fin, regarder si un des points est outside
    # si aucun, compter
    print_grid(parcours)

    seen.add((x, y))
    neigh = list(get_neighbours(x, y, xmax, ymax))
    if any(x in outside for x in neigh):
        outside.add((x, y))
        parcours[y][x] = 'O'
        return 0
    if all((x in seen or x in loop) for x in neigh):
        # if x == 6 and y == 3:
        #     print_grid(parcours)
        parcours[y][x] = 'I'
        return 1
    if is_on_edge(x, y) or has_neighbour_outside_loop(x, y):
        parcours[y][x] = 'O'
        outside.add((x, y))
        return 0
    else:
        a = [is_outside(nx, ny, seen) for nx, ny in neigh if (
            nx, ny) not in seen and lines[ny][nx] == '.']
        if 0 in a:
            parcours[y][x] = 'O'
            outside.add((x, y))
            return 0

        v = sum(a)
        if v > 0:
            parcours[y][x] = 'I'
            return v + 1
    parcours[y][x] = 'O'
    outside.add((x, y))
    return 0


xmax = len(lines[0]) - 1
ymax = len(lines) - 1

inside = 0
seen = set()
seen.add(((x, y)))
for cx, cy in loop:
    for x, y in get_neighbours(cx, cy, xmax, ymax):
        if lines[y][x] == '.' and (x, y) not in seen:
            seen.add((x, y))
            inside += is_outside(x, y, seen)


print_grid(parcours)
print(inside)
