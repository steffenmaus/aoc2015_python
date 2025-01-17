import sys

with open('input.txt') as file:
    lines = [line.rstrip() for line in file]


def calc_quantum_entanglement(packages):
    out = 1
    for p in packages:
        out *= p
    return out


def find_subsets_limited_size(selected, remaining, target_sum, limit_size):
    if sum(selected) == target_sum:
        return [selected]
    else:
        out = []
        if sum(selected) < target_sum and len(selected) < limit_size:
            for i, p in enumerate(remaining):
                out += find_subsets_limited_size(selected.union({p}), remaining[i + 1:], target_sum, limit_size)
        return out


def can_be_evenly_divided(selected, remaining, target_sum):
    if sum(selected) == target_sum:
        if remaining == []:
            return True
        else:
            return can_be_evenly_divided(set(), [p for p in remaining if p not in selected], target_sum)
    elif sum(selected) > target_sum:
        return False
    else:
        for i, p in enumerate(remaining):
            if can_be_evenly_divided(selected.union({p}), remaining[i + 1:], target_sum):
                return True
    return False


def f(groups_total):
    target_weight = sum(packages) // groups_total

    size = 1
    legroom_candidates = []
    while legroom_candidates == []:
        legroom_candidates = find_subsets_limited_size(set(), packages, target_weight, size)
        size += 1

    best = sys.maxsize
    for c in legroom_candidates:
        if can_be_evenly_divided(set(), [p for p in packages if p not in c], target_weight):
            best = min(best, calc_quantum_entanglement(c))
    return best


packages = []
for l in lines:
    n = int(l)
    packages.append(n)

p1 = f(3)
print("Part 1: " + str(p1))

p2 = f(4)
print("Part 2: " + str(p2))
