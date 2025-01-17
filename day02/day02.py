with open('input.txt') as file:
    lines = [line.rstrip() for line in file]

p1 = 0
p2 = 0

for line in lines:
    l, w, h = list(map(int, line.split("x")))
    s = sorted([l, w, h])
    a = l * w
    b = w * h
    c = h * l
    p1 += 2 * (a + b + c) + min(a, b, c)
    p2 += 2 * (s[0] + s[1]) + (l * w * h)

print("Part 1: " + str(p1))
print("Part 2: " + str(p2))
