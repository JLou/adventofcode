
def get_path(x, y, map):
    vectors = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    max_x, max_y = len(map[0]), len(map)
    vector_index = 0
    visited = set([(x, y, vector_index)])

    next_x, next_y = (
        x + vectors[vector_index][0], y + vectors[vector_index][1])

    while 0 <= next_y < max_y and 0 <= next_x < max_x:
        # next_x, next_y = (
        #     x + vectors[vector_index][0], y + vectors[vector_index][1])

        if (next_x, next_y, vector_index) in visited:
            return None

        next_char = map[next_y][next_x]
        if next_char == "#":
            vector_index = (vector_index + 1) % 4
        else:
            visited.add((next_x, next_y, vector_index))
            x, y = next_x, next_y

        next_x, next_y = (
            x + vectors[vector_index][0], y + vectors[vector_index][1])

    return set((x, y) for x, y, _ in visited)


def solve(input):

    map = [list(line) for line in input.splitlines()]
    start_x, start_y = (0, 0)

    for y, line in enumerate(map):
        for x, char in enumerate(line):
            if char == "^":
                start_x, start_y = (x, y)
                break

    visited = get_path(start_x, start_y, map)

    part1, part2 = len(visited), 0

    for x, y in visited:
        if map[y][x] == "^":
            continue
        map[y][x] = "#"
        if get_path(start_x, start_y, map) is None:
            part2 += 1

        map[y][x] = "."

    return part1, part2


assert solve("""....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...""") == (41, 6)

with open('inputs/06', 'r') as file:
    puzzle_input = file.read()

part1, part2 = solve(puzzle_input)
print(f'Part 1: {part1}, Part 2: {part2}')
