with open("./inputs/01", 'r') as f:
    lines = f.readlines()

# lines= """1abc2
# pqr3stu8vwx
# a1b2c3d4e5f
# treb7uchet""".splitlines()

sum = 0
for l in lines:
    for c in l:
        if c.isnumeric():
            sum += int(c) *10
            break
    for c in reversed(l):
        if c.isnumeric():
            sum+= int(c)
            break

print(sum)

dict= {
    "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6 , "seven": 7, "eight" : 8, "nine": 9
}

matches = dict.keys()

# lines = """two1nine
# eightwothree
# abcone2threexyz
# xtwone3four
# 4nineeightseven2
# zoneight234
# 7pqrstsixteen""".splitlines()
sum=0

for l in lines:
    for i, c in enumerate(l):
        done = False
        for m in matches:
            if l[i:].startswith(m):
                sum += dict[m] * 10
                done = True
                break
        if done:
            break
        elif c.isnumeric():
            sum += int(c) *10
            break
        
    for i, c in enumerate(l[::-1]):
        done = False
        for m in matches:
            if l[-i-1:].startswith(m):
                sum += dict[m]
                done = True
                break
        if done:
            break
        elif c.isnumeric():
            sum += int(c)
            break


print(sum)
    
        