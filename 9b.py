from math import prod

with open("9.txt") as f:
    grid = [[int(i) for i in line.strip("\n")] for line in f.readlines()]


def get_adjacent(grid, x: int, y: int):
    if y != 0:
        yield y-1, x
    if y != len(grid) - 1:
        yield y+1, x
    if x != 0:
        yield y, x-1
    if x != len(grid[0]) - 1:
        yield y, x+1


def do_floodfill(grid, x: int, y: int):
    if grid[y][x] != 1:
        return 0
    grid[y][x] = 2
    return 1 + sum(do_floodfill(grid, x_, y_) for y_, x_ in get_adjacent(grid, x, y))


for y, line in enumerate(grid):
    for x, value in enumerate(line):
        grid[y][x] = int(value != 9)


basin_sizes = []
for y, line in enumerate(grid):
    for x, value in enumerate(line):
        if value == 1:
            # New floodfill
            basin_sizes.append(do_floodfill(grid, x, y))

basin_sizes.sort()
print(prod(basin_sizes[-3:]))
