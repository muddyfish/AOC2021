class BingoBoard:
    def __init__(self, board: list[list[int]]):
        self.board = board
        self.marks = set()

    def __repr__(self):
        return f"BingoBoard({self.board!r})"

    def mark(self, number: int):
        for y, line in enumerate(self.board):
            try:
                x = line.index(number)
                self.marks.add((x, y))
            except ValueError:
                pass

    def is_winner(self):
        if len(self.marks) < 5:
            return False
        for i in range(5):
            if self.marks >= {(j, i) for j in range(5)}:
                return True
            if self.marks >= {(i, j) for j in range(5)}:
                return True
        return False

    def get_unmarked(self):
        for y, row in enumerate(self.board):
            yield from (value for x, value in enumerate(row) if (x, y) not in self.marks)

    def get_marked(self):
        for y, row in enumerate(self.board):
            yield from (value for x, value in enumerate(row) if (x, y) in self.marks)


def get_winning_board(boards: list[BingoBoard], numbers: list[int]) -> (int, BingoBoard):
    for number in numbers:
        for board in boards:
            board.mark(number)
            if board.is_winner():
                return number, board


def main():
    with open("4.txt") as f:
        numbers = [int(i) for i in f.readline().strip().split(",")]
        boards = []
        for line in f.readlines():
            line = line.strip()
            if line:
                board.append([int(i) for i in line.split(" ") if i.strip(" ")])
            else:
                board = []
                boards.append(board)

    boards = [BingoBoard(board) for board in boards]
    number, winner = get_winning_board(boards, numbers)
    print(sum(winner.get_unmarked()) * number)


if __name__ == "__main__":
    main()
