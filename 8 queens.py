def is_safe(board, row, col):
    # Check this row on left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on left side
    for i, j in zip(range(row, len(board)), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solve_n_queens_util(board, col):
    global step_count
    if col >= len(board):
        step_count += 1
        return True

    for i in range(len(board)):
        if is_safe(board, i, col):
            board[i][col] = 1  # Place queen
            if solve_n_queens_util(board, col + 1):
                return True
            board[i][col] = 0  # Backtrack

    return False

def solve_n_queens(n):
    global step_count
    step_count = 0
    board = [[0] * n for _ in range(n)]
    if solve_n_queens_util(board, 0):
        print("Final Board Configuration:")
        for row in board:
            print(" ".join("Q" if x else "." for x in row))
    else:
        print("No solution exists")

# Set the size of the chessboard
n = 8
solve_n_queens(n)