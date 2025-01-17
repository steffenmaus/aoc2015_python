from collections import defaultdict

with open('input.txt') as file:
    lines = [line.rstrip() for line in file]


def f(current, available, costs, part2):
    if not available:
        return costs
    res = []
    for n in distances[current]:
        if n[0] in available:
            res.append(f(n[0], available.difference({n[0]}), costs + n[1], part2))
    if part2:
        return max(res)
    else:
        return min(res)


distances = defaultdict(list)
for l in lines:
    a, _, b, _, n = l.split(" ")
    distances[a].append((b, int(n)))
    distances[b].append((a, int(n)))
    distances["start"].append((a, 0))

p1 = f("start", set(distances.keys()).difference({"start"}), 0, False)
p2 = f("start", set(distances.keys()).difference({"start"}), 0, True)

print("Part 1: " + str(p1))
print("Part 2: " + str(p2))
