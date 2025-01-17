with open('input.txt') as file:
    lines = [line.rstrip() for line in file]


def count(str, target):
    out = 0
    for c in str:
        if c in target:
            out += 1
    return out


def has_duplicate(str):
    for i in range(len(str)):
        if i > 0:
            if str[i] == str[i - 1]:
                return True
    return False


def how_to_call_this_one(str):
    for i in range(len(str)):
        if i > 1:
            if str[i] == str[i - 2]:
                return True
    return False


def has_double_pair(str):
    for i in range(len(str)):
        if i > 0:
            canditate = str[i - 1:i + 1]
            left = str[:i - 1]
            right = str[i + 1:]
            if canditate in left or canditate in right:
                return True
    return False


p1 = 0
p2 = 0

for l in lines:
    if count(l, list("aeiou")) >= 3 and has_duplicate(l) and not any(s in l for s in ["ab", "cd", "pq", "xy"]):
        p1 += 1
    if how_to_call_this_one(l) and has_double_pair(l):
        p2 += 1

print("Part 1: " + str(p1))
print("Part 2: " + str(p2))
