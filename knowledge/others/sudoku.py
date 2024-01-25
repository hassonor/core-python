# Validate a Sudoku board
def is_valid_sudoku_board(board):
    for i in range(9):
        row = {}
        col = {}
        box = {}
        for j in range(9):
            if board[i][j] != '.' and board[i][j] in row:
                return False
            row[board[i][j]] = 1

            if board[j][i] != '.' and board[j][i] in col:
                return False
            row[board[j][i]] = 1

            row_index = 3 * (i // 3)
            col_index = 3 * (i % 3)
            if board[row_index + j // 3][col_index + j % 3] != '.' and board[row_index + j // 3] \
                    [col_index + j % 3] in box:
                return False
            box[board[row_index + j // 3][col_index + j % 3]] = 1
    return True


# Sudoku Solver
def solve_sudoku(board):
    def is_valid(x, y, val):
        for i in range(9):
            if board[x][i] == val:
                return False
            if board[i][y] == val:
                return False
            if board[3 * (x // 3) + i // 3][3 * (y // 3) + i % 3] == val:
                return False
        return True

    def solve():
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    for c in range(1, 10):
                        if is_valid(i, j, str(c)):
                            board[i][j] = str(c)
                            if solve():
                                return True
                            else:
                                board[i][j] = '.'
                    return False
        return True

    solve()
    return board
