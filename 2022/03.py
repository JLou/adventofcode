def split(list_a, chunk_size):
    for i in range(0, len(list_a), chunk_size):
        yield list_a[i:i + chunk_size]


with open("inputs/03") as f:
    sacks = [(set(x[:len(x)//2]), set(x[len(x)//2:]))
             for x in f.read().splitlines()]

with open("inputs/03") as f:
    sacks2 = [(set(a), set(b), set(c))
              for a, b, c in split(f.read().splitlines(), 3)]


alpha = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

sum = 0
for l, r in sacks:
    for i in l.intersection(r):
        sum += alpha.index(i) + 1

print(sum)

sum = 0
for a, b, c in sacks2:
    u = a.intersection(b).intersection(c)
    for i in u:
        sum += alpha.index(i) + 1

print(sum)
