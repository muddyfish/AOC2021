import textwrap

input_number = -1


def convert(line):
    global input_number
    operator, *operands = line.split(" ")
    if operator == "inp":
        input_number += 1
        return f"{operands[0]} = inp[{input_number}]"
    a, b = operands
    if operator == "add":
        return f"{a} += {b}"
    elif operator == "mul":
        return f"{a} *= {b}"
    elif operator == "div":
        return f"{a} //= {b}"
    elif operator == "mod":
        return f"{a} %= {b}"
    elif operator == "eql":
        return f"{a} = int({a} == {b})"
    raise AssertionError(f"{operator!r} is not a valid operator")


def run2(inp: tuple[int], w=0, x=0, y=0, z=0):
    x_modifier = [14, 12, 11, -4, 10, 10, 15, -9, -9, 12, -15, -7, -10,  0]
    y_modifier = [ 7,  4,  8,  1,  5, 14, 12, 10,  5,  7,   6,  8,   4,  6]
    z_modifier = [ 1,  1,  1, 26,  1,  1,  1, 26, 26,  1,  26, 26,  26, 26]
    z_stack = []
    for i in range(14):
        w = inp[i]
        try:
            condition = z_stack[-1] + x_modifier[i] == w
        except IndexError:
            condition = x_modifier[i] == w

        if z_modifier[i] == 26:
            if not condition:
                raise AssertionError(i)
            z_stack.pop()
        if not condition:
            z_stack.append(w + y_modifier[i])

    return sum(26**i * val for i, val in enumerate(reversed(z_stack)))


def to_source(lines):
    #print("\n".join(lines))
    indented = textwrap.indent('\n'.join(lines), '    ')
    return compile(
        (
            "def run(inp, w=0, x=0, y=0, z=0):\n"
            f"{indented}\n"
            "    return z"
        ),
        "input",
        "exec"
    )


with open("24.txt") as f:
    lines = [convert(line.strip()) for line in f.readlines()]

exec(to_source(lines))


def is_valid(numbers: tuple[int]):
    z = run(numbers)
    z2 = run2(numbers)
    if z != z2:
        raise AssertionError(z, z2)
    return z == 0

# i[2] = i[3] - 4
# i[6] = i[7] - 3
# i[5] = i[8] - 5
# i[9] = i[10] + 8
# i[4] = i[11] + 2
# i[1] = i[12] -
# i[0] = i[13] - 7

print(is_valid({
    0: 1,
    1: 7,
    2: 1,
    3: 5,
    4: 3,
    5: 1,
    6: 1,
    7: 4,
    8: 6,
    9: 9,
    10: 1,
    11: 1,
    12: 1,
    13: 8
}))

number = 29599469991739
print(is_valid(list(int(i) for i in str(number))))
