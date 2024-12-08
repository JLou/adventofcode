from functools import cache


def parse(line):
    left, right = line.split(": ")
    operators = right.split(" ")

    return int(left), tuple(map(int, operators))


@cache
def can_be_solved(total, operators):
    if len(operators) == 1:
        return operators[0] == total
    last_operator = operators[-1]
    return can_be_solved(total - last_operator, operators[0:-1]) or (total % last_operator == 0 and can_be_solved(total // last_operator, operators[0:-1]))


@cache
def can_be_solved2(total, current, operators):
    if len(operators) == 0 or current > total:
        return current == total
    next_operator = operators[0]
    return can_be_solved2(total, next_operator + current, operators[1:]) or (can_be_solved2(total, current * next_operator, operators[1:])) or can_be_solved2(total, int(str(current) + str(next_operator)), operators[1:])


def solve(input):
    s = 0
    s2 = 0
    for total, operators in map(parse, input.splitlines()):
        if can_be_solved(total, operators):
            s += total
            s2 += total
        elif can_be_solved2(total, operators[0], operators[1:]):
            s2 += total

    return s, s2


test_input = """190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20"""

assert solve(test_input) == (3749, 11387)


with open("./inputs/07", 'r') as f:
    lines = f.read()

part1, part2 = solve(lines)
print(f'Part 1: {part1}, Part 2: {part2}')
