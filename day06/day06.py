import re
from collections import defaultdict

with open('input.txt') as file:
    lines = [line.rstrip() for line in file]


def all_ints_in_string(s):
    return [int(n) for n in re.findall(r'-?\d+', s)]


lights = set()
brightness = defaultdict(int)

for l in lines:
    nums = all_ints_in_string(l)
    for x in range(nums[0], nums[2] + 1):
        for y in range(nums[1], nums[3] + 1):
            p = x, y
            if l.startswith("turn on"):
                lights.add(p)
                brightness[p] += 1
            elif l.startswith("turn off"):
                lights.discard(p)
                brightness[p] = max(0, brightness[p] - 1)
            elif l.startswith("toggle"):
                if p in lights:
                    lights.remove(p)
                else:
                    lights.add(p)
                brightness[p] += 2

p1 = len(lights)
p2 = 0
for b in brightness.values():
    p2 += b

print("Part 1: " + str(p1))
print("Part 2: " + str(p2))
