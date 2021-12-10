brackets = {
    "{": "}",
    "(": ")",
    "[": "]",
    "<": ">"
}

errors = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137
}


with open("10.txt") as f:
    lines = [line.strip("\n") for line in f.readlines()]

acc = 0
for line in lines:
    stack = []
    for char in line:
        if char in brackets:
            stack.append(char)
        elif char == brackets[stack[-1]]:
            stack.pop()
        else:
            acc += errors[char]
            break

print(acc)
