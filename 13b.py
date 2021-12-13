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


for dir, line in folds:
    axis = "xy".index(dir)

    for point in list(points):
        if point[axis] > line:
            points.remove(point)
            if axis == 0:
                points.add((2 * line - point[0], point[1]))
            else:
                points.add((point[0], 2 * line - point[1]))

x = 1 + max(x for x, _ in points)
y = 1 + max(y for _, y in points)
for y_ in range(y):
    print("".join(" #"[(x_, y_) in points] for x_ in range(x)))
