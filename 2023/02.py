with open("./inputs/02", 'r') as f:
    lines = f.readlines()

# lines = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
# Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
# Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
# Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
# Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green""".splitlines()


def parse(line: str):
    res = [0, 0, 0]
    a, b = line.split(": ")
    l = b.replace(";", ',')
    groups = l.split(',')
    for group in groups:
        c, color = group.strip().split(" ")
        if (color == "red"):
            res[0] = max(res[0], int(c))
        elif (color == "green"):
            res[1] = max(res[1], int(c))
        else:
            res[2] = max(res[2], int(c))

    return res


res = 0
res2 = 0
for i, l in enumerate(lines):
    r, g, b = parse(l)
    if (r <= 12 and g <= 13 and b <= 14):
        res += int(i) + 1
    res2 += r*g*b

print(res)
print(res2)
