with open('input.txt') as file:
    lines = [line.rstrip() for line in file]


def f(wire):
    if wire not in solved:
        con = connections[wire]
        if con.islower():
            solved[wire] = f(con)
        elif con.isnumeric():
            solved[wire] = int(con)
        elif "AND" in con:
            l, r = con.split(" AND ")
            if l.isnumeric():
                l = int(l)
            else:
                l = f(l)
            if r.isnumeric():
                r = int(r)
            else:
                r = f(r)
            solved[wire] = l & r
        elif "LSHIFT" in con:
            l, r = con.split(" LSHIFT ")
            if l.isnumeric():
                l = int(l)
            else:
                l = f(l)
            r = int(r)
            solved[wire] = (l << r) & (2 ** 16 - 1)
        elif "RSHIFT" in con:
            l, r = con.split(" RSHIFT ")
            if l.isnumeric():
                l = int(l)
            else:
                l = f(l)
            r = int(r)
            solved[wire] = l >> r
        elif "OR" in con:
            l, r = con.split(" OR ")
            if l.isnumeric():
                l = int(l)
            else:
                l = f(l)
            if r.isnumeric():
                r = int(r)
            else:
                r = f(r)
            solved[wire] = l | r
        elif "NOT" in con:
            w = f(con[4:])
            solved[wire] = 2 ** 16 - 1 - w
    return solved[wire]


solved = {}
connections = {}

for l in lines:
    a, b = l.split(" -> ")
    connections[b] = a

p1 = f("a")

solved.clear()
connections["b"] = str(p1)
p2 = f("a")

print("Part 1: " + str(p1))
print("Part 2: " + str(p2))
