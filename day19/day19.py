from collections import defaultdict

with open('input.txt') as file:
    lines = [line.rstrip() for line in file]


def replace(seed):
    out = set()
    for i in range(len(seed)):
        current = seed[i:]
        l = seed[:i]
        for r in rules:
            if current.startswith(r):
                for n in rules[r]:
                    out.add(l + n + current[len(r):])
    return out


def undo(seed):
    out = []
    for i in range(len(seed)):
        current = seed[i:]
        l = seed[:i]
        for r in reverse_rules:
            if current.startswith(r):
                for n in reverse_rules[r]:
                    out.append(l + n + current[len(r):])
    return out


upper, seed = lines[:-2], lines[-1]
rules = defaultdict(list)
reverse_rules = defaultdict(list)

for l in upper:
    spl = l.split(" ")
    rules[spl[0]].append(spl[-1])
    reverse_rules[spl[-1]].append(spl[0])

p1 = len(replace(seed))

current = seed
p2 = 0
while current != "e":
    p2 += 1
    current = undo(current)[-1]  # not sure if this is lucky or by design

print("Part 1: " + str(p1))
print("Part 2: " + str(p2))
