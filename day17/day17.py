from collections import defaultdict

with open('input.txt') as file:
    lines = [line.rstrip() for line in file]

counts = defaultdict(int)


def f(idx, space, count):
    if space == 0:
        counts[count] += 1
        return 1
    if space < 0:
        return 0
    else:
        out = []
        for n in range(idx, len(containers)):
            out.append(f(n + 1, space - containers[n], count + 1))
        return sum(out)


containers = []
for l in lines:
    containers.append(int(l))

p1 = f(0, 150, 0)
p2 = counts[min(counts)]

print("Part 1: " + str(p1))
print("Part 2: " + str(p2))
