import functools
import re
from typing import List, NamedTuple
from collections import deque
from functools import cache
with open('inputs/16') as f:
    lines = f.readlines()

sample = """Valve AA has flow rate=0; tunnels lead to valves DD, II, BB
Valve BB has flow rate=13; tunnels lead to valves CC, AA
Valve CC has flow rate=2; tunnels lead to valves DD, BB
Valve DD has flow rate=20; tunnels lead to valves CC, AA, EE
Valve EE has flow rate=3; tunnels lead to valves FF, DD
Valve FF has flow rate=0; tunnels lead to valves EE, GG
Valve GG has flow rate=0; tunnels lead to valves FF, HH
Valve HH has flow rate=22; tunnel leads to valve GG
Valve II has flow rate=0; tunnels lead to valves AA, JJ
Valve JJ has flow rate=21; tunnel leads to valve II""".splitlines()


class Node(NamedTuple):
    name: str
    flowRate: int
    neighbours: List[str]


def compute_graph(data: List[str]):
    regexp = 'Valve (.+) has flow rate=(\d+); tunnels? leads? to valves? (.+)'
    graph: dict[str, Node] = dict()
    for l in data:
        m = re.match(regexp, l)
        valveInput = m.group(1)
        flowRate = int(m.group(2))
        neighbours = m.group(3).split(', ')
        graph[valveInput] = Node(valveInput, flowRate, neighbours)

    return graph


graph: dict[str, Node] = dict()
valves = []


@cache
def dijkstra(start_node: str):
    start = graph[start_node]
    distance = dict()
    for k in graph.keys():
        distance[k] = 1e7
    distance[start.name] = 0
    q = deque()
    for n in start.neighbours:
        q.append((n, start.name))
    visited = set(start.name)

    while len(q) > 0:

        curr, parent = q.popleft()
        distance[curr] = min(distance[parent] + 1, distance[curr])
        if curr not in visited:
            visited.add(curr)
            for n in graph[curr].neighbours:
                q.append((n, curr))

    return distance


def compute_points(l: List[str]):
    global graph
    if len(l) == 0:
        return 0
    s = sum(map(lambda x: graph[x].flowRate, l))
    return s * len(l)


@functools.cache
def compute_best(start, time, remaining):
    d = dijkstra(start)
    if time < 1:
        return 0
    flow = graph[start].flowRate * (time)
    return max([flow + compute_best(v, time - d[v] - 1,
                                    remaining-{v}) for v in remaining if d[v] < time] + [0])


def part1(data):
    global graph, valves
    graph = compute_graph(data)
    l = list(graph.keys())

    v = frozenset([x for x in l if graph[x].flowRate > 0])
    result = (compute_best("AA", 30, v))
    print(result)


if __name__ == "__main__":
    # part1(sample)
    part1(lines)
