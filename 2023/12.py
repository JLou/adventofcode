from functools import cache


with open("./inputs/12", 'r') as f:
    lines = f.read().splitlines()


def parse(s: str):
    record, numb = s.split(" ")
    return record, tuple(map(int, numb.split(",")))


def parse_v2(s: str):
    record, numb = s.split(" ")
    return '?'.join([record] * 5), tuple(map(int, numb.split(","))) * 5


@cache
def solve(s: str, numbers: tuple[int]) -> int:
    if len(numbers) == 0 and "#" not in s:
        return 1

    if "#" not in s and "?" not in s and len(numbers) > 0:
        return 0

    if not s and len(numbers) > 0:
        return 0

    if "#" in s and len(numbers) == 0:
        return 0

    to_solve = numbers[0]

    i = 0
    if s[-1] != '.':
        s += '.'

    while (s[i] == '.'):
        i += 1
    substr = s[i:]

    total = 0
    if not "." in substr[:to_solve] and substr[to_solve] in ".?":
        total += solve(substr[to_solve + 1:], numbers[1:])

    if substr[0] in '.?':
        total += solve(substr[1:], numbers)
    return total


assert solve("???.###", (1, 1, 3)) == 1
assert solve("?#?#?#?#?#?#?#?", (1, 3, 1, 6)) == 1
assert solve("????.#...#...", (4, 1, 1)) == 1
assert solve("????.######..#####.", (1, 6, 5)) == 4
assert solve("?###????????", (3, 2, 1)) == 10

total = 0
total_v2 = 0
for l in lines:
    s, n = parse(l)
    s2, n2 = parse_v2(l)
    total += (solve(s, n))
    total_v2 += (solve(s2, n2))

print(total)
print(total_v2)
