def f(seed, depth):
    current = list(seed)
    for _ in range(depth):
        next = []
        c = current[0]
        count = 0
        for i in range(len(current)):
            if current[i] != c:
                next.append(str(count))
                next.append(c)
                c = current[i]
                count = 1
            else:
                count += 1
        next.append(str(count))
        next.append(c)
        current = next
    return current


input = "1113222113"

p1 = len(f(input, 40))
p2 = len(f(input, 50))

print("Part 1: " + str(p1))
print("Part 2: " + str(p2))
