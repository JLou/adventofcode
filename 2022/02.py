with open("inputs/02", 'r') as f:
    lines = [line.split() for line in f.readlines()]

points_per_choice = {
    'R': 1, 'P':2, 'S': 3
}
outcome_map = {
    'W': 6, 'L': 0, 'D': 3
}

results = {'R': 'S', 'P':'R', 'S': 'P'}
results_inv = {'R': 'P', 'P':'S', 'S': 'R'}
str = 'RPS';
out = 'LDW';

sum = 0
for a,b in lines:
    me = str[ord(b) - ord('X')]
    them = str[ord(a) - ord('A')]
    if results[me] == them:
        sum += outcome_map['W']
    elif me == them:
        sum += outcome_map['D']
    else:
        sum += outcome_map['L']
    
    sum += points_per_choice[me]

print ("part 1", sum)

sum = 0
for a,b in lines:
    outcome = out[ord(b) - ord('X')]
    them = str[ord(a) - ord('A')]
    
    shape = them if outcome == "D" else  (results[them] if outcome == 'L' else results_inv[them])

    sum += points_per_choice[shape] + outcome_map[outcome]

print(sum)