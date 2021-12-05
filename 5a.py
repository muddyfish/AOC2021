import re
from itertools import permutations

regex = re.compile(r"(\d+),(\d+) -> (\d+),(\d+)")


def abs_range(a: int, b: int):
    if a > b:
        return range(b, a+1)
    return reversed(range(a, b+1))


with open("5.txt") as f:
    lines = [regex.match(i.strip()).groups() for i in f.readlines()]
    lines = [((int(i), int(j)), (int(k), int(l))) for i, j, k, l in lines]

valid_lines = []
for ((x1, y1), (x2, y2)) in lines:
    if x1 == x2:
        valid_lines.append({(x1, i) for i in abs_range(y1, y2)})
    elif y1 == y2:
        valid_lines.append({(i, y1) for i in abs_range(x1, x2)})
    else:
        pass

overlaps = set()
for l1, l2 in permutations(valid_lines, 2):
    overlaps |= l1 & l2

print(len(overlaps))
