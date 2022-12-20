with open('inputs/20') as f:
    lines = f.read().splitlines()

sample = """1
2
-3
3
-2
0
4""".splitlines()


def part1(sample):
    original_list = list(map(int, sample))
    n = len(original_list)
    final_list = [(x, False, i) for i, x in enumerate(original_list)]

    cursor = 0

    def print_list(l):
        print([x for x, m, i in l])

    for i in range(n):
        idx = 0
        cursor -= 1
        x, _, idx = final_list[cursor]
        while idx != i:
            cursor += 1
            cursor = cursor % n
            x, _, idx = final_list[cursor]

        if x == 0:
            continue

        final_list.pop(cursor)

        new_idx = (cursor + x) % (n - 1)
        # if x < 0:
        #     new_idx = 1

        if new_idx < cursor:
            final_list.insert(new_idx, (x, True, idx))
        else:
            final_list.insert(new_idx, (x, True, idx))
        # print_list(final_list)

    endgame = [x for x, _, _ in final_list]
    zero = endgame.index(0)
    # print_list(final_list)
    print('zero', zero)
    print([(x*1000+zero) % n for x in range(1, 4)])
    a = sum([endgame[(x*1000+zero) % n] for x in range(1, 4)])
    print("result", a)


def part2(sample):
    original_list = [int(x) * 811589153 for x in sample]
    n = len(original_list)
    final_list = [(x, False, i) for i, x in enumerate(original_list)]

    def print_list(l):
        print([x for x, m, i in l])

    cursor = 0
    # print_list(final_list)

    for u in range(0, 10):
        for i in range(n):
            idx = 0
            cursor -= min(0, cursor - 1)
            x, _, idx = final_list[cursor]
            while idx != i:
                cursor += 1
                cursor = cursor % n
                x, _, idx = final_list[cursor]

            if x == 0:
                continue

            final_list.pop(cursor)
            diff = x % (n-1)
            new_idx = (cursor + diff) % (n-1)
            # if x < 0:
            #     new_idx = 1

            if new_idx < cursor:
                final_list.insert(new_idx, (x, True, idx))
            else:
                final_list.insert(new_idx, (x, True, idx))
            #print([str(x[0])[:2] for x in final_list])
        print(f"loop {u+1}")
        # print_list(final_list)

    endgame = [x for x, _, _ in final_list]
    zero = endgame.index(0)
    # print_list(final_list)
    print('zero', zero)
    print([(x*1000+zero) % n for x in range(1, 4)])
    a = sum([endgame[(x*1000+zero) % n] for x in range(1, 4)])
    print("result", a)


part1(lines)
# part1(sample)
part2(lines)
