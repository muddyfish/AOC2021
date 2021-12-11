def get_adjacent(grid, y, x):
    if y != 0:
        yield y-1, x
        if x != 0:
            yield y-1, x-1
        if x != len(grid[0]) - 1:
            yield y-1, x+1
    if y != len(grid) - 1:
        yield y+1, x
        if x != 0:
            yield y+1, x-1
        if x != len(grid[0]) - 1:
            yield y+1, x+1
    if x != 0:
        yield y, x-1
    if x != len(grid[0]) - 1:
        yield y, x+1


with open("11.txt") as f:
    grid = [[int(i) for i in line.strip("\n")] for line in f.readlines()]

flashes = 0


def inc_pos(grid, y, x):
    global flashes
    grid[y][x] += 1
    if grid[y][x] == 10:
        flashes += 1
        for y_, x_ in get_adjacent(grid, y, x):
            inc_pos(grid, y_, x_)


for step in range(100):
    for y, line in enumerate(grid):
        for x, value in enumerate(line):
            inc_pos(grid, y, x)
    for y, line in enumerate(grid):
        for x, value in enumerate(line):
            if value > 9:
                grid[y][x] = 0

#print("\n".join("".join(map(str, line)) for line in grid))
print(flashes)
