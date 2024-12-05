import re


with open("./inputs/03", 'r') as f:
    lines = f.readlines()[0]

# lines = """xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))""".splitlines()

matches = re.findall(r'mul\((\d{1,3}),(\d{1,3})\)', lines)
print(
    f'Part 1: {sum(int(a) * int(b) for a, b in matches)}')

# lines = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"

s = 0
compute = True
for i in range(0, len(lines)):
    if lines[i:i+4] == 'do()':
        compute = True
    elif lines[i:i+7] == 'don\'t()':
        compute = False
    else:
        segment = lines[i:i+13]
        match = re.match(r'^mul\((\d{1,3}),(\d{1,3})\)', segment)
        if match and compute:
            s += int(match.group(1)) * int(match.group(2))

print(
    f'Part 2 : {s}')
