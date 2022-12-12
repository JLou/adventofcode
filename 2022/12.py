from collections import deque

def get_neighboors(x:int, y:int, xmax: int, ymax: int, grid: list[list[int]]):
    vectors = [(0,1), (0,-1), (1,0), (-1,0)]
    z = grid[x][y]
    for dx, dy in vectors:
        if 0<= x+dx < xmax and 0<= y+dy < ymax and grid[x+dx][y+dy] - z <= 1:
            yield (x+dx, y+dy)

def get_neighboors2(x:int, y:int, xmax: int, ymax: int, grid: list[list[int]]):
    vectors = [(0,1), (0,-1), (1,0), (-1,0)]
    z = grid[x][y]
    for dx, dy in vectors:
        if 0<= x+dx < xmax and 0<= y+dy < ymax and z - grid[x+dx][y+dy] <= 1:
            yield (x+dx, y+dy)

with open('inputs/12') as f:
    lines = f.read().splitlines()

grid = []
start = (0,0)
end = (0,0)
for line in lines:
    row = []
    for c in line:
        if c == 'S':
            start = (len(grid), len(row))
            c = 'a'
        if c == 'E':
            end = (len(grid), len(row))
            c = 'z'
        row.append(ord(c) - ord('a'))
    grid.append(row)


def part1():
        
    visited = set()
    to_visit = deque()
    to_visit.append(start)

    ymax = len(grid[0])
    xmax = len(lines)
    weights = [[float('inf')] * ymax for x in range(xmax)]
    weights[start[0]][start[1]] = 0

    while len(to_visit) > 0:
        x,y = to_visit.popleft()
        visited.add((x, y))
        for nx, ny in get_neighboors(x,y, xmax, ymax, grid):
            weights[nx][ny] = min(weights[nx][ny], weights[x][y] + 1)
            n = [nx,ny]
            if (nx, ny) not in visited and [nx, ny] not in to_visit:
                to_visit.append(n)

def part2():
    visited = set()
    to_visit = deque()
    to_visit.append(end)

    ymax = len(grid[0])
    xmax = len(lines)
    weights = [[float('inf')] * ymax for _ in range(xmax)]
    weights[end[0]][end[1]] = 0

    while len(to_visit) > 0:
        x,y = to_visit.popleft()
        visited.add((x, y))
        for nx, ny in get_neighboors2(x,y, xmax, ymax, grid):
            weights[nx][ny] = min(weights[nx][ny], weights[x][y] + 1)
            n = [nx,ny]
            if (nx, ny) not in visited and [nx, ny] not in to_visit:
                to_visit.append(n)

    best = float('inf')
    for line_grid, line_weight in zip(grid, weights):
        for e, w in zip(line_grid, line_weight):
            if e == 0 and w < best:
                best = w
    print(best)

part2()