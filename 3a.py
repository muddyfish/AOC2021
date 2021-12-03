from statistics import mode

with open("3.txt") as f:
    lines = [l.strip() for l in f.readlines()]

transposed = list(zip(*lines))
most_common = [mode(i) for i in transposed]
num = int("".join(most_common), 2)
invnum = int("".join("10"[int(i)] for i in most_common), 2)

print(num * invnum)
