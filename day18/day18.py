with open('input.txt') as file:
    lines = [line.rstrip() for line in file]


def get_all_nei_2d_8(p):
    x, y = p
    r = [(x, y + 1), (x, y - 1), (x + 1, y), (x - 1, y), (x + 1, y + 1), (x - 1, y - 1), (x + 1, y - 1), (x - 1, y + 1)]
    return r


def f(lights, part2):
    if part2:
        lights.update(corners)
    for _ in range(100):
        next = set()
        for y in range(0, Y):
            for x in range(0, X):
                p = x, y
                active_nei = len([n for n in get_all_nei_2d_8(p) if n in lights])
                if p in lights:
                    if active_nei in (2, 3):
                        next.add(p)
                else:
                    if active_nei == 3:
                        next.add(p)
        lights = next
        if part2:
            lights.update(corners)
    return len(lights)


X = len(lines[0])
Y = len(lines)

lights = set()

for y in range(0, Y):
    for x in range(0, X):
        if lines[y][x] == "#":
            lights.add((x, y))

corners = [(0, 0), (X - 1, 0), (X - 1, Y - 1), (0, Y - 1)]

p1 = f(lights.copy(), False)
print("Part 1: " + str(p1))

p2 = f(lights.copy(), True)
print("Part 2: " + str(p2))
