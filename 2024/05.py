from collections import defaultdict
from functools import cmp_to_key

with open("./inputs/05", 'r') as f:
    orders, updates = f.read().split("\n\n")

# orders, updates = """47|53
# 97|13
# 97|61
# 97|47
# 75|29
# 61|13
# 75|53
# 29|13
# 97|29
# 53|29
# 61|53
# 97|53
# 61|29
# 47|13
# 75|47
# 97|75
# 47|61
# 75|61
# 47|29
# 75|13
# 53|13

# 75,47,61,53,29
# 97,61,53,29,13
# 75,29,13
# 75,97,47,61,53
# 61,13,29
# 97,13,75,29,47
# """.split("\n\n")

page_orders = [map(int, order.split("|")) for order in orders.splitlines()]
page_updates = [list(map(int, update.split(",")))
                for update in updates.splitlines()]

map_orders = defaultdict(list)
pages = set()
final_order = []
for left, right in page_orders:
    map_orders[left].append(right)
    pages.add(left)
    pages.add(right)

for page in pages:
    if page not in map_orders:
        map_orders[page] = []


def is_valid_order(update, order_map):
    p = set()
    for page in update:
        if any([prev_page in order_map[page] for prev_page in p]):
            return False
        p.add(page)
    return True


def sortby(update, order_map):
    return sorted(update, key=cmp_to_key(
        lambda left, right: 1 if left in order_map[right] else -1))


def get_value(update):
    return update[len(update)//2]


sumValid = 0
sumInvalid = 0
for update in page_updates:
    if is_valid_order(update, map_orders):
        sumValid += get_value(update)
    else:
        sumInvalid += get_value(sortby(update, map_orders))

print(f"Part 1: {sumValid}")
print(f"Part 2: {sumInvalid}")
