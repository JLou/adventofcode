from collections import defaultdict


with open("./inputs/14", 'r') as f:
    lines = f.read().splitlines()

sample = """O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#....""".splitlines()


def tilt_north(grid: list[str]):
    copy = grid
    for x in range(len(grid[0])):
        current_blocker = -1

        for y in range(len(grid)):
            c = grid[y][x]
            if c == "O":
                current_blocker = current_blocker + 1
                copy[y][x] = "."
                copy[current_blocker][x] = "O"
            elif c == "#":
                current_blocker = y

    return copy


def rotate_90_degree_clckwise(matrix):
    new_matrix = []
    for i in range(len(matrix[0])):
        li = list(map(lambda x: x[i], matrix))
        li.reverse()
        new_matrix.append(li)

    return new_matrix


def rotate(grid):
    return list(list(x) for x in zip(*grid))[::-1]


def solve(grid: list[str]):
    total = 0
    for x in range(len(grid[0])):
        current_blocker = -1

        for y in range(len(grid)):
            c = grid[y][x]
            if c == "O":
                current_blocker = current_blocker + 1
                total += len(grid) - current_blocker

            elif c == "#":
                current_blocker = y

    return total


def compute_load(grid):
    H = len(grid)
    total = 0
    for i, line in enumerate(grid):
        for c in line:
            if c == 'O':
                total += H - i

    return total


def solve2(grid: list[str]):
    states = []
    end_state = None
    for _ in range(1000000000):

        for _ in range(4):
            grid = tilt_north(grid)
            grid = rotate_90_degree_clckwise(grid)

        state = "|".join(["".join(x) for x in grid])
        # find when the pattern loops
        if (state in states):
            debut_cycles = states.index(state)
            steps = 1000000000 - debut_cycles
            fin = steps % (len(states) - debut_cycles) + debut_cycles
            end_state = states[fin - 1]
            break
        else:
            states.append(state)

    return (compute_load(end_state.split("|")))


assert (solve(sample) == 136)
assert (solve2([[y for y in x] for x in sample]) == 64)

print(solve(lines))
print("PART2:", solve2([[x for x in line] for line in lines]))
