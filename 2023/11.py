with open("./inputs/11", 'r') as f:
    lines = f.read().splitlines()


def find(s, ch):
    return [i for i, ltr in enumerate(s) if ltr == ch]


def expansion(x, y, dx, dy, empty_lines, empty_cols, step=1):
    total = 0
    for i in range(x, dx, 1 if x < dx else -1):
        total += step if i in empty_cols else 0

    for i in range(y, dy, 1 if y < dy else -1):
        total += step if i in empty_lines else 0

    return total


# lines = """...#......
# .......#..
# #.........
# ..........
# ......#...
# .#........
# .........#
# ..........
# .......#..
# #...#.....""".splitlines()

galaxies = []
empty_lines = set()
empty_cols = set()

for y, l in enumerate(lines):
    galaxy_indexes = find(l, "#")
    for x in galaxy_indexes:
        galaxies.append((x, y))
    if len(galaxy_indexes) == 0:
        empty_lines.add(y)

for x in range(len(lines[0])):
    is_empty = True
    for y in range(len(lines)):
        if lines[y][x] == '#':
            is_empty = False
            break
    if is_empty:
        empty_cols.add(x)


def solve(step=1):
    total = 0
    d = []
    for i, coord in enumerate(galaxies):
        x, y = coord
        j = i
        for dx, dy in galaxies[i+1:]:
            j += 1
            dist = abs(x - dx) + abs(y - dy) + expansion(x,
                                                         y, dx, dy, empty_lines, empty_cols, step)
            total += dist
            d.append(str(i) + " " + str(j) + " " + str(dist))

    print(total)


solve()

solve(1000000-1)
