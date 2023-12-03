with open("./inputs/03", 'r') as f:
    lines = f.read().splitlines()

# lines = """467..114..
# ...*......
# ..35..633.
# ......#...
# 617*......
# .....+.58.
# ..592.....
# ......755.
# ...$.*....
# .664.598..""".splitlines()


gears_ratio = dict()


def is_in_bound(grid, i, j):
    return i >= 0 and j >= 0 and i < len(grid) and j < len(grid[0])


def is_part(xs, xe, y, grid, value):
    for i in range(xs-1, xe+2):
        for j in range(y-1, y+2):
            if is_in_bound(grid, j, i) and not grid[j][i].isnumeric() and not grid[j][i] == '.':
                if grid[j][i] == '*':
                    if not (i, j) in gears_ratio:
                        gears_ratio[(i, j)] = []
                    gears_ratio[(i, j)].append(value)
                return True
    return False


result = 0

for y, l in enumerate(lines):
    current_sequence = ''
    for x, c in enumerate(l + "."):
        if c.isnumeric():
            current_sequence += c
        elif len(current_sequence) > 0:
            number = int(current_sequence)
            if is_part(x - len(current_sequence), x - 1, y, lines, number):
                result += number
            current_sequence = ''


print(result)
a = list([values[0] * values[1]
          for k, values in gears_ratio.items() if len(values) == 2])
print(sum(a))
