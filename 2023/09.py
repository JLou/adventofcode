sample = """0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45"""

with open("./inputs/09", 'r') as f:
    lines = [list(map(int, l.split(" "))) for l in f.read().splitlines()]

# lines = [list(map(int, l.split(" "))) for l in sample.splitlines()]


def find_last(seq: list[int]):
    new_seq = []
    for i in range(len(seq) - 1):
        new_seq.append(seq[i+1] - seq[i])

    if (all(x == 0 for x in new_seq)):
        return seq[-1]
    else:
        return find_last(new_seq) + seq[-1]


def find_first(seq: list[int]):
    new_seq = []
    for i in range(len(seq) - 1):
        new_seq.append(seq[i+1] - seq[i])

    if (all(x == 0 for x in new_seq)):
        return seq[0]
    else:
        return seq[0] - find_first(new_seq)


total = 0
for line in lines:
    v = find_last(line)
    total += v

print("PART 1:", total)
print("PART 2:", sum([find_first(line) for line in lines]))
