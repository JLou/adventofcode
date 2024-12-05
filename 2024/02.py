with open("./inputs/02", 'r') as f:
    lines = f.readlines()

# lines = """7 6 4 2 1
# 1 2 7 8 9
# 9 7 6 2 1
# 1 3 2 4 5
# 8 6 4 4 1
# 1 3 6 7 9""".splitlines()

safe = 0


def checkSafety(values):
    isSafe = True
    errorId = 0
    previousDiff = 0
    for i, value in enumerate(values):
        if i == 0:
            continue
        diff = value - values[i-1]
        if abs(diff) > 3:
            isSafe = False
            errorId = i
            break
        if (previousDiff != 0 and (previousDiff * diff) < 0) or diff == 0:
            isSafe = False
            errorId = i
            break
        previousDiff = diff
    return [isSafe, errorId]


def checkSafety2(values):
    isSafe, errorIndex = checkSafety(values)
    if isSafe:
        return True
    else:
        for i in range(errorIndex - 2, errorIndex + 1):
            isSafe, _ = checkSafety(values[0:i] + values[i+1:])
            if isSafe:
                return True
                break
    return False


print(
    f'Part 1: {sum(1 for line in lines if checkSafety(list(map(int, line.split())))[0])}')

print(
    f'Part 2 : {sum(1 for line in lines if checkSafety2(list(map(int, line.split()))))}')
