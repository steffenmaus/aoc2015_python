with open('input.txt') as file:
    lines = [line.rstrip() for line in file]

code_len = 0
mem_len = 0
newly_len = 0

for l in lines:
    code_len += len(l)
    newly_len += len(l) + l.count("\"") + l.count("\\") + 2
    trimmed = l[1:-1]
    i = 0
    while i < len(trimmed):
        c = trimmed[i]
        if c == "\\":
            if trimmed[i + 1] == "x":
                mem_len += 1
                i += 4
            else:
                mem_len += 1
                i += 2
        else:
            mem_len += 1
            i += 1

p1 = code_len - mem_len
p2 = newly_len - code_len

# low 1098
# low 1327
# false 1474
# high 941432
print("Part 1: " + str(p1))
print("Part 2: " + str(p2))
