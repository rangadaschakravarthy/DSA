"""
Level 8: Word Search II (Trie + Backtracking Optimization)

Problem:
Given an m x n board of characters and a list of strings words, return all words on the board.

Time Complexity: O(M * N * 4^L)
Space Complexity: O(W * L) Trie storage
"""

class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None


def find_words(board: list[list[str]], words: list[str]) -> list[str]:
    # Build Trie
    root = TrieNode()
    for word in words:
        node = root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.word = word

    m, n = len(board), len(board[0])
    result = []

    def backtrack(r, c, parent_node):
        char = board[r][c]
        curr_node = parent_node.children[char]

        if curr_node.word:
            result.append(curr_node.word)
            curr_node.word = None  # Avoid duplicates

        board[r][c] = '#'  # Mark visited

        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < m and 0 <= nc < n and board[nr][nc] in curr_node.children:
                backtrack(nr, nc, curr_node)

        board[r][c] = char  # Unmark / Backtrack

        # Prune Trie leaf nodes
        if not curr_node.children:
            del parent_node.children[char]

    for r in range(m):
        for c in range(n):
            if board[r][c] in root.children:
                backtrack(r, c, root)

    return result


if __name__ == "__main__":
    board = [
        ['o','a','a','n'],
        ['e','t','a','e'],
        ['i','h','k','r'],
        ['i','f','l','v']
    ]
    words = ["oath", "pea", "eat", "rain"]
    res = find_words(board, words)
    assert "oath" in res
    assert "eat" in res
    assert "pea" not in res
    print("[PASS] Level 8 Word Search II tests passed!")
