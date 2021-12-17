import re

regex = re.compile(r"target area: x=(-?\d+)..(-?\d+), y=(-?\d+)..(-?\d+)")

with open("17.txt") as f:
    data = regex.match(f.readline().strip())
    x1, x2, y1, y2 = map(int, data.groups())

print((y1 * (y1 + 1)) // 2)
