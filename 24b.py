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


def run(inp: tuple[int], w=0, x=0, y=0, z=0):
    return z


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
    return z == 0

number = 17153114691118
print(number, is_valid(list(int(i) for i in str(number))))
