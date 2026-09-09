"""
Level 2: 2D Matrix DP & Subsequence Matching

Topics Covered:
1. Longest Common Subsequence (LCS O(M * N))
2. Unique Grid Paths O(M * N)

2D DP Transitions:
- LCS: If text1[i] == text2[j]: dp[i][j] = 1 + dp[i+1][j+1]. Else max(dp[i+1][j], dp[i][j+1])
- Unique Paths: dp[r][c] = dp[r-1][c] + dp[r][c-1]
"""

def longest_common_subsequence(text1: str, text2: str) -> int:
    """
    Finds length of longest common subsequence between text1 and text2.
    """
    m, n = len(text1), len(text2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(m - 1, -1, -1):
        for j in range(n - 1, -1, -1):
            if text1[i] == text2[j]:
                dp[i][j] = 1 + dp[i + 1][j + 1]
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])
                
    return dp[0][0]


def unique_paths(m: int, n: int) -> int:
    """
    Finds number of unique paths from top-left corner (0, 0) to bottom-right corner (m-1, n-1)
    moving only down or right.
    """
    dp = [1] * n
    for _ in range(m - 1):
        for c in range(1, n):
            dp[c] += dp[c - 1]
    return dp[n - 1]


if __name__ == "__main__":
    # Test LCS
    assert longest_common_subsequence("abcde", "ace") == 3  # "ace"
    assert longest_common_subsequence("abc", "abc") == 3
    assert longest_common_subsequence("abc", "def") == 0
    
    # Test Unique Paths
    assert unique_paths(3, 7) == 28
    assert unique_paths(3, 2) == 3
    
    print("[SUCCESS] All Level 2 2D DP tests passed!")
