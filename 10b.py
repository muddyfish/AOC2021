brackets = {
    "{": "}",
    "(": ")",
    "[": "]",
    "<": ">"
}

errors = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4
}


with open("10.txt") as f:
    lines = [line.strip("\n") for line in f.readlines()]

all_scores = []
for line in lines:
    lscore = 0
    stack = []
    for char in line:
        if char in brackets:
            stack.append(char)
        elif char == brackets[stack[-1]]:
            stack.pop()
        else:
            break
    else:
        for score in (errors[brackets[i]] for i in reversed(stack)):
            lscore = lscore * 5 + score
        all_scores.append(lscore)

all_scores.sort()
print(all_scores[len(all_scores) // 2])
