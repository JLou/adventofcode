with open("inputs/01", 'r') as f:
    lines = f.readlines()

elfs = []
currCal = 0
for l in lines:
    if l == '\n':
        elfs.append(currCal)
        currCal = 0
    else: 
        currCal += int(l)

elfs.append(currCal)
elfs.sort(reverse=True)
print(elfs[0])
print(sum(elfs[0:3]))