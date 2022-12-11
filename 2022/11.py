from math import lcm
import numpy
with open('inputs/11') as f:
    lines = f.readlines()

# monkeys = [[79, 98], [54, 65, 75, 74], [79, 60, 97], [
#     74]]
# next_monkey = [[2, 3], [2, 0], [1, 3], [0, 1]]
# divide_by_monkey = [23, 19, 13, 17]
# reducer = numpy.prod(divide_by_monkey)
# inspect_count = [0] * len(monkeys)

monkeys = [[54, 98, 50, 94, 69, 62, 53, 85], [71, 55, 82], [77, 73, 86, 72, 87], [
    97, 91], [78, 97, 51, 85, 66, 63, 62], [88], [87, 57, 63, 86, 87, 53], [73, 59, 82, 65]]
next_monkey = [[2, 1], [7, 2], [4, 7], [6, 5], [6, 3], [1, 0], [5, 0], [4, 3]]
divide_by_monkey = [3, 13, 19, 17, 5, 7, 11, 2]
reducer = lcm(*divide_by_monkey)
inspect_count = [0] * len(monkeys)


def apply_monkey_sample(n: int, item: int):
    inspect_count[n] += 1
    if n == 0:
        item *= 19
    elif n == 1:
        item += 6
    elif n == 2:
        item *= item
    else:
        item += 3

    item %= reducer
    if item % divide_by_monkey[n] == 0:
        return (next_monkey[n][0], item)
    return (next_monkey[n][1], item)


def apply_monkey(n: int, item: int):
    inspect_count[n] += 1
    if n == 0:
        item *= 13
    elif n == 1:
        item += 2
    elif n == 2:
        item += 8
    elif n == 3:
        item += 1
    elif n == 4:
        item *= 17
    elif n == 5:
        item += 3
    elif n == 6:
        item *= item
    elif n == 7:
        item += 6

    item %= reducer
    if item % divide_by_monkey[n] == 0:
        return (next_monkey[n][0], item)
    return (next_monkey[n][1], item)


for i in range(0, 10000):
    for monkey_number in range(len(monkeys)):
        while len(monkeys[monkey_number]) > 0:
            item = monkeys[monkey_number].pop(0)
            next, new = apply_monkey(monkey_number, item)
            monkeys[next].append(new)
inspect_count = sorted(inspect_count)

print(inspect_count[-1] * inspect_count[-2])
print(inspect_count)
