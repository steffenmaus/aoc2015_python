import re
from collections import defaultdict

with open('input.txt') as file:
    intlines = [[int(n) for n in re.findall(r'-?\d+', line)] for line in file]


def get_distances_at_time(time):
    distances = []
    for l in intlines:
        v, d_fly, d_rest = l
        full_cylces = time // (d_fly + d_rest)
        total_distance = full_cylces * v * d_fly + min(d_fly, time % (d_fly + d_rest)) * v
        distances.append(total_distance)
    return distances


time = 2503

p1 = max(get_distances_at_time(time))
print("Part 1: " + str(p1))

scores = defaultdict(int)
for t in range(1, time + 1):
    distances = get_distances_at_time(t)
    top = max(distances)
    for i, v in enumerate(distances):
        if v == top:
            scores[i] += 1

p2 = max(scores.values())
print("Part 2: " + str(p2))
