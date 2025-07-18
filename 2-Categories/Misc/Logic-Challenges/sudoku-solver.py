def is_valid(board, row, col, num):
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False
    x, y = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[x+i][y+j] == num:
                return False
    return True

def solve(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                for num in range(1, 10):
                    if is_valid(board, row, col, num):
                        board[row][col] = num
                        if solve(board):
                            return True
                        board[row][col] = 0
                return False
    return True

# Example usage
puzzle = [
    [5, 0, 0, 0, 0, 0, 0, 0, 2],
    [0, 0, 0, 5, 0, 1, 0, 0, 0],
    [0, 2, 0, 0, 0, 0, 0, 3, 0],
    [0, 0, 1, 0, 0, 0, 7, 0, 0],
    [0, 0, 0, 3, 0, 2, 0, 0, 0],
    [0, 0, 5, 0, 0, 0, 2, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 9, 0],
    [0, 0, 0, 8, 0, 6, 0, 0, 0],
    [2, 0, 0, 0, 0, 0, 0, 0, 5],
]

solve(puzzle)
for row in puzzle:
    print(row)