with open('inputs/06') as f:
    lines = f.readlines()

def findIndex(input, n):
    for i in range(n, len(input)):
        if len(set(input[i-n:i])) == n:
            return i

def part1(input):
        return findIndex(input, 4)

def part2(input):
    return findIndex(input, 14)

print(part1(lines[0]))
print(part2(lines[0]))