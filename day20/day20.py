input = 36000000
import math

prim_cache = {}


def get_prim_factors(n):
    if n < 2:
        return {}
    if n in prim_cache:
        return prim_cache[n]
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            out = {i}
            out.update(get_prim_factors((n // i)))
            prim_cache[n] = out
            return out
    prim_cache[n] = {n}
    return {n}


div_cache = {}


def get_divisors(n):
    if n < 1:
        return {}
    if n in div_cache:
        return div_cache[n]
    out = {1, n}
    if n == 1:
        return out
    for p in get_prim_factors(n):
        out.add(p)
        out.add(n // p)
        out.update(get_divisors(n // p))

    div_cache[n] = out
    return out


n = 0
p1 = None
p2 = None
while p1 is None or p2 is None:
    n += 1 * 2 * 3 * 4 * 5  # increase only by 1 to be on the safe side...
    divisors = get_divisors(n)
    if p1 is None and (sum(divisors) * 10) >= input:
        p1 = n
    if p2 is None:
        count = 0
        for d in divisors:
            if (n / d) <= 50:
                count += d
        if count * 11 >= input:
            p2 = n

print("Part 1: " + str(p1))
print("Part 2: " + str(p2))
