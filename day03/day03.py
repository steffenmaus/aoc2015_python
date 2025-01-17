with open('input.txt') as file:
    lines = [line.rstrip() for line in file]


def f(moves):
    x, y = 0, 0
    points = {(x, y)}
    for c in moves:
        match c:
            case "^":
                y -= 1
            case "v":
                y += 1
            case "<":
                x -= 1
            case ">":
                x += 1
        points.add((x, y))
    return points


p1 = len(f(lines[0]))

a = f(lines[0][::2])
b = f(lines[0][1::2])
p2 = len(a.union(b))
print("Part 1: " + str(p1))
print("Part 2: " + str(p2))
