with open("./inputs/13", 'r') as f:
    patterns = [block.splitlines() for block in f.read().split('\n\n')]


def solve(pattern: list[str]) -> int:
    for i, line in enumerate(pattern[:-1]):
        if pattern[i+1] == line:
            to_lookup = min(i + 1, len(pattern) - (i+1))
            is_mirrored = True
            for j in range(1, to_lookup):
                if pattern[i-j] != pattern[i+1+j]:
                    is_mirrored = False
                    break
            if is_mirrored:
                return (i + 1) * 100

    rotated = [''.join(x) for x in zip(*pattern[::-1])]
    for i, line in enumerate(rotated[:-1]):
        if rotated[i+1] == line:
            to_lookup = min(i + 1, len(rotated) - (i+1))
            is_mirrored = True
            for j in range(1, to_lookup):
                if rotated[i-j] != rotated[i+1+j]:
                    is_mirrored = False
                    break
            if is_mirrored:
                return (i + 1)

    return 0


sample1 = """#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.""".splitlines()

sample2 = """#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#""".splitlines()

assert (solve(sample2) == 400)
assert (solve(sample1) == 5)

print(sum(solve(block) for block in patterns))
