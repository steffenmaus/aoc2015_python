with open('input.txt') as file:
    lines = [line.rstrip() for line in file]


def f(a):
    r = {}
    r["a"] = a
    r["b"] = 0

    i = 0
    while i in range(len(lines)):
        l = lines[i]
        if l.startswith("hlf"):
            r[l.split(" ")[1]] = r[l.split(" ")[1]] // 2
        elif l.startswith("tpl"):
            r[l.split(" ")[1]] *= 3
        elif l.startswith("inc"):
            r[l.split(" ")[1]] += 1
        elif l.startswith("jmp"):
            i += int(l.split(" ")[1]) - 1
        elif l.startswith("jie"):
            if r[l.split(" ")[1][0]] % 2 == 0:
                i += int(l.split(" ")[2]) - 1
        elif l.startswith("jio"):
            if r[l.split(" ")[1][0]] == 1:
                i += int(l.split(" ")[2]) - 1

        i += 1

    return r["b"]


p1 = f(0)
p2 = f(1)

print("Part 1: " + str(p1))
print("Part 2: " + str(p2))

"""


def sort_tuples_by_second(tuples):
    return sorted(tuples, key=lambda t: t[1])


def sort_dict_by_content(dict):
    l = []
    for k in dict:
        l.append((k, dict[k]))
    return sort_tuples_by_second(l)


min_x = min([p[0] for p in nodes])
max_x = max([p[0] for p in nodes])
min_y = min([p[1] for p in nodes])
max_y = max([p[1] for p in nodes])


def get_deltas(ints):
    deltas = []
    prev = ints[0]
    for i in range(1, len(ints)):
        deltas.append(ints[i] - prev)
        prev = ints[i]
    return deltas


def count(grid,e):
    c = 0
    for x in grid:
        for y in x:
            if y == e:
                c += 1
    return c


def contains(grid,e):
    for x in grid:
        for y in x:
            if y == e:
                return True
    return False

def get_all_nei_2d_4(p):
    x, y = p
    r = [(x, y + 1), (x, y - 1), (x + 1, y), (x - 1, y)]
    return r


def get_all_nei_2d_8(p):
    x, y = p
    r = get_all_nei_2d_4(p) + [(x + 1, y + 1), (x - 1, y - 1), (x + 1, y - 1), (x - 1, y + 1)]
    return r

def get_all_nei_3d_6(p):
    r = []
    x,y,z = p
    for dx in (-1,0,1):
        for dy in (-1,0,1):
            for dz in (-1,0,1):
                if abs(dx) + abs(dy) + abs(dz) == 1:
                    r.append((x+dx,y+dy,z+dz))
    return r

def get_default_distances_in_maze():
    distances = defaultdict(list)
    for y in range(Y):
        for x in range(X):
            p = (x,y)
            if maze[p] == ".":
                for n in get_all_nei_2d_4(p):
                    distances[p].append((n,1))
    return distances

def get_all_nei_2d_within_man_dist(p, max_dist):
    x, y = p
    out = set()
    for d in range(1, max_dist + 1):
        for dx in range(d+1):
            dy = d - dx
            out.add((x + dx, y + dy))
            out.add((x + dx, y - dy))
            out.add((x - dx, y + dy))
            out.add((x - dx, y - dy))
    return out




def cart_to_rad(x, y):
    if x > 0:
        return math.atan(y / x)
    elif x < 0 and y >= 0:
        return math.atan(y / x) + math.pi
    elif x < 0 and y < 0:
        return math.atan(y / x) - math.pi
    elif x == 0 and y > 0:
        return math.pi / 2
    elif x == 0 and y < 0:
        return -math.pi / 2
   

def flood_maze(maze, start):
    open = set()
    completed = set()
    open.add(start)
    while open:
        current = open.pop()
        completed.add(current)
        for n in get_all_nei_2d_4(current): #TODO change nei
            if n in maze.keys() and n not in completed:
                if maze[n] == ".": #TODO change reqs
                    open.add(n)
    return completed

def add_ring_around_maze(maze, c):
    out = maze.copy()
    for x in range(min([p[0] for p in maze.keys()]) - 1, max([p[0] for p in maze.keys()]) + 2):
        for y in range(min([p[1] for p in maze.keys()]) - 1, max([p[1] for p in maze.keys()]) + 2):
            p = (x, y)
            if p not in maze.keys():
                out[p] = c
    return out
     

def steps_in_maze(maze, start):
    out = {}
    border = set()
    border.add(start)
    completed = set()
    steps = 0
    while border:
        next_border = set()
        completed.update(border)
        for p in border:
            out[p] = steps
            for n in get_all_nei_2d_4(p): #TODO change nei
                if n in maze.keys() and n not in completed:
                    if maze[n] == ".": #TODO change reqs
                        next_border.add(n)
        border = next_border
        steps +=1
    return out

#shortestpath:2022d12
#"https://www.youtube.com/watch?v=bZkzH5x0SKU"
import heapq
def dijkstra_full(start, distances): #distances[a] = [(b,10),(c,19)]
    out = {}
    out_paths = {} #TODO verify
    out[start] = 0
    out_paths[start] = [start]
    Q = []
    for nei in distances[start]:
        node, dist = nei
        heapq.heappush(Q, (dist, node, start))
    while len(out.keys()) != len(distances.keys()):
        dist, current, prev = heapq.heappop(Q)
        if current not in out.keys():
            out[current] = dist
            path = out_paths[prev].copy()
            path.append(current)
            out_paths[current] = path
            for nei in distances[current]:
                n, d = nei
                heapq.heappush(Q, (d + dist, n, current))
    return out, out_paths


def draw_points(points):
    min_x = min([p[0] for p in points])
    max_x = max([p[0] for p in points])
    min_y = min([p[1] for p in points])
    max_y = max([p[1] for p in points])
    for y in range(min_y, max_y + 1):
        line = ""
        for x in range(min_x, max_x + 1):
            if (x, y) in points:
                line += "█"
            else:
                line += " "
        print(line)


def draw_maze(points):
    min_x = min([p[0] for p in points])
    max_x = max([p[0] for p in points])
    min_y = min([p[1] for p in points])
    max_y = max([p[1] for p in points])
    for y in range(min_y, max_y + 1):
        line = ""
        for x in range(min_x, max_x + 1):
            if (x, y) in points:
                line += points[(x,y)]
            else:
                line += "?"
        print(line)
"""
