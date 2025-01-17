with open('input.txt') as file:
    lines = [line.rstrip() for line in file]


def next_code(code):
    return (code * 252533) % 33554393


def code_at(code, steps):
    return (pow(252533, steps, 33554393) * code) % 33554393


def f_slow(init, row, column):
    code = init
    pos = 1, 1
    steps = 1
    while pos != (row, column):
        if pos[0] == 1:
            pos = (pos[1] + 1, 1)
        else:
            pos = (pos[0] - 1, pos[1] + 1)
        code = next_code(code)
        steps += 1
    return code


def f_efficient(init, row, column):
    target_y = row + column - 1
    y = 1
    step_size = 1
    steps_total = 0
    while y != target_y:
        steps_total += step_size
        step_size += 1
        y += 1
    steps_total += column - 1
    return code_at(init, steps_total)


row = int(lines[0].split(" ")[-3][:-1])
column = int(lines[0].split(" ")[-1][:-1])

init = 20151125

p1 = f_efficient(init, row, column)
# p1 = f_slow(init, row, column)
print("Part 1: " + str(p1))
