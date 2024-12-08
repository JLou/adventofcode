from collections import defaultdict


def create_bound_func(max_x, max_y):
    def is_in_bounds(x, y):
        return 0 <= x < max_x and 0 <= y < max_y

    return is_in_bounds


def solve(input):
    positions = defaultdict(list)
    lines = input.splitlines()

    nodes = set()
    all_nodes = set()
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char != ".":
                positions[char].append((x, y))

    max_x, max_y = len(lines), len(lines[0])
    is_in_bounds = create_bound_func(max_x, max_y)
    for values in positions.values():
        if len(values) < 2:
            continue

        all_nodes.update(values)
        for i, (x, y) in enumerate(values[:-1]):
            for next_x, next_y in values[i+1:]:
                dx = x - next_x
                dy = y - next_y
                if is_in_bounds(x + dx, y + dy):
                    nodes.add((x + dx, y + dy))
                if is_in_bounds(next_x - dx, next_y - dy):
                    nodes.add((next_x - dx, next_y - dy))

                new_x = x + dx
                new_y = y + dy
                while is_in_bounds(new_x, new_y):
                    all_nodes.add((new_x, new_y))
                    new_x += dx
                    new_y += dy

                new_x = next_x - dx
                new_y = next_y - dy
                while is_in_bounds(new_x, new_y):
                    all_nodes.add((new_x, new_y))
                    new_x -= dx
                    new_y -= dy

    s = len(nodes)
    s2 = len(all_nodes)

    return s, s2


test_input = """............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............"""

assert solve(test_input) == (14, 34)


with open("./inputs/08", 'r') as f:
    lines = f.read()

part1, part2 = solve(lines)
print(f'Part 1: {part1}, Part 2: {part2}')
