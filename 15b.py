from dijkstar import Graph, find_path


def get_adjacent(grid, x: int, y: int):
    if y != 0:
        yield y-1, x
    if y != len(grid) - 1:
        yield y+1, x
    if x != 0:
        yield y, x-1
    if x != len(grid[0]) - 1:
        yield y, x+1


with open("15.txt") as f:
    grid = [[int(i) for i in line.strip("\n")] for line in f.readlines()]
    for _ in range(2):
        grid = [list(i) for i in zip(*grid)]
        for line in grid:
            orig_line = line[:]
            for i in range(1, 5):
                line.extend(j+i for j in orig_line)


graph = Graph(undirected=False)

for y, line in enumerate(grid):
    for x, value in enumerate(line):
        for y_, x_ in get_adjacent(grid, x, y):
            value = grid[y_][x_]
            if value > 9:
                value -= 9
            graph.add_edge((x, y), (x_, y_), value)

path = find_path(graph, (0, 0), (x, y))
print(path.total_cost)
