with open('input.txt') as file:
    lines = [line.rstrip() for line in file]

target = {}
target["children"] = 3
target["cats"] = 7
target["samoyeds"] = 2
target["pomeranians"] = 3
target["akitas"] = 0
target["vizslas"] = 0
target["goldfish"] = 5
target["trees"] = 3
target["cars"] = 2
target["perfumes"] = 1

p1 = None
p2 = None

for l in lines:
    _, id, a, na, b, nb, c, nc = l.split(" ")
    id = int(id[:-1])
    a = a[:-1]
    b = b[:-1]
    c = c[:-1]
    na = int(na[:-1])
    nb = int(nb[:-1])
    nc = int(nc)
    props = [(a, na), (b, nb), (c, nc)]

    if all(target[k] == n for k, n in props):
        p1 = id

    valid = True
    for p in props:
        k, n = p
        if k in ("cats", "trees"):
            valid &= n > target[k]
        elif k in ("pomeranians", "goldfish"):
            valid &= n < target[k]
        else:
            valid &= n == target[k]
    if valid:
        p2 = id

print("Part 1: " + str(p1))
print("Part 2: " + str(p2))
