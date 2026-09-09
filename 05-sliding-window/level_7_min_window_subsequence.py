"""
Level 7: Minimum Window Subsequence (Two-Pointer Expansion & Contraction)

Topics Covered:
1. Minimum Window Subsequence O(N * M) time, O(1) space

Algorithm:
Forward Pass: Find end index where s2 is fully matched as a subsequence in s1.
Backward Pass: Move pointers backward from end index to shrink window to minimal start index!
"""

def min_window_subsequence(s1: str, s2: str) -> str:
    """
    Finds minimum window substring of s1 containing s2 as a subsequence.
    """
    n1, n2 = len(s1), len(s2)
    p1, p2 = 0, 0
    min_len = float('inf')
    start_idx = -1
    
    while p1 < n1:
        if s1[p1] == s2[p2]:
            p2 += 1
            if p2 == n2:
                # Forward match complete! Now shrink backward to find optimal start
                end = p1
                p2 -= 1
                while p2 >= 0:
                    while s1[p1] != s2[p2]:
                        p1 -= 1
                    p1 -= 1
                    p2 -= 1
                p1 += 1
                p2 = 0
                
                if end - p1 + 1 < min_len:
                    min_len = end - p1 + 1
                    start_idx = p1
                    
        p1 += 1
        
    return "" if start_idx == -1 else s1[start_idx : start_idx + min_len]


if __name__ == "__main__":
    assert min_window_subsequence("abcdebdde", "bde") == "bcde"
    assert min_window_subsequence("jmeqksfrsdcmsiwvaovnhffeddphbwsmoff", "u") == ""
    
    print("[SUCCESS] All Level 7 Minimum Window Subsequence tests passed!")
