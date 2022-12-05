from collections import deque
import re

with open("inputs/05") as f:
    initial, ops = f.read().split("\n\n")

stacks = []
stacks2 = []
init = initial.splitlines()[:-1]

for u in range((len(init[-1]) + 1) // 4 + 1):
    stacks.append(deque())
    stacks2.append(deque())


for l in initial.splitlines()[:-1]:
    for index, letter in enumerate(l[1::4]):
        if letter != ' ':
            stacks[index].append(letter)
            stacks2[index].append(letter)

for op in ops.splitlines():
    reg = r'move (\d+) from (\d+) to (\d+)'
    m = re.search(reg, op)
    n,f,t = map(int, m.groups())
    moved = []
    for i in range(n):
        v = stacks[f-1].popleft()
        stacks[t-1].appendleft(v)

        v = stacks2[f-1].popleft()
        moved.append(v)
    moved.reverse()
    stacks2[t-1].extendleft(moved)

str = ""
for q in stacks:
    if(len(q) > 0):
        str += q[0]

print(str)

str = ""
for q in stacks2:
    if(len(q) > 0):
        str += q[0]

print(str)

