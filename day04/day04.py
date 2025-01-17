import hashlib

input = "iwrupvqb"


def md5(str):
    return hashlib.md5(str.encode()).hexdigest()


def f(prefix):
    i = 0
    while not md5(input + str(i)).startswith(prefix):
        i += 1
    return i


p1 = f("00000")
print("Part 1: " + str(p1))

p2 = f("000000")
print("Part 2: " + str(p2))
