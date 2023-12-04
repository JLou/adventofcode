
from collections import defaultdict


with open("./inputs/04", 'r') as f:
    lines = f.read().splitlines()

# lines = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
# Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
# Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
# Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
# Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
# Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11""".splitlines()


total = 0
cards = defaultdict(int)
for idx, l in enumerate(lines):
    _, nums = l.split(":")
    winning, mine = nums.split(" | ")
    s1 = set(map(int, filter(len, winning.split(" "))))
    s2 = set(map(int, filter(len, mine.split(" "))))
    i = len(s1.intersection(s2))
    if (i > 0):
        total += pow(2, i - 1)

    cards[idx+1] += 1
    for n in range(i):
        cards[idx+2+n] += cards[idx+1]


print(total)
print(sum(cards.values()))
