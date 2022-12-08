with open('inputs/08') as f:
    lines = f.read().splitlines()

# lines = """30373
# 25512
# 65332
# 33549
# 35390""".splitlines()

visible_map = [[False for c in line] for line in lines]


xmax = len(lines[0])
ymax = len(lines)

for i in range(xmax):
    best = -1
    for j in range(ymax):
        c = int(lines[j][i])
        if c > best:
            visible_map[j][i] = True
        best = max(best, c)

for i in range(ymax):
    best = -1
    for j in range(xmax):
        c = int(lines[i][j])
        if c > best:
            visible_map[i][j] = True
        best = max(best, c)

for i in range(xmax-1 ,0, -1):
    best = -1
    for j in range(ymax -1,0, -1):
        c = int(lines[j][i])
        if c > best:
            visible_map[j][i] = True
        best = max(best, c)

for i in range(ymax -1 ,0, -1):
    best = -1
    for j in range(xmax -1 ,0, -1):
        c = int(lines[i][j])
        if c > best:
            visible_map[i][j] = True
        best = max(best, c)

s = 0
for l in visible_map:
    for v in l:
        s += 1 if v else 0

score_map = [[0] * len(lines[0])]*len(lines)


def compute_score(x, y):
    score = [0]*4
    for i in range(x-1, -1, -1):
        score[0] +=1
        if lines[x][y] <= lines[i][y]:
            break
    
    for i in range(x+1, xmax):
        score[1] +=1
        if lines[x][y] <= lines[i][y]:
            break
    
    for i in range(y-1, -1, -1):
        score[2] +=1
        if lines[x][y] <= lines[x][i]:
            break
    
    for i in range(y+1, ymax):
        score[3] +=1
        if lines[x][y] <= lines[x][i]:
            break
    
    return score[0] * score[1] *score[2] *score[3] 



best = 0
for i in range(1, xmax):
    for j in range(1, ymax):
        best = max(best, compute_score(i, j))
        

print(s)
print(best)