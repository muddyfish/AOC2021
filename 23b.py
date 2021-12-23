with open("23.txt") as f:
    f.readline()
    f.readline()

    a, b, c, d = [], [], [], []
    for i in range(4):
        a_, b_, c_, d_ = f.readline().strip(" #\n")[::2]
        a.append(a_)
        b.append(b_)
        c.append(c_)
        d.append(d_)


costs = {"A": 1, "B": 10, "C": 100, "D": 1000}
destination_zones = {"A": 2, "B": 4, "C": 6, "D": 8}
# [(".", ".", "AAAA", ".", "BBBB", ".", "CCCC", ".", "DDDD", ".", ".")]


def can_reach(board, source_index: int, destination_index: int) -> bool:
    for index in range(min(source_index, destination_index)+1, max(source_index, destination_index)):
        if len(board[index]) == 1 and board[index] != ".":
            return False
    return True


def is_valid_move(board, character: str, source_index: int, destination_index: int) -> bool:
    if len(board[destination_index]) == 4:
        if destination_zones[character] != destination_index:
            return False
        if not (set(".DDD") <= {".", "A"}):
            return False
    return can_reach(board, source_index, destination_index)


def generate_dest(board, stripped: str, source_index: int, destination_index: int):
    new_board = board[:]
    dest = board[destination_index]
    assert "." in dest
    new_board[destination_index] = (stripped[0] + dest.strip(".")).rjust(len(dest), ".")
    new_board[source_index] = stripped[1:].rjust(len(board[source_index]), ".")
    return new_board


def get_possible_moves(board) -> list:
    for source_index, pos in enumerate(board):
        stripped = pos.strip(".")
        if stripped:
            char_to_move = stripped[0]
            if len(pos) == 1:
                dest_index = destination_zones[char_to_move]
                pos2 = board[dest_index]
                if set(pos2) <= {".", char_to_move} and can_reach(board, source_index, dest_index):
                    yield generate_dest(board, stripped, source_index, dest_index), costs[char_to_move] * (abs(source_index-dest_index) + pos.count(".") + pos2.count("."))
                continue

            if destination_zones[char_to_move] == source_index and set(pos) <= {".", char_to_move}:
                # Already in position
                continue

            for dest_index, pos2 in enumerate(board):
                if "." in pos2 and is_valid_move(board, char_to_move, source_index, dest_index):
                    yield generate_dest(board, stripped, source_index, dest_index), costs[char_to_move] * (abs(source_index-dest_index) + pos.count(".") + pos2.count("."))


def solve(board):
    states = {tuple(board): 0}
    queue = [board]
    while queue:
        board = queue.pop()
        initial_cost = states[tuple(board)]
        possible_moves = get_possible_moves(board)
        for move, new_cost in possible_moves:
            tuple_move = tuple(move)
            if tuple_move not in states or states[tuple_move] > initial_cost + new_cost:
                states[tuple_move] = initial_cost + new_cost
                queue.append(move)
    return states[(".", ".", "AAAA", ".", "BBBB", ".", "CCCC", ".", "DDDD", ".", ".")]


start = [".", ".", "".join(a), ".", "".join(b), ".", "".join(c), ".", "".join(d), ".", "."]
final = solve(start)
print(final)
