"""
Level 4: Word Search I

Problem:
Given an m x n grid of characters board and a string word, return true if word exists in the grid.
The word can be constructed from letters of sequentially adjacent cells (horizontally or vertically).

Time Complexity: O(M * N * 4^L) where L is length of word
Space Complexity: O(L) recursion stack depth
"""

def exist(board: list[list[str]], word: str) -> bool:
    m, n = len(board), len(board[0])

    def backtrack(r, c, idx):
        if idx == len(word):
            return True
        if r < 0 or r >= m or c < 0 or c >= n or board[r][c] != word[idx]:
            return False

        temp = board[r][c]
        board[r][c] = '#'  # Mark visited

        found = (backtrack(r + 1, c, idx + 1) or
                 backtrack(r - 1, c, idx + 1) or
                 backtrack(r, c + 1, idx + 1) or
                 backtrack(r, c - 1, idx + 1))

        board[r][c] = temp  # Unmark / Backtrack
        return found

    for r in range(m):
        for c in range(n):
            if backtrack(r, c, 0):
                return True
    return False


if __name__ == "__main__":
    board = [
        ['A', 'B', 'C', 'E'],
        ['S', 'F', 'C', 'S'],
        ['A', 'D', 'E', 'E']
    ]
    assert exist(board, "ABCCED") == True
    assert exist(board, "SEE") == True
    assert exist(board, "ABCB") == False
    print("[PASS] Level 4 Word Search I tests passed!")
