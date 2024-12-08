def solve(input):
    s = 0
    s2 = 0

    return s, s2


test_input = """"""

assert solve(test_input) == (0, 0)


with open("./inputs/20", 'r') as f:
    lines = f.read()

part1, part2 = solve(lines)
print(f'Part 1: {part1}, Part 2: {part2}')