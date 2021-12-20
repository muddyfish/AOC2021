from collections import defaultdict
grid = defaultdict(lambda: False)

with open("20.txt") as f:
    enhancements = [i == "#" for i in f.readline().strip()]
    f.readline()
    for y, line in enumerate(f.readlines()):
        line = line.strip()
        for x, value in enumerate(line):
            grid[(x, y)] = value == "#"


def get_adjacent(pos):
    x, y = pos
    return [
        (x+1, y+1), (x, y+1), (x-1, y+1),
        (x+1, y), (x, y), (x-1, y),
        (x+1, y-1), (x, y-1), (x-1, y-1),
    ]


def process_step(grid):
    min_x = min(x for x, y in grid.keys()) - 1
    min_y = min(y for x, y in grid.keys()) - 1
    max_x = max(x for x, y in grid.keys()) + 2
    max_y = max(y for x, y in grid.keys()) + 2
    if enhancements[0]:
        background_colour = grid["_"]
        new_grid = defaultdict(lambda: not background_colour)
    else:
        new_grid = defaultdict(lambda: False)

    for y in range(min_y, max_y):
        for x in range(min_x, max_x):
            new_grid[(x, y)] = enhancements[sum(grid[adj]*(2**i) for i, adj in enumerate(get_adjacent((x, y))))]
    return new_grid


def print_grid(grid):
    min_x = min(x for x, y in grid.keys())
    min_y = min(y for x, y in grid.keys())
    max_x = max(x for x, y in grid.keys()) + 1
    max_y = max(y for x, y in grid.keys()) + 1
    for y in range(min_y, max_y):
        print("".join(".#"[grid[(x, y)]] for x in range(min_x, max_x)))


for _ in range(2):
    grid = process_step(grid)
print_grid(grid)
print(sum(grid.values()))
