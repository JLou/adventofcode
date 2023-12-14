with open("./inputs/13", 'r') as f:
    patterns = [block.splitlines() for block in f.read().split('\n\n')]


def count_diff(line1, line2):
    return sum(1 for a, b in zip(line1, line2) if a != b)


def find_mirror(pattern, factor):
    for i, line in enumerate(pattern[:-1]):
        if pattern[i+1] == line:
            to_lookup = min(i + 1, len(pattern) - (i+1))
            is_mirrored = True
            for j in range(1, to_lookup):
                if pattern[i-j] != pattern[i+1+j]:
                    is_mirrored = False
                    break
            if is_mirrored:
                return (i + 1) * factor
    return None


def solve(pattern: list[str]) -> int:
    res = find_mirror(pattern, 100)
    if res != None:
        return res
    rotated = [''.join(x) for x in zip(*pattern[::-1])]
    return find_mirror(rotated, 1)


def find_mirror_smudged(pattern, factor):
    for i, line in enumerate(pattern[:-1]):
        diff = count_diff(pattern[i+1], line)
        if diff < 2:
            to_lookup = min(i + 1, len(pattern) - (i+1))
            is_mirrored = True
            for j in range(1, to_lookup):
                diff += count_diff(pattern[i-j], pattern[i+1+j])
                if diff > 1:
                    is_mirrored = False
                    break
            if diff > 0 and is_mirrored:
                return (i + 1) * factor
    return None


def solve_2(pattern: list[str]) -> int:
    res = find_mirror_smudged(pattern, 100)
    if res != None:
        return res
    rotated = [''.join(x) for x in zip(*pattern[::-1])]
    return find_mirror_smudged(rotated, 1)


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
assert (solve_2(sample1) == 300)
assert (solve_2(sample2) == 100)

print(sum(solve(block) for block in patterns))
print(sum(solve_2(block) for block in patterns))
