def is_valid(board):
    for i in range(9):
        row = {}
        col = {}
        box = {}
        for j in range(9):
            if board[i][j] != "." and board[i][j] in row:
                return False
            row[board[i][j]] = 1
            if board[j][i] != "." and board[j][i] in col:
                return False
            col[board[j][i]] = 1

            row_index = 3 * (i // 3)
            col_index = 3 * (i % 3)
            if board[row_index + j // 3][col_index + j % 3] != "." and board[row_index + j // 3][
                col_index + j % 3] in box:
                return False
            box[board[row_index + j // 3][col_index + j % 3]] = 1

    return True


print(is_valid([["5", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."],
                [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
                ["4", ".", ".", "8", ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"],
                [".", ".", ".", ".", "8", ".", ".", "7", "9"]]))
