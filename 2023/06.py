t = [45, 97, 72, 95]
d = [305, 1062, 1110, 1695]


# sample
# t = [7, 15, 30]
# d = [9, 40, 200]

def compute_combinations(time, distance):
    start = end = 0

    for i in range(time):
        if (- (i ** 2) + (i * time)) > distance:
            end = i
            if start == 0:
                start = i
        elif start > 0:
            break
    return end - start + 1


total = 1
for time, record in zip(t, d):
    total *= compute_combinations(time, record)


print(total)

print(compute_combinations(45977295, 305106211101695))
