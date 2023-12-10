import math
import re
from collections import deque

with open("./inputs/08", 'r') as f:
    directions_str, nodes = f.read().split('\n\n')

# directions_str, nodes = """LR

# 11A = (11B, XXX)
# 11B = (XXX, 11Z)
# 11Z = (11B, XXX)
# 22A = (22B, XXX)
# 22B = (22C, 22C)
# 22C = (22Z, 22Z)
# 22Z = (22B, 22B)
# XXX = (XXX, XXX)""".split('\n\n')

node_pattern = re.compile(r'(\w{3}) = \((\w{3}), (\w{3})\)')


class Node:
    def __init__(self, input_str: str) -> None:
        name, left, right = re.findall(node_pattern, input_str)[0]
        self.name = name
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        return self.name + " = (" + self.left + ", " + self.right + ")"


node_dict: "dict[str, Node]" = {}


def move(start_pos, instruction) -> str:
    return node_dict[start_pos].left if instruction == 'L' else node_dict[start_pos].right


for l in nodes.splitlines():
    node = Node(l)
    node_dict[node.name] = node

directions = deque(directions_str)

position = "AAA"


def count(start, is_part1=False):
    directions_copy = deque(directions_str)
    count = 0
    while (start != "ZZZ" if is_part1 else not start.endswith("Z")):
        count += 1
        current_dir = directions_copy[0]
        start = move(start_pos=start, instruction=current_dir)
        directions_copy.rotate(-1)

    return count


print("PART 1:", count("AAA", True))


start_nodes = list(filter(lambda x: x.endswith("A"), node_dict.keys()))
counts = [count(x) for x in start_nodes]
ppcm = math.lcm(*counts)

print("Part 2:", ppcm)
