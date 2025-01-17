import itertools

with open('input.txt') as file:
    lines = [line.rstrip() for line in file]


def calc_total_happiness(order):
    out = 0
    for i, _ in enumerate(order):
        if i > 0:
            out += happiness[(order[i - 1], order[i])]
            out += happiness[(order[i], order[i - 1])]
    out += happiness[(order[-1], order[0])]
    out += happiness[(order[0], order[-1])]
    return out


happiness = {}
guests = set()
for l in lines:
    spl = l.split(" ")
    n = int(spl[3])
    if spl[2] == "lose":
        n = -n
    happiness[(spl[0], spl[-1][:-1])] = n
    guests.add(spl[0])

p1 = 0
for p in itertools.permutations(guests, len(guests)):
    p1 = max(p1, calc_total_happiness(p))
print("Part 1: " + str(p1))

for g in guests:
    happiness[(g, "me")] = 0
    happiness[("me", g)] = 0
guests.add("me")

p2 = 0
for p in itertools.permutations(guests, len(guests)):
    p2 = max(p2, calc_total_happiness(p))
print("Part 2: " + str(p2))
