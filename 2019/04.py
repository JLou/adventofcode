input = "108457-562041"
minus,max = map(int, input.split("-"))


def isValidPwd(s):
    prev = s[0]
    hasAdj = False
    currGroup = 1
    minGroup = 6
    for i in s[1:]:
        if i == prev:
            hasAdj = True
            currGroup += 1
        else:
            if currGroup > 1:
                minGroup = min(currGroup, minGroup)
            currGroup = 1
        if i < prev:
            return False
        prev = i
    if currGroup > 1:
        minGroup = min(currGroup, minGroup)

    
    return hasAdj and minGroup == 2 

t = 0

for i in range(minus, max+1):
    s = str(i)
    if isValidPwd(s):
        t+=1
        print(s)

print(t)