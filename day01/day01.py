with open('input.txt') as file:
    lines = [line.rstrip() for line in file]

p1 = 0
p2 = None
for i, c in enumerate(lines[0]):
    if p2 is None and p1 == -1:
        p2 = i
    match c:
        case "(":
            p1 += 1
        case ")":
            p1 -= 1

print("Part 1: " + str(p1))
print("Part 2: " + str(p2))
