with open('inputs/09') as f:
    lines = f.readlines()


def are_touching(h, t):
    return abs(h[0] - t[0]) < 2 and abs(h[1] - t[1]) < 2


def move_closer(h, t):
    dx = h[0] - t[0]
    dy = h[1] - t[1]

    if abs(dx) > 0 and abs(dy) > 0:
        t = (t[0] + dx // abs(dx), t[1] + dy // abs(dy))
    else:
        if dx > 1:
            t = (t[0] + 1, t[1])
        if dy > 1:
            t = (t[0], t[1] + 1)
        if dx < -1:
            t = (t[0] - 1, t[1])
        if dy < -1:
            t = (t[0], t[1] - 1)

    return t


h_pos = set()

def increment(l, h, t):
    dir, scale = l.split(" ")
    intscale = int(scale)
    if dir == 'R':
        vect = (1, 0)
    elif dir == 'L':
        vect = (-1, 0)
    elif dir == 'U':
        vect = (0, - 1)
    else:
        vect = (0, 1)

    dx, dy = vect
    for i in range(intscale):
        h = (h[0] + dx, h[1] + dy)
        if not are_touching(h, t):
            t = move_closer(h, t)
        h_pos.add(t)


    return (h, t)


def increment_knots(l, h, t):
    dir, scale = l.split(" ")
    intscale = int(scale)
    if dir == 'R':
        vect = (1, 0)
    elif dir == 'L':
        vect = (-1, 0)
    elif dir == 'U':
        vect = (0, - 1)
    else:
        vect = (0, 1)

    dx, dy = vect
    
    for i in range(intscale):
        h = (h[0] + dx, h[1] + dy)
        
        prev = h
        for j in range(9):
            curr_t = t[j]
            if not are_touching(prev, curr_t):
                t[j] = move_closer(prev, curr_t)
            prev = t[j]
        h_pos.add(t[8])

    return (h, t)


h = (0, 0)
t = (0, 0)

total= 0

for l in lines:
    h, t = increment(l, h, t)

print(len(h_pos))

h_pos.clear()
t = [(0,0)] * 9
h = (0,0)

for l in lines:
    h, t = increment_knots(l, h, t)

print(len(h_pos))
