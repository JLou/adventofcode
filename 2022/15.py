import re
from typing import NamedTuple, Set, Tuple
with open('inputs/15') as f:
    lines = f.readlines()

sample = """Sensor at x=2, y=18: closest beacon is at x=-2, y=15
Sensor at x=9, y=16: closest beacon is at x=10, y=16
Sensor at x=13, y=2: closest beacon is at x=15, y=3
Sensor at x=12, y=14: closest beacon is at x=10, y=16
Sensor at x=10, y=20: closest beacon is at x=10, y=16
Sensor at x=14, y=17: closest beacon is at x=10, y=16
Sensor at x=8, y=7: closest beacon is at x=2, y=10
Sensor at x=2, y=0: closest beacon is at x=2, y=10
Sensor at x=0, y=11: closest beacon is at x=2, y=10
Sensor at x=20, y=14: closest beacon is at x=25, y=17
Sensor at x=17, y=20: closest beacon is at x=21, y=22
Sensor at x=16, y=7: closest beacon is at x=15, y=3
Sensor at x=14, y=3: closest beacon is at x=15, y=3
Sensor at x=20, y=1: closest beacon is at x=15, y=3""".splitlines()


def part1(lines, row):
    beacon_pos = []
    sensor_pos = []
    most_left = 0
    most_right = 0

    for l in lines:
        m = re.search(
            'Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)', l)
        sx = int(m.group(1))
        sy = int(m.group(2))
        bx = int(m.group(3))
        by = int(m.group(4))

        d = abs(sx-bx) + abs(sy-by)
        beacon_pos.append((bx, by))
        sensor_pos.append((sx, sy, d))
        most_left = min(sx - d, most_left)
        most_right = max(sx + d, most_right)

    visible = []
    for x in range(most_left, most_right+1):
        y = row

        for sx, sy, d in sensor_pos:
            if abs(sx-x) + abs(sy-y) <= d:
                if (x, y) not in beacon_pos:
                    visible.append((x, y))
                break

    print(len(visible))


class Line(NamedTuple):
    m: float
    b: float


class Point(NamedTuple):
    x: int
    y: int


def line_intersection(line1: Line, line2: Line):
    x = (line1.b - line2.b) / (line2.m - line1.m)
    y = line1.m * x + line1.b
    return Point(round(x), round(y))


def part2(data, minv, maxv):
    lines: Set[Line] = set()
    line_pairs: Set[Tuple[Line, Line]] = set()
    for l in data:
        sensor_x, sensor_y, beacon_x, beacon_y = map(
            int, re.findall("-?\d+", l))

        d = abs(sensor_x-beacon_x) + abs(sensor_y-beacon_y)
        points = [Point(sensor_x + d, sensor_y), Point(sensor_x - d, sensor_y),
                  Point(sensor_x, sensor_y + d), Point(sensor_x, sensor_y - d)]

        for a, b in [(a, b) for i, a in enumerate(points) for b in points[i+1:]]:
            if not a.x == b.x and not a.y == b.y:
                m = (a.x - b.x) / (a.y - b.y)
                b = a.y - m * a.x
                lines.add(Line(m, b))

        for line1 in lines:
            for line2 in lines:
                if line1 is not line2:
                    def by_b(x): return x.b
                    if line1.m == line2.m and abs(line1.b - line2.b) == 2:
                        line_pairs.add(
                            (min(line1, line2, key=by_b), max(line1, line2, key=by_b)))

    pairs = sorted(line_pairs, key=lambda x: x[0].b)
    print(pairs)
    intersection = line_intersection(pairs[0][1], pairs[1][0])
    print((intersection.x + 1) * 4_000_000 + intersection.y)


part1(lines, 2000000)
part2(lines, 0, 4000000)
