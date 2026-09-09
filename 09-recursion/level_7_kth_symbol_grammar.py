"""
Level 7: K-th Symbol in Grammar

Problem:
We start with 0 in row 1. In every subsequent row, we replace 0 with 01 and 1 with 10.
Given row n and index k (1-indexed), return the kth symbol in row n.

Time Complexity: O(N)
Space Complexity: O(N) stack call depth
"""

def kth_grammar(n: int, k: int) -> int:
    if n == 1 and k == 1:
        return 0
        
    mid = 2 ** (n - 2)
    if k <= mid:
        return kth_grammar(n - 1, k)
    else:
        return 1 - kth_grammar(n - 1, k - mid)


if __name__ == "__main__":
    assert kth_grammar(1, 1) == 0
    assert kth_grammar(2, 1) == 0
    assert kth_grammar(2, 2) == 1
    assert kth_grammar(3, 3) == 1
    print("[PASS] Level 7 K-th Symbol in Grammar tests passed!")
