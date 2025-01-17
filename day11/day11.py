from string import ascii_lowercase


def get_next_password(password):
    out = []
    inc = True
    for pos in reversed(range(8)):
        prev = password[pos]
        if inc:
            out.append(next_char[prev])
            inc = out[-1] == "a"
        else:
            out.append(prev)
    return out[::-1]


def has_increasing_straight(password):
    for i in range(len(password)):
        if i > 1:
            a, b, c = password[i - 2:i + 1]
            if next_char[a] == b and next_char[b] == c and b != "a" and c != "a":
                return True
    return False


def has_no_confuse_chars(password):
    return not any(c in password for c in ("i", "o", "l"))


def has_two_pairs(password):
    pairs = set()
    for i in range(len(password)):
        if i > 0:
            if password[i - 1] == password[i]:
                pairs.add(password[i])
    return len(pairs) > 1


def is_valid_password(password):
    return has_increasing_straight(password) & has_no_confuse_chars(password) & has_two_pairs(password)


def f(input):
    password = get_next_password(list(input))
    while not is_valid_password(password):
        password = get_next_password(password)
    return "".join(password)


next_char = {}
for i, c in enumerate(ascii_lowercase):
    if i > 0:
        next_char[ascii_lowercase[i - 1]] = c
next_char["z"] = "a"

input = "hxbxwxba"

p1 = f(input)
print("Part 1: " + str(p1))

p2 = f(p1)
print("Part 2: " + str(p2))
