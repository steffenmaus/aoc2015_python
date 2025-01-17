import re

with open('input.txt') as file:
    intlines = [[int(n) for n in re.findall(r'-?\d+', line)] for line in file]

p1 = 0
p2 = 0

cands = []
for a in range(101):
    for b in range(101 - a):
        for c in range(101 - a - b):
            d = 100 - a - b - c

            props = [0, 0, 0, 0, 0]
            for i in range(5):
                props[i] += intlines[0][i] * a
                props[i] += intlines[1][i] * b
                props[i] += intlines[2][i] * c
                props[i] += intlines[3][i] * d
            score = 1
            for i in range(4):
                score *= max(0, props[i])

            p1 = max(p1, score)
            if props[4] == 500:
                p2 = max(p2, score)

print("Part 1: " + str(p1))
print("Part 2: " + str(p2))
