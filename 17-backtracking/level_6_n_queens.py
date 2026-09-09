"""
Level 6: N-Queens Problem

Problem:
The n-queens puzzle is the problem of placing n queens on an n x n chessboard 
such that no two queens attack each other. Return all distinct solutions.

Time Complexity: O(N!)
Space Complexity: O(N) sets tracking columns and diagonals
"""

def solve_n_queens(n: int) -> list[list[str]]:
    result = []
    cols = set()
    pos_diag = set()  # (r + c)
    neg_diag = set()  # (r - c)

    board = [["."] * n for _ in range(n)]

    def backtrack(r):
        if r == n:
            copy = ["".join(row) for row in board]
            result.append(copy)
            return

        for c in range(n):
            if c in cols or (r + c) in pos_diag or (r - c) in neg_diag:
                continue

            cols.add(c)
            pos_diag.add(r + c)
            neg_diag.add(r - c)
            board[r][c] = "Q"

            backtrack(r + 1)

            cols.remove(c)
            pos_diag.remove(r + c)
            neg_diag.remove(r - c)
            board[r][c] = "."

    backtrack(0)
    return result


if __name__ == "__main__":
    res4 = solve_n_queens(4)
    assert len(res4) == 2
    assert len(solve_n_queens(1)) == 1
    print("[PASS] Level 6 N-Queens tests passed!")
