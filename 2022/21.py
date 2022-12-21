from typing import Dict, List, NamedTuple


with open('inputs/21') as f:
    lines = f.read().splitlines()


sample = """root: pppw + sjmn
dbpl: 5
cczh: sllz + lgvd
zczc: 2
ptdq: humn - dvpt
dvpt: 3
lfqf: 4
humn: 5
ljgn: 2
sjmn: drzm * dbpl
sllz: 4
pppw: cczh / lfqf
lgvd: ljgn * ptdq
drzm: hmdt - zczc
hmdt: 32""".splitlines()


class Node(object):
    name: str
    value: int
    left: 'Node'
    right: 'Node'
    operation: str

    def __init__(self, name, value, left, right, operation):
        self.name = name
        self.value = value
        self.left = left
        self.right = right
        self.operation = operation

    def __iter__(self):
        return iter((self.name, self.value, self.left, self.right, self.operation))


def get_value(node: Node):
    if node.value > -1:
        return node.value
    elif node.operation == '+':
        return get_value(node.left) + get_value(node.right)
    elif node.operation == '-':
        return get_value(node.left) - get_value(node.right)
    elif node.operation == '*':
        return get_value(node.left) * get_value(node.right)
    elif node.operation == '/':
        return get_value(node.left) // get_value(node.right)
    else:
        return 0


def get_operation(node: Node, compute=False):
    if node.name == 'humn':
        return 'X'
    if node.name == 'root':
        return f'{get_operation(node.left)}=={node.right.value}'
    if node.value > 0:
        return str(node.value)
    elif node.left.value > 0 and node.right.value > 0:
        node.value = get_value(node)
        return str(node.value)
    else:
        return f'({get_operation(node.left)}{node.operation}{get_operation(node.right)})'


def balance_eq(node: Node):
    while node.left.name != 'humn':
        equal_to = node.right.value
        balance_left = node.left.left.value > 0
        node_to_balance = node.left.left if node.left.left.value > 0 else node.left.right

        if node.left.operation == '+':
            equal_to -= node_to_balance.value
        if node.left.operation == '-' and balance_left:
            equal_to = node_to_balance.value - equal_to
        if node.left.operation == '-' and not balance_left:
            equal_to += node_to_balance.value
        if node.left.operation == '/' and balance_left:
            equal_to = node_to_balance.value / equal_to
        if node.left.operation == '/' and not balance_left:
            equal_to *= node_to_balance.value
        if node.left.operation == '*':
            equal_to /= node_to_balance.value

        node.left = node.left.right if node.left.left.value > 0 else node.left.left
        node.right.value = equal_to
        print(get_operation(node))


def simplify_tree(node: Node):
    if node.name == 'humn':
        return
    if node.value > 0:
        return
    simplify_tree(node.left)
    simplify_tree(node.right)
    if node.left.value > 0 and node.right.value > 0:
        node.value = get_value(node)
        node.left = None
        node.right = None


def part1(data: List[str]):
    monkeys: Dict[str, Node] = dict()
    for monkey in data:
        name, value = monkey.split(': ')
        if value.isnumeric():
            monkeys[name] = Node(name, int(value), None, None, None)
        else:
            monkeys[name] = Node(name, -1, None, None, value)

    for name, value, _, _, op in monkeys.values():
        if value == -1:
            left = op[:4]
            right = op[-4:]
            sign = op[5]
            monkeys[name].right = monkeys[right]
            monkeys[name].left = monkeys[left]
            monkeys[name].operation = sign

    return get_value(monkeys['root'])


def part2(data: List[str]):
    monkeys: Dict[str, Node] = dict()
    for monkey in data:
        name, value = monkey.split(': ')
        if value.isnumeric():
            monkeys[name] = Node(name, int(value), None, None, None)
        else:
            monkeys[name] = Node(name, -1, None, None, value)

    for name, value, _, _, op in monkeys.values():
        if name == "humn":
            monkeys[name].value = -1
        elif value == -1:
            left = op[:4]
            right = op[-4:]
            sign = op[5]
            monkeys[name].right = monkeys[right]
            monkeys[name].left = monkeys[left]
            monkeys[name].operation = sign

    simplify_tree(monkeys['root'])
    balance_eq(monkeys['root'])
    return monkeys['root'].right.value


print(part1(sample))
print(part1(lines))

print(part2(sample))
print(part2(lines))
