"""
Level 3: N-Queens & Fast Constraint Tracking

Topics Covered:
1. N-Queens Solver O(N!) with O(1) Diagonal Check Sets

Constraint Tracking:
For a queen placed at row r and col c:
- Column constraint: `col in cols`
- Positive diagonal constraint: `(r + c) in pos_diag` (runs bottom-left to top-right)
- Negative diagonal constraint: `(r - c) in neg_diag` (runs top-left to bottom-right)
"""

def solve_n_queens(n: int) -> list[list[str]]:
    """
    Solves the N-Queens problem returning all distinct board configurations.
    """
    cols = set()
    pos_diag = set()  # (r + c)
    neg_diag = set()  # (r - c)
    
    results = []
    board = [["."] * n for _ in range(n)]
    
    def backtrack(r: int):
        if r == n:
            copy = ["".join(row) for row in board]
            results.append(copy)
            return
            
        for c in range(n):
            if c in cols or (r + c) in pos_diag or (r - c) in neg_diag:
                continue
                
            # Place Queen
            cols.add(c)
            pos_diag.add(r + c)
            neg_diag.add(r - c)
            board[r][c] = "Q"
            
            # Explore next row
            backtrack(r + 1)
            
            # Backtrack / Remove Queen
            cols.remove(c)
            pos_diag.remove(r + c)
            neg_diag.remove(r - c)
            board[r][c] = "."
            
    backtrack(0)
    return results


if __name__ == "__main__":
    # Test N-Queens
    solutions_4 = solve_n_queens(4)
    assert len(solutions_4) == 2  # Exactly 2 solutions for N=4
    
    solutions_1 = solve_n_queens(1)
    assert len(solutions_1) == 1
    
    print("[SUCCESS] All Level 3 N-Queens tests passed!")
