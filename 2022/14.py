with open('inputs/14') as f:
    lines = f.readlines()

# lines = """498,4 -> 498,6 -> 496,6
# 503,4 -> 502,4 -> 502,9 -> 494,9""".splitlines()

points = [[map(int, point.split(',')) for point in line.split(' -> ')] for line in lines ]

solid = set()
maxy = 0

for l in points:
    prev = None
    for x,y in l:
        if prev is not None:
            maxy = max(maxy, y)
            start = min(prev[0], x)
            end = max(prev[0], x)
            for i in range(start, end + 1):
                solid.add((i, y))
            start = min(prev[1], y)
            end = max(prev[1], y)
            for i in range(start, end + 1):
                solid.add((x, i))
        prev = (x,y)

rocks = solid.copy()

def print_cave(xstart, xend, ystart,yend, cave):
    for j in range(ystart, yend):
        s = f'{j:03}' + " "
        for i in range(xstart, xend):
            if (i,j ) in rocks:
                s += '#'
            elif (i,j) in solid:
                s += 'o'
            else:
                s += '.'
        print(s)
    print("  " + "#" * (xend - xstart + 1))
    print("")


print_cave(493, 504,0, 10, solid)


def part1():
    count = 0
    while True:
        x = 500
        for i in range(0, maxy+2):
            if (x , i) not in solid:
                continue
            elif (x-1, i) not in solid:
                x -= 1
                continue
            elif (x+1, i) not in solid:
                x += 1
                continue
            else:
                solid.add((x, i - 1))
                break
        
        print_cave(493, 504,0, 10, solid)
        
        if i > maxy:
            return count            
        count += 1

solid = rocks.copy()

def part2():
    floor = maxy + 2
    count = 0
    while True:
        x = 500
        for i in range(0, floor):
            if (x , i + 1) not in solid:
                continue
            elif (x-1, i + 1) not in solid:
                x -= 1
                continue
            elif (x+1, i + 1) not in solid:
                x += 1
                continue
            else:
                break
        solid.add((x, i))
        if (500,0) in solid:
            return count + 1
        count += 1
        #print_cave(488, 513, 0, floor, solid)

print(part2())