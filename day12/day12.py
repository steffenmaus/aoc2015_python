import re

with open('input.txt') as file:
    lines = [line.rstrip() for line in file]


def all_ints_in_string(s):
    return [int(n) for n in re.findall(r'-?\d+', s)]


def extract_next_json(str):
    depth = 0
    for i in range(len(str)):
        current = str[i:]
        if current.startswith("{"):
            depth += 1
        elif current.startswith("}"):
            depth -= 1
            if depth == 0:
                return str[:i + 1]


def contains_red(json):
    depth = 0
    for i in range(len(json)):
        current = json[i:]
        if current.startswith("{"):
            depth += 1
        elif current.startswith("}"):
            depth -= 1
        elif depth == 1 and current.startswith(":\"red\""):
            return True
    return False


p1 = 0
p2 = 0

for n in all_ints_in_string(lines[0]):
    p1 += n

i = 0
while i < len(lines[0]):
    current = lines[0][i:]
    if current.startswith("{"):
        njson = extract_next_json(current)
        if contains_red(njson):
            i += len(njson) - 1
    else:
        res = re.match(r'-?\d+', current)
        if res is not None:
            p2 += int(res[0])
            i += len(res[0]) - 1
    i += 1

print("Part 1: " + str(p1))
print("Part 2: " + str(p2))
