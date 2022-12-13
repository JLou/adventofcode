import functools

with open('inputs/13') as f:
    lines = f.read().splitlines()

# lines = """[1,1,3,1,1]
# [1,1,5,1,1]

# [[1],[2,3,4]]
# [[1],4]

# [9]
# [[8,7,6]]

# [[4,4],4,4]
# [[4,4],4,4,4]

# [7,7,7,7]
# [7,7,7]

# []
# [3]

# [[[]]]
# [[]]

# [1,[2,[3,[4,[5,6,7]]]],8,9]
# [1,[2,[3,[4,[5,6,0]]]],8,9]

# """.splitlines()


def compare(left, right):
    left_is_list = isinstance(left, list)
    right_is_list = isinstance(right, list)
    if (left_is_list and right_is_list):
        for a, b in zip(left, right):
            c = compare(a, b)
            if c != 0:
                return c
        if len(left) < len(right):
            return 1
        if len(left) == len(right):
            return 0
        else:
            return -1
    elif not left_is_list and not right_is_list:
        if left == right:
            return 0
        elif left < right:
            return 1
        else: 
            return -1
    elif not left_is_list and right_is_list:
        return compare([left], right)
    else:
        return compare(left, [right])

def part1():
    i = 1
    s = 0
    while len(lines) > 0:
        left = eval(lines.pop(0))
        right = eval(lines.pop(0))
        if len(lines) > 0:
            lines.pop(0)

        if compare(left, right) == 1:
            s += i
        i += 1

    print("part1=", s)

def part2():
    with open('inputs/13-2') as f:
        lines = list(map(eval, f.read().splitlines()))

        s= [[2]]
        e = [[6]]
        lines.append(s)
        lines.append(e)
        sorted_lines = sorted(lines, key=functools.cmp_to_key(compare), reverse=True)
        print("part2=", (sorted_lines.index(s) + 1) * (sorted_lines.index(e) + 1))

part1()
part2()