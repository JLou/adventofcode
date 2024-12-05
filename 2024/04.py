import re


with open("./inputs/04", 'r') as f:
    lines = [line.strip() for line in f.readlines()]

# lines = """MMMSXXMASM
# MSAMXMSMSA
# AMXSXMAAMM
# MSAMASMSMX
# XMASAMXAMM
# XXAMMXXAMA
# SMSMSASXSS
# SAXAMASAAA
# MAMMMXMMMM
# MXMXAXMASX""".splitlines()

columns = [''.join(row[i] for row in lines) for i in range(len(lines[0]))]


def get_diagonals(lines):
    diagonals = []
    n = len(lines)
    m = len(lines[0])

    # Top-left to bottom-right diagonals
    for d in range(n + m - 1):
        diag1 = []
        diag2 = []
        for i in range(max(0, d - m + 1), min(n, d + 1)):
            diag1.append(lines[i][d - i])
            diag2.append(lines[i][m - 1 - (d - i)])
        diagonals.append(''.join(diag1))
        diagonals.append(''.join(diag2))

    return diagonals


diagonals = get_diagonals(lines)


def count_occurrences(lines):
    search_area = lines + [row[::-1] for row in lines]
    return sum(line.count('XMAS') for line in search_area)


print(count_occurrences(lines) + count_occurrences(columns) +
      count_occurrences(diagonals))


def find_crosses(lines):
    crosses = 0
    for j, line in enumerate(lines[0:-1]):
        if j == 0:
            continue

        indexes = [m.start()
                   for m in re.finditer('A', line)]

        for i in indexes:
            if i == 0 or i == len(line) - 1:
                continue
            corners = "".join([lines[j+dj][i+di]
                               for di, dj in [[-1, -1], [-1, 1], [1, 1], [1, -1]]])
            if corners == "MSSM" or corners == "SMMS" or corners == "SSMM" or corners == "MMSS":
                crosses += 1

    return crosses


print(find_crosses(lines))
