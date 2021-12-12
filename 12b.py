import copy


class Node:
    def __init__(self, name: str):
        self.name = name
        self.conns = []

    def __repr__(self):
        return f"Node({self.name!r})"

    def add_conn(self, conn: "Node"):
        self.conns.append(conn)

    @property
    def is_start(self):
        return self.name == "start"

    @property
    def is_end(self):
        return self.name == "end"

    @property
    def is_small(self):
        return self.name.islower()


with open("12.txt") as f:
    paths = [line.strip("\n").split("-") for line in f.readlines()]


nodes = {}
for start, end in paths:
    if start not in nodes:
        nodes[start] = Node(start)
    if end not in nodes:
        nodes[end] = Node(end)

    nodes[start].add_conn(nodes[end])
    nodes[end].add_conn(nodes[start])


def visit_node(node: Node, visited: set[str]) -> int:
    if node.is_end:
        return 1
    do_extra = False
    if node.is_small:
        if node.name in visited:
            if "EXTRA" in visited or node.is_start:
                return 0
            do_extra = True
        visited.add(node.name)
    count = 0
    for conn in node.conns:
        if do_extra:
            count += visit_node(conn, {*visited, "EXTRA"})
        else:
            count += visit_node(conn, copy.deepcopy(visited))
    return count


total = visit_node(nodes["start"], set())
print(total)
