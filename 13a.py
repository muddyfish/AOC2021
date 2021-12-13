points = set()
folds = []
with open("13.txt") as f:
    lines = iter(f.readlines())
    for line in lines:
        line = line.strip()
        if not line:
            break
        points.add(tuple(map(int, line.split(","))))
    for line in lines:
        dir, value = line.split("=")
        folds.append((dir[-1], int(value)))


dir, line = folds[0]
axis = "xy".index(dir)

for point in set(points):
    if point[axis] > line:
        points.remove(point)
        if axis == 0:
            points.add((2 * line - point[0], point[1]))
        else:
            points.add((point[0], 2 * line - point[1]))

print(len(points))
