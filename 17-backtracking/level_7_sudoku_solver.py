"""
Level 7: Sudoku Solver

Problem:
Write a program to solve a Sudoku puzzle by filling the empty cells.
A sudoku solution must satisfy:
1. Each of the digits 1-9 must occur exactly once in each row.
2. Each of the digits 1-9 must occur exactly once in each column.
3. Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.

Time Complexity: O(9^(N)) where N is number of empty cells
Space Complexity: O(1) in-place board state
"""

def solve_sudoku(board: list[list[str]]) -> None:
    def is_valid(r, c, char):
        for i in range(9):
            if board[r][i] == char or board[i][c] == char:
                return False
            if board[3 * (r // 3) + i // 3][3 * (c // 3) + i % 3] == char:
                return False
        return True

    def backtrack():
        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    for char in map(str, range(1, 10)):
                        if is_valid(r, c, char):
                            board[r][c] = char
                            if backtrack():
                                return True
                            board[r][c] = '.'
                    return False
        return True

    backtrack()


if __name__ == "__main__":
    board = [
        ["5","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]
    ]
    solve_sudoku(board)
    assert board[0][2] == "4"
    assert board[8][8] == "9"
    print("[PASS] Level 7 Sudoku Solver tests passed!")
