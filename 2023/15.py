from collections import defaultdict
from functools import cache


with open("./inputs/15", 'r') as f:
    lines = f.read().splitlines()[0]

sample = "rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7"


@cache
def hash(str: str) -> int:
    value = 0
    for c in str:
        value += ord(c)
        value *= 17
        value %= 256

    return value


def solve(str: str) -> int:
    chunks = str.split(',')

    return sum(hash(c) for c in chunks)


def solve2(str: str) -> int:
    chunks = str.split(',')

    hashmap = defaultdict(list)
    for op in chunks:
        if op.endswith('-'):
            box = hash(op[:-1])
            for e in hashmap[box]:
                if e.startswith(f'{op[:-1]} '):
                    hashmap[box].remove(e)
                    break
        else:
            code, lens = op.split('=')
            box = hash(code)
            found = False
            for i, e in enumerate(hashmap[box]):
                if e.startswith(f'{code} '):
                    hashmap[box][i] = f'{code} {lens}'
                    found = True
                    break

            if not found:
                hashmap[box].append(f'{code} {lens}')

    total = 0
    for k, v in hashmap.items():
        for i, lens in enumerate(v):
            _, value = lens.split(" ")
            total += (k + 1) * (i+1) * int(value)

    return total


assert(solve(sample) == 1320)
assert(solve2(sample) == 145)

print("PART1:", solve(lines))
print("PART2:", solve2(lines))
