with open("9.txt") as f:
    grid = [[int(i) for i in line.strip("\n")] for line in f.readlines()]


def get_adjacent(grid, x, y):
    if y != 0:
        yield grid[y-1][x]
    if y != len(grid) - 1:
        yield grid[y+1][x]
    if x != 0:
        yield grid[y][x-1]
    if x != len(grid[0]) - 1:
        yield grid[y][x+1]

acc = 0
for y, line in enumerate(grid):
    for x, value in enumerate(line):
        adjacent = list(get_adjacent(grid, x, y))
        if min(adjacent) > value:
            acc += value + 1

print(acc)
