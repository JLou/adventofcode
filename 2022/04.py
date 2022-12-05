with open("inputs/04") as f:
    lines = f.readlines()

sum = 0
s2 = 0
for l in lines:
    a, b = l.split(",")
    s, e = map(int, a.split("-"))
    u = set(range(s, e+1))
    s, e = map(int, b.split("-"))
    v = set(range(s, e+1))

    if v.issubset(u) or u.issubset(v):
        sum += 1
    if len(v.intersection(u)) > 0:
        s2 += 1

print(sum)
print(s2)
