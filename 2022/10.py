with open('inputs/10') as f:
    lines = f.read().splitlines()

cycles = [1]
n = 0
x = 1
for l in lines:
    cycles_to_add = 1
    value_to_add = 0

    if l.startswith("addx"):
        value_to_add = int(l[5:])
        cycles_to_add = 2

    for i in range(0, cycles_to_add):
        cycles.append(x)

    x += value_to_add
    n += cycles_to_add

cycles_to_add = range(20, 221, 40)

s = 0
for i in cycles_to_add:
    s += cycles[i] * i

for i in range(0, 6):
    line = ""
    for j in range(0, 40):
        x = cycles[i * 40 + j + 1]
        if x - 1 <= j <= x + 1:
            line += '#'
        else:
            line += '.'
    print(line)
print(s)
